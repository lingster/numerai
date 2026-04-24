import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { gql, toolResult } from "./graphql";

const TOURNAMENT = z
	.number()
	.int()
	.optional()
	.default(8)
	.describe("Tournament ID — 8=Classic, 11=Signals, 12=Crypto");

function authToken(env: Env): string | undefined {
	if (env.NUMERAI_PUBLIC_ID && env.NUMERAI_SECRET_KEY) {
		return `${env.NUMERAI_PUBLIC_ID}$${env.NUMERAI_SECRET_KEY}`;
	}
	return undefined;
}

export function registerTools(server: McpServer, env: Env) {
	// ── Arbitrary query ────────────────────────────────────────────────────────

	server.registerTool(
		"graphql_query",
		{
			description:
				"Run an arbitrary GraphQL query against the Numerai API. Use this as an escape hatch when other tools don't cover your use case. Returns raw JSON.",
			inputSchema: {
				query: z.string().describe("GraphQL query string"),
				variables_json: z
					.string()
					.optional()
					.describe("JSON object of query variables, e.g. {\"id\": \"abc123\"}"),
				use_auth: z
					.boolean()
					.optional()
					.default(true)
					.describe("Include API credentials if configured on the server"),
			},
		},
		({ query, variables_json, use_auth }) =>
			toolResult(async () => {
				let variables: Record<string, unknown> | undefined;
				if (variables_json) {
					try {
						variables = JSON.parse(variables_json) as Record<string, unknown>;
					} catch {
						throw new Error(`Invalid variables JSON: ${variables_json}`);
					}
				}
				return gql(query, variables, use_auth ? authToken(env) : undefined);
			}),
	);

	// ── Tournaments ────────────────────────────────────────────────────────────

	server.registerTool(
		"list_tournaments",
		{
			description: "List all active Numerai tournaments with their IDs and names.",
			inputSchema: {},
		},
		() =>
			toolResult(() =>
				gql<unknown>(`{ tournaments { id tournament name active } }`),
			),
	);

	// ── Rounds ─────────────────────────────────────────────────────────────────

	server.registerTool(
		"get_rounds",
		{
			description:
				"List tournament rounds. Defaults to the latest open round. Filter by status or number.",
			inputSchema: {
				tournament: TOURNAMENT,
				limit: z.number().int().optional().default(1).describe("Number of rounds to return"),
				number: z.number().int().optional().describe("Fetch a specific round by number"),
				status: z
					.enum(["OPEN", "UPCOMING", "RESOLVING", "RESOLVED"])
					.optional()
					.describe("Filter by round status"),
			},
		},
		({ tournament, limit, number, status }) =>
			toolResult(() =>
				gql<unknown>(
					`query($t: Int, $l: Int, $n: Int, $s: RoundStatus) {
            rounds(tournament: $t, limit: $l, number: $n, status: $s) {
              number openTime closeTime closeStakingTime resolveTime scoreTime
              resolvedGeneral resolvedStaking isDaily payoutFactor stakeThreshold
              dataDatestamp numTickers numValidationEras
            }
          }`,
					{ t: tournament, l: limit, n: number ?? null, s: status ?? null },
				),
			),
	);

	// ── Pipeline status ────────────────────────────────────────────────────────

	server.registerTool(
		"get_pipeline_status",
		{
			description:
				"Get the current scoring/data pipeline status including data readiness and scoring ETAs.",
			inputSchema: {
				tournament: z
					.enum(["classic", "signals", "crypto"])
					.optional()
					.default("classic")
					.describe("Tournament name"),
			},
		},
		({ tournament }) =>
			toolResult(() =>
				gql<unknown>(
					`query($t: String) {
            pipelineStatus(tournament: $t) {
              isScoringDay dataReadyAt scoredAt resolvedAt startedAt
              dataP90Eta dataP99Eta scoreP90Eta scoreP99Eta
              resolveP90Eta resolveP99Eta nextStartP90Eta startP90Eta
            }
          }`,
					{ t: tournament },
				),
			),
	);

	// ── Account (authenticated) ────────────────────────────────────────────────

	server.registerTool(
		"get_account",
		{
			description:
				"Fetch the authenticated Numerai account details including NMR balance, models, and staking info. Requires NUMERAI_PUBLIC_ID and NUMERAI_SECRET_KEY to be set on the server.",
			inputSchema: {
				show_archived: z
					.boolean()
					.optional()
					.default(false)
					.describe("Include archived models"),
			},
		},
		({ show_archived }) =>
			toolResult(() => {
				const token = authToken(env);
				if (!token) {
					throw new Error(
						"No credentials configured. Set NUMERAI_PUBLIC_ID and NUMERAI_SECRET_KEY as Worker secrets.",
					);
				}
				return gql<unknown>(
					`query($archived: Boolean) {
            account {
              username email status availableNmr availableStakeCredit
              onChainWalletBalance walletAddress
              models(showArchived: $archived) {
                id name tournament archived computeEnabled
                v2Stake { stakeValue latestValue status }
                latestSubmissions(latestNRounds: 1) { roundNumber status }
              }
              pendingTxns { amount type status time }
              scheduledStakeTxns { model amount type dueDate status }
            }
          }`,
					{ archived: show_archived },
					token,
				);
			}),
	);

	// ── Public account profile ─────────────────────────────────────────────────

	server.registerTool(
		"get_account_profile",
		{
			description:
				"Fetch a public Numerai account profile by username. Includes model list with IDs — use model IDs from here in get_model_performances.",
			inputSchema: {
				username: z.string().describe("Numerai username"),
				tournament: TOURNAMENT,
			},
		},
		({ username, tournament }) =>
			toolResult(() =>
				gql<unknown>(
					`query($u: String!, $t: Int) {
            accountProfile(username: $u, tournament: $t) {
              username displayName bio title totalStake
              returns { oneDay threeMonths oneYear allTime }
              models {
                id displayName tournament stake startDate
                corrRep mmcRep tcRep alphaRep return1y
              }
              achievements { type tier score date }
            }
          }`,
					{ u: username, t: tournament },
				),
			),
	);

	// ── Leaderboard ────────────────────────────────────────────────────────────

	server.registerTool(
		"get_leaderboard",
		{
			description:
				"Fetch the Numerai account leaderboard for Classic (tournament=8) or Signals (tournament=11). Supports sorting by any score metric.",
			inputSchema: {
				tournament: TOURNAMENT,
				limit: z
					.number()
					.int()
					.optional()
					.default(20)
					.describe("Number of rows (max 100 recommended)"),
				offset: z.number().int().optional().default(0).describe("Pagination offset"),
				order_by: z
					.string()
					.optional()
					.default("rank")
					.describe(
						"Field to sort by, e.g. 'corr', 'mmc', 'tc', 'nmrStaked', 'return1y', 'rank'",
					),
				direction: z
					.enum(["asc", "desc"])
					.optional()
					.default("asc")
					.describe("Sort direction"),
				filter_by: z.string().optional().describe("Optional filter expression"),
			},
		},
		({ tournament, limit, offset, order_by, direction, filter_by }) =>
			toolResult(() =>
				gql<unknown>(
					`query($t: Int, $l: Int, $o: Int, $ob: String, $d: String, $f: String) {
            accountLeaderboard(tournament: $t, limit: $l, offset: $o,
                               orderBy: $ob, direction: $d, filterBy: $f) {
              rank username displayName title nmrStaked
              corr corrV4 corr60 mmc mmc60 tc alpha ric mpc
              return1y return3m returnAllTime
              rankChange1d rankChange3m rankChange1y
            }
          }`,
					{
						t: tournament,
						l: limit,
						o: offset,
						ob: order_by,
						d: direction,
						f: filter_by ?? null,
					},
				),
			),
	);

	// ── Model (by UUID) ────────────────────────────────────────────────────────

	server.registerTool(
		"get_model",
		{
			description:
				"Fetch model metadata by model UUID. Use get_account_profile first to resolve a model UUID from a username.",
			inputSchema: {
				model_id: z.string().describe("Model UUID (from get_account_profile)"),
			},
		},
		({ model_id }) =>
			toolResult(() =>
				gql<unknown>(
					`query($id: ID) {
            model(modelId: $id) {
              id name tournament archived computeEnabled
              v2Stake { stakeValue latestValue status pendingV2ChangeStakeRequest { amount type dueDate } }
              latestSubmissions(latestNRounds: 5) {
                roundNumber status roundOpen roundClose
              }
              returns { oneDay threeMonths oneYear allTime }
            }
          }`,
					{ id: model_id },
					authToken(env),
				),
			),
	);

	// ── Model round performances ───────────────────────────────────────────────

	server.registerTool(
		"get_model_performances",
		{
			description:
				"Fetch per-round score history for a model. Returns corr, mmc, tc, fnc, and payout for each round.",
			inputSchema: {
				model_id: z.string().describe("Model UUID (from get_account_profile)"),
				tournament: TOURNAMENT,
				last_n_rounds: z
					.number()
					.int()
					.optional()
					.default(20)
					.describe("Number of most recent rounds"),
				round_number: z
					.number()
					.int()
					.optional()
					.describe("Fetch a specific round only (overrides last_n_rounds)"),
				resolved_only: z
					.boolean()
					.optional()
					.default(false)
					.describe("Only return fully resolved rounds"),
				include_intra_round: z
					.boolean()
					.optional()
					.default(false)
					.describe("Include daily intra-round submission scores"),
			},
		},
		({ model_id, tournament, last_n_rounds, round_number, resolved_only, include_intra_round }) =>
			toolResult(() =>
				gql<unknown>(
					`query($id: ID!, $t: Int, $n: Int, $rn: Int, $res: Boolean) {
            v2RoundModelPerformances(
              modelId: $id, tournament: $t,
              lastNRounds: $n, roundNumberEq: $rn, resolvedOnly: $res
            ) {
              roundNumber roundOpenTime roundResolveTime roundResolved roundPayoutFactor roundTarget
              corrMultiplier mmcMultiplier tcMultiplier
              atRisk payout
              submissionScores { displayName value percentile day date payoutPending payoutSettled }
              ${include_intra_round ? "intraRoundSubmissionScores { displayName value percentile day date }" : ""}
            }
          }`,
					{
						id: model_id,
						t: tournament,
						n: round_number ? null : last_n_rounds,
						rn: round_number ?? null,
						res: resolved_only,
					},
				),
			),
	);

	// ── Public model profile ───────────────────────────────────────────────────

	server.registerTool(
		"get_model_profile",
		{
			description:
				"Fetch the public profile for a model by its display name. Includes reputation scores, ranks, returns, and stake info.",
			inputSchema: {
				model_name: z.string().describe("Model display name (not UUID)"),
				tournament: TOURNAMENT,
			},
		},
		({ model_name, tournament }) =>
			toolResult(() =>
				gql<unknown>(
					`query($name: String!, $t: Int) {
            v3UserProfile(modelName: $name, tournament: $t) {
              username stakeValue nmrStaked isActive computeEnabled team
              latestRanks { corr corrV4 corr20 corr60 mmc mmc60 tc fnc fncV4 ic icV2 alpha ric mpc }
              latestReps  { corr corrV4 corr20 corr60 mmc mmc60 tc fnc fncV4 ic icV2 alpha ric mpc }
              latestReturns { oneDay threeMonths oneYear allTime oneDayNmr threeMonthsNmr oneYearNmr allTimeNmr }
              stakeInfo { payoutSelection corrMultiplier mmcMultiplier tcMultiplier }
              latestUserScores { displayName reputation rank stakedRank date }
            }
          }`,
					{ name: model_name, t: tournament },
				),
			),
	);

	// ── Round details ──────────────────────────────────────────────────────────

	server.registerTool(
		"get_round_details",
		{
			description:
				"Fetch full details for a specific round including aggregate stats, payout totals, and all model scores.",
			inputSchema: {
				round_number: z.number().int().describe("Round number"),
				tournament: TOURNAMENT,
				include_all_models: z
					.boolean()
					.optional()
					.default(false)
					.describe(
						"Include per-model score breakdown (can be large — omit for summary only)",
					),
			},
		},
		({ round_number, tournament, include_all_models }) =>
			toolResult(() =>
				gql<unknown>(
					`query($rn: Int!, $t: Int) {
            roundDetails(roundNumber: $rn, tournament: $t) {
              roundNumber roundResolved roundTarget openTime closeTime scoreTime roundResolveTime
              payoutFactor totalAtStake totalPayout totalBurned totalEarned totalStakes totalSubmitted
              ${
								include_all_models
									? `models {
                  modelName corr corrPercentile mmc mmcPercentile tc tcPercentile
                  payoutPending payoutSettled selectedStakeValue
                }`
									: ""
							}
            }
          }`,
					{ rn: round_number, t: tournament },
				),
			),
	);

	// ── Datasets ───────────────────────────────────────────────────────────────

	server.registerTool(
		"list_datasets",
		{
			description: "List dataset files available for a tournament and optionally a specific round.",
			inputSchema: {
				tournament: TOURNAMENT,
				round_number: z
					.number()
					.int()
					.optional()
					.describe("Round number (omit for current round)"),
			},
		},
		({ tournament, round_number }) =>
			toolResult(() =>
				gql<unknown>(
					`query($t: Int, $r: Int) { listDatasets(tournament: $t, round: $r) }`,
					{ t: tournament, r: round_number ?? null },
				),
			),
	);

	server.registerTool(
		"get_dataset_url",
		{
			description:
				"Get a presigned download URL for a specific Numerai dataset file. URL expires after a short time.",
			inputSchema: {
				filename: z
					.string()
					.describe("Dataset filename, e.g. 'v5/live.parquet' (from list_datasets)"),
				tournament: TOURNAMENT,
				round_number: z
					.number()
					.int()
					.optional()
					.describe("Round number (omit for current round)"),
			},
		},
		({ filename, tournament, round_number }) =>
			toolResult(() =>
				gql<unknown>(
					`query($f: String!, $t: Int, $r: Int) { dataset(filename: $f, tournament: $t, round: $r) }`,
					{ f: filename, t: tournament, r: round_number ?? null },
				),
			),
	);

	// ── Currency price ─────────────────────────────────────────────────────────

	server.registerTool(
		"get_currency_price",
		{
			description: "Get the latest exchange rate for a currency pair. Defaults to NMR/USD.",
			inputSchema: {
				base_symbol: z
					.string()
					.optional()
					.default("NMR")
					.describe("Source currency symbol, e.g. 'NMR', 'ETH'"),
				target_symbol: z
					.string()
					.optional()
					.default("USD")
					.describe("Target currency symbol, e.g. 'USD', 'EUR'"),
			},
		},
		({ base_symbol, target_symbol }) =>
			toolResult(() =>
				gql<unknown>(
					`query($b: String!, $t: String!) {
            latestCurrencyPrice(baseSymbol: $b, targetSymbol: $t) {
              baseSymbol targetSymbol price lastUpdated
            }
          }`,
					{ b: base_symbol, t: target_symbol },
				),
			),
	);
}
