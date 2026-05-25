# Numerai GraphQL Schema Reference

> **Generated** from `.schema/introspection.json` by `numerai-mcp/scripts/codegen.py`.
> Do not edit by hand. Re-run the codegen after the upstream schema changes.

Endpoint: `https://api-tournament.numer.ai/`

- Queries: **77**
- Mutations: **64**
- Object types: **107**
- Input objects: **1**
- Enums: **6**
- Custom scalars: **9**

## Contents

- [Queries](#queries)
- [Mutations](#mutations)
- [Object types](#object-types)
- [Input objects](#input-objects)
- [Enums](#enums)
- [Scalars](#scalars)

## Queries

### `account`
Fetch the authenticated account

**Returns:** [`Account`](#account)

### `accountLeaderboard`
Account-level leaderboard for the specified tournament

**Returns:** [`[AccountLeaderboardEntry]`](#accountleaderboardentry)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `direction` | `String` |  |  |
| `filterBy` | `String` |  |  |
| `limit` | `Int` | `500` |  |
| `offset` | `Int` |  |  |
| `orderBy` | `String` |  |  |
| `tournament` | `Int` | `8` |  |

### `accountNameAvailable`
Check if an account username is available

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `String!` |  |  |

### `accountProfile`
Public account profile by username

**Returns:** [`AccountProfile`](#accountprofile)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tournament` | `Int` | `8` |  |
| `username` | `String!` |  |  |

### `accountProfileImageUploadAuth`
Presigned upload URL for account avatars

**Returns:** [`FileUploadAuth`](#fileuploadauth)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `filename` | `String!` |  |  |

### `activityFeed`
Latest public activity feed entries

**Returns:** [`[ActivityFeedEntry]`](#activityfeedentry)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cursor` | `ID` |  |  |
| `limit` | `Int` | `20` |  |
| `tournament` | `Int` | `8` |  |

### `apiTokenInfo`
Get information about the current API token being used

**Returns:** [`ApiTokenInfo`](#apitokeninfo)

### `apiTokenScopes`
List available OAuth scopes for API tokens

**Returns:** [`[Scope]`](#scope)

### `computePickleDataVersions`
List compute data versions that can be targeted by uploads

**Returns:** [`[ComputePickleDataVersion]`](#computepickledataversion)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `deprecated` | `Boolean!` | `false` |  |

### `computePickleDockerImages`
List compute docker images available for scheduled compute

**Returns:** [`[ComputePickleDockerImage]`](#computepickledockerimage)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `deprecated` | `Boolean` | `false` |  |

### `computePickleDownloadAuth`
Presigned download URL for compute pickle (requires download scope)

**Returns:** [`FileUploadAuth`](#fileuploadauth)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID!` |  |  |
| `pickleId` | `ID` |  |  |

### `computePickleUploadAuth`
Presigned upload URL for compute pickle (requires upload scope)

**Returns:** [`FileUploadAuth`](#fileuploadauth)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `filename` | `String` | `"model.pkl"` |  |
| `modelId` | `ID` |  |  |

### `computePickles`
List compute pickle uploads for a model or account

**Returns:** [`[ComputePickleUpload]`](#computepickleupload)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `ID` |  |  |
| `modelId` | `ID` |  |  |
| `unassigned` | `Boolean!` | `false` |  |

### `countryCode`
Country code inferred from request metadata

**Returns:** `String`

### `cryptosignalsLeaderboard`
CryptoSignals leaderboard with paging/sorting

**Returns:** [`[CryptosignalsLeaderboardEntry]`](#cryptosignalsleaderboardentry)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `direction` | `String` |  |  |
| `filterBy` | `String` |  |  |
| `limit` | `Int` |  |  |
| `offset` | `Int` |  |  |
| `orderBy` | `String` |  |  |

### `cryptosignalsLeaderboardOverview`
Aggregated metrics for the CryptoSignals tournament

**Returns:** [`CryptosignalsOverview`](#cryptosignalsoverview)

### `cryptosignalsMetaModelPage`
CryptoSignals meta model info for the marketing page

**Returns:** [`MetaModelPage`](#metamodelpage)

### `currencyCodes`
List supported currency codes and symbols

**Returns:** [`[CurrencyCode]`](#currencycode)

### `dataset`
Return a single dataset download location by filename

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `filename` | `String!` |  |  |
| `round` | `Int` |  |  |
| `tournament` | `Int` |  |  |

### `defaultApiToken`
Return or lazily create the default API token for the account

**Returns:** [`ApiTokenWithSecret`](#apitokenwithsecret)

### `diagnostics`
List diagnostics runs for a model or account

**Returns:** [`[V2Diagnostics]`](#v2diagnostics)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `ID` |  |  |
| `modelId` | `ID` |  |  |

### `diagnosticsTriggerLogs`
Invocation logs for diagnostics triggers

**Returns:** [`[InvocationLog]`](#invocationlog)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pickleId` | `ID!` |  |  |

### `diagnosticsUploadAuth`
Presigned upload URL for diagnostics payloads

**Returns:** [`FileUploadAuth`](#fileuploadauth)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `filename` | `String!` |  |  |
| `modelId` | `ID` |  |  |
| `tournament` | `Int!` |  |  |

### `earnQuestsProgress`
Progress for the Earn quests for an account

**Returns:** [`EarnQuestsProgress`](#earnquestsprogress)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tournament` | `Int!` |  |  |

### `emailPreferences`
Fetch email preferences via update token

**Returns:** [`EmailPreferences`](#emailpreferences)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `updateToken` | `String!` |  |  |

### `featureFlag`
Lookup a single feature flag by key

**Returns:** [`FeatureFlag`](#featureflag)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `String!` |  |  |

### `geoIp`
GeoIP lookup for an IP address

**Returns:** [`GeoIp`](#geoip)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ip` | `String` |  |  |

### `ghostBlogPosts`
Published blog posts from the Ghost CMS (blog.numer.ai)

**Returns:** [`[GhostBlogPost]`](#ghostblogpost)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `limit` | `Int` | `10` |  |

### `grandmasterTierConfigs`
Grandmaster tier configuration for a tournament

**Returns:** [`[GrandmasterTierConfig]`](#grandmastertierconfig)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tournament` | `Int!` |  |  |

### `latestCurrencyPrice`
Get FX conversion for a currency pair

**Returns:** [`SymbolPriceConversion`](#symbolpriceconversion)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `baseSymbol` | `String!` |  |  |
| `targetSymbol` | `String!` |  |  |

### `latestEthPrice`
Fetch the latest ETH price in USD

**Returns:** [`EthPrice`](#ethprice)

### `latestNmrPrice`
Fetch the latest NMR price in USD

**Returns:** [`NmrPrice`](#nmrprice)

### `listDatasets`
List dataset files available for a round/tournament

**Returns:** `[String]`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `round` | `Int` |  |  |
| `tournament` | `Int` |  |  |

### `mfaRecovery`
Retrieve MFA recovery codes (password check required)

**Returns:** `[String]`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `code` | `String` |  |  |
| `password` | `String!` |  |  |

### `model`
Fetch a model the authenticated user can access

**Returns:** [`Model`](#model)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID` |  |  |

### `modelNameAvailable`
Check if a model name is available in a tournament

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `String!` |  |  |
| `tournament` | `Int!` |  |  |

### `nftee`
NFTee data for the authenticated user

**Returns:** [`Nftees`](#nftees)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `network` | `String!` |  |  |

### `nfteeContract`
NFTee contract metadata for a network

**Returns:** [`NfteeContract`](#nfteecontract)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `network` | `String!` |  |  |

### `nfteeVoucher`
Voucher information for minting an NFTee

**Returns:** [`NfteeVoucher`](#nfteevoucher)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `contractNetwork` | `String!` | `"rinkeby"` |  |
| `minterAddress` | `String!` |  |  |
| `secret` | `String!` |  |  |

### `nfteeWithAddress`
NFTee data fetched by wallet address

**Returns:** [`Nftees`](#nftees)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `network` | `String!` |  |  |
| `walletAddress` | `String!` |  |  |

### `nfteeWithSecret`
NFTee data fetched by secret code

**Returns:** [`Nftees`](#nftees)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `network` | `String!` |  |  |
| `secret` | `String!` |  |  |

### `pendingModelPayouts`
Pending payout amounts for the authenticated user's models

**Returns:** [`UserPayouts`](#userpayouts)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tournament` | `Int!` |  |  |

### `pipelineStatus`
Latest pipeline status (deprecated date arg kept for compatibility)

**Returns:** [`PipelineStatus`](#pipelinestatus)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `date` | `String` |  | Deprecated. Response is determined by latest pipeline run and current UTC date. |
| `tournament` | `String` | `"classic"` | "classic" or "signals" |

### `profileImageUploadAuth`
Presigned upload URL for model/profile images

**Returns:** [`FileUploadAuth`](#fileuploadauth)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `filename` | `String!` |  |  |
| `modelId` | `ID` |  |  |

### `reportLink`
Signed report download link

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `String!` |  |  |

### `roundDetails`
Round-level details including payouts and timelines

**Returns:** [`RoundDetails`](#rounddetails)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `roundNumber` | `Int!` |  |  |
| `tournament` | `Int!` |  |  |

### `rounds`
List rounds with optional filters by tournament, status, target, or number

**Returns:** [`[Round]`](#round)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `limit` | `Int` |  |  |
| `number` | `Int` |  |  |
| `status` | [`RoundStatus`](#roundstatus) |  |  |
| `target` | `String` |  |  |
| `tournament` | `Int` |  |  |

### `seasonAccountSummary`
Season account summaries for a tournament

**Returns:** [`[SeasonAccountSummary]`](#seasonaccountsummary)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tournament` | `Int!` |  |  |

### `seasonLeaderboard`
Season leaderboard standings for a tournament season

**Returns:** [`[SeasonLeaderboardEntry]`](#seasonleaderboardentry)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `seasonYear` | `Int!` |  |  |
| `tierNumberLte` | `Int` |  |  |
| `tournament` | `Int!` |  |  |

### `signalsLeaderboard`
Signals leaderboard with paging/sorting

**Returns:** [`[SignalsLeaderboardEntry]`](#signalsleaderboardentry)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `direction` | `String` |  |  |
| `filterBy` | `String` |  |  |
| `limit` | `Int` |  |  |
| `offset` | `Int` |  |  |
| `orderBy` | `String` |  |  |

### `signalsLeaderboardOverview`
Aggregated metrics for the Signals tournament

**Returns:** [`SignalsOverview`](#signalsoverview)

### `sso`
Validate SSO payload and return SSO details

**Returns:** [`Sso`](#sso)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `payload` | `String!` |  |  |
| `signature` | `String!` |  |  |

### `stakeTransactions`
List stake transactions for one or more models

**Returns:** [`[StakeTxn]`](#staketxn)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `limit` | `Int` |  |  |
| `modelId` | `ID` |  |  |
| `modelIds` | `[ID]` |  |  |
| `offset` | `Int` |  |  |
| `type` | `String` |  |  |

### `submissionDownloadAuth`
Presigned download URL for a submission artifact

**Returns:** [`FileUploadAuth`](#fileuploadauth)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `ID!` |  |  |

### `submissionScores`
Submission score history for a model

**Returns:** [`[SubmissionScore]`](#submissionscore)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `day` | `Int` |  |  |
| `displayName` | `String` |  |  |
| `distinctOnRound` | `Boolean` |  |  |
| `lastNRounds` | `Int` |  |  |
| `modelId` | `ID!` |  |  |
| `resolved` | `Boolean` |  |  |
| `tournament` | `Int` |  |  |
| `version` | `String` |  |  |

### `submissionUploadAuth`
Presigned upload URL for Numerai tournament submissions

**Returns:** [`FileUploadAuth`](#fileuploadauth)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `filename` | `String!` |  |  |
| `modelId` | `ID` |  |  |
| `tournament` | `Int!` |  |  |

### `submissionUploadSignalsAuth`
Presigned upload URL for Signals submissions

**Returns:** [`FileUploadAuth`](#fileuploadauth)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `filename` | `String!` |  |  |
| `modelId` | `ID` |  |  |
| `tournament` | `Int` | `11` |  |

### `submissions`
List submissions for a model/account

**Returns:** [`[V2Submission]`](#v2submission)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `ID` |  |  |
| `modelId` | `ID` |  |  |

### `supportRequestUploadAuth`
Presigned upload URL for support request attachments

**Returns:** [`FileUploadAuth`](#fileuploadauth)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `filename` | `String!` |  |  |

### `supportRequests`
List support requests for the authenticated account

**Returns:** [`[SupportRequest]`](#supportrequest)

### `tournamentOverview`
Overview of all tournaments (current status, rounds, payouts)

**Returns:** [`Overview`](#overview)

### `tournaments`
List all active tournaments and their metadata

**Returns:** [`[Tournament]`](#tournament)

### `triggerLogs`
Invocation logs for compute pickle triggers

**Returns:** [`[InvocationLog]`](#invocationlog)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `triggerId` | `ID!` |  |  |

### `unreadBanners`
List unread announcement banners for the user

**Returns:** [`[Banner]`](#banner)

### `unreadEarnedTitleNotifications`
List unread earned-title notifications for the user

**Returns:** [`[Notification]`](#notification)

### `unreadNotifications`
List unread notifications for the user

**Returns:** [`[Notification]`](#notification)

### `userScores`
Score history for a model

**Returns:** [`[UserScore]`](#userscore)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID!` |  |  |

### `v2Leaderboard`
Numerai main leaderboard with paging/sorting

**Returns:** [`[V2LeaderboardEntry]`](#v2leaderboardentry)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `direction` | `String` |  |  |
| `filterBy` | `String` |  |  |
| `limit` | `Int` |  |  |
| `offset` | `Int` |  |  |
| `orderBy` | `String` |  |  |

### `v2RoundModelPerformances`
Per-round performance for a model with flexible filtering

**Returns:** [`[V2RoundModelPerformance]`](#v2roundmodelperformance)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `distinctOnRound` | `Boolean` |  |  |
| `lastNRounds` | `Int` |  |  |
| `limit` | `Int` |  |  |
| `modelId` | `ID!` |  |  |
| `offset` | `Int` |  |  |
| `resolvedOnly` | `Boolean` |  |  |
| `resolvedWithinLastNDays` | `Int` |  |  |
| `roundDataDatestampGte` | `Int` |  |  |
| `roundNumberEq` | `Int` |  |  |
| `roundNumberGte` | `Int` |  |  |
| `roundNumberLte` | `Int` |  |  |
| `scoredWithinLastNDays` | `Int` |  |  |
| `submittedOnly` | `Boolean` |  |  |
| `tournament` | `Int` | `8` |  |

### `v2SignalsProfile`
Public Signals-flavored profile for a model name

**Returns:** [`V3UserProfile`](#v3userprofile)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelName` | `String!` |  |  |
| `tournament` | `Int` | `11` |  |

### `v2TournamentOverview`
Detailed Numerai tournament overview for a given tournament number

**Returns:** [`V2Overview`](#v2overview)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tournament` | `Int!` |  |  |

### `v3StakeAuth`
Issue a staging/dev staking-v3 authorization for a selected submission

**Returns:** [`V3StakeAuthorization`](#v3stakeauthorization)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `maxAmount` | `String!` |  |  |
| `staker` | `String!` |  |  |
| `submissionId` | `ID!` |  |  |

### `v3StakeClaim`
Staging/dev staking-v3 claim proof for an authenticated model and staker

**Returns:** [`V3StakeClaim`](#v3stakeclaim)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID!` |  |  |
| `roundId` | `String!` |  |  |
| `staker` | `String!` |  |  |

### `v3StakeConfig`
Staging/dev staking-v3 contract configuration

**Returns:** [`V3StakeConfig`](#v3stakeconfig)

### `v3StakeRound`
Staging/dev staking-v3 round status by round id

**Returns:** [`V3StakeRound`](#v3stakeround)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `roundId` | `String!` |  |  |

### `v3StakeServiceWallet`
Staging/dev staking-v3 service wallet balance and allowance

**Returns:** [`V3StakeWallet`](#v3stakewallet)

### `v3UserProfile`
Public Numerai model profile

**Returns:** [`V3UserProfile`](#v3userprofile)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelName` | `String!` |  |  |
| `tournament` | `Int` | `8` |  |

## Mutations

### `absorbAccount`
Merge another account into the current one using a token

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `token` | `String!` |  |  |

### `acceptTos`
Mark the authenticated account as having accepted the Terms of Service

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `accepted` | `Boolean` | `true` |  |

### `addModel`
Create a new model in a tournament

**Returns:** [`Model`](#model)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `String!` |  |  |
| `tournament` | `Int!` |  |  |

### `archiveModel`
Archive a model to hide it from public view and exclude from model limits

**Returns:** [`Model`](#model)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID!` |  |  |

### `assignPickleToModel`
Assign an uploaded pickle to a model

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `String` |  |  |
| `pickleId` | `ID` |  |  |

### `cancelPendingStakeRelease`
Cancel a pending stake release

**Returns:** [`V2ChangeStakeRequest`](#v2changestakerequest)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID!` |  |  |

### `changeEmail`
Change the account email (password check required)

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `code` | `String` |  |  |
| `newEmail` | `String!` |  |  |
| `password` | `String!` |  |  |

### `changePassword`
Change password for the authenticated account

**Returns:** [`Session`](#session)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `code` | `String` |  |  |
| `newPassword` | `String!` |  |  |
| `password` | `String!` |  |  |

### `confirmCreateUser`
Confirm account creation with a token and start session

**Returns:** [`Session`](#session)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `token` | `String!` |  |  |

### `createApiToken`
Create a new API token with scopes

**Returns:** [`ApiTokenWithSecret`](#apitokenwithsecret)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `code` | `String` |  |  |
| `name` | `String!` |  |  |
| `password` | `String!` |  |  |
| `scopes` | `[String]!` |  |  |

### `createComputePickleUpload`
Create a compute pickle upload record and presigned URL

**Returns:** [`ComputePickleUpload`](#computepickleupload)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `dataVersionId` | `ID` |  |  |
| `dockerImageId` | `ID` |  |  |
| `filename` | `String!` |  |  |
| `modelId` | `ID` |  |  |
| `source` | `String` |  |  |
| `tournament` | `Int!` |  |  |

### `createDiagnostics`
Register a diagnostics upload

**Returns:** [`V2Diagnostics`](#v2diagnostics)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `filename` | `String!` |  |  |
| `modelId` | `ID` |  |  |
| `tournament` | `Int!` |  |  |

### `createPrivyUser`
Create a Privy user for the authenticated account and return its DID

**Returns:** `String`

### `createSignalsSubmission`
Register a Signals submission upload

**Returns:** [`V2Submission`](#v2submission)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `dataDatestamp` | `Int` |  |  |
| `filename` | `String!` |  |  |
| `modelId` | `ID` |  |  |
| `source` | `String` |  |  |
| `tournament` | `Int` | `11` |  |
| `triggerId` | `ID` |  |  |
| `version` | `Int` |  |  |

### `createSubmission`
Register a Numerai submission upload

**Returns:** [`V2Submission`](#v2submission)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `dataDatestamp` | `Int` |  |  |
| `filename` | `String!` |  |  |
| `modelId` | `ID` |  |  |
| `source` | `String` |  |  |
| `tournament` | `Int!` |  |  |
| `triggerId` | `ID` |  |  |
| `version` | `Int` |  |  |

### `createSupportRequest`
Create a support request for the authenticated account

**Returns:** [`SupportRequest`](#supportrequest)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `attachments` | `[String]` |  |  |
| `captcha` | `String` |  |  |
| `description` | `String!` |  |  |
| `title` | `String!` |  |  |
| `type` | [`SupportRequestTypeEnum!`](#supportrequesttypeenum) |  |  |

### `createUser`
Create a new Numerai/Signals account

**Returns:** [`Account`](#account)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `acceptedTos` | `Boolean` | `false` |  |
| `campaignId` | `String` |  |  |
| `captcha` | `String!` |  |  |
| `email` | `String!` |  |  |
| `isSignals` | `Boolean` |  |  |
| `password` | `String!` |  |  |
| `source` | `String` |  |  |
| `tournament` | `Int` | `8` |  |
| `username` | `String!` |  |  |

### `deleteAccount`
Delete the authenticated account

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `code` | `String` |  |  |
| `password` | `String!` |  |  |

### `deleteDiagnostics`
Delete diagnostics jobs/runs

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `v2DiagnosticsIds` | `[String]!` |  |  |

### `dismissNotification`
Dismiss a notification for the user

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `notificationId` | `String!` |  |  |

### `generateKaggleVerificationToken`
Generate a Kaggle verification token for linking accounts

**Returns:** [`KaggleVerificationTokenResult`](#kaggleverificationtokenresult)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `kaggleUsername` | `String!` |  |  |

### `increaseStake`
Increase stake for a model

**Returns:** [`V2ChangeStakeRequest`](#v2changestakerequest)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `amount` | `String!` |  |  |
| `modelId` | `ID!` |  |  |

### `login`
Authenticate and start a session

**Returns:** [`Session`](#session)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `code` | `String` |  |  |
| `email` | `String!` |  |  |
| `password` | `String!` |  |  |

### `logout`
Invalidate the current session

**Returns:** `Boolean`

### `markBannerAsRead`
Mark a banner notification as read

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `String!` |  |  |

### `mfaDisable`
Disable MFA for the account

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `code` | `String!` |  |  |
| `password` | `String!` |  |  |

### `mfaEnable`
Enable MFA for the account

**Returns:** [`Session`](#session)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `code` | `String!` |  |  |
| `password` | `String!` |  |  |

### `mfaQr`
Generate MFA QR and recovery codes

**Returns:** [`QrBoject`](#qrboject)

### `releaseStake`
Begin releasing stake for a model

**Returns:** [`V2ChangeStakeRequest`](#v2changestakerequest)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `amount` | `String!` |  |  |
| `drain` | `Boolean` | `false` |  |
| `modelId` | `ID!` |  |  |

### `removeDiscordAccount`
Unlink the connected Discord account

**Returns:** `String`

### `renameAccount`
Rename the authenticated account

**Returns:** [`Account`](#account)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `String!` |  |  |

### `renameModel`
Rename an existing model

**Returns:** [`Model`](#model)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID!` |  |  |
| `name` | `String!` |  |  |

### `resendEmailVerification`
Resend email verification to an address

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `email` | `String!` |  |  |

### `resetEmailChange`
Cancel a pending email change via token

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `token` | `String!` |  |  |

### `resetPassword`
Send a password reset email

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `email` | `String!` |  |  |

### `resetPasswordFromToken`
Reset password using a reset token

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `newPassword` | `String!` |  |  |
| `token` | `String!` |  |  |

### `revokeApiToken`
Revoke an API token by public id

**Returns:** [`ApiToken`](#apitoken)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `publicId` | `String!` |  |  |

### `setAccountMeta`
Update account-level metadata like display name and links

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `bio` | `String` |  |  |
| `displayName` | `String` |  |  |
| `github` | `String` |  |  |
| `kaggle` | `String` |  |  |
| `linkedin` | `String` |  |  |
| `location` | `String` |  |  |
| `occupation` | `String` |  |  |
| `organization` | `String` |  |  |
| `twitter` | `String` |  |  |
| `website` | `String` |  |  |

### `setAiManagerExperience`
Toggle AI manager experience for the account

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `enabled` | `Boolean!` |  |  |

### `setComputeWeekdayEnabled`
Toggle weekday compute scheduling for a model (deprecated; always true)

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `computeWeekdayEnabled` | `Boolean` |  |  |
| `modelId` | `String` |  |  |

### `setDefaultCurrency`
Set the default currency for the account

**Returns:** [`Account`](#account)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `currency` | [`DefaultCurrencyEnum!`](#defaultcurrencyenum) |  |  |

### `setHideOnboardingTutorials`
Toggle onboarding tutorials visibility for the account

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `enabled` | `Boolean!` |  |  |

### `setIsBeta`
Toggle beta flag for the account

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `enabled` | `Boolean!` |  |  |

### `setSubmissionWebhook`
Set or update the submission webhook for a model

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `String` |  |  |
| `newSubmissionWebhook` | `String` |  |  |

### `setUserBio`
Set the public bio for a model

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID` |  |  |
| `value` | `String!` |  |  |

### `setUserLink`
Set the external link for a model

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `linkText` | `String` |  |  |
| `linkUrl` | `String!` |  |  |
| `modelId` | `ID` |  |  |

### `submitKaggleVerification`
Submit a Kaggle account for verification

**Returns:** [`KaggleVerificationResult`](#kaggleverificationresult)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `kaggleProfileData` | [`KaggleProfileDataInput`](#kaggleprofiledatainput) |  |  |
| `kaggleUsername` | `String!` |  |  |

### `submitW9`
Submit a W-9 form for tax compliance

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `address` | `String!` |  |  |
| `businessName` | `String` |  |  |
| `city` | `String!` |  |  |
| `exemptions` | `String` |  |  |
| `fullName` | `String!` |  |  |
| `otherTaxClassDetail` | `String` |  |  |
| `signature` | `String!` |  |  |
| `state` | `String!` |  |  |
| `taxClass` | [`TaxClassEnum!`](#taxclassenum) |  |  |
| `taxYear` | `String!` | `"2021"` |  |
| `taxpayerIdentificationNumber` | `String!` |  |  |
| `zipCode` | `String!` |  |  |

### `subscribeToCryptoMmMailingList`
Subscribe to the Crypto market-making mailing list

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `email` | `String!` |  |  |

### `subscribeToMailingList`
Subscribe an email to a mailing list

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `email` | `String!` |  |  |
| `list` | `String` |  |  |

### `testSubmissionWebhook`
Deprecated test submission webhook placeholder

**Returns:** `String`

### `triggerComputePickleUpload`
Trigger a compute pickle upload/job for an existing pickle

**Returns:** [`ComputePickleUpload`](#computepickleupload)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID` |  |  |
| `pickleId` | `ID` |  |  |
| `triggerValidation` | `Boolean` | `false` |  |

### `triggerModelWebhook`
Manually trigger the submission webhook for a model

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `String!` |  |  |

### `unarchiveModel`
Unarchive a model to make it visible and active again

**Returns:** [`Model`](#model)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID!` |  |  |

### `unsubscribeFromMailingList`
Unsubscribe from a mailing list using a token

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `list` | `String!` |  |  |
| `unsubscribeToken` | `String!` |  |  |

### `updateEmailPreferences`
Update email notification preferences for the authenticated account

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `compute` | `Boolean` |  |  |
| `cryptoRoundOpen` | `Boolean` |  |  |
| `cryptoRoundSummary` | `Boolean` |  |  |
| `cryptoSubmission` | `Boolean` |  |  |
| `deposit` | `Boolean` |  |  |
| `diagnostics` | `Boolean` |  |  |
| `modelUploadReceipt` | `Boolean` |  |  |
| `pickleRoundOpen` | `Boolean` |  |  |
| `pickleRoundStatus` | `Boolean` |  |  |
| `roundOpen` | `Boolean` |  |  |
| `roundSummary` | `Boolean` |  |  |
| `signalsRoundOpen` | `Boolean` |  |  |
| `signalsRoundSummary` | `Boolean` |  |  |
| `signalsSubmission` | `Boolean` |  |  |
| `stakeChange` | `Boolean` |  |  |
| `submission` | `Boolean` |  |  |
| `submissionSuccess` | `Boolean` |  |  |
| `submissionsStatus` | `Boolean` |  |  |
| `withdrawal` | `Boolean` |  |  |

### `updateEmailPreferencesWithToken`
Update email preferences using a token (no auth)

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `announcement` | `Boolean` |  |  |
| `compute` | `Boolean` |  |  |
| `cryptoRoundOpen` | `Boolean` |  |  |
| `cryptoRoundSummary` | `Boolean` |  |  |
| `cryptoSubmission` | `Boolean` |  |  |
| `deposit` | `Boolean` |  |  |
| `diagnostics` | `Boolean` |  |  |
| `modelUploadReceipt` | `Boolean` |  |  |
| `pickleRoundOpen` | `Boolean` |  |  |
| `pickleRoundStatus` | `Boolean` |  |  |
| `roundOpen` | `Boolean` |  |  |
| `roundSummary` | `Boolean` |  |  |
| `signalsRoundOpen` | `Boolean` |  |  |
| `signalsRoundSummary` | `Boolean` |  |  |
| `signalsSubmission` | `Boolean` |  |  |
| `stakeChange` | `Boolean` |  |  |
| `submission` | `Boolean` |  |  |
| `submissionSuccess` | `Boolean` |  |  |
| `submissionsStatus` | `Boolean` |  |  |
| `updateToken` | `String` |  |  |
| `withdrawal` | `Boolean` |  |  |

### `updatePickleLabel`
Update the label on a compute pickle upload

**Returns:** [`ComputePickleUpload`](#computepickleupload)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `label` | `String` |  |  |
| `pickleId` | `ID!` |  |  |

### `v2ChangePayoutSelection`
Deprecated payout selection mutation; use v3ChangePayoutSelection

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `corrMultiplier` | `Float` |  |  |
| `mmcMultiplier` | `Float` |  |  |
| `modelId` | `ID` |  |  |
| `selection` | `String` |  |  |
| `signals` | `Boolean` | `false` |  |
| `takeProfit` | `Boolean` |  |  |
| `tcMultiplier` | `Float` |  |  |
| `tournamentNumber` | `Int` |  |  |

### `v2ChangeStake`
Change stake value/type for a model

**Returns:** [`V2ChangeStakeRequest`](#v2changestakerequest)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID` |  |  |
| `tournamentNumber` | `Int!` |  |  |
| `type` | `String!` |  |  |
| `value` | `String!` |  |  |

### `v2WithdrawNmr`
Withdraw NMR to an external address

**Returns:** [`V2NmrTransfer`](#v2nmrtransfer)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `code` | `String` |  |  |
| `nmrAmount` | `String!` |  |  |
| `password` | `String!` |  |  |
| `toAddress` | `String!` |  |  |

### `v3ChangePayoutSelection`
Set payout selection for a model (current API)

**Returns:** `String`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modelId` | `ID!` |  |  |
| `takeProfit` | `Boolean!` |  |  |
| `tournamentNumber` | `Int!` |  |  |

### `verifyEmail`
Verify an email address using a verification token

**Returns:** `Boolean`

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `token` | `String!` |  |  |

### `verifyLoginIp`
Verify a login attempt from a new IP

**Returns:** [`Session`](#session)

**Args:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `token` | `String!` |  |  |

## Object types

### `Account`

<a id="account"></a>

| Field | Type | Description |
|-------|------|-------------|
| `acceptedTos` | `Boolean` |  |
| `achievements` | [`[Achievement]`](#achievement) | List of title achievements |
| `aiManagerExperience` | `Boolean` |  |
| `apiTokens` | [`[ApiToken]`](#apitoken) |  |
| `availableNmr` | `Nmr` |  |
| `availableStakeCredit` | `Nmr` |  |
| `bannerUrl` | `String` |  |
| `bio` | `String` |  |
| `defaultCurrency` | `String` |  |
| `defaultCurrencySymbol` | `String` |  |
| `discordLinkToken` | `String` |  |
| `discordUsername` | `String` |  |
| `displayName` | `String` |  |
| `email` | `String` |  |
| `emailPreferences` | [`EmailPreferences`](#emailpreferences) |  |
| `github` | `String` |  |
| `heldForFusionStakes` | `Nmr` |  |
| `heldForPendingWithdrawals` | `Nmr` |  |
| `heldForScheduledStakeIncreases` | `Nmr` |  |
| `hideOnboardingTutorials` | `Boolean` |  |
| `id` | `ID` |  |
| `insertedAt` | `Time` |  |
| `isBeta` | `Boolean` |  |
| `isTestPilot` | `Boolean` |  |
| `kaggle` | `String` |  |
| `kaggleVerified` | `Boolean` |  |
| `linkedin` | `String` |  |
| `location` | `String` |  |
| `maxModelSlots` | `Int` | Maximum model slots allowed for your achievements |
| `mfaEnabled` | `Boolean` |  |
| `models` | [`[Model]`](#model) |  |
| `nmrReturns` | [`NmrReturnStats`](#nmrreturnstats) |  |
| `occupation` | `String` |  |
| `onChainWalletBalance` | `Nmr` |  |
| `organization` | `String` |  |
| `pendingTxns` | [`[WalletTxn]`](#wallettxn) |  |
| `profileUrl` | `String` |  |
| `reports` | [`[Reports]`](#reports) |  |
| `returns` | [`SwReturns`](#swreturns) | Average stake weighted returns for all account models per tournament |
| `returnsValues` | [`[SwReturnsValue]`](#swreturnsvalue) | Time series average stake weighted returns for all account models per tournament |
| `scheduledStakeTxns` | [`[ScheduledStakeTxn]`](#scheduledstaketxn) |  |
| `status` | [`AccountStatusEnum`](#accountstatusenum) |  |
| `title` | `String` | The highest earned title |
| `totalStakeValue` | [`[StakeValue]`](#stakevalue) |  |
| `totalStakeValues` | [`[StakeValue]`](#stakevalue) |  |
| `tutorials` | [`AccountTutorials`](#accounttutorials) |  |
| `twitter` | `String` |  |
| `updatedAt` | `Time` |  |
| `username` | `String` |  |
| `w9Info` | [`W9Info`](#w9info) |  |
| `walletAddress` | `String` |  |
| `walletTxns` | [`[WalletTxn]`](#wallettxn) |  |
| `website` | `String` |  |

### `AccountLeaderboardEntry`

<a id="accountleaderboardentry"></a>

| Field | Type | Description |
|-------|------|-------------|
| `alpha` | `Float` |  |
| `bio` | `String` |  |
| `bmc` | `Float` |  |
| `corJ60` | `Float` |  |
| `corr` | `Float` |  |
| `corr60` | `Float` |  |
| `corrV4` | `Float` |  |
| `cort20` | `Float` |  |
| `displayName` | `String` |  |
| `fncV3` | `Float` |  |
| `fncV4` | `Float` |  |
| `icV2` | `Float` |  |
| `id` | `ID` |  |
| `mmc` | `Float` |  |
| `mmc60` | `Float` |  |
| `mpc` | `Float` |  |
| `nmrStaked` | `Nmr` |  |
| `profileUrl` | `String` |  |
| `rank` | `Int` |  |
| `rankChange1d` | `Int` |  |
| `rankChange1y` | `Int` |  |
| `rankChange3m` | `Int` |  |
| `return1y` | `Float` |  |
| `return1yNmr` | `Nmr` |  |
| `return3m` | `Float` |  |
| `return3mNmr` | `Nmr` |  |
| `returnAllTime` | `Float` |  |
| `returnAllTimeNmr` | `Nmr` |  |
| `ric` | `Float` |  |
| `storedRank` | `Int` |  |
| `tc` | `Float` |  |
| `team` | `Boolean` |  |
| `title` | `String` |  |
| `username` | `String` |  |
| `v2Corr20` | `Float` |  |

### `AccountProfile`

<a id="accountprofile"></a>

| Field | Type | Description |
|-------|------|-------------|
| `acceptedTos` | `Boolean` |  |
| `achievements` | [`[Achievement]`](#achievement) | List of title achievements |
| `bannerUrl` | `String` |  |
| `bio` | `String` |  |
| `discord` | [`DiscordInfo`](#discordinfo) |  |
| `displayName` | `String` |  |
| `github` | `String` |  |
| `id` | `ID` |  |
| `isActive` | `Boolean` |  |
| `kaggle` | `String` |  |
| `kaggleTier` | `String` | Kaggle tier from verification (novice, contributor, expert, master, grandmaster) |
| `kaggleVerified` | `Boolean` |  |
| `linkedin` | `String` |  |
| `location` | `String` |  |
| `models` | [`[ModelProfile]`](#modelprofile) |  |
| `occupation` | `String` |  |
| `organization` | `String` |  |
| `profileUrl` | `String` |  |
| `returns` | [`SwReturns`](#swreturns) | Average stake weighted returns for all account models per tournament |
| `returnsTs` | [`[SwReturnsValue]`](#swreturnsvalue) | Time series average stake weighted returns for all account models per tournament |
| `scores` | [`AccountScores`](#accountscores) |  |
| `scoresTs` | [`[AccountScores]`](#accountscores) |  |
| `startDate` | `Time` |  |
| `team` | `Boolean` |  |
| `title` | `String` | The highest earned title |
| `totalStake` | `Nmr` |  |
| `totalStakeTs` | [`[AccountStakeValue]`](#accountstakevalue) |  |
| `tournament` | `Int` |  |
| `twitter` | `String` |  |
| `username` | `String` |  |
| `website` | `String` |  |

### `AccountScores`

<a id="accountscores"></a>

| Field | Type | Description |
|-------|------|-------------|
| `alpha` | `Float` |  |
| `alphaLtm` | `Float` |  |
| `alphaLtmRank` | `Int` |  |
| `corr` | `Float` |  |
| `corr60` | `Float` |  |
| `corr60Ltm` | `Float` |  |
| `corr60LtmRank` | `Int` |  |
| `corrLtm` | `Float` |  |
| `corrLtmRank` | `Int` |  |
| `date` | `Date` |  |
| `fncV4` | `Float` |  |
| `fncV4Ltm` | `Float` |  |
| `fncV4LtmRank` | `Int` |  |
| `mmc` | `Float` |  |
| `mmc60` | `Float` |  |
| `mmc60Ltm` | `Float` |  |
| `mmc60LtmRank` | `Int` |  |
| `mmcLtm` | `Float` |  |
| `mmcLtmRank` | `Int` |  |
| `mpc` | `Float` |  |
| `mpcLtm` | `Float` |  |
| `mpcLtmRank` | `Int` |  |
| `seasonRank` | `Int` |  |
| `tc` | `Float` |  |
| `tcLtm` | `Float` |  |
| `tcLtmRank` | `Int` |  |
| `v2Corr20` | `Float` |  |
| `v2Corr20Ltm` | `Float` |  |
| `v2Corr20LtmRank` | `Int` |  |

### `AccountStakeValue`

<a id="accountstakevalue"></a>

| Field | Type | Description |
|-------|------|-------------|
| `date` | `Date` |  |
| `delta` | `Nmr` |  |
| `time` | `Time` |  |
| `value` | `Nmr` |  |

### `AccountTutorials`

<a id="accounttutorials"></a>

| Field | Type | Description |
|-------|------|-------------|
| `numerai` | [`NumeraiTutorials`](#numeraitutorials) |  |
| `signals` | [`SignalsTutorials`](#signalstutorials) |  |

### `Achievement`

<a id="achievement"></a>

| Field | Type | Description |
|-------|------|-------------|
| `date` | `Date` |  |
| `rank` | `Int` |  |
| `score` | `Float` |  |
| `season` | `String` |  |
| `tier` | `String` |  |
| `tournament` | `Int` |  |
| `type` | `String` |  |

### `ActivityFeedEntry`

<a id="activityfeedentry"></a>

| Field | Type | Description |
|-------|------|-------------|
| `accountId` | `ID` |  |
| `activityType` | `String` |  |
| `avatar` | `String` |  |
| `description` | `String` |  |
| `eventAt` | `String` |  |
| `id` | `ID` |  |
| `insertedAt` | `String` |  |
| `tournamentId` | `ID` |  |
| `username` | `String` |  |

### `ApiToken`

<a id="apitoken"></a>

| Field | Type | Description |
|-------|------|-------------|
| `name` | `String` |  |
| `publicId` | `String` |  |
| `scopes` | `[String]` |  |

### `ApiTokenInfo`

<a id="apitokeninfo"></a>

| Field | Type | Description |
|-------|------|-------------|
| `accountUsername` | `String` |  |
| `name` | `String` |  |
| `publicId` | `String` |  |
| `scopes` | `[String]` |  |

### `ApiTokenWithSecret`

<a id="apitokenwithsecret"></a>

| Field | Type | Description |
|-------|------|-------------|
| `name` | `String` |  |
| `publicId` | `String` |  |
| `scopes` | `[String]` |  |
| `secretKey` | `String` |  |

### `Banner`

<a id="banner"></a>

| Field | Type | Description |
|-------|------|-------------|
| `expirationDate` | `String` |  |
| `type` | `String` |  |

### `ComputePickleDataVersion`

<a id="computepickledataversion"></a>

| Field | Type | Description |
|-------|------|-------------|
| `default` | `Boolean` |  |
| `deprecated` | `Boolean` |  |
| `experimental` | `Boolean` |  |
| `id` | `ID` |  |
| `name` | `String` |  |
| `type` | `String` |  |
| `version` | `String` |  |

### `ComputePickleDockerImage`

<a id="computepickledockerimage"></a>

| Field | Type | Description |
|-------|------|-------------|
| `default` | `Boolean` |  |
| `deprecated` | `Boolean` |  |
| `experimental` | `Boolean` |  |
| `id` | `ID` |  |
| `image` | `String` |  |
| `insertedAt` | `Time` |  |
| `name` | `String` |  |
| `tag` | `String` |  |

### `ComputePickleTrigger`

<a id="computepickletrigger"></a>

| Field | Type | Description |
|-------|------|-------------|
| `computePickleUploadId` | `ID` |  |
| `id` | `ID` |  |
| `insertedAt` | `Time` |  |
| `roundId` | `ID` |  |
| `status` | `String` |  |
| `statuses` | [`[ComputePickleTriggerStatus]`](#computepickletriggerstatus) |  |
| `submissionId` | `ID` |  |
| `type` | `String` |  |
| `updatedAt` | `Time` |  |

### `ComputePickleTriggerStatus`

<a id="computepickletriggerstatus"></a>

| Field | Type | Description |
|-------|------|-------------|
| `computePickleTriggerId` | `ID` |  |
| `description` | `String` |  |
| `id` | `ID` |  |
| `insertedAt` | `Time` |  |
| `status` | `String` |  |
| `updatedAt` | `Time` |  |

### `ComputePickleUpload`

<a id="computepickleupload"></a>

| Field | Type | Description |
|-------|------|-------------|
| `assignedModelSlots` | `[ID]` | List of model_id's assigned to use this pickle model for submissions |
| `dataVersion` | `String` | The data version of the pickle upload |
| `dataVersionId` | `ID` |  |
| `diagnosticsId` | `String` | The diagnostics ID of the pickle upload |
| `diagnosticsStatus` | `String` | The diagnostics status of the pickle upload |
| `diagnosticsStatusDescription` | `String` | The diagnostics status description of the pickle upload |
| `dockerImage` | `String` | The docker image of the pickle upload |
| `dockerImageId` | `ID` |  |
| `dockerImageName` | `String` | The name of the docker image for the pickle upload |
| `filename` | `String` |  |
| `id` | `ID` |  |
| `insertedAt` | `Time` |  |
| `label` | `String` | The label of the pickle upload |
| `modelId` | `String` | The parent model of this pickle |
| `runtime` | `String` | The runtime of the pickle upload |
| `triggerStatus` | `String` | The model's most recent trigger status |
| `triggers` | [`[ComputePickleTrigger]`](#computepickletrigger) | List of submissions triggers for this pickle upload |
| `updatedAt` | `Time` |  |
| `validationStatus` | `String` | The model's validation status |
| `version` | `Int` |  |

### `CryptosignalsLeaderboardEntry`

<a id="cryptosignalsleaderboardentry"></a>

| Field | Type | Description |
|-------|------|-------------|
| `canonCorrLtm` | `Float` |  |
| `canonCorrRankLtm` | `Int` |  |
| `canonMmcLtm` | `Float` |  |
| `canonMmcRankLtm` | `Int` |  |
| `canonTcLtm` | `Float` |  |
| `computeEnabled` | `Boolean` |  |
| `control` | `Float` |  |
| `corrRank` | `Int` |  |
| `corrRep` | `Float` |  |
| `id` | `ID` |  |
| `isActive` | `Boolean` |  |
| `latestUserScores` | [`[UserScore]`](#userscore) |  |
| `mmcRank` | `Int` |  |
| `mmcRep` | `Float` |  |
| `nmrStaked` | `Nmr` |  |
| `profileUrl` | `String` |  |
| `rank` | `Int` |  |
| `rankChange1d` | `Int` |  |
| `rankChange1y` | `Int` |  |
| `rankChange3m` | `Int` |  |
| `return13Weeks` | `Float` |  |
| `return1Day` | `Float` |  |
| `return52Weeks` | `Float` |  |
| `storedRank` | `Int` |  |
| `team` | `Boolean` |  |
| `username` | `String` |  |

### `CryptosignalsOverview`

<a id="cryptosignalsoverview"></a>

| Field | Type | Description |
|-------|------|-------------|
| `returns` | [`SwReturns`](#swreturns) | Average Stake Weighted Returns |
| `returnsValues` | [`[SwReturnsValue]`](#swreturnsvalue) | Time series of average stake weighted returns |
| `stakedAccounts` | [`[StakedAccountsCount]`](#stakedaccountscount) | Time series count of distinct accounts with a staked submission in a currently unresolved round |
| `stakedAccountsLtm` | `Int` | Count of distinct accounts with a staked submission in the last 12 months |
| `stakedModels` | [`[StakedModelsCount]`](#stakedmodelscount) | Time series count of distinct models with a staked submission in a currently unresolved round |
| `stakedSubmissions` | `Int` |  |
| `totalAccounts` | `Int` | Total number of accounts currently on the leaderboard |
| `totalAtStake` | `Nmr` |  |
| `totalAtStakeValues` | [`[StakeValue]`](#stakevalue) | Time series of total NMR staked |
| `totalStakes` | `Int` |  |

### `CurrencyCode`

<a id="currencycode"></a>

| Field | Type | Description |
|-------|------|-------------|
| `code` | `String` |  |
| `symbol` | `String` |  |

### `DailyModelPerformance`

<a id="dailymodelperformance"></a>

| Field | Type | Description |
|-------|------|-------------|
| `alphaRank` | `Int` |  |
| `alphaRep` | `Float` |  |
| `apy` | `Float` |  |
| `corr60Rank` | `Int` |  |
| `corr60Rep` | `Float` |  |
| `corrRank` | `Int` |  |
| `corrRep` | `Float` |  |
| `corrV4Rank` | `Int` |  |
| `corrV4Rep` | `Float` |  |
| `date` | `Time` |  |
| `fncRank` | `Int` |  |
| `fncRep` | `Float` |  |
| `fncV3Rank` | `Int` |  |
| `fncV3Rep` | `Float` |  |
| `fncV4Rank` | `Int` |  |
| `fncV4Rep` | `Float` |  |
| `icRank` | `Int` |  |
| `icRep` | `Float` |  |
| `icV2Rank` | `Int` |  |
| `icV2Rep` | `Float` |  |
| `mmcRank` | `Int` |  |
| `mmcRep` | `Float` |  |
| `mpcRank` | `Int` |  |
| `mpcRep` | `Float` |  |
| `return13Weeks` | `Float` |  |
| `return52Weeks` | `Float` |  |
| `tcRank` | `Int` |  |
| `tcRep` | `Float` |  |

### `DiscordInfo`

<a id="discordinfo"></a>

| Field | Type | Description |
|-------|------|-------------|
| `userId` | `String` |  |
| `username` | `String` |  |

### `EarnQuestsProgress`

<a id="earnquestsprogress"></a>

| Field | Type | Description |
|-------|------|-------------|
| `firstDiagnostics` | `Boolean` |  |
| `firstStake` | `Boolean` |  |
| `firstSubmission` | `Boolean` |  |
| `madeFiveModels` | `Boolean` |  |
| `stakeSubmittedFourWeeks` | [`QuestProgress`](#questprogress) |  |

### `EmailPreferences`

<a id="emailpreferences"></a>

| Field | Type | Description |
|-------|------|-------------|
| `compute` | `Boolean` |  |
| `cryptoRoundOpen` | `Boolean` |  |
| `cryptoRoundSummary` | `Boolean` |  |
| `cryptoSubmission` | `Boolean` |  |
| `deposit` | `Boolean` |  |
| `diagnostics` | `Boolean` |  |
| `modelUploadReceipt` | `Boolean` |  |
| `pickleRoundOpen` | `Boolean` |  |
| `pickleRoundStatus` | `Boolean` |  |
| `roundOpen` | `Boolean` |  |
| `roundSummary` | `Boolean` |  |
| `signalsRoundOpen` | `Boolean` |  |
| `signalsRoundSummary` | `Boolean` |  |
| `signalsSubmission` | `Boolean` |  |
| `stakeChange` | `Boolean` |  |
| `submission` | `Boolean` |  |
| `submissionSuccess` | `Boolean` |  |
| `submissionsStatus` | `Boolean` |  |
| `withdrawal` | `Boolean` |  |

### `EthPrice`

<a id="ethprice"></a>

| Field | Type | Description |
|-------|------|-------------|
| `lastUpdated` | `String` |  |
| `priceUsd` | `String` |  |
| `volume` | `String` |  |

### `FeatureFlag`

<a id="featureflag"></a>

| Field | Type | Description |
|-------|------|-------------|
| `enabled` | `Boolean` |  |
| `key` | `String` |  |
| `value` | `Float` |  |

### `FileUploadAuth`

<a id="fileuploadauth"></a>

| Field | Type | Description |
|-------|------|-------------|
| `accelerated` | `Boolean` |  |
| `countryCode` | `String` |  |
| `filename` | `String` |  |
| `url` | `String` |  |

### `GeoIp`

<a id="geoip"></a>

| Field | Type | Description |
|-------|------|-------------|
| `code` | `String` |  |
| `ip` | `String` |  |
| `location` | `String` |  |

### `GhostBlogPost`

<a id="ghostblogpost"></a>
A blog post from the Ghost CMS

| Field | Type | Description |
|-------|------|-------------|
| `excerpt` | `String` | Post excerpt/summary |
| `featureImage` | `String` | URL of the featured image |
| `id` | `String` | Internal Ghost post ID |
| `publishedAt` | `String` | ISO 8601 timestamp when the post was published |
| `slug` | `String` | URL slug for the post |
| `title` | `String` | Title of the blog post |
| `url` | `String` | Full URL to the blog post |
| `uuid` | `String` | UUID of the post |

### `GrandmasterTierConfig`

<a id="grandmastertierconfig"></a>

| Field | Type | Description |
|-------|------|-------------|
| `maxModelSlots` | `Int` |  |
| `minimumStakeSubs` | `Int` |  |
| `seasonId` | `ID` |  |
| `tierName` | `String` |  |
| `tierNumber` | `Int` |  |
| `topXPct` | `Float` |  |
| `topXRank` | `Int` |  |
| `tournament` | [`Tournament`](#tournament) |  |
| `year` | `Int` |  |

### `HistogramData`

<a id="histogramdata"></a>

| Field | Type | Description |
|-------|------|-------------|
| `bins` | `[Float]` |  |
| `counts` | `[Int]` |  |

### `InvocationLog`

<a id="invocationlog"></a>

| Field | Type | Description |
|-------|------|-------------|
| `message` | `String` |  |
| `timestamp` | `Int` |  |

### `KaggleVerificationResult`

<a id="kaggleverificationresult"></a>

| Field | Type | Description |
|-------|------|-------------|
| `success` | `Boolean` |  |

### `KaggleVerificationTokenResult`

<a id="kaggleverificationtokenresult"></a>

| Field | Type | Description |
|-------|------|-------------|
| `token` | `String` |  |

### `LatestSubmission`

<a id="latestsubmission"></a>

| Field | Type | Description |
|-------|------|-------------|
| `filename` | `String` |  |
| `id` | `ID` |  |
| `roundClose` | `Date` |  |
| `roundCloseStaking` | `Date` |  |
| `roundNumber` | `Int` |  |
| `roundOpen` | `Date` |  |
| `status` | `String` |  |
| `timestamp` | `Time` |  |

### `LeaderboardEntry`

<a id="leaderboardentry"></a>

| Field | Type | Description |
|-------|------|-------------|
| `accountCorr` | `Float` |  |
| `accountCorrRank` | `Int` |  |
| `accountDisplayName` | `String` |  |
| `accountSeasonScore` | `Float` |  |
| `accountSeasonScoreRank` | `Float` |  |
| `accountTc` | `Float` |  |
| `accountTcRank` | `Int` |  |
| `accountTitle` | `String` |  |
| `accountUsername` | `String` |  |
| `cryptosignalsTitle` | `String` |  |
| `excludeFromSeason` | `Boolean` |  |
| `numeraiTitle` | `String` |  |
| `profileUrl` | `String` |  |
| `signalsTitle` | `String` |  |

### `MedalCounts`

<a id="medalcounts"></a>

| Field | Type | Description |
|-------|------|-------------|
| `bronze` | `Int` |  |
| `gold` | `Int` |  |
| `silver` | `Int` |  |

### `MetaModelHolding`

<a id="metamodelholding"></a>

| Field | Type | Description |
|-------|------|-------------|
| `latestPrice` | `Nmr` |  |
| `logo` | `String` |  |
| `mmRank` | `Int` |  |
| `symbol` | `String` |  |
| `value` | `Float` |  |

### `MetaModelPage`

<a id="metamodelpage"></a>

| Field | Type | Description |
|-------|------|-------------|
| `lastUpdated` | `Time` |  |
| `tableData` | [`[MetaModelHolding]`](#metamodelholding) |  |
| `totalAtStake` | `Nmr` |  |
| `totalStakes` | `Int` |  |
| `tournament` | `Int` |  |

### `Model`

<a id="model"></a>

| Field | Type | Description |
|-------|------|-------------|
| `accountId` | `ID` |  |
| `archived` | `Boolean` |  |
| `archivedAt` | `Time` |  |
| `computeEnabled` | `Boolean` |  |
| `computeLiteEnabled` | `Boolean` |  |
| `computePickleUpload` | [`ComputePickleUpload`](#computepickleupload) |  |
| `currentPayoutSelection` | [`PayoutSelection`](#payoutselection) |  |
| `description` | `String` |  |
| `earliestReleaseDate` | `Time` |  |
| `hidden` | `Boolean` |  |
| `id` | `ID` |  |
| `insertedAt` | `Time` |  |
| `isComputeWeekdayEnabled` | `Boolean` |  |
| `latestSignalsSubmission` | [`[V2Submission]`](#v2submission) |  |
| `latestSignalsSubmissionV2` | [`V2Submission`](#v2submission) |  |
| `latestSubmission` | [`[V2Submission]`](#v2submission) |  |
| `latestSubmissionV2` | [`V2Submission`](#v2submission) |  |
| `latestSubmissions` | [`[LatestSubmission]`](#latestsubmission) |  |
| `latestUserScores` | [`[UserScore]`](#userscore) |  |
| `name` | `String` |  |
| `nmrReturns` | [`NmrReturnStats`](#nmrreturnstats) |  |
| `profileUrl` | `String` |  |
| `returns` | [`Returns`](#returns) | Percentage & NMR returns for model |
| `returnsValues` | [`[ReturnsValue]`](#returnsvalue) | Percentage & NMR returns for model |
| `signalsStake` | [`V2Stake`](#v2stake) |  |
| `signalsSubmissions` | [`[V2Submission]`](#v2submission) |  |
| `submissionWebhook` | `String` |  |
| `submissions` | [`[V2Submission]`](#v2submission) |  |
| `tournament` | `Int` |  |
| `username` | `String` |  |
| `v2Stake` | [`V2Stake`](#v2stake) |  |

### `ModelData`

<a id="modeldata"></a>

| Field | Type | Description |
|-------|------|-------------|
| `alpha` | `Float` |  |
| `alphaPercentile` | `Float` |  |
| `apcwnm` | `Float` |  |
| `apcwnmPercentile` | `Float` |  |
| `apcwsm` | `Float` |  |
| `apcwsmPercentile` | `Float` |  |
| `bmc` | `Float` |  |
| `bmcPercentile` | `Float` |  |
| `computeEnabled` | `Boolean` |  |
| `corj60` | `Float` |  |
| `corj60Percentile` | `Float` |  |
| `corr` | `Float` |  |
| `corr20` | `Float` |  |
| `corr20Percentile` | `Float` |  |
| `corr60` | `Float` |  |
| `corr60Percentile` | `Float` |  |
| `corrMedal` | `String` |  |
| `corrPercentile` | `Float` |  |
| `corrV4` | `Float` |  |
| `corrV4Percentile` | `Float` |  |
| `corrWMetaModel` | `Float` |  |
| `corrWMetaModelPercentile` | `Float` |  |
| `cort20` | `Float` |  |
| `cort20Percentile` | `Float` |  |
| `cwmm` | `Float` |  |
| `cwmmPercentile` | `Float` |  |
| `cwsnmm` | `Float` |  |
| `cwsnmmPercentile` | `Float` |  |
| `fnc` | `Float` |  |
| `fncPercentile` | `Float` |  |
| `fncV3` | `Float` |  |
| `fncV3Percentile` | `Float` |  |
| `fncV4` | `Float` |  |
| `fncV4Percentile` | `Float` |  |
| `icV2` | `Float` |  |
| `icV2Percentile` | `Float` |  |
| `id` | `ID` |  |
| `mcwnm` | `Float` |  |
| `mcwnmPercentile` | `Float` |  |
| `mcwsm` | `Float` |  |
| `mcwsmPercentile` | `Float` |  |
| `mmc` | `Float` |  |
| `mmc60` | `Float` |  |
| `mmcMedal` | `String` |  |
| `mmcPercentile` | `Float` |  |
| `modelName` | `String` |  |
| `mpc` | `Float` |  |
| `mpcPercentile` | `Float` |  |
| `payoutPending` | `Nmr` |  |
| `payoutSettled` | `Nmr` |  |
| `profileUrl` | `String` |  |
| `ric` | `Float` |  |
| `ricPercentile` | `Float` |  |
| `roundId` | `ID` |  |
| `selectedStakeValue` | `Nmr` |  |
| `tc` | `Float` |  |
| `tcMedal` | `String` |  |
| `tcPercentile` | `Float` |  |
| `team` | `Boolean` |  |
| `v2Corr20` | `Float` |  |
| `v2Corr20Percentile` | `Float` |  |

### `ModelProfile`

<a id="modelprofile"></a>

| Field | Type | Description |
|-------|------|-------------|
| `accountId` | `ID` |  |
| `alphaRep` | `Float` |  |
| `corj60Rep` | `Float` |  |
| `corr20V2Rep` | `Float` |  |
| `corr60Rep` | `Float` |  |
| `corrRep` | `Float` |  |
| `corrV4Rep` | `Float` |  |
| `displayName` | `String` |  |
| `fncV3Rep` | `Float` |  |
| `fncV4Rep` | `Float` |  |
| `icV2Rep` | `Float` |  |
| `id` | `ID` |  |
| `mmc60Rep` | `Float` |  |
| `mmcRep` | `Float` |  |
| `mpcRep` | `Float` |  |
| `profileUrl` | `String` |  |
| `return1y` | `Float` |  |
| `ricRep` | `Float` |  |
| `stake` | `Nmr` |  |
| `startDate` | `Time` |  |
| `tcRep` | `Float` |  |
| `tournament` | `Int` |  |
| `username` | `String` |  |

### `Nftee`

<a id="nftee"></a>

| Field | Type | Description |
|-------|------|-------------|
| `tokenId` | `Int` |  |

### `NfteeContract`

<a id="nfteecontract"></a>

| Field | Type | Description |
|-------|------|-------------|
| `address` | `String` |  |
| `network` | `String` |  |

### `NfteeVoucher`

<a id="nfteevoucher"></a>

| Field | Type | Description |
|-------|------|-------------|
| `secret` | `String` |  |
| `signature` | `String` |  |
| `tokenIds` | `[Int]` |  |

### `Nftees`

<a id="nftees"></a>

| Field | Type | Description |
|-------|------|-------------|
| `nftees` | [`[Nftee]`](#nftee) |  |
| `voucher` | [`NfteeVoucher`](#nfteevoucher) |  |

### `NmrPrice`

<a id="nmrprice"></a>

| Field | Type | Description |
|-------|------|-------------|
| `lastUpdated` | `String` |  |
| `priceUsd` | `String` |  |

### `NmrReturnStats`

<a id="nmrreturnstats"></a>
Legacy returns stats. Use Account.returns

| Field | Type | Description |
|-------|------|-------------|
| `sw1dReturn` | `Float` |  |
| `sw1yReturn` | `Float` |  |
| `sw3mReturn` | `Float` |  |

### `Notification`

<a id="notification"></a>

| Field | Type | Description |
|-------|------|-------------|
| `bodyText` | `String` |  |
| `ctaButtonLink` | `String` |  |
| `ctaButtonText` | `String` |  |
| `data` | `String` |  |
| `id` | `ID` |  |
| `titleText` | `String` |  |

### `NumeraiTutorials`

<a id="numeraitutorials"></a>

| Field | Type | Description |
|-------|------|-------------|
| `discordConnected` | `Boolean` |  |
| `featureNeutralization` | `Boolean` |  |
| `helloNumerai` | `Boolean` |  |
| `kaggleConnected` | `Boolean` |  |
| `targetEnsemble` | `Boolean` |  |

### `Overview`

<a id="overview"></a>

| Field | Type | Description |
|-------|------|-------------|
| `averageThreeMonthsReturns` | `Float` |  |
| `returns` | [`SwReturns`](#swreturns) | Average stake weighted returns |
| `returnsValues` | [`[SwReturnsValue]`](#swreturnsvalue) | Time series of average stake weighted returns |
| `stakeWeightedAverageThreeMonthsReturns` | `Float` |  |
| `stakedAccounts` | [`[StakedAccountsCount]`](#stakedaccountscount) | Time series count of distinct accounts with a staked submission in a currently unresolved round |
| `stakedAccountsLtm` | `Int` | Count of distinct accounts with a staked submission in the last 12 months |
| `stakedModels` | [`[StakedModelsCount]`](#stakedmodelscount) | Time series count of distinct models with a staked submission in a currently unresolved round |
| `stakedSubmissions` | `Int` |  |
| `totalAccounts` | `Int` | Count of distinct accounts with a submission in the last 12 months |
| `totalAtStake` | `Nmr` |  |
| `totalAtStakeValues` | [`[StakeValue]`](#stakevalue) | Time series of total NMR staked |
| `totalNetEarnings` | `Nmr` |  |
| `totalStakes` | `Int` |  |

### `Payout`

<a id="payout"></a>

| Field | Type | Description |
|-------|------|-------------|
| `currencySymbol` | `String` |  |
| `modelDisplayName` | `String` |  |
| `modelId` | `ID` |  |
| `modelName` | `String` |  |
| `payoutNmr` | `Nmr` |  |
| `payoutValue` | `Usd` |  |
| `roundId` | `ID` |  |
| `roundNumber` | `Int` |  |
| `roundResolveTime` | `Date` |  |

### `PayoutSelection`

<a id="payoutselection"></a>

| Field | Type | Description |
|-------|------|-------------|
| `corrMultiplier` | `Float` |  |
| `insertedAt` | `Time` |  |
| `mmcMultiplier` | `Float` |  |
| `payoutSelection` | `String` |  |
| `takeProfit` | `Boolean` |  |
| `tcMultiplier` | `Float` |  |
| `updatedAt` | `Time` |  |
| `userId` | `ID` |  |

### `PipelineStatus`

<a id="pipelinestatus"></a>

| Field | Type | Description |
|-------|------|-------------|
| `dataP90Eta` | `Time` |  |
| `dataP99Eta` | `Time` |  |
| `dataReadyAt` | `Time` |  |
| `isScoringDay` | `Boolean` |  |
| `nextStartP90Eta` | `Time` |  |
| `resolveP90Eta` | `Time` |  |
| `resolveP99Eta` | `Time` |  |
| `resolvedAt` | `Time` |  |
| `scoreP90Eta` | `Time` |  |
| `scoreP99Eta` | `Time` |  |
| `scoredAt` | `Time` |  |
| `startP90Eta` | `Time` |  |
| `startedAt` | `Time` |  |
| `tournament` | `Time` |  |

### `QrBoject`

<a id="qrboject"></a>

| Field | Type | Description |
|-------|------|-------------|
| `image` | `String` |  |
| `recovery` | `[String]` |  |
| `secret` | `String` |  |

### `QuestProgress`

<a id="questprogress"></a>

| Field | Type | Description |
|-------|------|-------------|
| `complete` | `Boolean` |  |
| `status` | `String` |  |

### `Ranks`

<a id="ranks"></a>

| Field | Type | Description |
|-------|------|-------------|
| `alpha` | `Int` |  |
| `bmc` | `Int` |  |
| `corj60` | `Int` |  |
| `corr` | `Int` |  |
| `corr20V2` | `Int` |  |
| `corr20d` | `Int` |  |
| `corr60` | `Int` |  |
| `corrV4` | `Int` |  |
| `cort20` | `Int` |  |
| `fnc` | `Int` |  |
| `fncV3` | `Int` |  |
| `fncV4` | `Int` |  |
| `ic` | `Int` |  |
| `icV2` | `Int` |  |
| `mmc` | `Int` |  |
| `mmc20d` | `Int` |  |
| `mmc60` | `Int` |  |
| `mpc` | `Int` |  |
| `ric` | `Int` |  |
| `tc` | `Int` |  |

### `Reports`

<a id="reports"></a>

| Field | Type | Description |
|-------|------|-------------|
| `id` | `ID` |  |
| `insertedAt` | `Time` |  |
| `key` | `String` |  |
| `name` | `String` |  |
| `updatedAt` | `Time` |  |

### `Reps`

<a id="reps"></a>

| Field | Type | Description |
|-------|------|-------------|
| `alpha` | `Float` |  |
| `bmc` | `Float` |  |
| `corj60` | `Float` |  |
| `corr` | `Float` |  |
| `corr20V2` | `Float` |  |
| `corr20d` | `Float` |  |
| `corr60` | `Float` |  |
| `corrV4` | `Float` |  |
| `cort20` | `Float` |  |
| `fnc` | `Float` |  |
| `fncV3` | `Float` |  |
| `fncV4` | `Float` |  |
| `ic` | `Float` |  |
| `icV2` | `Float` |  |
| `mmc` | `Float` |  |
| `mmc20d` | `Float` |  |
| `mmc60` | `Float` |  |
| `mpc` | `Float` |  |
| `ric` | `Float` |  |
| `tc` | `Float` |  |

### `Returns`

<a id="returns"></a>
Percentage Returns

| Field | Type | Description |
|-------|------|-------------|
| `allTime` | `Float` |  |
| `allTimeNmr` | `Nmr` |  |
| `oneDay` | `Float` |  |
| `oneDayNmr` | `Nmr` |  |
| `oneYear` | `Float` |  |
| `oneYearNmr` | `Nmr` |  |
| `threeMonths` | `Float` |  |
| `threeMonthsNmr` | `Nmr` |  |

### `ReturnsValue`

<a id="returnsvalue"></a>
Percentage Returns

| Field | Type | Description |
|-------|------|-------------|
| `allTime` | `Float` |  |
| `allTimeNmr` | `Nmr` |  |
| `date` | `Date` |  |
| `oneDay` | `Float` |  |
| `oneDayNmr` | `Nmr` |  |
| `oneYear` | `Float` |  |
| `oneYearNmr` | `Nmr` |  |
| `threeMonths` | `Float` |  |
| `threeMonthsNmr` | `Nmr` |  |

### `Round`

<a id="round"></a>

| Field | Type | Description |
|-------|------|-------------|
| `closeStakingTime` | `Time` |  |
| `closeTime` | `Time` |  |
| `dataDatestamp` | `Int` |  |
| `defaultCorrMultiplier` | `Float` |  |
| `defaultMmcMultiplier` | `Float` |  |
| `defaultTcMultiplier` | `Float` |  |
| `id` | `ID` |  |
| `isDaily` | `Boolean` |  |
| `maxCorrMultiplier` | `Float` |  |
| `maxMmcMultiplier` | `Float` |  |
| `maxTcMultiplier` | `Float` |  |
| `minCorrMultiplier` | `Float` |  |
| `minMmcMultiplier` | `Float` |  |
| `minTcMultiplier` | `Float` |  |
| `numTickers` | `Int` |  |
| `numValidationEras` | `Int` |  |
| `numValidationTickers` | `Int` |  |
| `number` | `Int` |  |
| `openTime` | `Time` |  |
| `payoutFactor` | `String` |  |
| `resolveTime` | `Time` |  |
| `resolvedGeneral` | `Boolean` |  |
| `resolvedStaking` | `Boolean` |  |
| `scoreTime` | `Time` |  |
| `stakeThreshold` | `Float` |  |
| `target` | `String` |  |
| `tournament` | `Int` |  |

### `RoundDetails`

<a id="rounddetails"></a>

| Field | Type | Description |
|-------|------|-------------|
| `allHistogramData` | [`HistogramData`](#histogramdata) |  |
| `closeStakingTime` | `Time` |  |
| `closeTime` | `Time` |  |
| `isDaily` | `Boolean` |  |
| `models` | [`[ModelData]`](#modeldata) |  |
| `openTime` | `Time` |  |
| `payoutFactor` | `String` |  |
| `payoutMultipliers` | [`[RoundPayoutMultiplier]`](#roundpayoutmultiplier) |  |
| `roundId` | `ID` |  |
| `roundNumber` | `Int` |  |
| `roundResolveTime` | `Time` |  |
| `roundResolved` | `Boolean` |  |
| `roundTarget` | `String` |  |
| `scoreTime` | `Time` |  |
| `scoresUpdatedTime` | `Time` |  |
| `stakedHistogramData` | [`HistogramData`](#histogramdata) |  |
| `status` | `String` |  |
| `totalAtStake` | `Float` |  |
| `totalBurned` | `Float` |  |
| `totalEarned` | `Float` |  |
| `totalPayout` | `Float` |  |
| `totalStakes` | `Int` |  |
| `totalSubmitted` | `Int` |  |
| `tournament` | `Int` |  |

### `RoundModelPerformance`

<a id="roundmodelperformance"></a>

| Field | Type | Description |
|-------|------|-------------|
| `apcwnm` | `Float` |  |
| `apcwnmPercentile` | `Float` |  |
| `apcwsm` | `Float` |  |
| `apcwsmPercentile` | `Float` |  |
| `corr` | `Float` |  |
| `corr20V2` | `Float` |  |
| `corr20V2Percentile` | `Float` |  |
| `corr20d` | `Float` |  |
| `corr20dPercentile` | `Float` |  |
| `corr60` | `Float` |  |
| `corr60Percentile` | `Float` |  |
| `corrMultiplier` | `Float` |  |
| `corrPercentile` | `Float` |  |
| `corrV4` | `Float` |  |
| `corrV4Percentile` | `Float` |  |
| `corrWMetamodel` | `Float` |  |
| `cwmm` | `Float` |  |
| `cwmmPercentile` | `Float` |  |
| `cwsnmmr` | `Float` |  |
| `cwsnmmrPercentile` | `Float` |  |
| `fnc` | `Float` |  |
| `fncPercentile` | `Float` |  |
| `fncV3` | `Float` |  |
| `fncV3Percentile` | `Float` |  |
| `fncV4` | `Float` |  |
| `fncV4Percentile` | `Float` |  |
| `ic` | `Float` |  |
| `icPercentile` | `Float` |  |
| `icV2` | `Float` |  |
| `icV2Percentile` | `Float` |  |
| `mcwnm` | `Float` |  |
| `mcwnmPercentile` | `Float` |  |
| `mcwsm` | `Float` |  |
| `mcwsmPercentile` | `Float` |  |
| `mmc` | `Float` |  |
| `mmc20d` | `Float` |  |
| `mmc20dPercentile` | `Float` |  |
| `mmcMultiplier` | `Float` |  |
| `mmcPercentile` | `Float` |  |
| `payout` | `Nmr` |  |
| `ric` | `Float` |  |
| `ricPercentile` | `Float` |  |
| `roundNumber` | `Int` |  |
| `roundOpenTime` | `Time` |  |
| `roundPayoutFactor` | `String` |  |
| `roundResolveTime` | `Time` |  |
| `roundResolved` | `Boolean` |  |
| `roundScoreTime` | `Time` |  |
| `roundTarget` | `String` |  |
| `selectedStakeValue` | `Nmr` |  |
| `tc` | `Float` |  |
| `tcMultiplier` | `Float` |  |
| `tcPercentile` | `Float` |  |

### `RoundPayoutMultiplier`

<a id="roundpayoutmultiplier"></a>

| Field | Type | Description |
|-------|------|-------------|
| `displayName` | `String` |  |
| `multiplier` | `Float` |  |

### `ScheduledStakeTxn`

<a id="scheduledstaketxn"></a>

| Field | Type | Description |
|-------|------|-------------|
| `amount` | `Nmr` |  |
| `drain` | `Boolean` |  |
| `dueDate` | `Time` |  |
| `model` | `String` |  |
| `status` | `String` |  |
| `time` | `Time` |  |
| `tournament` | `Int` |  |
| `type` | `String` |  |

### `Scope`

<a id="scope"></a>

| Field | Type | Description |
|-------|------|-------------|
| `description` | `String` |  |
| `name` | `String` |  |

### `SeasonAccountPerformance`

<a id="seasonaccountperformance"></a>

| Field | Type | Description |
|-------|------|-------------|
| `rank` | `Int` |  |
| `scoreName` | `String` |  |

### `SeasonAccountSummary`

<a id="seasonaccountsummary"></a>

| Field | Type | Description |
|-------|------|-------------|
| `closeStakingEnd` | `Date` |  |
| `daysUntilNextSeasonOpen` | `Int` |  |
| `firstScoreDate` | `Date` |  |
| `hasScores` | `Boolean` |  |
| `hasStakedOneNmr` | `Boolean` |  |
| `id` | `ID` |  |
| `maxScoreDate` | `Date` |  |
| `minQualifyingSubmissions` | `Int` |  |
| `numQualifyingSubmissions` | `Int` |  |
| `openDate` | `Date` |  |
| `participants` | `Int` |  |
| `resolveDate` | `Date` |  |
| `roundNumberEnd` | `Int` |  |
| `roundNumberStart` | `Int` |  |
| `roundsLeft` | `Int` |  |
| `seasonAccountPerformance` | [`[SeasonAccountPerformance]`](#seasonaccountperformance) |  |
| `status` | `String` |  |
| `titleInfo` | [`TitleInfo`](#titleinfo) |  |
| `tournament` | `Int` |  |
| `year` | `Int` |  |

### `SeasonLeaderboardEntry`

<a id="seasonleaderboardentry"></a>

| Field | Type | Description |
|-------|------|-------------|
| `seasonYear` | `Int` |  |
| `tiers` | [`[TierLeaderboard]`](#tierleaderboard) |  |

### `Session`

<a id="session"></a>

| Field | Type | Description |
|-------|------|-------------|
| `token` | `String` |  |
| `username` | `String` |  |

### `SignalsLeaderboardEntry`

<a id="signalsleaderboardentry"></a>

| Field | Type | Description |
|-------|------|-------------|
| `alphaRank` | `Int` |  |
| `alphaRep` | `Float` |  |
| `apy` | `Float` |  |
| `canonAlphaLtm` | `Float` |  |
| `canonAlphaRankLtm` | `Int` |  |
| `canonCorrLtm` | `Float` |  |
| `canonCorrRankLtm` | `Int` |  |
| `canonMmcLtm` | `Float` |  |
| `canonMmcRankLtm` | `Int` |  |
| `canonMpcLtm` | `Float` |  |
| `canonMpcRankLtm` | `Int` |  |
| `computeEnabled` | `Boolean` |  |
| `control` | `Float` |  |
| `corr20Rank` | `Int` |  |
| `corr20Rep` | `Float` |  |
| `corr20V2Rank` | `Int` |  |
| `corr20V2Rep` | `Float` |  |
| `corr20dRank` | `Int` |  |
| `corr20dRep` | `Float` |  |
| `corr60Rank` | `Int` |  |
| `corr60Rep` | `Float` |  |
| `corrRank` | `Int` |  |
| `corrV4Rank` | `Int` |  |
| `corrV4Rep` | `Float` |  |
| `fncV4Rank` | `Int` |  |
| `fncV4Rep` | `Float` |  |
| `icRank` | `Int` |  |
| `icRep` | `Float` |  |
| `icV2Rank` | `Int` |  |
| `icV2Rep` | `Float` |  |
| `id` | `ID` |  |
| `isActive` | `Boolean` |  |
| `latestUserScores` | [`[UserScore]`](#userscore) |  |
| `mmc` | `Float` |  |
| `mmc20dRank` | `Int` |  |
| `mmc20dRep` | `Float` |  |
| `mmcRank` | `Int` |  |
| `mmcRep` | `Float` |  |
| `mpcRank` | `Int` |  |
| `mpcRep` | `Float` |  |
| `nmrStaked` | `Nmr` |  |
| `nmrStakedRank` | `Int` |  |
| `prevAlphaRank` | `Int` |  |
| `prevCorr20V2Rank` | `Int` |  |
| `prevCorr20dRank` | `Int` |  |
| `prevCorr60Rank` | `Int` |  |
| `prevCorrRank` | `Int` |  |
| `prevCorrV4Rank` | `Int` |  |
| `prevFncV4Rank` | `Int` |  |
| `prevIcRank` | `Int` |  |
| `prevIcV2Rank` | `Int` |  |
| `prevMmc20dRank` | `Int` |  |
| `prevMmcRank` | `Int` |  |
| `prevMpcRank` | `Int` |  |
| `prevRank` | `Int` |  |
| `prevRicRank` | `Int` |  |
| `prevTcRank` | `Int` |  |
| `profileUrl` | `String` |  |
| `rank` | `Int` |  |
| `rankChange1d` | `Int` |  |
| `rankChange1y` | `Int` |  |
| `rankChange3m` | `Int` |  |
| `reputation` | `Float` |  |
| `return13Weeks` | `Float` |  |
| `return13WeeksRank` | `Int` |  |
| `return1Day` | `Float` |  |
| `return1DayRank` | `Int` |  |
| `return52Weeks` | `Float` |  |
| `return52WeeksRank` | `Int` |  |
| `ricRank` | `Int` |  |
| `ricRep` | `Float` |  |
| `sharpe` | `Float` |  |
| `storedRank` | `Int` |  |
| `tcRank` | `Int` |  |
| `tcRep` | `Float` |  |
| `team` | `Boolean` |  |
| `today` | `Float` |  |
| `username` | `String` |  |

### `SignalsOverview`

<a id="signalsoverview"></a>

| Field | Type | Description |
|-------|------|-------------|
| `averageThreeMonthsReturns` | `Float` |  |
| `returns` | [`SwReturns`](#swreturns) | Average Stake Weighted Returns |
| `returnsValues` | [`[SwReturnsValue]`](#swreturnsvalue) | Time series of average stake weighted returns |
| `stakeWeightedAverageThreeMonthsReturns` | `Float` |  |
| `stakedAccounts` | [`[StakedAccountsCount]`](#stakedaccountscount) | Time series count of distinct accounts with a staked submission in a currently unresolved round |
| `stakedAccountsLtm` | `Int` | Count of distinct accounts with a staked submission in the last 12 months |
| `stakedModels` | [`[StakedModelsCount]`](#stakedmodelscount) | Time series count of distinct models with a staked submission in a currently unresolved round |
| `stakedSubmissions` | `Int` |  |
| `totalAccounts` | `Int` | Total number of accounts currently on the leaderboard |
| `totalAtStake` | `Nmr` |  |
| `totalAtStakeValues` | [`[StakeValue]`](#stakevalue) | Time series of total NMR staked |
| `totalStakes` | `Int` |  |

### `SignalsTutorials`

<a id="signalstutorials"></a>

| Field | Type | Description |
|-------|------|-------------|
| `helloSignals` | `Boolean` |  |

### `Sso`

<a id="sso"></a>

| Field | Type | Description |
|-------|------|-------------|
| `payload` | `String` |  |
| `signature` | `String` |  |
| `url` | `String` |  |

### `StakeTxn`

<a id="staketxn"></a>

| Field | Type | Description |
|-------|------|-------------|
| `amount` | `Nmr` |  |
| `model` | `String` |  |
| `modelId` | `ID` |  |
| `nmrPrice` | `Nmr` |  |
| `nmrPriceLastUpdated` | `Time` |  |
| `note` | `String` |  |
| `round` | `Int` |  |
| `timestamp` | `Time` |  |
| `tournament` | `Int` |  |
| `type` | `String` |  |
| `value` | `Nmr` |  |

### `StakeValue`

<a id="stakevalue"></a>

| Field | Type | Description |
|-------|------|-------------|
| `delta` | `Nmr` |  |
| `time` | `Time` |  |
| `value` | `Nmr` |  |

### `StakedAccountsCount`

<a id="stakedaccountscount"></a>

| Field | Type | Description |
|-------|------|-------------|
| `count` | `Int` |  |
| `date` | `Date` |  |

### `StakedModelsCount`

<a id="stakedmodelscount"></a>

| Field | Type | Description |
|-------|------|-------------|
| `count` | `Int` |  |
| `date` | `Date` |  |

### `SubmissionScore`

<a id="submissionscore"></a>

| Field | Type | Description |
|-------|------|-------------|
| `date` | `Time` |  |
| `day` | `Int` |  |
| `displayName` | `String` |  |
| `payoutPending` | `Nmr` |  |
| `payoutSettled` | `Nmr` |  |
| `percentile` | `Float` |  |
| `resolveDate` | `Time` |  |
| `resolved` | `Boolean` |  |
| `roundCloseStakingTime` | `Time` |  |
| `roundId` | `ID` |  |
| `roundNumber` | `Int` |  |
| `roundResolveTime` | `Time` |  |
| `roundScoreTime` | `Time` |  |
| `submissionId` | `ID` |  |
| `value` | `Float` |  |
| `version` | `String` |  |

### `SupportRequest`

<a id="supportrequest"></a>

| Field | Type | Description |
|-------|------|-------------|
| `accountId` | `ID` |  |
| `description` | `String` |  |
| `id` | `ID` |  |
| `insertedAt` | `Time` |  |
| `issueStatus` | [`SupportRequestIssueStatusEnum`](#supportrequestissuestatusenum) |  |
| `title` | `String` |  |
| `type` | [`SupportRequestTypeEnum`](#supportrequesttypeenum) |  |
| `updatedAt` | `Time` |  |

### `SwReturns`

<a id="swreturns"></a>
Average Stake Weighted Returns

| Field | Type | Description |
|-------|------|-------------|
| `allTime` | `Float` |  |
| `allTimeNmr` | `Nmr` |  |
| `oneDay` | `Float` |  |
| `oneDayNmr` | `Nmr` |  |
| `oneYear` | `Float` |  |
| `oneYearNmr` | `Nmr` |  |
| `threeMonths` | `Float` |  |
| `threeMonthsNmr` | `Nmr` |  |

### `SwReturnsValue`

<a id="swreturnsvalue"></a>
Average Stake Weighted Returns

| Field | Type | Description |
|-------|------|-------------|
| `allTime` | `Float` |  |
| `allTimeNmr` | `Nmr` |  |
| `date` | `Date` |  |
| `oneYear` | `Float` |  |
| `oneYearNmr` | `Nmr` |  |
| `threeMonths` | `Float` |  |
| `threeMonthsNmr` | `Nmr` |  |

### `SymbolPriceConversion`

<a id="symbolpriceconversion"></a>

| Field | Type | Description |
|-------|------|-------------|
| `baseSymbol` | `String` |  |
| `lastUpdated` | `String` |  |
| `price` | `String` |  |
| `targetSymbol` | `String` |  |

### `TierLeaderboard`

<a id="tierleaderboard"></a>

| Field | Type | Description |
|-------|------|-------------|
| `leaderboard` | [`[LeaderboardEntry]`](#leaderboardentry) |  |
| `tierDescription` | `String` |  |
| `tierName` | `String` |  |
| `tierNumber` | `Int` |  |

### `TitleInfo`

<a id="titleinfo"></a>

| Field | Type | Description |
|-------|------|-------------|
| `title` | `String` |  |
| `titleDescription` | `String` |  |

### `Tournament`

<a id="tournament"></a>

| Field | Type | Description |
|-------|------|-------------|
| `active` | `Boolean` |  |
| `id` | `ID` |  |
| `name` | `String` |  |
| `rounds` | [`[Round]`](#round) |  |
| `tournament` | `Int` |  |

### `TypedMedalCounts`

<a id="typedmedalcounts"></a>

| Field | Type | Description |
|-------|------|-------------|
| `counts` | [`MedalCounts`](#medalcounts) |  |
| `type` | `String` |  |

### `UserPayouts`

<a id="userpayouts"></a>

| Field | Type | Description |
|-------|------|-------------|
| `actual` | [`[Payout]`](#payout) |  |
| `pending` | [`[Payout]`](#payout) |  |

### `UserScore`

<a id="userscore"></a>

| Field | Type | Description |
|-------|------|-------------|
| `date` | `Time` |  |
| `displayName` | `String` |  |
| `rank` | `Int` |  |
| `reputation` | `Float` |  |
| `stakedRank` | `Int` |  |

### `V2ChangeStakeRequest`

<a id="v2changestakerequest"></a>

| Field | Type | Description |
|-------|------|-------------|
| `drain` | `Boolean` |  |
| `dueDate` | `Time` |  |
| `id` | `String` |  |
| `requestedAmount` | `String` |  |
| `status` | `String` |  |
| `type` | `String` |  |

### `V2Diagnostics`

<a id="v2diagnostics"></a>

| Field | Type | Description |
|-------|------|-------------|
| `computePickleUploadId` | `String` |  |
| `erasAcceptedCount` | `Int` |  |
| `erasMissing` | `[String]` |  |
| `examplePredsCorrMean` | `Float` |  |
| `filename` | `String` |  |
| `id` | `String` |  |
| `insertedAt` | `Time` |  |
| `message` | `String` |  |
| `parentId` | `String` |  |
| `perEraDiagnostics` | [`[V2DiagnosticsEras]`](#v2diagnosticseras) |  |
| `processSecs` | `Float` |  |
| `status` | `String` |  |
| `tb200Diagnostics` | [`V2Diagnostics`](#v2diagnostics) |  |
| `tickersAcceptedCount` | `Int` |  |
| `tickersSubmittedCount` | `Int` |  |
| `topBottom` | `Int` |  |
| `tournament` | `Int` |  |
| `trainedOnVal` | `Boolean` |  |
| `updatedAt` | `Time` |  |
| `validationAdjustedSharpe` | `Float` |  |
| `validationAlphaCorrWExamplePreds` | `Float` |  |
| `validationAlphaMaxDrawdown` | `Float` |  |
| `validationAlphaMean` | `Float` |  |
| `validationAlphaSharpe` | `Float` |  |
| `validationAlphaStd` | `Float` |  |
| `validationApy` | `Float` |  |
| `validationAutocorr` | `Float` |  |
| `validationBmcMean` | `Float` |  |
| `validationChurnMax` | `Float` |  |
| `validationChurnMean` | `Float` |  |
| `validationChurnStd` | `Float` |  |
| `validationCorrCorrWExamplePreds` | `Float` |  |
| `validationCorrMaxDrawdown` | `Float` |  |
| `validationCorrMean` | `Float` |  |
| `validationCorrMeanRating` | `Float` |  |
| `validationCorrPlusMmcMean` | `Float` |  |
| `validationCorrPlusMmcMeanRating` | `Float` |  |
| `validationCorrPlusMmcSharpe` | `Float` |  |
| `validationCorrPlusMmcSharpeDiff` | `Float` |  |
| `validationCorrPlusMmcSharpeDiffRating` | `Float` |  |
| `validationCorrPlusMmcSharpeRating` | `Float` |  |
| `validationCorrPlusMmcStd` | `Float` |  |
| `validationCorrPlusMmcStdRating` | `Float` |  |
| `validationCorrSharpe` | `Float` |  |
| `validationCorrSharpeRating` | `Float` |  |
| `validationCorrStd` | `Float` |  |
| `validationCorrStdRating` | `Float` |  |
| `validationCorrV4CorrWExamplePreds` | `Float` |  |
| `validationCorrV4MaxDrawdown` | `Float` |  |
| `validationCorrV4Mean` | `Float` |  |
| `validationCorrV4Sharpe` | `Float` |  |
| `validationCorrV4Std` | `Float` |  |
| `validationFeatureCorrMax` | `Float` |  |
| `validationFeatureCorrMaxRating` | `Float` |  |
| `validationFeatureNeutralCorrMean` | `Float` |  |
| `validationFeatureNeutralCorrMeanRating` | `Float` |  |
| `validationFeatureNeutralCorrV3Mean` | `Float` |  |
| `validationFeatureNeutralCorrV3MeanRating` | `Float` |  |
| `validationFncV4CorrWExamplePreds` | `Float` |  |
| `validationFncV4MaxDrawdown` | `Float` |  |
| `validationFncV4Mean` | `Float` |  |
| `validationFncV4Sharpe` | `Float` |  |
| `validationFncV4Std` | `Float` |  |
| `validationIcV2CorrWExamplePreds` | `Float` |  |
| `validationIcV2MaxDrawdown` | `Float` |  |
| `validationIcV2Mean` | `Float` |  |
| `validationIcV2Sharpe` | `Float` |  |
| `validationIcV2Std` | `Float` |  |
| `validationMaxDrawdown` | `Float` |  |
| `validationMaxDrawdownRating` | `Float` |  |
| `validationMmcMean` | `Float` |  |
| `validationMmcMeanRating` | `Float` |  |
| `validationMmcSharpe` | `Float` |  |
| `validationMmcSharpeRating` | `Float` |  |
| `validationMmcStd` | `Float` |  |
| `validationMmcStdRating` | `Float` |  |
| `validationRicCorrWExamplePreds` | `Float` |  |
| `validationRicMaxDrawdown` | `Float` |  |
| `validationRicMean` | `Float` |  |
| `validationRicSharpe` | `Float` |  |
| `validationRicStd` | `Float` |  |
| `validationTurnoverMax` | `Float` |  |
| `validationTurnoverMean` | `Float` |  |
| `validationTurnoverStd` | `Float` |  |

### `V2DiagnosticsEras`

<a id="v2diagnosticseras"></a>

| Field | Type | Description |
|-------|------|-------------|
| `era` | `String` |  |
| `examplePredsCorr` | `Float` |  |
| `validationAlpha` | `Float` |  |
| `validationBmc` | `Float` |  |
| `validationChurn` | `Float` |  |
| `validationCorr` | `Float` |  |
| `validationCorrV4` | `Float` |  |
| `validationFeatureCorrMax` | `Float` |  |
| `validationFeatureNeutralCorr` | `Float` |  |
| `validationFeatureNeutralCorrV3` | `Float` |  |
| `validationFncV4` | `Float` |  |
| `validationIcV2` | `Float` |  |
| `validationMmc` | `Float` |  |
| `validationRic` | `Float` |  |
| `validationTurnover` | `Float` |  |

### `V2LeaderboardEntry`

<a id="v2leaderboardentry"></a>

| Field | Type | Description |
|-------|------|-------------|
| `bmcRep` | `Float` |  |
| `canonCorrLtm` | `Float` |  |
| `canonCorrRankLtm` | `Int` |  |
| `canonMmcLtm` | `Float` |  |
| `canonMmcRankLtm` | `Int` |  |
| `corj60Rep` | `Float` |  |
| `corr20Rep` | `Float` |  |
| `corr20V2Rep` | `Float` |  |
| `corr60Rep` | `Float` |  |
| `cort20Rep` | `Float` |  |
| `fncRep` | `Float` |  |
| `fncV3Rep` | `Float` |  |
| `id` | `ID` |  |
| `isActive` | `Boolean` |  |
| `latestUserScores` | [`[UserScore]`](#userscore) |  |
| `mmc60Rep` | `Float` |  |
| `mmcRep` | `Float` |  |
| `nmrStaked` | `Nmr` |  |
| `nmrStakedRank` | `Int` |  |
| `profileUrl` | `String` |  |
| `rank` | `Int` |  |
| `rankChange1d` | `Int` |  |
| `rankChange1y` | `Int` |  |
| `rankChange3m` | `Int` |  |
| `return13Weeks` | `Float` |  |
| `return13WeeksRank` | `Int` |  |
| `return1Day` | `Float` |  |
| `return1DayRank` | `Int` |  |
| `return52Weeks` | `Float` |  |
| `return52WeeksRank` | `Int` |  |
| `storedRank` | `Int` |  |
| `tcRep` | `Float` |  |
| `team` | `Boolean` |  |
| `username` | `String` |  |

### `V2NmrTransfer`

<a id="v2nmrtransfer"></a>

| Field | Type | Description |
|-------|------|-------------|
| `blockTimestamp` | `Time` |  |
| `fromAddress` | `String` |  |
| `logIndex` | `Int` |  |
| `status` | `String` |  |
| `toAddress` | `String` |  |
| `txHash` | `String` |  |
| `value` | `String` |  |

### `V2Overview`

<a id="v2overview"></a>

| Field | Type | Description |
|-------|------|-------------|
| `returns` | [`SwReturns`](#swreturns) | Average stake weighted returns |
| `stakedAccounts` | [`[StakedAccountsCount]`](#stakedaccountscount) | Time series count of distinct accounts with a staked submission in a currently unresolved round |
| `stakedModels` | [`[StakedModelsCount]`](#stakedmodelscount) | Time series count of distinct models with a staked submission in a currently unresolved round |
| `stakedSubmissions` | `Int` |  |
| `totalAccounts` | `Int` | Count of distinct accounts with a submission in the last 12 months |
| `totalAtRisk` | `Nmr` |  |
| `totalAtStake` | `Nmr` |  |
| `totalStakes` | `Int` |  |
| `tournament` | `Int` |  |

### `V2RoundModelPerformance`

<a id="v2roundmodelperformance"></a>

| Field | Type | Description |
|-------|------|-------------|
| `allSubmissionScores` | [`[SubmissionScore]`](#submissionscore) | All submission scores for the round (includes all versions of all scores) |
| `atRisk` | `Nmr` |  |
| `churnThreshold` | `Float` |  |
| `corrMultiplier` | `Float` |  |
| `intraRoundSubmissionScores` | [`[SubmissionScore]`](#submissionscore) | Daily official submission scores for the round |
| `mmcMultiplier` | `Float` |  |
| `prevWeekChurnMax` | `Float` |  |
| `prevWeekTurnoverMax` | `Float` |  |
| `roundCloseStakingTime` | `Time` |  |
| `roundDataDatestamp` | `Int` |  |
| `roundId` | `ID` |  |
| `roundNumber` | `Int` |  |
| `roundOpenTime` | `Time` |  |
| `roundPayoutFactor` | `String` |  |
| `roundResolveTime` | `Time` |  |
| `roundResolved` | `Boolean` |  |
| `roundScoreTime` | `Time` |  |
| `roundTarget` | `String` |  |
| `submissionId` | `ID` |  |
| `submissionScores` | [`[SubmissionScore]`](#submissionscore) | Latest official submission scores for the round |
| `tcMultiplier` | `Float` |  |
| `tickersAcceptedCount` | `Int` |  |
| `tickersSubmittedCount` | `Int` |  |
| `turnoverThreshold` | `Float` |  |

### `V2Stake`

<a id="v2stake"></a>

| Field | Type | Description |
|-------|------|-------------|
| `latestValue` | `Nmr` |  |
| `latestValueSettled` | `Nmr` |  |
| `pendingV2ChangeStakeRequest` | [`V2ChangeStakeRequest`](#v2changestakerequest) |  |
| `stakeValue` | `Nmr` |  |
| `status` | `String` |  |
| `tournamentNumber` | `Int` |  |
| `txHash` | `String` |  |

### `V2Submission`

<a id="v2submission"></a>

| Field | Type | Description |
|-------|------|-------------|
| `corrWithExamplePreds` | `Float` |  |
| `dataDatestamp` | `Int` |  |
| `diagnosticStatus` | `String` |  |
| `errorInfo` | `String` |  |
| `filename` | `String` |  |
| `filteredCount` | `Int` |  |
| `firstEffectiveDate` | `Time` |  |
| `hasDiagnostics` | `Boolean` |  |
| `hasHistoric` | `Boolean` |  |
| `historicMaxDrawdown` | `Float` |  |
| `historicMean` | `Float` |  |
| `historicSharpe` | `Float` |  |
| `historicStd` | `Float` |  |
| `id` | `ID` |  |
| `insertedAt` | `Time` |  |
| `invalidTickers` | `String` |  |
| `notes` | `String` |  |
| `prevWeekChurnMax` | `Float` |  |
| `prevWeekTurnoverMax` | `Float` |  |
| `round` | [`Round`](#round) |  |
| `selected` | `Boolean` |  |
| `sourceIp` | `String` |  |
| `sourcePlatform` | `String` |  |
| `status` | `String` |  |
| `submissionIp` | `String` |  |
| `submittedCount` | `Int` |  |
| `tickersAcceptedCount` | `Int` |  |
| `tickersSubmittedCount` | `Int` |  |
| `trainedOnVal` | `Boolean` |  |
| `triggerId` | `String` |  |
| `validationApy` | `Float` |  |
| `validationCorrPlusMmcMean` | `Float` |  |
| `validationCorrPlusMmcMeanRating` | `Int` |  |
| `validationCorrPlusMmcSharpe` | `Float` |  |
| `validationCorrPlusMmcSharpeDiff` | `Float` |  |
| `validationCorrPlusMmcSharpeDiffRating` | `Int` |  |
| `validationCorrPlusMmcSharpeRating` | `Int` |  |
| `validationCorrelation` | `Float` |  |
| `validationCorrelationRating` | `Int` |  |
| `validationErasAccepted` | `Int` |  |
| `validationErasSubmitted` | `Int` |  |
| `validationFeatureExposure` | `Float` |  |
| `validationFeatureNeutralMean` | `Float` |  |
| `validationFeatureNeutralMeanRating` | `Int` |  |
| `validationMaxDrawdown` | `Float` |  |
| `validationMaxDrawdownRating` | `Int` |  |
| `validationMaxFeatureExposure` | `Float` |  |
| `validationMaxFeatureExposureRating` | `Int` |  |
| `validationMmcMean` | `Float` |  |
| `validationMmcMeanRating` | `Int` |  |
| `validationSharpe` | `Float` |  |
| `validationSharpeRating` | `Int` |  |
| `validationStd` | `Float` |  |
| `validationStdRating` | `Int` |  |
| `validationTickersAccepted` | `Int` |  |
| `validationTickersSubmitted` | `Int` |  |

### `V3StakeAuthorization`

<a id="v3stakeauthorization"></a>

| Field | Type | Description |
|-------|------|-------------|
| `authorizationDigest` | `String` |  |
| `authorizationSigner` | `String` |  |
| `chainId` | `String` |  |
| `deadline` | `String` |  |
| `maxAmount` | `String` |  |
| `modelId` | `String` |  |
| `nmrAddress` | `String` |  |
| `nonce` | `String` |  |
| `roundId` | `String` |  |
| `signature` | `String` |  |
| `staker` | `String` |  |
| `stakingAddress` | `String` |  |
| `submissionHash` | `String` |  |
| `submissionId` | `String` |  |
| `tournamentId` | `String` |  |

### `V3StakeClaim`

<a id="v3stakeclaim"></a>

| Field | Type | Description |
|-------|------|-------------|
| `apiModelId` | `ID` |  |
| `burnAmountWei` | `String` |  |
| `merkleRoot` | `String` |  |
| `modelId` | `String` |  |
| `payoutAmountWei` | `String` |  |
| `proof` | `[String]` |  |
| `roundId` | `String` |  |
| `staker` | `String` |  |
| `submissionId` | `ID` |  |
| `tournamentId` | `String` |  |

### `V3StakeConfig`

<a id="v3stakeconfig"></a>

| Field | Type | Description |
|-------|------|-------------|
| `address` | `String` |  |
| `authorizationSigner` | `String` |  |
| `nmrAddress` | `String` |  |
| `owner` | `String` |  |
| `paused` | `Boolean` |  |
| `pendingOwner` | `String` |  |
| `serviceWallet` | `String` |  |

### `V3StakeRound`

<a id="v3stakeround"></a>

| Field | Type | Description |
|-------|------|-------------|
| `closeTime` | `String` |  |
| `merkleRoot` | `String` |  |
| `openTime` | `String` |  |
| `payoutFactor` | `String` |  |
| `remainingBurn` | `String` |  |
| `remainingPayout` | `String` |  |
| `resolveTime` | `String` |  |
| `resolved` | `Boolean` |  |
| `roundId` | `String` |  |
| `stakeCap` | `String` |  |
| `stakeThreshold` | `String` |  |
| `state` | `String` |  |
| `totalPayout` | `String` |  |
| `totalStaked` | `String` |  |
| `tournamentId` | `String` |  |

### `V3StakeWallet`

<a id="v3stakewallet"></a>

| Field | Type | Description |
|-------|------|-------------|
| `nmrAddress` | `String` |  |
| `serviceWallet` | `String` |  |
| `stakingAddress` | `String` |  |
| `stakingAllowance` | `String` |  |
| `walletBalance` | `String` |  |

### `V3UserProfile`

<a id="v3userprofile"></a>

| Field | Type | Description |
|-------|------|-------------|
| `accountName` | `String` |  |
| `bio` | `String` |  |
| `computeEnabled` | `Boolean` |  |
| `computeLiteEnabled` | `Boolean` |  |
| `control` | `Float` |  |
| `dailyModelPerformances` | [`[DailyModelPerformance]`](#dailymodelperformance) |  |
| `id` | `ID` |  |
| `isActive` | `Boolean` |  |
| `latestRanks` | [`Ranks`](#ranks) |  |
| `latestReps` | [`Reps`](#reps) |  |
| `latestReturns` | [`Returns`](#returns) |  |
| `latestSubmissionScores` | [`[SubmissionScore]`](#submissionscore) |  |
| `latestUserScores` | [`[UserScore]`](#userscore) |  |
| `linkText` | `String` |  |
| `linkUrl` | `String` |  |
| `nmrStaked` | `Nmr` |  |
| `profileUrl` | `String` |  |
| `returns` | [`[ReturnsValue]`](#returnsvalue) |  |
| `roundModelPerformances` | [`[RoundModelPerformance]`](#roundmodelperformance) |  |
| `stakeInfo` | [`PayoutSelection`](#payoutselection) |  |
| `stakeValue` | `Nmr` |  |
| `stakeValues` | [`[StakeValue]`](#stakevalue) |  |
| `startDate` | `Time` |  |
| `team` | `Boolean` |  |
| `tournament` | `Int` |  |
| `typedMedals` | [`[TypedMedalCounts]`](#typedmedalcounts) |  |
| `username` | `String` |  |

### `W9Info`

<a id="w9info"></a>

| Field | Type | Description |
|-------|------|-------------|
| `address` | `String` |  |
| `businessName` | `String` |  |
| `city` | `String` |  |
| `exemptions` | `String` |  |
| `fullName` | `String` |  |
| `insertedAt` | `Time` |  |
| `otherTaxClassDetail` | `String` |  |
| `signature` | `String` |  |
| `state` | `String` |  |
| `taxClass` | [`TaxClassEnum`](#taxclassenum) |  |
| `taxYear` | `String` |  |
| `taxpayerIdentificationNumber` | `String` |  |
| `updatedAt` | `Time` |  |
| `zipCode` | `String` |  |

### `WalletTxn`

<a id="wallettxn"></a>

| Field | Type | Description |
|-------|------|-------------|
| `amount` | `Nmr` |  |
| `from` | `String` |  |
| `status` | `String` |  |
| `time` | `Time` |  |
| `to` | `String` |  |
| `tournament` | `Int` |  |
| `txHash` | `String` |  |
| `type` | `String` |  |

## Input objects

### `KaggleProfileDataInput`

<a id="kaggleprofiledatainput"></a>

| Field | Type | Description |
|-------|------|-------------|
| `accountCreated` | `String` |  |
| `bio` | `String` |  |
| `displayName` | `String` |  |
| `profileId` | `String` |  |
| `tier` | `String` |  |

## Enums

### `AccountStatusEnum`

<a id="accountstatusenum"></a>
| Value | Description |
|-------|-------------|
| `CREATED` |  |
| `DELETED` |  |
| `FLAGGED` |  |
| `UNVERIFIED` |  |
| `VERIFIED` |  |

### `DefaultCurrencyEnum`

<a id="defaultcurrencyenum"></a>
| Value | Description |
|-------|-------------|
| `AUD` |  |
| `CAD` |  |
| `CNY` |  |
| `EUR` |  |
| `GBP` |  |
| `JPY` |  |
| `MXN` |  |
| `USD` |  |
| `ZAR` |  |

### `RoundStatus`

<a id="roundstatus"></a>
| Value | Description |
|-------|-------------|
| `OPEN` |  |
| `RESOLVED` |  |
| `RESOLVING` |  |
| `UPCOMING` |  |

### `SupportRequestIssueStatusEnum`

<a id="supportrequestissuestatusenum"></a>
| Value | Description |
|-------|-------------|
| `COMPLETED` |  |
| `INPROGRESS` |  |
| `SUBMITTED` |  |

### `SupportRequestTypeEnum`

<a id="supportrequesttypeenum"></a>
| Value | Description |
|-------|-------------|
| `BUG_REPORT` |  |
| `FEATURE_REQUEST` |  |
| `LIMIT_INCREASE` |  |
| `SECURITY_REPORT` |  |

### `TaxClassEnum`

<a id="taxclassenum"></a>
Federal Tax Classification

| Value | Description |
|-------|-------------|
| `C_CORP` | C Corporation |
| `LLC_C_CORP` | LLC - C Corporation |
| `LLC_PARTNERSHIP` | LLC - Partnership |
| `LLC_S_CORP` | LLC - S Corporation |
| `OTHER` | Other |
| `PARTNERSHIP` | Partnership |
| `S_CORP` | S Corporation |
| `SOLE_PROPRIETOR` | Individual/sole proprieter or single-member LLC |
| `TRUST_ESTATE` | Trust/estate |

## Scalars

- `Boolean` — The `Boolean` scalar type represents `true` or `false`.
- `Date` — The `Date` scalar type represents a date. The Date appears in a JSON response as an ISO8601 formatted string, without a time component.
- `Float` — The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point).
- `ID` — The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.
- `Int` — The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between `-(2^53 - 1)` and `2^53 - 1` since it is represented in JSON as double-precision floating point numbers specified by [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point).
- `Nmr` — Formatted NMR strings
- `String` — The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.
- `Time` — ISOz time
- `Usd` — Formatted USD strings
