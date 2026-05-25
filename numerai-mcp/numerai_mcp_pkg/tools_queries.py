"""
Query tools for the Numerai GraphQL API.

Each tool wraps a single top-level GraphQL query and returns a dict envelope:

    {"data": <parsed pydantic dict>}     on success
    {"errors": [...], "raw": ...}        on GraphQL/HTTP error

Responses are parsed through `models.py` (auto-generated). All response fields
are Optional — only fields named in the selection set come back populated.

Selection sets are intentionally minimal but useful. Anything not selected here
is still reachable via `graphql_query()` with a hand-written query.

Sections:
  1. Escape hatch + diagnostics
  2. Tournament-wide queries
  3. Accounts & profiles
  4. Models
  5. Leaderboards (per tournament)
  6. Stakes (queries; mutations in tools_mutations.py)
  7. Prices
  8. Datasets
  9. Submission upload/download auth
  10. Compute pickles (queries; mutations in tools_mutations.py)
"""

from __future__ import annotations

import json
import os
from typing import Any, Optional

from .client import auth_header, post_graphql, parse, extract
from . import models as M


def register(mcp) -> None:
    """Register every query tool on the given FastMCP instance."""

    # ----------------------------------------------------------------------
    # 1. Escape hatch + diagnostics
    # ----------------------------------------------------------------------

    @mcp.tool()
    def auth_status() -> dict[str, Any]:
        """Report whether Numerai auth env vars are configured."""
        public_id = os.getenv("NUMERAI_PUBLIC_ID") or os.getenv("NUMERAI_API_PUBLIC_ID")
        secret_key = os.getenv("NUMERAI_SECRET_KEY") or os.getenv("NUMERAI_API_SECRET_KEY")
        return {
            "has_public_id": bool(public_id),
            "has_secret_key": bool(secret_key),
            "uses_auth_header": bool(auth_header()),
        }

    @mcp.tool()
    def graphql_query(
        query: str,
        variables_json: Optional[str] = None,
        use_auth: bool = True,
    ) -> dict[str, Any]:
        """Execute an arbitrary GraphQL operation against the Numerai API.

        Args:
            query: Full GraphQL document.
            variables_json: Optional JSON-encoded variables map.
            use_auth: Include the Authorization header if credentials are configured.
        """
        variables = json.loads(variables_json) if variables_json else None
        return post_graphql(query, variables=variables, use_auth=use_auth)

    # ----------------------------------------------------------------------
    # 2. Tournament-wide queries
    # ----------------------------------------------------------------------

    @mcp.tool()
    def list_tournaments(use_auth: bool = False) -> dict[str, Any]:
        """List available tournaments (Classic=8, Signals=11, Crypto=12)."""
        query = "{ tournaments { id name tournament active } }"
        return parse(post_graphql(query, use_auth=use_auth), "tournaments", M.Tournament)

    @mcp.tool()
    def rounds(
        tournament: int = 8,
        limit: Optional[int] = 5,
        number: Optional[int] = None,
        status: Optional[str] = None,
        target: Optional[str] = None,
        use_auth: bool = False,
    ) -> dict[str, Any]:
        """Round info filterable by tournament/limit/number/status/target.

        `status` is a RoundStatus enum: OPEN / RESOLVED / RESOLVING / UPCOMING.
        """
        query = """
        query Rounds($tournament: Int, $limit: Int, $number: Int, $status: RoundStatus, $target: String) {
          rounds(tournament: $tournament, limit: $limit, number: $number, status: $status, target: $target) {
            id number tournament target isDaily dataDatestamp
            openTime closeTime closeStakingTime resolveTime scoreTime
            resolvedGeneral resolvedStaking
            numTickers payoutFactor stakeThreshold
            defaultCorrMultiplier defaultMmcMultiplier defaultTcMultiplier
          }
        }
        """
        variables = {"tournament": tournament, "limit": limit, "number": number, "status": status, "target": target}
        return parse(post_graphql(query, variables=variables, use_auth=use_auth), "rounds", M.Round)

    @mcp.tool()
    def round_details(
        tournament: int,
        round_number: int,
        include_models: bool = True,
        include_histograms: bool = False,
        use_auth: bool = False,
    ) -> dict[str, Any]:
        """Comprehensive details for a single round.

        Includes all per-model performance entries when `include_models=True`
        (large response — ~1.5MB for active classic rounds) and stake/score
        histograms when `include_histograms=True`.
        """
        model_block = """
            models {
              id modelName profileUrl team computeEnabled
              selectedStakeValue payoutPending payoutSettled
              tc tcPercentile mmc mmcPercentile bmc bmcPercentile
              corr corrPercentile corr20 corr60 mmc60
              corrWMetaModel fnc fncV3 fncV4 mcwnm apcwnm
              corrV4 ric icV2 cwsnmm mcwsm apcwsm alpha mpc
            }
        """ if include_models else ""
        histogram_block = """
            allHistogramData { bins counts }
            stakedHistogramData { bins counts }
        """ if include_histograms else ""

        query = f"""
        query RoundDetails($tournament: Int!, $roundNumber: Int!) {{
          roundDetails(tournament: $tournament, roundNumber: $roundNumber) {{
            roundNumber roundId tournament status roundTarget
            openTime closeTime closeStakingTime scoreTime scoresUpdatedTime roundResolveTime
            payoutFactor totalPayout totalEarned totalBurned totalAtStake totalStakes totalSubmitted
            isDaily
            {model_block}
            {histogram_block}
          }}
        }}
        """
        return parse(
            post_graphql(query, variables={"tournament": tournament, "roundNumber": round_number}, use_auth=use_auth),
            "roundDetails",
            M.RoundDetails,
        )

    @mcp.tool()
    def tournament_overview(use_auth: bool = False) -> dict[str, Any]:
        """Top-level snapshot of the Classic tournament (stakes/accounts/returns)."""
        query = """
        {
          tournamentOverview {
            totalAccounts stakedAccountsLtm stakedSubmissions
            totalAtStake totalStakes totalNetEarnings
            averageThreeMonthsReturns stakeWeightedAverageThreeMonthsReturns
            stakedAccounts { count date }
            stakedModels { count date }
          }
        }
        """
        return parse(post_graphql(query, use_auth=use_auth), "tournamentOverview", M.Overview)

    @mcp.tool()
    def v2_tournament_overview(tournament: int = 8, use_auth: bool = False) -> dict[str, Any]:
        """V2 snapshot for any tournament (8 Classic / 11 Signals / 12 Crypto)."""
        query = """
        query V2TournamentOverview($tournament: Int!) {
          v2TournamentOverview(tournament: $tournament) {
            tournament totalAccounts stakedSubmissions
            totalAtStake totalAtRisk totalStakes
            stakedAccounts { count date }
            stakedModels { count date }
          }
        }
        """
        return parse(
            post_graphql(query, variables={"tournament": tournament}, use_auth=use_auth),
            "v2TournamentOverview",
            M.V2Overview,
        )

    # ----------------------------------------------------------------------
    # 3. Accounts & profiles
    # ----------------------------------------------------------------------

    @mcp.tool()
    def account(use_auth: bool = True) -> dict[str, Any]:
        """Current authenticated account: NMR balance, models, returns, stake values.

        Requires NUMERAI_PUBLIC_ID + NUMERAI_SECRET_KEY env vars.
        """
        query = """
        {
          account {
            id username displayName email status
            availableNmr availableStakeCredit
            heldForFusionStakes heldForPendingWithdrawals heldForScheduledStakeIncreases
            totalStakeValues { time value delta }
            models {
              id name tournament description computeEnabled hidden archived submissionWebhook
              returns { oneDay threeMonths oneYear allTime }
            }
            returns { oneDay threeMonths oneYear allTime }
          }
        }
        """
        return parse(post_graphql(query, use_auth=use_auth), "account", M.Account)

    @mcp.tool()
    def account_profile(username: str, tournament: int = 8, use_auth: bool = False) -> dict[str, Any]:
        """Public profile for a username. tournament: 8 Classic / 11 Signals / 12 Crypto."""
        query = """
        query AccountProfile($username: String!, $tournament: Int) {
          accountProfile(username: $username, tournament: $tournament) {
            id username displayName bio location title isActive
            tournament team profileUrl startDate totalStake
            github twitter linkedin kaggle website
            models { id displayName tournament accountId profileUrl }
            returns { oneDay threeMonths oneYear allTime }
            scores { date corr corr60 mmc mmc60 tc fncV4 alpha mpc v2Corr20 seasonRank }
          }
        }
        """
        return parse(
            post_graphql(query, variables={"username": username, "tournament": tournament}, use_auth=use_auth),
            "accountProfile",
            M.AccountProfile,
        )

    @mcp.tool()
    def v3_user_profile(model_name: str, use_auth: bool = False) -> dict[str, Any]:
        """V3 user profile by model name. Includes ranks/reps/returns and round performances."""
        query = """
        query V3UserProfile($modelName: String!) {
          v3UserProfile(modelName: $modelName) {
            id username accountName bio tournament profileUrl startDate isActive computeEnabled
            nmrStaked stakeValue
            latestRanks { corr corr60 mmc mmc60 tc fnc fncV3 fncV4 corrV4 icV2 ric alpha bmc mpc cort20 }
            latestReps { corr corr60 mmc mmc60 tc fnc fncV3 fncV4 corrV4 icV2 ric alpha bmc mpc cort20 }
            latestReturns { oneDay threeMonths oneYear allTime }
            latestUserScores { date displayName rank reputation stakedRank }
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelName": model_name}, use_auth=use_auth),
            "v3UserProfile",
            M.V3UserProfile,
        )

    @mcp.tool()
    def v2_signals_profile(model_name: str, use_auth: bool = False) -> dict[str, Any]:
        """Signals (tournament 11) profile by model name. Returns the V3UserProfile shape."""
        query = """
        query V2SignalsProfile($modelName: String!) {
          v2SignalsProfile(modelName: $modelName) {
            id username accountName bio tournament profileUrl startDate isActive computeEnabled
            nmrStaked stakeValue
            latestRanks { corr corr60 mmc mmc60 corrV4 fncV4 icV2 ric alpha mpc }
            latestReps { corr corr60 mmc mmc60 corrV4 fncV4 icV2 ric alpha mpc }
            latestReturns { oneDay threeMonths oneYear allTime }
            latestUserScores { date displayName rank reputation stakedRank }
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelName": model_name}, use_auth=use_auth),
            "v2SignalsProfile",
            M.V3UserProfile,
        )

    @mcp.tool()
    def user_scores(model_id: str, use_auth: bool = False) -> dict[str, Any]:
        """Reputation/scores history for a model — list of UserScore entries."""
        query = """
        query UserScores($modelId: ID!) {
          userScores(modelId: $modelId) {
            date displayName rank reputation stakedRank
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelId": model_id}, use_auth=use_auth),
            "userScores",
            M.UserScore,
        )

    # ----------------------------------------------------------------------
    # 4. Models
    # ----------------------------------------------------------------------

    @mcp.tool()
    def model(model_id: str, use_auth: bool = False) -> dict[str, Any]:
        """Detail for a single model by UUID."""
        query = """
        query Model($modelId: ID!) {
          model(modelId: $modelId) {
            id name username tournament description hidden archived
            computeEnabled computeLiteEnabled isComputeWeekdayEnabled submissionWebhook
            profileUrl insertedAt accountId
            returns { oneDay threeMonths oneYear allTime }
            returnsValues { date oneDay threeMonths oneYear allTime }
            v2Stake { status stakeValue latestValue latestValueSettled txHash tournamentNumber }
            latestSubmission { id filename status insertedAt round { number tournament } }
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelId": model_id}, use_auth=use_auth),
            "model",
            M.Model,
        )

    @mcp.tool()
    def model_name_available(name: str, tournament: int = 8, use_auth: bool = False) -> dict[str, Any]:
        """Check whether a model name is free before calling add_model()."""
        query = """
        query ModelNameAvailable($name: String!, $tournament: Int!) {
          modelNameAvailable(name: $name, tournament: $tournament)
        }
        """
        resp = post_graphql(query, variables={"name": name, "tournament": tournament}, use_auth=use_auth)
        return {"available": extract(resp, "modelNameAvailable"), "raw": resp}

    @mcp.tool()
    def submissions(model_id: str, use_auth: bool = False) -> dict[str, Any]:
        """Submission history (V2Submission rows) for a model."""
        query = """
        query Submissions($modelId: ID!) {
          submissions(modelId: $modelId) {
            id filename insertedAt status
            dataDatestamp tickersAcceptedCount tickersSubmittedCount
            validationCorrelation validationMmcMean validationSharpe
            round { number tournament openTime closeTime }
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelId": model_id}, use_auth=use_auth),
            "submissions",
            M.V2Submission,
        )

    @mcp.tool()
    def submission_scores(
        model_id: str,
        last_n_rounds: Optional[int] = None,
        day: Optional[int] = None,
        display_name: Optional[str] = None,
        distinct_on_round: Optional[bool] = None,
        resolved: Optional[bool] = None,
        tournament: Optional[int] = None,
        version: Optional[str] = None,
        use_auth: bool = False,
    ) -> dict[str, Any]:
        """Score entries for a model's submissions (flat list across rounds).

        Use `last_n_rounds` to limit. `display_name` filters to a single metric
        (e.g. "mmc20"). `distinct_on_round=True` returns one row per round.
        """
        query = """
        query SubmissionScores(
          $modelId: ID!, $lastNRounds: Int, $day: Int, $displayName: String,
          $distinctOnRound: Boolean, $resolved: Boolean, $tournament: Int, $version: String
        ) {
          submissionScores(
            modelId: $modelId, lastNRounds: $lastNRounds, day: $day, displayName: $displayName,
            distinctOnRound: $distinctOnRound, resolved: $resolved, tournament: $tournament, version: $version
          ) {
            date day displayName value percentile
            payoutPending payoutSettled resolved resolveDate
            roundNumber roundId roundCloseStakingTime roundResolveTime roundScoreTime
          }
        }
        """
        variables = {
            "modelId": model_id, "lastNRounds": last_n_rounds, "day": day, "displayName": display_name,
            "distinctOnRound": distinct_on_round, "resolved": resolved, "tournament": tournament, "version": version,
        }
        return parse(
            post_graphql(query, variables=variables, use_auth=use_auth),
            "submissionScores",
            M.SubmissionScore,
        )

    @mcp.tool()
    def v2_round_model_performances(
        model_id: str,
        tournament: int = 8,
        last_n_rounds: Optional[int] = None,
        round_number_eq: Optional[int] = None,
        round_number_gte: Optional[int] = None,
        round_number_lte: Optional[int] = None,
        resolved_only: Optional[bool] = None,
        submitted_only: Optional[bool] = None,
        distinct_on_round: Optional[bool] = None,
        include_intra_round: bool = False,
        use_auth: bool = False,
    ) -> dict[str, Any]:
        """Per-round model performance with optional intra-round (daily) scores.

        Top-level scores are inside `submissionScores`/`intraRoundSubmissionScores`,
        not direct fields on V2RoundModelPerformance.

        Set `include_intra_round=True` to fetch daily intra-round scores (mmc20,
        corr20, etc.). Filter with `round_number_eq` for one round or
        `last_n_rounds` for a recent slice.
        """
        intra_block = """
              intraRoundSubmissionScores {
                date day displayName value percentile payoutPending payoutSettled
              }
        """ if include_intra_round else ""

        # NOTE: the live API accepts roundNumber__eq / __gte / __lte (double
        # underscore), even though the introspection reports them as camelCase
        # (roundNumberEq, etc). Trust the live API.
        query = f"""
        query V2RoundModelPerformances(
          $modelId: ID!, $tournament: Int,
          $lastNRounds: Int,
          $roundNumber__eq: Int, $roundNumber__gte: Int, $roundNumber__lte: Int,
          $resolvedOnly: Boolean, $submittedOnly: Boolean, $distinctOnRound: Boolean
        ) {{
          v2RoundModelPerformances(
            modelId: $modelId, tournament: $tournament, lastNRounds: $lastNRounds,
            roundNumber__eq: $roundNumber__eq, roundNumber__gte: $roundNumber__gte, roundNumber__lte: $roundNumber__lte,
            resolvedOnly: $resolvedOnly, submittedOnly: $submittedOnly, distinctOnRound: $distinctOnRound
          ) {{
            roundNumber roundId roundTarget roundResolved
            roundOpenTime roundCloseStakingTime roundResolveTime roundScoreTime roundPayoutFactor roundDataDatestamp
            atRisk corrMultiplier mmcMultiplier tcMultiplier
            submissionId tickersAcceptedCount tickersSubmittedCount
            churnThreshold turnoverThreshold prevWeekChurnMax prevWeekTurnoverMax
            submissionScores {{ date day displayName value percentile payoutPending payoutSettled }}
            {intra_block}
          }}
        }}
        """
        variables = {
            "modelId": model_id, "tournament": tournament, "lastNRounds": last_n_rounds,
            "roundNumber__eq": round_number_eq, "roundNumber__gte": round_number_gte, "roundNumber__lte": round_number_lte,
            "resolvedOnly": resolved_only, "submittedOnly": submitted_only, "distinctOnRound": distinct_on_round,
        }
        return parse(
            post_graphql(query, variables=variables, use_auth=use_auth),
            "v2RoundModelPerformances",
            M.V2RoundModelPerformance,
        )

    @mcp.tool()
    def pending_model_payouts(use_auth: bool = True) -> dict[str, Any]:
        """Pending + actual payouts grouped into actual/pending Payout lists. Requires auth."""
        query = """
        {
          pendingModelPayouts {
            actual {
              modelId modelName modelDisplayName
              roundId roundNumber roundResolveTime
              payoutNmr payoutValue currencySymbol
            }
            pending {
              modelId modelName modelDisplayName
              roundId roundNumber roundResolveTime
              payoutNmr payoutValue currencySymbol
            }
          }
        }
        """
        return parse(post_graphql(query, use_auth=use_auth), "pendingModelPayouts", M.UserPayouts)

    # ----------------------------------------------------------------------
    # 5. Leaderboards
    # ----------------------------------------------------------------------

    @mcp.tool()
    def account_leaderboard(
        tournament: int = 8,
        limit: int = 25,
        offset: int = 0,
        order_by: str = "corr60",
        direction: str = "desc",
        filter_by: Optional[str] = None,
        use_auth: bool = False,
    ) -> dict[str, Any]:
        """Classic / Signals / Crypto account leaderboard.

        `order_by`: one of bmc, corj60, corr20V2, corr60, cort20, fnc_v3, fnc_v4,
        mmc, mmc60, tc, etc. (Note: plain "corr" is not accepted — use corr60.)
        `direction`: asc/desc.
        """
        query = """
        query AccountLeaderboard(
          $tournament: Int, $limit: Int, $offset: Int,
          $orderBy: String, $direction: String, $filterBy: String
        ) {
          accountLeaderboard(
            tournament: $tournament, limit: $limit, offset: $offset,
            orderBy: $orderBy, direction: $direction, filterBy: $filterBy
          ) {
            username displayName rank storedRank profileUrl team title bio
            corr corr60 mmc mmc60 tc bmc alpha ric mpc fncV3 fncV4 icV2 corrV4 cort20 corJ60 v2Corr20
            nmrStaked
            return1y return3m returnAllTime return1yNmr return3mNmr returnAllTimeNmr
            rankChange1d rankChange3m rankChange1y
          }
        }
        """
        variables = {
            "tournament": tournament, "limit": limit, "offset": offset,
            "orderBy": order_by, "direction": direction, "filterBy": filter_by,
        }
        return parse(
            post_graphql(query, variables=variables, use_auth=use_auth),
            "accountLeaderboard",
            M.AccountLeaderboardEntry,
        )

    @mcp.tool()
    def v2_leaderboard(
        limit: int = 25,
        offset: int = 0,
        order_by: Optional[str] = None,
        direction: Optional[str] = None,
        filter_by: Optional[str] = None,
        use_auth: bool = False,
    ) -> dict[str, Any]:
        """V2 reputation-based leaderboard."""
        query = """
        query V2Leaderboard($limit: Int, $offset: Int, $orderBy: String, $direction: String, $filterBy: String) {
          v2Leaderboard(limit: $limit, offset: $offset, orderBy: $orderBy, direction: $direction, filterBy: $filterBy) {
            id username team profileUrl isActive
            rank storedRank rankChange1d rankChange3m rankChange1y
            nmrStaked nmrStakedRank
            corr20Rep corr60Rep corr20V2Rep mmcRep mmc60Rep tcRep fncRep fncV3Rep bmcRep cort20Rep corj60Rep
            return1Day return13Weeks return52Weeks
            canonCorrLtm canonCorrRankLtm canonMmcLtm canonMmcRankLtm
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={
                    "limit": limit, "offset": offset,
                    "orderBy": order_by, "direction": direction, "filterBy": filter_by,
                },
                use_auth=use_auth,
            ),
            "v2Leaderboard",
            M.V2LeaderboardEntry,
        )

    @mcp.tool()
    def signals_leaderboard(
        limit: int = 25,
        offset: int = 0,
        order_by: Optional[str] = None,
        direction: Optional[str] = None,
        filter_by: Optional[str] = None,
        use_auth: bool = False,
    ) -> dict[str, Any]:
        """Signals (tournament 11) leaderboard with signals-specific metrics."""
        query = """
        query SignalsLeaderboard($limit: Int, $offset: Int, $orderBy: String, $direction: String, $filterBy: String) {
          signalsLeaderboard(limit: $limit, offset: $offset, orderBy: $orderBy, direction: $direction, filterBy: $filterBy) {
            id username team profileUrl computeEnabled isActive
            rank storedRank rankChange1d rankChange3m rankChange1y
            nmrStaked nmrStakedRank mmc reputation sharpe apy
            corr20Rep corr60Rep corrV4Rep fncV4Rep icV2Rep ricRep tcRep alphaRep mpcRep
            corrRank corr60Rank corrV4Rank fncV4Rank icV2Rank ricRank tcRank alphaRank mpcRank
            canonCorrLtm canonMmcLtm canonAlphaLtm canonMpcLtm
            return1Day return13Weeks return52Weeks
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={
                    "limit": limit, "offset": offset,
                    "orderBy": order_by, "direction": direction, "filterBy": filter_by,
                },
                use_auth=use_auth,
            ),
            "signalsLeaderboard",
            M.SignalsLeaderboardEntry,
        )

    @mcp.tool()
    def signals_leaderboard_overview(use_auth: bool = False) -> dict[str, Any]:
        """Aggregate metrics for the Signals leaderboard."""
        query = """
        {
          signalsLeaderboardOverview {
            totalAccounts stakedAccountsLtm stakedSubmissions
            totalAtStake totalStakes
            averageThreeMonthsReturns stakeWeightedAverageThreeMonthsReturns
            stakedAccounts { count date }
            stakedModels { count date }
          }
        }
        """
        return parse(post_graphql(query, use_auth=use_auth), "signalsLeaderboardOverview", M.SignalsOverview)

    @mcp.tool()
    def cryptosignals_leaderboard(
        limit: int = 25,
        offset: int = 0,
        order_by: Optional[str] = None,
        direction: Optional[str] = None,
        filter_by: Optional[str] = None,
        use_auth: bool = False,
    ) -> dict[str, Any]:
        """Crypto (tournament 12) leaderboard."""
        query = """
        query CryptoLeaderboard($limit: Int, $offset: Int, $orderBy: String, $direction: String, $filterBy: String) {
          cryptosignalsLeaderboard(limit: $limit, offset: $offset, orderBy: $orderBy, direction: $direction, filterBy: $filterBy) {
            id username team profileUrl computeEnabled isActive
            rank storedRank rankChange1d rankChange3m rankChange1y
            nmrStaked
            corrRep mmcRep corrRank mmcRank
            canonCorrLtm canonMmcLtm canonTcLtm
            return1Day return13Weeks return52Weeks
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={
                    "limit": limit, "offset": offset,
                    "orderBy": order_by, "direction": direction, "filterBy": filter_by,
                },
                use_auth=use_auth,
            ),
            "cryptosignalsLeaderboard",
            M.CryptosignalsLeaderboardEntry,
        )

    @mcp.tool()
    def cryptosignals_leaderboard_overview(use_auth: bool = False) -> dict[str, Any]:
        """Aggregate metrics for the Crypto leaderboard."""
        query = """
        {
          cryptosignalsLeaderboardOverview {
            totalAccounts stakedAccountsLtm stakedSubmissions
            totalAtStake totalStakes
            stakedAccounts { count date }
            stakedModels { count date }
          }
        }
        """
        return parse(post_graphql(query, use_auth=use_auth), "cryptosignalsLeaderboardOverview", M.CryptosignalsOverview)

    @mcp.tool()
    def cryptosignals_meta_model_page(use_auth: bool = False) -> dict[str, Any]:
        """Crypto meta-model snapshot with per-symbol holdings."""
        query = """
        {
          cryptosignalsMetaModelPage {
            tournament lastUpdated totalAtStake totalStakes
            tableData { symbol value mmRank latestPrice logo }
          }
        }
        """
        return parse(post_graphql(query, use_auth=use_auth), "cryptosignalsMetaModelPage", M.MetaModelPage)

    # ----------------------------------------------------------------------
    # 6. Stakes (queries)
    # ----------------------------------------------------------------------

    @mcp.tool()
    def stake_transactions(model_id: str, use_auth: bool = True) -> dict[str, Any]:
        """Historical stake transactions for a model."""
        query = """
        query StakeTransactions($modelId: String!) {
          stakeTransactions(modelId: $modelId) {
            type amount value timestamp tournament note round
            nmrPrice nmrPriceLastUpdated
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelId": model_id}, use_auth=use_auth),
            "stakeTransactions",
            M.StakeTxn,
        )

    @mcp.tool()
    def v3_stake_round(round_id: str, use_auth: bool = False) -> dict[str, Any]:
        """V3 stake info for a round (lookup by string roundId)."""
        query = """
        query V3StakeRound($roundId: String!) {
          v3StakeRound(roundId: $roundId) {
            roundId tournamentId state resolved
            openTime closeTime resolveTime
            payoutFactor stakeCap stakeThreshold
            totalStaked totalPayout remainingPayout remainingBurn
            merkleRoot
          }
        }
        """
        return parse(
            post_graphql(query, variables={"roundId": round_id}, use_auth=use_auth),
            "v3StakeRound",
            M.V3StakeRound,
        )

    @mcp.tool()
    def v3_stake_config(use_auth: bool = False) -> dict[str, Any]:
        """V3 stake contract configuration (addresses, signer, pause state)."""
        query = """
        {
          v3StakeConfig {
            address authorizationSigner nmrAddress owner pendingOwner paused serviceWallet
          }
        }
        """
        return parse(post_graphql(query, use_auth=use_auth), "v3StakeConfig", M.V3StakeConfig)

    # ----------------------------------------------------------------------
    # 7. Prices
    # ----------------------------------------------------------------------

    @mcp.tool()
    def latest_currency_price(
        target_symbol: str,
        base_symbol: str = "NMR",
        use_auth: bool = False,
    ) -> dict[str, Any]:
        """Exchange rate between two currencies (e.g. NMR→USD)."""
        query = """
        query LatestCurrencyPrice($targetSymbol: String!, $baseSymbol: String!) {
          latestCurrencyPrice(targetSymbol: $targetSymbol, baseSymbol: $baseSymbol) {
            lastUpdated baseSymbol targetSymbol price
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={"targetSymbol": target_symbol, "baseSymbol": base_symbol},
                use_auth=use_auth,
            ),
            "latestCurrencyPrice",
            M.SymbolPriceConversion,
        )

    @mcp.tool()
    def latest_nmr_price(use_auth: bool = False) -> dict[str, Any]:
        """Most recent NMR/USD price."""
        query = "{ latestNmrPrice { priceUsd lastUpdated } }"
        return parse(post_graphql(query, use_auth=use_auth), "latestNmrPrice", M.NmrPrice)

    @mcp.tool()
    def latest_eth_price(use_auth: bool = False) -> dict[str, Any]:
        """Most recent ETH/USD price and volume."""
        query = "{ latestEthPrice { priceUsd volume lastUpdated } }"
        return parse(post_graphql(query, use_auth=use_auth), "latestEthPrice", M.EthPrice)

    # ----------------------------------------------------------------------
    # 8. Datasets — these return raw String URLs, not objects
    # ----------------------------------------------------------------------

    @mcp.tool()
    def dataset(
        tournament: int,
        round_number: int,
        filename: str,
        use_auth: bool = False,
    ) -> dict[str, Any]:
        """Signed download URL for a specific dataset file."""
        query = """
        query Dataset($tournament: Int, $round: Int, $filename: String) {
          dataset(tournament: $tournament, round: $round, filename: $filename)
        }
        """
        resp = post_graphql(
            query,
            variables={"tournament": tournament, "round": round_number, "filename": filename},
            use_auth=use_auth,
        )
        return {"url": extract(resp, "dataset"), "raw": resp}

    @mcp.tool()
    def list_datasets(tournament: int, round_number: int, use_auth: bool = False) -> dict[str, Any]:
        """List of available dataset filenames for a round."""
        query = """
        query ListDatasets($tournament: Int, $round: Int) {
          listDatasets(tournament: $tournament, round: $round)
        }
        """
        resp = post_graphql(
            query,
            variables={"tournament": tournament, "round": round_number},
            use_auth=use_auth,
        )
        return {"filenames": extract(resp, "listDatasets"), "raw": resp}

    # ----------------------------------------------------------------------
    # 9. Submission upload/download auth
    # ----------------------------------------------------------------------

    @mcp.tool()
    def submission_upload_auth(
        filename: str,
        tournament: int = 8,
        model_id: Optional[str] = None,
        use_auth: bool = True,
    ) -> dict[str, Any]:
        """Presigned URL for uploading a Classic-tournament predictions CSV.

        The returned `url` is a PUT target; once uploaded, finalize with
        `create_submission(filename=..., tournament=..., model_id=...)`.
        """
        query = """
        query SubmissionUploadAuth($filename: String!, $tournament: Int, $modelId: String) {
          submissionUploadAuth(filename: $filename, tournament: $tournament, modelId: $modelId) {
            filename url accelerated countryCode
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={"filename": filename, "tournament": tournament, "modelId": model_id},
                use_auth=use_auth,
            ),
            "submissionUploadAuth",
            M.FileUploadAuth,
        )

    @mcp.tool()
    def submission_upload_signals_auth(
        filename: str,
        model_id: Optional[str] = None,
        use_auth: bool = True,
    ) -> dict[str, Any]:
        """Presigned upload URL for a Signals tournament submission."""
        query = """
        query SubmissionUploadSignalsAuth($filename: String!, $modelId: String) {
          submissionUploadSignalsAuth(filename: $filename, modelId: $modelId) {
            filename url accelerated countryCode
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={"filename": filename, "modelId": model_id},
                use_auth=use_auth,
            ),
            "submissionUploadSignalsAuth",
            M.FileUploadAuth,
        )

    @mcp.tool()
    def submission_download_auth(submission_id: str, use_auth: bool = True) -> dict[str, Any]:
        """Presigned URL for downloading a previously uploaded submission."""
        query = """
        query SubmissionDownloadAuth($id: ID!) {
          submissionDownloadAuth(id: $id) {
            filename url
          }
        }
        """
        return parse(
            post_graphql(query, variables={"id": submission_id}, use_auth=use_auth),
            "submissionDownloadAuth",
            M.FileUploadAuth,
        )

    # ----------------------------------------------------------------------
    # 10. Compute pickles (queries)
    # ----------------------------------------------------------------------

    @mcp.tool()
    def compute_pickles(model_id: Optional[str] = None, use_auth: bool = True) -> dict[str, Any]:
        """List compute-pickle uploads, optionally filtered to one model."""
        query = """
        query ComputePickles($modelId: String) {
          computePickles(modelId: $modelId) {
            id label filename modelId
            dockerImageId dockerImageName dockerImage
            dataVersionId dataVersion
            insertedAt updatedAt runtime
            triggerStatus validationStatus diagnosticsStatus diagnosticsStatusDescription
            version assignedModelSlots
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelId": model_id}, use_auth=use_auth),
            "computePickles",
            M.ComputePickleUpload,
        )

    @mcp.tool()
    def compute_pickle_data_versions(use_auth: bool = False) -> dict[str, Any]:
        """Data versions available for compute-pickle predictions."""
        query = """
        {
          computePickleDataVersions {
            id name version type default deprecated experimental
          }
        }
        """
        return parse(
            post_graphql(query, use_auth=use_auth),
            "computePickleDataVersions",
            M.ComputePickleDataVersion,
        )

    @mcp.tool()
    def compute_pickle_docker_images(use_auth: bool = False) -> dict[str, Any]:
        """Docker images available for compute-pickle execution."""
        query = """
        {
          computePickleDockerImages {
            id name image tag insertedAt default deprecated experimental
          }
        }
        """
        return parse(
            post_graphql(query, use_auth=use_auth),
            "computePickleDockerImages",
            M.ComputePickleDockerImage,
        )

    @mcp.tool()
    def compute_pickle_upload_auth(
        filename: Optional[str] = None,
        model_id: Optional[str] = None,
        use_auth: bool = True,
    ) -> dict[str, Any]:
        """Presigned URL for uploading a compute-pickle (.pkl) artifact."""
        query = """
        query ComputePickleUploadAuth($filename: String, $modelId: ID) {
          computePickleUploadAuth(filename: $filename, modelId: $modelId) {
            filename url accelerated countryCode
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={"filename": filename, "modelId": model_id},
                use_auth=use_auth,
            ),
            "computePickleUploadAuth",
            M.FileUploadAuth,
        )

    @mcp.tool()
    def compute_pickle_download_auth(
        model_id: str,
        pickle_id: Optional[str] = None,
        use_auth: bool = True,
    ) -> dict[str, Any]:
        """Presigned URL for downloading a compute-pickle.

        `model_id` is required; `pickle_id` defaults to the model's latest
        pickle when omitted.
        """
        query = """
        query ComputePickleDownloadAuth($modelId: ID!, $pickleId: ID) {
          computePickleDownloadAuth(modelId: $modelId, pickleId: $pickleId) {
            filename url
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={"modelId": model_id, "pickleId": pickle_id},
                use_auth=use_auth,
            ),
            "computePickleDownloadAuth",
            M.FileUploadAuth,
        )
