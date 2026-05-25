"""
Pydantic models generated from the Numerai GraphQL schema.

DO NOT EDIT BY HAND. Regenerate with:

    python scripts/codegen.py

All fields are Optional because a GraphQL response only contains the fields
named in the selection set. Custom scalars (Nmr, Usd, Date, Time) are mapped
to str — they come back as strings from the API.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

# --- Enums ---

class AccountStatusEnum(str, Enum):
    CREATED = "CREATED"
    DELETED = "DELETED"
    FLAGGED = "FLAGGED"
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"

class DefaultCurrencyEnum(str, Enum):
    AUD = "AUD"
    CAD = "CAD"
    CNY = "CNY"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    MXN = "MXN"
    USD = "USD"
    ZAR = "ZAR"

class RoundStatus(str, Enum):
    OPEN = "OPEN"
    RESOLVED = "RESOLVED"
    RESOLVING = "RESOLVING"
    UPCOMING = "UPCOMING"

class SupportRequestIssueStatusEnum(str, Enum):
    COMPLETED = "COMPLETED"
    INPROGRESS = "INPROGRESS"
    SUBMITTED = "SUBMITTED"

class SupportRequestTypeEnum(str, Enum):
    BUG_REPORT = "BUG_REPORT"
    FEATURE_REQUEST = "FEATURE_REQUEST"
    LIMIT_INCREASE = "LIMIT_INCREASE"
    SECURITY_REPORT = "SECURITY_REPORT"

class TaxClassEnum(str, Enum):
    """Federal Tax Classification"""
    C_CORP = "C_CORP"
    LLC_C_CORP = "LLC_C_CORP"
    LLC_PARTNERSHIP = "LLC_PARTNERSHIP"
    LLC_S_CORP = "LLC_S_CORP"
    OTHER = "OTHER"
    PARTNERSHIP = "PARTNERSHIP"
    S_CORP = "S_CORP"
    SOLE_PROPRIETOR = "SOLE_PROPRIETOR"
    TRUST_ESTATE = "TRUST_ESTATE"

# --- Input objects ---

class KaggleProfileDataInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    accountCreated: Optional[str] = None
    bio: Optional[str] = None
    displayName: Optional[str] = None
    profileId: Optional[str] = None
    tier: Optional[str] = None

# --- Object types ---

class Account(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    acceptedTos: Optional[bool] = None
    achievements: Optional[list["Achievement"]] = None
    aiManagerExperience: Optional[bool] = None
    apiTokens: Optional[list["ApiToken"]] = None
    availableNmr: Optional[str] = None
    availableStakeCredit: Optional[str] = None
    bannerUrl: Optional[str] = None
    bio: Optional[str] = None
    defaultCurrency: Optional[str] = None
    defaultCurrencySymbol: Optional[str] = None
    discordLinkToken: Optional[str] = None
    discordUsername: Optional[str] = None
    displayName: Optional[str] = None
    email: Optional[str] = None
    emailPreferences: Optional["EmailPreferences"] = None
    github: Optional[str] = None
    heldForFusionStakes: Optional[str] = None
    heldForPendingWithdrawals: Optional[str] = None
    heldForScheduledStakeIncreases: Optional[str] = None
    hideOnboardingTutorials: Optional[bool] = None
    id: Optional[str] = None
    insertedAt: Optional[str] = None
    isBeta: Optional[bool] = None
    isTestPilot: Optional[bool] = None
    kaggle: Optional[str] = None
    kaggleVerified: Optional[bool] = None
    linkedin: Optional[str] = None
    location: Optional[str] = None
    maxModelSlots: Optional[int] = None
    mfaEnabled: Optional[bool] = None
    models: Optional[list["Model"]] = None
    nmrReturns: Optional["NmrReturnStats"] = None
    occupation: Optional[str] = None
    onChainWalletBalance: Optional[str] = None
    organization: Optional[str] = None
    pendingTxns: Optional[list["WalletTxn"]] = None
    profileUrl: Optional[str] = None
    reports: Optional[list["Reports"]] = None
    returns: Optional["SwReturns"] = None
    returnsValues: Optional[list["SwReturnsValue"]] = None
    scheduledStakeTxns: Optional[list["ScheduledStakeTxn"]] = None
    status: Optional["AccountStatusEnum"] = None
    title: Optional[str] = None
    totalStakeValue: Optional[list["StakeValue"]] = None
    totalStakeValues: Optional[list["StakeValue"]] = None
    tutorials: Optional["AccountTutorials"] = None
    twitter: Optional[str] = None
    updatedAt: Optional[str] = None
    username: Optional[str] = None
    w9Info: Optional["W9Info"] = None
    walletAddress: Optional[str] = None
    walletTxns: Optional[list["WalletTxn"]] = None
    website: Optional[str] = None

class AccountLeaderboardEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    alpha: Optional[float] = None
    bio: Optional[str] = None
    bmc: Optional[float] = None
    corJ60: Optional[float] = None
    corr: Optional[float] = None
    corr60: Optional[float] = None
    corrV4: Optional[float] = None
    cort20: Optional[float] = None
    displayName: Optional[str] = None
    fncV3: Optional[float] = None
    fncV4: Optional[float] = None
    icV2: Optional[float] = None
    id: Optional[str] = None
    mmc: Optional[float] = None
    mmc60: Optional[float] = None
    mpc: Optional[float] = None
    nmrStaked: Optional[str] = None
    profileUrl: Optional[str] = None
    rank: Optional[int] = None
    rankChange1d: Optional[int] = None
    rankChange1y: Optional[int] = None
    rankChange3m: Optional[int] = None
    return1y: Optional[float] = None
    return1yNmr: Optional[str] = None
    return3m: Optional[float] = None
    return3mNmr: Optional[str] = None
    returnAllTime: Optional[float] = None
    returnAllTimeNmr: Optional[str] = None
    ric: Optional[float] = None
    storedRank: Optional[int] = None
    tc: Optional[float] = None
    team: Optional[bool] = None
    title: Optional[str] = None
    username: Optional[str] = None
    v2Corr20: Optional[float] = None

class AccountProfile(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    acceptedTos: Optional[bool] = None
    achievements: Optional[list["Achievement"]] = None
    bannerUrl: Optional[str] = None
    bio: Optional[str] = None
    discord: Optional["DiscordInfo"] = None
    displayName: Optional[str] = None
    github: Optional[str] = None
    id: Optional[str] = None
    isActive: Optional[bool] = None
    kaggle: Optional[str] = None
    kaggleTier: Optional[str] = None
    kaggleVerified: Optional[bool] = None
    linkedin: Optional[str] = None
    location: Optional[str] = None
    models: Optional[list["ModelProfile"]] = None
    occupation: Optional[str] = None
    organization: Optional[str] = None
    profileUrl: Optional[str] = None
    returns: Optional["SwReturns"] = None
    returnsTs: Optional[list["SwReturnsValue"]] = None
    scores: Optional["AccountScores"] = None
    scoresTs: Optional[list["AccountScores"]] = None
    startDate: Optional[str] = None
    team: Optional[bool] = None
    title: Optional[str] = None
    totalStake: Optional[str] = None
    totalStakeTs: Optional[list["AccountStakeValue"]] = None
    tournament: Optional[int] = None
    twitter: Optional[str] = None
    username: Optional[str] = None
    website: Optional[str] = None

class AccountScores(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    alpha: Optional[float] = None
    alphaLtm: Optional[float] = None
    alphaLtmRank: Optional[int] = None
    corr: Optional[float] = None
    corr60: Optional[float] = None
    corr60Ltm: Optional[float] = None
    corr60LtmRank: Optional[int] = None
    corrLtm: Optional[float] = None
    corrLtmRank: Optional[int] = None
    date: Optional[str] = None
    fncV4: Optional[float] = None
    fncV4Ltm: Optional[float] = None
    fncV4LtmRank: Optional[int] = None
    mmc: Optional[float] = None
    mmc60: Optional[float] = None
    mmc60Ltm: Optional[float] = None
    mmc60LtmRank: Optional[int] = None
    mmcLtm: Optional[float] = None
    mmcLtmRank: Optional[int] = None
    mpc: Optional[float] = None
    mpcLtm: Optional[float] = None
    mpcLtmRank: Optional[int] = None
    seasonRank: Optional[int] = None
    tc: Optional[float] = None
    tcLtm: Optional[float] = None
    tcLtmRank: Optional[int] = None
    v2Corr20: Optional[float] = None
    v2Corr20Ltm: Optional[float] = None
    v2Corr20LtmRank: Optional[int] = None

class AccountStakeValue(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    date: Optional[str] = None
    delta: Optional[str] = None
    time: Optional[str] = None
    value: Optional[str] = None

class AccountTutorials(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    numerai: Optional["NumeraiTutorials"] = None
    signals: Optional["SignalsTutorials"] = None

class Achievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    date: Optional[str] = None
    rank: Optional[int] = None
    score: Optional[float] = None
    season: Optional[str] = None
    tier: Optional[str] = None
    tournament: Optional[int] = None
    type: Optional[str] = None

class ActivityFeedEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    accountId: Optional[str] = None
    activityType: Optional[str] = None
    avatar: Optional[str] = None
    description: Optional[str] = None
    eventAt: Optional[str] = None
    id: Optional[str] = None
    insertedAt: Optional[str] = None
    tournamentId: Optional[str] = None
    username: Optional[str] = None

class ApiToken(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    name: Optional[str] = None
    publicId: Optional[str] = None
    scopes: Optional[list[str]] = None

class ApiTokenInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    accountUsername: Optional[str] = None
    name: Optional[str] = None
    publicId: Optional[str] = None
    scopes: Optional[list[str]] = None

class ApiTokenWithSecret(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    name: Optional[str] = None
    publicId: Optional[str] = None
    scopes: Optional[list[str]] = None
    secretKey: Optional[str] = None

class Banner(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    expirationDate: Optional[str] = None
    type: Optional[str] = None

class ComputePickleDataVersion(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    default: Optional[bool] = None
    deprecated: Optional[bool] = None
    experimental: Optional[bool] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    version: Optional[str] = None

class ComputePickleDockerImage(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    default: Optional[bool] = None
    deprecated: Optional[bool] = None
    experimental: Optional[bool] = None
    id: Optional[str] = None
    image: Optional[str] = None
    insertedAt: Optional[str] = None
    name: Optional[str] = None
    tag: Optional[str] = None

class ComputePickleTrigger(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    computePickleUploadId: Optional[str] = None
    id: Optional[str] = None
    insertedAt: Optional[str] = None
    roundId: Optional[str] = None
    status: Optional[str] = None
    statuses: Optional[list["ComputePickleTriggerStatus"]] = None
    submissionId: Optional[str] = None
    type: Optional[str] = None
    updatedAt: Optional[str] = None

class ComputePickleTriggerStatus(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    computePickleTriggerId: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    insertedAt: Optional[str] = None
    status: Optional[str] = None
    updatedAt: Optional[str] = None

class ComputePickleUpload(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    assignedModelSlots: Optional[list[str]] = None
    dataVersion: Optional[str] = None
    dataVersionId: Optional[str] = None
    diagnosticsId: Optional[str] = None
    diagnosticsStatus: Optional[str] = None
    diagnosticsStatusDescription: Optional[str] = None
    dockerImage: Optional[str] = None
    dockerImageId: Optional[str] = None
    dockerImageName: Optional[str] = None
    filename: Optional[str] = None
    id: Optional[str] = None
    insertedAt: Optional[str] = None
    label: Optional[str] = None
    modelId: Optional[str] = None
    runtime: Optional[str] = None
    triggerStatus: Optional[str] = None
    triggers: Optional[list["ComputePickleTrigger"]] = None
    updatedAt: Optional[str] = None
    validationStatus: Optional[str] = None
    version: Optional[int] = None

class CryptosignalsLeaderboardEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    canonCorrLtm: Optional[float] = None
    canonCorrRankLtm: Optional[int] = None
    canonMmcLtm: Optional[float] = None
    canonMmcRankLtm: Optional[int] = None
    canonTcLtm: Optional[float] = None
    computeEnabled: Optional[bool] = None
    control: Optional[float] = None
    corrRank: Optional[int] = None
    corrRep: Optional[float] = None
    id: Optional[str] = None
    isActive: Optional[bool] = None
    latestUserScores: Optional[list["UserScore"]] = None
    mmcRank: Optional[int] = None
    mmcRep: Optional[float] = None
    nmrStaked: Optional[str] = None
    profileUrl: Optional[str] = None
    rank: Optional[int] = None
    rankChange1d: Optional[int] = None
    rankChange1y: Optional[int] = None
    rankChange3m: Optional[int] = None
    return13Weeks: Optional[float] = None
    return1Day: Optional[float] = None
    return52Weeks: Optional[float] = None
    storedRank: Optional[int] = None
    team: Optional[bool] = None
    username: Optional[str] = None

class CryptosignalsOverview(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    returns: Optional["SwReturns"] = None
    returnsValues: Optional[list["SwReturnsValue"]] = None
    stakedAccounts: Optional[list["StakedAccountsCount"]] = None
    stakedAccountsLtm: Optional[int] = None
    stakedModels: Optional[list["StakedModelsCount"]] = None
    stakedSubmissions: Optional[int] = None
    totalAccounts: Optional[int] = None
    totalAtStake: Optional[str] = None
    totalAtStakeValues: Optional[list["StakeValue"]] = None
    totalStakes: Optional[int] = None

class CurrencyCode(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    code: Optional[str] = None
    symbol: Optional[str] = None

class DailyModelPerformance(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    alphaRank: Optional[int] = None
    alphaRep: Optional[float] = None
    apy: Optional[float] = None
    corr60Rank: Optional[int] = None
    corr60Rep: Optional[float] = None
    corrRank: Optional[int] = None
    corrRep: Optional[float] = None
    corrV4Rank: Optional[int] = None
    corrV4Rep: Optional[float] = None
    date: Optional[str] = None
    fncRank: Optional[int] = None
    fncRep: Optional[float] = None
    fncV3Rank: Optional[int] = None
    fncV3Rep: Optional[float] = None
    fncV4Rank: Optional[int] = None
    fncV4Rep: Optional[float] = None
    icRank: Optional[int] = None
    icRep: Optional[float] = None
    icV2Rank: Optional[int] = None
    icV2Rep: Optional[float] = None
    mmcRank: Optional[int] = None
    mmcRep: Optional[float] = None
    mpcRank: Optional[int] = None
    mpcRep: Optional[float] = None
    return13Weeks: Optional[float] = None
    return52Weeks: Optional[float] = None
    tcRank: Optional[int] = None
    tcRep: Optional[float] = None

class DiscordInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    userId: Optional[str] = None
    username: Optional[str] = None

class EarnQuestsProgress(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    firstDiagnostics: Optional[bool] = None
    firstStake: Optional[bool] = None
    firstSubmission: Optional[bool] = None
    madeFiveModels: Optional[bool] = None
    stakeSubmittedFourWeeks: Optional["QuestProgress"] = None

class EmailPreferences(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    compute: Optional[bool] = None
    cryptoRoundOpen: Optional[bool] = None
    cryptoRoundSummary: Optional[bool] = None
    cryptoSubmission: Optional[bool] = None
    deposit: Optional[bool] = None
    diagnostics: Optional[bool] = None
    modelUploadReceipt: Optional[bool] = None
    pickleRoundOpen: Optional[bool] = None
    pickleRoundStatus: Optional[bool] = None
    roundOpen: Optional[bool] = None
    roundSummary: Optional[bool] = None
    signalsRoundOpen: Optional[bool] = None
    signalsRoundSummary: Optional[bool] = None
    signalsSubmission: Optional[bool] = None
    stakeChange: Optional[bool] = None
    submission: Optional[bool] = None
    submissionSuccess: Optional[bool] = None
    submissionsStatus: Optional[bool] = None
    withdrawal: Optional[bool] = None

class EthPrice(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    lastUpdated: Optional[str] = None
    priceUsd: Optional[str] = None
    volume: Optional[str] = None

class FeatureFlag(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    enabled: Optional[bool] = None
    key: Optional[str] = None
    value: Optional[float] = None

class FileUploadAuth(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    accelerated: Optional[bool] = None
    countryCode: Optional[str] = None
    filename: Optional[str] = None
    url: Optional[str] = None

class GeoIp(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    code: Optional[str] = None
    ip: Optional[str] = None
    location: Optional[str] = None

class GhostBlogPost(BaseModel):
    """A blog post from the Ghost CMS"""
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    excerpt: Optional[str] = None
    featureImage: Optional[str] = None
    id: Optional[str] = None
    publishedAt: Optional[str] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    uuid: Optional[str] = None

class GrandmasterTierConfig(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    maxModelSlots: Optional[int] = None
    minimumStakeSubs: Optional[int] = None
    seasonId: Optional[str] = None
    tierName: Optional[str] = None
    tierNumber: Optional[int] = None
    topXPct: Optional[float] = None
    topXRank: Optional[int] = None
    tournament: Optional["Tournament"] = None
    year: Optional[int] = None

class HistogramData(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    bins: Optional[list[float]] = None
    counts: Optional[list[int]] = None

class InvocationLog(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    message: Optional[str] = None
    timestamp: Optional[int] = None

class KaggleVerificationResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    success: Optional[bool] = None

class KaggleVerificationTokenResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    token: Optional[str] = None

class LatestSubmission(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    filename: Optional[str] = None
    id: Optional[str] = None
    roundClose: Optional[str] = None
    roundCloseStaking: Optional[str] = None
    roundNumber: Optional[int] = None
    roundOpen: Optional[str] = None
    status: Optional[str] = None
    timestamp: Optional[str] = None

class LeaderboardEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    accountCorr: Optional[float] = None
    accountCorrRank: Optional[int] = None
    accountDisplayName: Optional[str] = None
    accountSeasonScore: Optional[float] = None
    accountSeasonScoreRank: Optional[float] = None
    accountTc: Optional[float] = None
    accountTcRank: Optional[int] = None
    accountTitle: Optional[str] = None
    accountUsername: Optional[str] = None
    cryptosignalsTitle: Optional[str] = None
    excludeFromSeason: Optional[bool] = None
    numeraiTitle: Optional[str] = None
    profileUrl: Optional[str] = None
    signalsTitle: Optional[str] = None

class MedalCounts(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    bronze: Optional[int] = None
    gold: Optional[int] = None
    silver: Optional[int] = None

class MetaModelHolding(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    latestPrice: Optional[str] = None
    logo: Optional[str] = None
    mmRank: Optional[int] = None
    symbol: Optional[str] = None
    value: Optional[float] = None

class MetaModelPage(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    lastUpdated: Optional[str] = None
    tableData: Optional[list["MetaModelHolding"]] = None
    totalAtStake: Optional[str] = None
    totalStakes: Optional[int] = None
    tournament: Optional[int] = None

class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    accountId: Optional[str] = None
    archived: Optional[bool] = None
    archivedAt: Optional[str] = None
    computeEnabled: Optional[bool] = None
    computeLiteEnabled: Optional[bool] = None
    computePickleUpload: Optional["ComputePickleUpload"] = None
    currentPayoutSelection: Optional["PayoutSelection"] = None
    description: Optional[str] = None
    earliestReleaseDate: Optional[str] = None
    hidden: Optional[bool] = None
    id: Optional[str] = None
    insertedAt: Optional[str] = None
    isComputeWeekdayEnabled: Optional[bool] = None
    latestSignalsSubmission: Optional[list["V2Submission"]] = None
    latestSignalsSubmissionV2: Optional["V2Submission"] = None
    latestSubmission: Optional[list["V2Submission"]] = None
    latestSubmissionV2: Optional["V2Submission"] = None
    latestSubmissions: Optional[list["LatestSubmission"]] = None
    latestUserScores: Optional[list["UserScore"]] = None
    name: Optional[str] = None
    nmrReturns: Optional["NmrReturnStats"] = None
    profileUrl: Optional[str] = None
    returns: Optional["Returns"] = None
    returnsValues: Optional[list["ReturnsValue"]] = None
    signalsStake: Optional["V2Stake"] = None
    signalsSubmissions: Optional[list["V2Submission"]] = None
    submissionWebhook: Optional[str] = None
    submissions: Optional[list["V2Submission"]] = None
    tournament: Optional[int] = None
    username: Optional[str] = None
    v2Stake: Optional["V2Stake"] = None

class ModelData(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    alpha: Optional[float] = None
    alphaPercentile: Optional[float] = None
    apcwnm: Optional[float] = None
    apcwnmPercentile: Optional[float] = None
    apcwsm: Optional[float] = None
    apcwsmPercentile: Optional[float] = None
    bmc: Optional[float] = None
    bmcPercentile: Optional[float] = None
    computeEnabled: Optional[bool] = None
    corj60: Optional[float] = None
    corj60Percentile: Optional[float] = None
    corr: Optional[float] = None
    corr20: Optional[float] = None
    corr20Percentile: Optional[float] = None
    corr60: Optional[float] = None
    corr60Percentile: Optional[float] = None
    corrMedal: Optional[str] = None
    corrPercentile: Optional[float] = None
    corrV4: Optional[float] = None
    corrV4Percentile: Optional[float] = None
    corrWMetaModel: Optional[float] = None
    corrWMetaModelPercentile: Optional[float] = None
    cort20: Optional[float] = None
    cort20Percentile: Optional[float] = None
    cwmm: Optional[float] = None
    cwmmPercentile: Optional[float] = None
    cwsnmm: Optional[float] = None
    cwsnmmPercentile: Optional[float] = None
    fnc: Optional[float] = None
    fncPercentile: Optional[float] = None
    fncV3: Optional[float] = None
    fncV3Percentile: Optional[float] = None
    fncV4: Optional[float] = None
    fncV4Percentile: Optional[float] = None
    icV2: Optional[float] = None
    icV2Percentile: Optional[float] = None
    id: Optional[str] = None
    mcwnm: Optional[float] = None
    mcwnmPercentile: Optional[float] = None
    mcwsm: Optional[float] = None
    mcwsmPercentile: Optional[float] = None
    mmc: Optional[float] = None
    mmc60: Optional[float] = None
    mmcMedal: Optional[str] = None
    mmcPercentile: Optional[float] = None
    modelName: Optional[str] = None
    mpc: Optional[float] = None
    mpcPercentile: Optional[float] = None
    payoutPending: Optional[str] = None
    payoutSettled: Optional[str] = None
    profileUrl: Optional[str] = None
    ric: Optional[float] = None
    ricPercentile: Optional[float] = None
    roundId: Optional[str] = None
    selectedStakeValue: Optional[str] = None
    tc: Optional[float] = None
    tcMedal: Optional[str] = None
    tcPercentile: Optional[float] = None
    team: Optional[bool] = None
    v2Corr20: Optional[float] = None
    v2Corr20Percentile: Optional[float] = None

class ModelProfile(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    accountId: Optional[str] = None
    alphaRep: Optional[float] = None
    corj60Rep: Optional[float] = None
    corr20V2Rep: Optional[float] = None
    corr60Rep: Optional[float] = None
    corrRep: Optional[float] = None
    corrV4Rep: Optional[float] = None
    displayName: Optional[str] = None
    fncV3Rep: Optional[float] = None
    fncV4Rep: Optional[float] = None
    icV2Rep: Optional[float] = None
    id: Optional[str] = None
    mmc60Rep: Optional[float] = None
    mmcRep: Optional[float] = None
    mpcRep: Optional[float] = None
    profileUrl: Optional[str] = None
    return1y: Optional[float] = None
    ricRep: Optional[float] = None
    stake: Optional[str] = None
    startDate: Optional[str] = None
    tcRep: Optional[float] = None
    tournament: Optional[int] = None
    username: Optional[str] = None

class Nftee(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    tokenId: Optional[int] = None

class NfteeContract(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    address: Optional[str] = None
    network: Optional[str] = None

class NfteeVoucher(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    secret: Optional[str] = None
    signature: Optional[str] = None
    tokenIds: Optional[list[int]] = None

class Nftees(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    nftees: Optional[list["Nftee"]] = None
    voucher: Optional["NfteeVoucher"] = None

class NmrPrice(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    lastUpdated: Optional[str] = None
    priceUsd: Optional[str] = None

class NmrReturnStats(BaseModel):
    """Legacy returns stats. Use Account.returns"""
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    sw1dReturn: Optional[float] = None
    sw1yReturn: Optional[float] = None
    sw3mReturn: Optional[float] = None

class Notification(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    bodyText: Optional[str] = None
    ctaButtonLink: Optional[str] = None
    ctaButtonText: Optional[str] = None
    data: Optional[str] = None
    id: Optional[str] = None
    titleText: Optional[str] = None

class NumeraiTutorials(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    discordConnected: Optional[bool] = None
    featureNeutralization: Optional[bool] = None
    helloNumerai: Optional[bool] = None
    kaggleConnected: Optional[bool] = None
    targetEnsemble: Optional[bool] = None

class Overview(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    averageThreeMonthsReturns: Optional[float] = None
    returns: Optional["SwReturns"] = None
    returnsValues: Optional[list["SwReturnsValue"]] = None
    stakeWeightedAverageThreeMonthsReturns: Optional[float] = None
    stakedAccounts: Optional[list["StakedAccountsCount"]] = None
    stakedAccountsLtm: Optional[int] = None
    stakedModels: Optional[list["StakedModelsCount"]] = None
    stakedSubmissions: Optional[int] = None
    totalAccounts: Optional[int] = None
    totalAtStake: Optional[str] = None
    totalAtStakeValues: Optional[list["StakeValue"]] = None
    totalNetEarnings: Optional[str] = None
    totalStakes: Optional[int] = None

class Payout(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    currencySymbol: Optional[str] = None
    modelDisplayName: Optional[str] = None
    modelId: Optional[str] = None
    modelName: Optional[str] = None
    payoutNmr: Optional[str] = None
    payoutValue: Optional[str] = None
    roundId: Optional[str] = None
    roundNumber: Optional[int] = None
    roundResolveTime: Optional[str] = None

class PayoutSelection(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    corrMultiplier: Optional[float] = None
    insertedAt: Optional[str] = None
    mmcMultiplier: Optional[float] = None
    payoutSelection: Optional[str] = None
    takeProfit: Optional[bool] = None
    tcMultiplier: Optional[float] = None
    updatedAt: Optional[str] = None
    userId: Optional[str] = None

class PipelineStatus(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    dataP90Eta: Optional[str] = None
    dataP99Eta: Optional[str] = None
    dataReadyAt: Optional[str] = None
    isScoringDay: Optional[bool] = None
    nextStartP90Eta: Optional[str] = None
    resolveP90Eta: Optional[str] = None
    resolveP99Eta: Optional[str] = None
    resolvedAt: Optional[str] = None
    scoreP90Eta: Optional[str] = None
    scoreP99Eta: Optional[str] = None
    scoredAt: Optional[str] = None
    startP90Eta: Optional[str] = None
    startedAt: Optional[str] = None
    tournament: Optional[str] = None

class QrBoject(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    image: Optional[str] = None
    recovery: Optional[list[str]] = None
    secret: Optional[str] = None

class QuestProgress(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    complete: Optional[bool] = None
    status: Optional[str] = None

class Ranks(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    alpha: Optional[int] = None
    bmc: Optional[int] = None
    corj60: Optional[int] = None
    corr: Optional[int] = None
    corr20V2: Optional[int] = None
    corr20d: Optional[int] = None
    corr60: Optional[int] = None
    corrV4: Optional[int] = None
    cort20: Optional[int] = None
    fnc: Optional[int] = None
    fncV3: Optional[int] = None
    fncV4: Optional[int] = None
    ic: Optional[int] = None
    icV2: Optional[int] = None
    mmc: Optional[int] = None
    mmc20d: Optional[int] = None
    mmc60: Optional[int] = None
    mpc: Optional[int] = None
    ric: Optional[int] = None
    tc: Optional[int] = None

class Reports(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    id: Optional[str] = None
    insertedAt: Optional[str] = None
    key: Optional[str] = None
    name: Optional[str] = None
    updatedAt: Optional[str] = None

class Reps(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    alpha: Optional[float] = None
    bmc: Optional[float] = None
    corj60: Optional[float] = None
    corr: Optional[float] = None
    corr20V2: Optional[float] = None
    corr20d: Optional[float] = None
    corr60: Optional[float] = None
    corrV4: Optional[float] = None
    cort20: Optional[float] = None
    fnc: Optional[float] = None
    fncV3: Optional[float] = None
    fncV4: Optional[float] = None
    ic: Optional[float] = None
    icV2: Optional[float] = None
    mmc: Optional[float] = None
    mmc20d: Optional[float] = None
    mmc60: Optional[float] = None
    mpc: Optional[float] = None
    ric: Optional[float] = None
    tc: Optional[float] = None

class Returns(BaseModel):
    """Percentage Returns"""
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    allTime: Optional[float] = None
    allTimeNmr: Optional[str] = None
    oneDay: Optional[float] = None
    oneDayNmr: Optional[str] = None
    oneYear: Optional[float] = None
    oneYearNmr: Optional[str] = None
    threeMonths: Optional[float] = None
    threeMonthsNmr: Optional[str] = None

class ReturnsValue(BaseModel):
    """Percentage Returns"""
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    allTime: Optional[float] = None
    allTimeNmr: Optional[str] = None
    date: Optional[str] = None
    oneDay: Optional[float] = None
    oneDayNmr: Optional[str] = None
    oneYear: Optional[float] = None
    oneYearNmr: Optional[str] = None
    threeMonths: Optional[float] = None
    threeMonthsNmr: Optional[str] = None

class RootMutationType(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    absorbAccount: Optional[str] = None
    acceptTos: Optional[bool] = None
    addModel: Optional["Model"] = None
    archiveModel: Optional["Model"] = None
    assignPickleToModel: Optional[str] = None
    cancelPendingStakeRelease: Optional["V2ChangeStakeRequest"] = None
    changeEmail: Optional[bool] = None
    changePassword: Optional["Session"] = None
    confirmCreateUser: Optional["Session"] = None
    createApiToken: Optional["ApiTokenWithSecret"] = None
    createComputePickleUpload: Optional["ComputePickleUpload"] = None
    createDiagnostics: Optional["V2Diagnostics"] = None
    createPrivyUser: Optional[str] = None
    createSignalsSubmission: Optional["V2Submission"] = None
    createSubmission: Optional["V2Submission"] = None
    createSupportRequest: Optional["SupportRequest"] = None
    createUser: Optional["Account"] = None
    deleteAccount: Optional[str] = None
    deleteDiagnostics: Optional[str] = None
    dismissNotification: Optional[str] = None
    generateKaggleVerificationToken: Optional["KaggleVerificationTokenResult"] = None
    increaseStake: Optional["V2ChangeStakeRequest"] = None
    login: Optional["Session"] = None
    logout: Optional[bool] = None
    markBannerAsRead: Optional[str] = None
    mfaDisable: Optional[bool] = None
    mfaEnable: Optional["Session"] = None
    mfaQr: Optional["QrBoject"] = None
    releaseStake: Optional["V2ChangeStakeRequest"] = None
    removeDiscordAccount: Optional[str] = None
    renameAccount: Optional["Account"] = None
    renameModel: Optional["Model"] = None
    resendEmailVerification: Optional[bool] = None
    resetEmailChange: Optional[bool] = None
    resetPassword: Optional[bool] = None
    resetPasswordFromToken: Optional[bool] = None
    revokeApiToken: Optional["ApiToken"] = None
    setAccountMeta: Optional[bool] = None
    setAiManagerExperience: Optional[bool] = None
    setComputeWeekdayEnabled: Optional[bool] = None
    setDefaultCurrency: Optional["Account"] = None
    setHideOnboardingTutorials: Optional[bool] = None
    setIsBeta: Optional[bool] = None
    setSubmissionWebhook: Optional[str] = None
    setUserBio: Optional[bool] = None
    setUserLink: Optional[bool] = None
    submitKaggleVerification: Optional["KaggleVerificationResult"] = None
    submitW9: Optional[bool] = None
    subscribeToCryptoMmMailingList: Optional[bool] = None
    subscribeToMailingList: Optional[bool] = None
    testSubmissionWebhook: Optional[str] = None
    triggerComputePickleUpload: Optional["ComputePickleUpload"] = None
    triggerModelWebhook: Optional[str] = None
    unarchiveModel: Optional["Model"] = None
    unsubscribeFromMailingList: Optional[bool] = None
    updateEmailPreferences: Optional[bool] = None
    updateEmailPreferencesWithToken: Optional[bool] = None
    updatePickleLabel: Optional["ComputePickleUpload"] = None
    v2ChangePayoutSelection: Optional[str] = None
    v2ChangeStake: Optional["V2ChangeStakeRequest"] = None
    v2WithdrawNmr: Optional["V2NmrTransfer"] = None
    v3ChangePayoutSelection: Optional[str] = None
    verifyEmail: Optional[bool] = None
    verifyLoginIp: Optional["Session"] = None

class RootQueryType(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    account: Optional["Account"] = None
    accountLeaderboard: Optional[list["AccountLeaderboardEntry"]] = None
    accountNameAvailable: Optional[bool] = None
    accountProfile: Optional["AccountProfile"] = None
    accountProfileImageUploadAuth: Optional["FileUploadAuth"] = None
    activityFeed: Optional[list["ActivityFeedEntry"]] = None
    apiTokenInfo: Optional["ApiTokenInfo"] = None
    apiTokenScopes: Optional[list["Scope"]] = None
    computePickleDataVersions: Optional[list["ComputePickleDataVersion"]] = None
    computePickleDockerImages: Optional[list["ComputePickleDockerImage"]] = None
    computePickleDownloadAuth: Optional["FileUploadAuth"] = None
    computePickleUploadAuth: Optional["FileUploadAuth"] = None
    computePickles: Optional[list["ComputePickleUpload"]] = None
    countryCode: Optional[str] = None
    cryptosignalsLeaderboard: Optional[list["CryptosignalsLeaderboardEntry"]] = None
    cryptosignalsLeaderboardOverview: Optional["CryptosignalsOverview"] = None
    cryptosignalsMetaModelPage: Optional["MetaModelPage"] = None
    currencyCodes: Optional[list["CurrencyCode"]] = None
    dataset: Optional[str] = None
    defaultApiToken: Optional["ApiTokenWithSecret"] = None
    diagnostics: Optional[list["V2Diagnostics"]] = None
    diagnosticsTriggerLogs: Optional[list["InvocationLog"]] = None
    diagnosticsUploadAuth: Optional["FileUploadAuth"] = None
    earnQuestsProgress: Optional["EarnQuestsProgress"] = None
    emailPreferences: Optional["EmailPreferences"] = None
    featureFlag: Optional["FeatureFlag"] = None
    geoIp: Optional["GeoIp"] = None
    ghostBlogPosts: Optional[list["GhostBlogPost"]] = None
    grandmasterTierConfigs: Optional[list["GrandmasterTierConfig"]] = None
    latestCurrencyPrice: Optional["SymbolPriceConversion"] = None
    latestEthPrice: Optional["EthPrice"] = None
    latestNmrPrice: Optional["NmrPrice"] = None
    listDatasets: Optional[list[str]] = None
    mfaRecovery: Optional[list[str]] = None
    model: Optional["Model"] = None
    modelNameAvailable: Optional[bool] = None
    nftee: Optional["Nftees"] = None
    nfteeContract: Optional["NfteeContract"] = None
    nfteeVoucher: Optional["NfteeVoucher"] = None
    nfteeWithAddress: Optional["Nftees"] = None
    nfteeWithSecret: Optional["Nftees"] = None
    pendingModelPayouts: Optional["UserPayouts"] = None
    pipelineStatus: Optional["PipelineStatus"] = None
    profileImageUploadAuth: Optional["FileUploadAuth"] = None
    reportLink: Optional[str] = None
    roundDetails: Optional["RoundDetails"] = None
    rounds: Optional[list["Round"]] = None
    seasonAccountSummary: Optional[list["SeasonAccountSummary"]] = None
    seasonLeaderboard: Optional[list["SeasonLeaderboardEntry"]] = None
    signalsLeaderboard: Optional[list["SignalsLeaderboardEntry"]] = None
    signalsLeaderboardOverview: Optional["SignalsOverview"] = None
    sso: Optional["Sso"] = None
    stakeTransactions: Optional[list["StakeTxn"]] = None
    submissionDownloadAuth: Optional["FileUploadAuth"] = None
    submissionScores: Optional[list["SubmissionScore"]] = None
    submissionUploadAuth: Optional["FileUploadAuth"] = None
    submissionUploadSignalsAuth: Optional["FileUploadAuth"] = None
    submissions: Optional[list["V2Submission"]] = None
    supportRequestUploadAuth: Optional["FileUploadAuth"] = None
    supportRequests: Optional[list["SupportRequest"]] = None
    tournamentOverview: Optional["Overview"] = None
    tournaments: Optional[list["Tournament"]] = None
    triggerLogs: Optional[list["InvocationLog"]] = None
    unreadBanners: Optional[list["Banner"]] = None
    unreadEarnedTitleNotifications: Optional[list["Notification"]] = None
    unreadNotifications: Optional[list["Notification"]] = None
    userScores: Optional[list["UserScore"]] = None
    v2Leaderboard: Optional[list["V2LeaderboardEntry"]] = None
    v2RoundModelPerformances: Optional[list["V2RoundModelPerformance"]] = None
    v2SignalsProfile: Optional["V3UserProfile"] = None
    v2TournamentOverview: Optional["V2Overview"] = None
    v3StakeAuth: Optional["V3StakeAuthorization"] = None
    v3StakeClaim: Optional["V3StakeClaim"] = None
    v3StakeConfig: Optional["V3StakeConfig"] = None
    v3StakeRound: Optional["V3StakeRound"] = None
    v3StakeServiceWallet: Optional["V3StakeWallet"] = None
    v3UserProfile: Optional["V3UserProfile"] = None

class Round(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    closeStakingTime: Optional[str] = None
    closeTime: Optional[str] = None
    dataDatestamp: Optional[int] = None
    defaultCorrMultiplier: Optional[float] = None
    defaultMmcMultiplier: Optional[float] = None
    defaultTcMultiplier: Optional[float] = None
    id: Optional[str] = None
    isDaily: Optional[bool] = None
    maxCorrMultiplier: Optional[float] = None
    maxMmcMultiplier: Optional[float] = None
    maxTcMultiplier: Optional[float] = None
    minCorrMultiplier: Optional[float] = None
    minMmcMultiplier: Optional[float] = None
    minTcMultiplier: Optional[float] = None
    numTickers: Optional[int] = None
    numValidationEras: Optional[int] = None
    numValidationTickers: Optional[int] = None
    number: Optional[int] = None
    openTime: Optional[str] = None
    payoutFactor: Optional[str] = None
    resolveTime: Optional[str] = None
    resolvedGeneral: Optional[bool] = None
    resolvedStaking: Optional[bool] = None
    scoreTime: Optional[str] = None
    stakeThreshold: Optional[float] = None
    target: Optional[str] = None
    tournament: Optional[int] = None

class RoundDetails(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    allHistogramData: Optional["HistogramData"] = None
    closeStakingTime: Optional[str] = None
    closeTime: Optional[str] = None
    isDaily: Optional[bool] = None
    models: Optional[list["ModelData"]] = None
    openTime: Optional[str] = None
    payoutFactor: Optional[str] = None
    payoutMultipliers: Optional[list["RoundPayoutMultiplier"]] = None
    roundId: Optional[str] = None
    roundNumber: Optional[int] = None
    roundResolveTime: Optional[str] = None
    roundResolved: Optional[bool] = None
    roundTarget: Optional[str] = None
    scoreTime: Optional[str] = None
    scoresUpdatedTime: Optional[str] = None
    stakedHistogramData: Optional["HistogramData"] = None
    status: Optional[str] = None
    totalAtStake: Optional[float] = None
    totalBurned: Optional[float] = None
    totalEarned: Optional[float] = None
    totalPayout: Optional[float] = None
    totalStakes: Optional[int] = None
    totalSubmitted: Optional[int] = None
    tournament: Optional[int] = None

class RoundModelPerformance(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    apcwnm: Optional[float] = None
    apcwnmPercentile: Optional[float] = None
    apcwsm: Optional[float] = None
    apcwsmPercentile: Optional[float] = None
    corr: Optional[float] = None
    corr20V2: Optional[float] = None
    corr20V2Percentile: Optional[float] = None
    corr20d: Optional[float] = None
    corr20dPercentile: Optional[float] = None
    corr60: Optional[float] = None
    corr60Percentile: Optional[float] = None
    corrMultiplier: Optional[float] = None
    corrPercentile: Optional[float] = None
    corrV4: Optional[float] = None
    corrV4Percentile: Optional[float] = None
    corrWMetamodel: Optional[float] = None
    cwmm: Optional[float] = None
    cwmmPercentile: Optional[float] = None
    cwsnmmr: Optional[float] = None
    cwsnmmrPercentile: Optional[float] = None
    fnc: Optional[float] = None
    fncPercentile: Optional[float] = None
    fncV3: Optional[float] = None
    fncV3Percentile: Optional[float] = None
    fncV4: Optional[float] = None
    fncV4Percentile: Optional[float] = None
    ic: Optional[float] = None
    icPercentile: Optional[float] = None
    icV2: Optional[float] = None
    icV2Percentile: Optional[float] = None
    mcwnm: Optional[float] = None
    mcwnmPercentile: Optional[float] = None
    mcwsm: Optional[float] = None
    mcwsmPercentile: Optional[float] = None
    mmc: Optional[float] = None
    mmc20d: Optional[float] = None
    mmc20dPercentile: Optional[float] = None
    mmcMultiplier: Optional[float] = None
    mmcPercentile: Optional[float] = None
    payout: Optional[str] = None
    ric: Optional[float] = None
    ricPercentile: Optional[float] = None
    roundNumber: Optional[int] = None
    roundOpenTime: Optional[str] = None
    roundPayoutFactor: Optional[str] = None
    roundResolveTime: Optional[str] = None
    roundResolved: Optional[bool] = None
    roundScoreTime: Optional[str] = None
    roundTarget: Optional[str] = None
    selectedStakeValue: Optional[str] = None
    tc: Optional[float] = None
    tcMultiplier: Optional[float] = None
    tcPercentile: Optional[float] = None

class RoundPayoutMultiplier(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    displayName: Optional[str] = None
    multiplier: Optional[float] = None

class ScheduledStakeTxn(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    amount: Optional[str] = None
    drain: Optional[bool] = None
    dueDate: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None
    time: Optional[str] = None
    tournament: Optional[int] = None
    type: Optional[str] = None

class Scope(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    description: Optional[str] = None
    name: Optional[str] = None

class SeasonAccountPerformance(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    rank: Optional[int] = None
    scoreName: Optional[str] = None

class SeasonAccountSummary(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    closeStakingEnd: Optional[str] = None
    daysUntilNextSeasonOpen: Optional[int] = None
    firstScoreDate: Optional[str] = None
    hasScores: Optional[bool] = None
    hasStakedOneNmr: Optional[bool] = None
    id: Optional[str] = None
    maxScoreDate: Optional[str] = None
    minQualifyingSubmissions: Optional[int] = None
    numQualifyingSubmissions: Optional[int] = None
    openDate: Optional[str] = None
    participants: Optional[int] = None
    resolveDate: Optional[str] = None
    roundNumberEnd: Optional[int] = None
    roundNumberStart: Optional[int] = None
    roundsLeft: Optional[int] = None
    seasonAccountPerformance: Optional[list["SeasonAccountPerformance"]] = None
    status: Optional[str] = None
    titleInfo: Optional["TitleInfo"] = None
    tournament: Optional[int] = None
    year: Optional[int] = None

class SeasonLeaderboardEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    seasonYear: Optional[int] = None
    tiers: Optional[list["TierLeaderboard"]] = None

class Session(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    token: Optional[str] = None
    username: Optional[str] = None

class SignalsLeaderboardEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    alphaRank: Optional[int] = None
    alphaRep: Optional[float] = None
    apy: Optional[float] = None
    canonAlphaLtm: Optional[float] = None
    canonAlphaRankLtm: Optional[int] = None
    canonCorrLtm: Optional[float] = None
    canonCorrRankLtm: Optional[int] = None
    canonMmcLtm: Optional[float] = None
    canonMmcRankLtm: Optional[int] = None
    canonMpcLtm: Optional[float] = None
    canonMpcRankLtm: Optional[int] = None
    computeEnabled: Optional[bool] = None
    control: Optional[float] = None
    corr20Rank: Optional[int] = None
    corr20Rep: Optional[float] = None
    corr20V2Rank: Optional[int] = None
    corr20V2Rep: Optional[float] = None
    corr20dRank: Optional[int] = None
    corr20dRep: Optional[float] = None
    corr60Rank: Optional[int] = None
    corr60Rep: Optional[float] = None
    corrRank: Optional[int] = None
    corrV4Rank: Optional[int] = None
    corrV4Rep: Optional[float] = None
    fncV4Rank: Optional[int] = None
    fncV4Rep: Optional[float] = None
    icRank: Optional[int] = None
    icRep: Optional[float] = None
    icV2Rank: Optional[int] = None
    icV2Rep: Optional[float] = None
    id: Optional[str] = None
    isActive: Optional[bool] = None
    latestUserScores: Optional[list["UserScore"]] = None
    mmc: Optional[float] = None
    mmc20dRank: Optional[int] = None
    mmc20dRep: Optional[float] = None
    mmcRank: Optional[int] = None
    mmcRep: Optional[float] = None
    mpcRank: Optional[int] = None
    mpcRep: Optional[float] = None
    nmrStaked: Optional[str] = None
    nmrStakedRank: Optional[int] = None
    prevAlphaRank: Optional[int] = None
    prevCorr20V2Rank: Optional[int] = None
    prevCorr20dRank: Optional[int] = None
    prevCorr60Rank: Optional[int] = None
    prevCorrRank: Optional[int] = None
    prevCorrV4Rank: Optional[int] = None
    prevFncV4Rank: Optional[int] = None
    prevIcRank: Optional[int] = None
    prevIcV2Rank: Optional[int] = None
    prevMmc20dRank: Optional[int] = None
    prevMmcRank: Optional[int] = None
    prevMpcRank: Optional[int] = None
    prevRank: Optional[int] = None
    prevRicRank: Optional[int] = None
    prevTcRank: Optional[int] = None
    profileUrl: Optional[str] = None
    rank: Optional[int] = None
    rankChange1d: Optional[int] = None
    rankChange1y: Optional[int] = None
    rankChange3m: Optional[int] = None
    reputation: Optional[float] = None
    return13Weeks: Optional[float] = None
    return13WeeksRank: Optional[int] = None
    return1Day: Optional[float] = None
    return1DayRank: Optional[int] = None
    return52Weeks: Optional[float] = None
    return52WeeksRank: Optional[int] = None
    ricRank: Optional[int] = None
    ricRep: Optional[float] = None
    sharpe: Optional[float] = None
    storedRank: Optional[int] = None
    tcRank: Optional[int] = None
    tcRep: Optional[float] = None
    team: Optional[bool] = None
    today: Optional[float] = None
    username: Optional[str] = None

class SignalsOverview(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    averageThreeMonthsReturns: Optional[float] = None
    returns: Optional["SwReturns"] = None
    returnsValues: Optional[list["SwReturnsValue"]] = None
    stakeWeightedAverageThreeMonthsReturns: Optional[float] = None
    stakedAccounts: Optional[list["StakedAccountsCount"]] = None
    stakedAccountsLtm: Optional[int] = None
    stakedModels: Optional[list["StakedModelsCount"]] = None
    stakedSubmissions: Optional[int] = None
    totalAccounts: Optional[int] = None
    totalAtStake: Optional[str] = None
    totalAtStakeValues: Optional[list["StakeValue"]] = None
    totalStakes: Optional[int] = None

class SignalsTutorials(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    helloSignals: Optional[bool] = None

class Sso(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    payload: Optional[str] = None
    signature: Optional[str] = None
    url: Optional[str] = None

class StakeTxn(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    amount: Optional[str] = None
    model: Optional[str] = None
    modelId: Optional[str] = None
    nmrPrice: Optional[str] = None
    nmrPriceLastUpdated: Optional[str] = None
    note: Optional[str] = None
    round: Optional[int] = None
    timestamp: Optional[str] = None
    tournament: Optional[int] = None
    type: Optional[str] = None
    value: Optional[str] = None

class StakeValue(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    delta: Optional[str] = None
    time: Optional[str] = None
    value: Optional[str] = None

class StakedAccountsCount(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    count: Optional[int] = None
    date: Optional[str] = None

class StakedModelsCount(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    count: Optional[int] = None
    date: Optional[str] = None

class SubmissionScore(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    date: Optional[str] = None
    day: Optional[int] = None
    displayName: Optional[str] = None
    payoutPending: Optional[str] = None
    payoutSettled: Optional[str] = None
    percentile: Optional[float] = None
    resolveDate: Optional[str] = None
    resolved: Optional[bool] = None
    roundCloseStakingTime: Optional[str] = None
    roundId: Optional[str] = None
    roundNumber: Optional[int] = None
    roundResolveTime: Optional[str] = None
    roundScoreTime: Optional[str] = None
    submissionId: Optional[str] = None
    value: Optional[float] = None
    version: Optional[str] = None

class SupportRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    accountId: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    insertedAt: Optional[str] = None
    issueStatus: Optional["SupportRequestIssueStatusEnum"] = None
    title: Optional[str] = None
    type: Optional["SupportRequestTypeEnum"] = None
    updatedAt: Optional[str] = None

class SwReturns(BaseModel):
    """Average Stake Weighted Returns"""
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    allTime: Optional[float] = None
    allTimeNmr: Optional[str] = None
    oneDay: Optional[float] = None
    oneDayNmr: Optional[str] = None
    oneYear: Optional[float] = None
    oneYearNmr: Optional[str] = None
    threeMonths: Optional[float] = None
    threeMonthsNmr: Optional[str] = None

class SwReturnsValue(BaseModel):
    """Average Stake Weighted Returns"""
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    allTime: Optional[float] = None
    allTimeNmr: Optional[str] = None
    date: Optional[str] = None
    oneYear: Optional[float] = None
    oneYearNmr: Optional[str] = None
    threeMonths: Optional[float] = None
    threeMonthsNmr: Optional[str] = None

class SymbolPriceConversion(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    baseSymbol: Optional[str] = None
    lastUpdated: Optional[str] = None
    price: Optional[str] = None
    targetSymbol: Optional[str] = None

class TierLeaderboard(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    leaderboard: Optional[list["LeaderboardEntry"]] = None
    tierDescription: Optional[str] = None
    tierName: Optional[str] = None
    tierNumber: Optional[int] = None

class TitleInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    title: Optional[str] = None
    titleDescription: Optional[str] = None

class Tournament(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    active: Optional[bool] = None
    id: Optional[str] = None
    name: Optional[str] = None
    rounds: Optional[list["Round"]] = None
    tournament: Optional[int] = None

class TypedMedalCounts(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    counts: Optional["MedalCounts"] = None
    type: Optional[str] = None

class UserPayouts(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    actual: Optional[list["Payout"]] = None
    pending: Optional[list["Payout"]] = None

class UserScore(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    date: Optional[str] = None
    displayName: Optional[str] = None
    rank: Optional[int] = None
    reputation: Optional[float] = None
    stakedRank: Optional[int] = None

class V2ChangeStakeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    drain: Optional[bool] = None
    dueDate: Optional[str] = None
    id: Optional[str] = None
    requestedAmount: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None

class V2Diagnostics(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    computePickleUploadId: Optional[str] = None
    erasAcceptedCount: Optional[int] = None
    erasMissing: Optional[list[str]] = None
    examplePredsCorrMean: Optional[float] = None
    filename: Optional[str] = None
    id: Optional[str] = None
    insertedAt: Optional[str] = None
    message: Optional[str] = None
    parentId: Optional[str] = None
    perEraDiagnostics: Optional[list["V2DiagnosticsEras"]] = None
    processSecs: Optional[float] = None
    status: Optional[str] = None
    tb200Diagnostics: Optional["V2Diagnostics"] = None
    tickersAcceptedCount: Optional[int] = None
    tickersSubmittedCount: Optional[int] = None
    topBottom: Optional[int] = None
    tournament: Optional[int] = None
    trainedOnVal: Optional[bool] = None
    updatedAt: Optional[str] = None
    validationAdjustedSharpe: Optional[float] = None
    validationAlphaCorrWExamplePreds: Optional[float] = None
    validationAlphaMaxDrawdown: Optional[float] = None
    validationAlphaMean: Optional[float] = None
    validationAlphaSharpe: Optional[float] = None
    validationAlphaStd: Optional[float] = None
    validationApy: Optional[float] = None
    validationAutocorr: Optional[float] = None
    validationBmcMean: Optional[float] = None
    validationChurnMax: Optional[float] = None
    validationChurnMean: Optional[float] = None
    validationChurnStd: Optional[float] = None
    validationCorrCorrWExamplePreds: Optional[float] = None
    validationCorrMaxDrawdown: Optional[float] = None
    validationCorrMean: Optional[float] = None
    validationCorrMeanRating: Optional[float] = None
    validationCorrPlusMmcMean: Optional[float] = None
    validationCorrPlusMmcMeanRating: Optional[float] = None
    validationCorrPlusMmcSharpe: Optional[float] = None
    validationCorrPlusMmcSharpeDiff: Optional[float] = None
    validationCorrPlusMmcSharpeDiffRating: Optional[float] = None
    validationCorrPlusMmcSharpeRating: Optional[float] = None
    validationCorrPlusMmcStd: Optional[float] = None
    validationCorrPlusMmcStdRating: Optional[float] = None
    validationCorrSharpe: Optional[float] = None
    validationCorrSharpeRating: Optional[float] = None
    validationCorrStd: Optional[float] = None
    validationCorrStdRating: Optional[float] = None
    validationCorrV4CorrWExamplePreds: Optional[float] = None
    validationCorrV4MaxDrawdown: Optional[float] = None
    validationCorrV4Mean: Optional[float] = None
    validationCorrV4Sharpe: Optional[float] = None
    validationCorrV4Std: Optional[float] = None
    validationFeatureCorrMax: Optional[float] = None
    validationFeatureCorrMaxRating: Optional[float] = None
    validationFeatureNeutralCorrMean: Optional[float] = None
    validationFeatureNeutralCorrMeanRating: Optional[float] = None
    validationFeatureNeutralCorrV3Mean: Optional[float] = None
    validationFeatureNeutralCorrV3MeanRating: Optional[float] = None
    validationFncV4CorrWExamplePreds: Optional[float] = None
    validationFncV4MaxDrawdown: Optional[float] = None
    validationFncV4Mean: Optional[float] = None
    validationFncV4Sharpe: Optional[float] = None
    validationFncV4Std: Optional[float] = None
    validationIcV2CorrWExamplePreds: Optional[float] = None
    validationIcV2MaxDrawdown: Optional[float] = None
    validationIcV2Mean: Optional[float] = None
    validationIcV2Sharpe: Optional[float] = None
    validationIcV2Std: Optional[float] = None
    validationMaxDrawdown: Optional[float] = None
    validationMaxDrawdownRating: Optional[float] = None
    validationMmcMean: Optional[float] = None
    validationMmcMeanRating: Optional[float] = None
    validationMmcSharpe: Optional[float] = None
    validationMmcSharpeRating: Optional[float] = None
    validationMmcStd: Optional[float] = None
    validationMmcStdRating: Optional[float] = None
    validationRicCorrWExamplePreds: Optional[float] = None
    validationRicMaxDrawdown: Optional[float] = None
    validationRicMean: Optional[float] = None
    validationRicSharpe: Optional[float] = None
    validationRicStd: Optional[float] = None
    validationTurnoverMax: Optional[float] = None
    validationTurnoverMean: Optional[float] = None
    validationTurnoverStd: Optional[float] = None

class V2DiagnosticsEras(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    era: Optional[str] = None
    examplePredsCorr: Optional[float] = None
    validationAlpha: Optional[float] = None
    validationBmc: Optional[float] = None
    validationChurn: Optional[float] = None
    validationCorr: Optional[float] = None
    validationCorrV4: Optional[float] = None
    validationFeatureCorrMax: Optional[float] = None
    validationFeatureNeutralCorr: Optional[float] = None
    validationFeatureNeutralCorrV3: Optional[float] = None
    validationFncV4: Optional[float] = None
    validationIcV2: Optional[float] = None
    validationMmc: Optional[float] = None
    validationRic: Optional[float] = None
    validationTurnover: Optional[float] = None

class V2LeaderboardEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    bmcRep: Optional[float] = None
    canonCorrLtm: Optional[float] = None
    canonCorrRankLtm: Optional[int] = None
    canonMmcLtm: Optional[float] = None
    canonMmcRankLtm: Optional[int] = None
    corj60Rep: Optional[float] = None
    corr20Rep: Optional[float] = None
    corr20V2Rep: Optional[float] = None
    corr60Rep: Optional[float] = None
    cort20Rep: Optional[float] = None
    fncRep: Optional[float] = None
    fncV3Rep: Optional[float] = None
    id: Optional[str] = None
    isActive: Optional[bool] = None
    latestUserScores: Optional[list["UserScore"]] = None
    mmc60Rep: Optional[float] = None
    mmcRep: Optional[float] = None
    nmrStaked: Optional[str] = None
    nmrStakedRank: Optional[int] = None
    profileUrl: Optional[str] = None
    rank: Optional[int] = None
    rankChange1d: Optional[int] = None
    rankChange1y: Optional[int] = None
    rankChange3m: Optional[int] = None
    return13Weeks: Optional[float] = None
    return13WeeksRank: Optional[int] = None
    return1Day: Optional[float] = None
    return1DayRank: Optional[int] = None
    return52Weeks: Optional[float] = None
    return52WeeksRank: Optional[int] = None
    storedRank: Optional[int] = None
    tcRep: Optional[float] = None
    team: Optional[bool] = None
    username: Optional[str] = None

class V2NmrTransfer(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    blockTimestamp: Optional[str] = None
    fromAddress: Optional[str] = None
    logIndex: Optional[int] = None
    status: Optional[str] = None
    toAddress: Optional[str] = None
    txHash: Optional[str] = None
    value: Optional[str] = None

class V2Overview(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    returns: Optional["SwReturns"] = None
    stakedAccounts: Optional[list["StakedAccountsCount"]] = None
    stakedModels: Optional[list["StakedModelsCount"]] = None
    stakedSubmissions: Optional[int] = None
    totalAccounts: Optional[int] = None
    totalAtRisk: Optional[str] = None
    totalAtStake: Optional[str] = None
    totalStakes: Optional[int] = None
    tournament: Optional[int] = None

class V2RoundModelPerformance(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    allSubmissionScores: Optional[list["SubmissionScore"]] = None
    atRisk: Optional[str] = None
    churnThreshold: Optional[float] = None
    corrMultiplier: Optional[float] = None
    intraRoundSubmissionScores: Optional[list["SubmissionScore"]] = None
    mmcMultiplier: Optional[float] = None
    prevWeekChurnMax: Optional[float] = None
    prevWeekTurnoverMax: Optional[float] = None
    roundCloseStakingTime: Optional[str] = None
    roundDataDatestamp: Optional[int] = None
    roundId: Optional[str] = None
    roundNumber: Optional[int] = None
    roundOpenTime: Optional[str] = None
    roundPayoutFactor: Optional[str] = None
    roundResolveTime: Optional[str] = None
    roundResolved: Optional[bool] = None
    roundScoreTime: Optional[str] = None
    roundTarget: Optional[str] = None
    submissionId: Optional[str] = None
    submissionScores: Optional[list["SubmissionScore"]] = None
    tcMultiplier: Optional[float] = None
    tickersAcceptedCount: Optional[int] = None
    tickersSubmittedCount: Optional[int] = None
    turnoverThreshold: Optional[float] = None

class V2Stake(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    latestValue: Optional[str] = None
    latestValueSettled: Optional[str] = None
    pendingV2ChangeStakeRequest: Optional["V2ChangeStakeRequest"] = None
    stakeValue: Optional[str] = None
    status: Optional[str] = None
    tournamentNumber: Optional[int] = None
    txHash: Optional[str] = None

class V2Submission(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    corrWithExamplePreds: Optional[float] = None
    dataDatestamp: Optional[int] = None
    diagnosticStatus: Optional[str] = None
    errorInfo: Optional[str] = None
    filename: Optional[str] = None
    filteredCount: Optional[int] = None
    firstEffectiveDate: Optional[str] = None
    hasDiagnostics: Optional[bool] = None
    hasHistoric: Optional[bool] = None
    historicMaxDrawdown: Optional[float] = None
    historicMean: Optional[float] = None
    historicSharpe: Optional[float] = None
    historicStd: Optional[float] = None
    id: Optional[str] = None
    insertedAt: Optional[str] = None
    invalidTickers: Optional[str] = None
    notes: Optional[str] = None
    prevWeekChurnMax: Optional[float] = None
    prevWeekTurnoverMax: Optional[float] = None
    round: Optional["Round"] = None
    selected: Optional[bool] = None
    sourceIp: Optional[str] = None
    sourcePlatform: Optional[str] = None
    status: Optional[str] = None
    submissionIp: Optional[str] = None
    submittedCount: Optional[int] = None
    tickersAcceptedCount: Optional[int] = None
    tickersSubmittedCount: Optional[int] = None
    trainedOnVal: Optional[bool] = None
    triggerId: Optional[str] = None
    validationApy: Optional[float] = None
    validationCorrPlusMmcMean: Optional[float] = None
    validationCorrPlusMmcMeanRating: Optional[int] = None
    validationCorrPlusMmcSharpe: Optional[float] = None
    validationCorrPlusMmcSharpeDiff: Optional[float] = None
    validationCorrPlusMmcSharpeDiffRating: Optional[int] = None
    validationCorrPlusMmcSharpeRating: Optional[int] = None
    validationCorrelation: Optional[float] = None
    validationCorrelationRating: Optional[int] = None
    validationErasAccepted: Optional[int] = None
    validationErasSubmitted: Optional[int] = None
    validationFeatureExposure: Optional[float] = None
    validationFeatureNeutralMean: Optional[float] = None
    validationFeatureNeutralMeanRating: Optional[int] = None
    validationMaxDrawdown: Optional[float] = None
    validationMaxDrawdownRating: Optional[int] = None
    validationMaxFeatureExposure: Optional[float] = None
    validationMaxFeatureExposureRating: Optional[int] = None
    validationMmcMean: Optional[float] = None
    validationMmcMeanRating: Optional[int] = None
    validationSharpe: Optional[float] = None
    validationSharpeRating: Optional[int] = None
    validationStd: Optional[float] = None
    validationStdRating: Optional[int] = None
    validationTickersAccepted: Optional[int] = None
    validationTickersSubmitted: Optional[int] = None

class V3StakeAuthorization(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    authorizationDigest: Optional[str] = None
    authorizationSigner: Optional[str] = None
    chainId: Optional[str] = None
    deadline: Optional[str] = None
    maxAmount: Optional[str] = None
    modelId: Optional[str] = None
    nmrAddress: Optional[str] = None
    nonce: Optional[str] = None
    roundId: Optional[str] = None
    signature: Optional[str] = None
    staker: Optional[str] = None
    stakingAddress: Optional[str] = None
    submissionHash: Optional[str] = None
    submissionId: Optional[str] = None
    tournamentId: Optional[str] = None

class V3StakeClaim(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    apiModelId: Optional[str] = None
    burnAmountWei: Optional[str] = None
    merkleRoot: Optional[str] = None
    modelId: Optional[str] = None
    payoutAmountWei: Optional[str] = None
    proof: Optional[list[str]] = None
    roundId: Optional[str] = None
    staker: Optional[str] = None
    submissionId: Optional[str] = None
    tournamentId: Optional[str] = None

class V3StakeConfig(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    address: Optional[str] = None
    authorizationSigner: Optional[str] = None
    nmrAddress: Optional[str] = None
    owner: Optional[str] = None
    paused: Optional[bool] = None
    pendingOwner: Optional[str] = None
    serviceWallet: Optional[str] = None

class V3StakeRound(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    closeTime: Optional[str] = None
    merkleRoot: Optional[str] = None
    openTime: Optional[str] = None
    payoutFactor: Optional[str] = None
    remainingBurn: Optional[str] = None
    remainingPayout: Optional[str] = None
    resolveTime: Optional[str] = None
    resolved: Optional[bool] = None
    roundId: Optional[str] = None
    stakeCap: Optional[str] = None
    stakeThreshold: Optional[str] = None
    state: Optional[str] = None
    totalPayout: Optional[str] = None
    totalStaked: Optional[str] = None
    tournamentId: Optional[str] = None

class V3StakeWallet(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    nmrAddress: Optional[str] = None
    serviceWallet: Optional[str] = None
    stakingAddress: Optional[str] = None
    stakingAllowance: Optional[str] = None
    walletBalance: Optional[str] = None

class V3UserProfile(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    accountName: Optional[str] = None
    bio: Optional[str] = None
    computeEnabled: Optional[bool] = None
    computeLiteEnabled: Optional[bool] = None
    control: Optional[float] = None
    dailyModelPerformances: Optional[list["DailyModelPerformance"]] = None
    id: Optional[str] = None
    isActive: Optional[bool] = None
    latestRanks: Optional["Ranks"] = None
    latestReps: Optional["Reps"] = None
    latestReturns: Optional["Returns"] = None
    latestSubmissionScores: Optional[list["SubmissionScore"]] = None
    latestUserScores: Optional[list["UserScore"]] = None
    linkText: Optional[str] = None
    linkUrl: Optional[str] = None
    nmrStaked: Optional[str] = None
    profileUrl: Optional[str] = None
    returns: Optional[list["ReturnsValue"]] = None
    roundModelPerformances: Optional[list["RoundModelPerformance"]] = None
    stakeInfo: Optional["PayoutSelection"] = None
    stakeValue: Optional[str] = None
    stakeValues: Optional[list["StakeValue"]] = None
    startDate: Optional[str] = None
    team: Optional[bool] = None
    tournament: Optional[int] = None
    typedMedals: Optional[list["TypedMedalCounts"]] = None
    username: Optional[str] = None

class W9Info(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    address: Optional[str] = None
    businessName: Optional[str] = None
    city: Optional[str] = None
    exemptions: Optional[str] = None
    fullName: Optional[str] = None
    insertedAt: Optional[str] = None
    otherTaxClassDetail: Optional[str] = None
    signature: Optional[str] = None
    state: Optional[str] = None
    taxClass: Optional["TaxClassEnum"] = None
    taxYear: Optional[str] = None
    taxpayerIdentificationNumber: Optional[str] = None
    updatedAt: Optional[str] = None
    zipCode: Optional[str] = None

class WalletTxn(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
    amount: Optional[str] = None
    from_: Optional[str] = Field(default=None, alias="from")
    status: Optional[str] = None
    time: Optional[str] = None
    to: Optional[str] = None
    tournament: Optional[int] = None
    txHash: Optional[str] = None
    type: Optional[str] = None

# --- Resolve forward references ---
_module_globals = dict(globals())
Account.model_rebuild(_types_namespace=_module_globals)
AccountLeaderboardEntry.model_rebuild(_types_namespace=_module_globals)
AccountProfile.model_rebuild(_types_namespace=_module_globals)
AccountScores.model_rebuild(_types_namespace=_module_globals)
AccountStakeValue.model_rebuild(_types_namespace=_module_globals)
AccountTutorials.model_rebuild(_types_namespace=_module_globals)
Achievement.model_rebuild(_types_namespace=_module_globals)
ActivityFeedEntry.model_rebuild(_types_namespace=_module_globals)
ApiToken.model_rebuild(_types_namespace=_module_globals)
ApiTokenInfo.model_rebuild(_types_namespace=_module_globals)
ApiTokenWithSecret.model_rebuild(_types_namespace=_module_globals)
Banner.model_rebuild(_types_namespace=_module_globals)
ComputePickleDataVersion.model_rebuild(_types_namespace=_module_globals)
ComputePickleDockerImage.model_rebuild(_types_namespace=_module_globals)
ComputePickleTrigger.model_rebuild(_types_namespace=_module_globals)
ComputePickleTriggerStatus.model_rebuild(_types_namespace=_module_globals)
ComputePickleUpload.model_rebuild(_types_namespace=_module_globals)
CryptosignalsLeaderboardEntry.model_rebuild(_types_namespace=_module_globals)
CryptosignalsOverview.model_rebuild(_types_namespace=_module_globals)
CurrencyCode.model_rebuild(_types_namespace=_module_globals)
DailyModelPerformance.model_rebuild(_types_namespace=_module_globals)
DiscordInfo.model_rebuild(_types_namespace=_module_globals)
EarnQuestsProgress.model_rebuild(_types_namespace=_module_globals)
EmailPreferences.model_rebuild(_types_namespace=_module_globals)
EthPrice.model_rebuild(_types_namespace=_module_globals)
FeatureFlag.model_rebuild(_types_namespace=_module_globals)
FileUploadAuth.model_rebuild(_types_namespace=_module_globals)
GeoIp.model_rebuild(_types_namespace=_module_globals)
GhostBlogPost.model_rebuild(_types_namespace=_module_globals)
GrandmasterTierConfig.model_rebuild(_types_namespace=_module_globals)
HistogramData.model_rebuild(_types_namespace=_module_globals)
InvocationLog.model_rebuild(_types_namespace=_module_globals)
KaggleVerificationResult.model_rebuild(_types_namespace=_module_globals)
KaggleVerificationTokenResult.model_rebuild(_types_namespace=_module_globals)
LatestSubmission.model_rebuild(_types_namespace=_module_globals)
LeaderboardEntry.model_rebuild(_types_namespace=_module_globals)
MedalCounts.model_rebuild(_types_namespace=_module_globals)
MetaModelHolding.model_rebuild(_types_namespace=_module_globals)
MetaModelPage.model_rebuild(_types_namespace=_module_globals)
Model.model_rebuild(_types_namespace=_module_globals)
ModelData.model_rebuild(_types_namespace=_module_globals)
ModelProfile.model_rebuild(_types_namespace=_module_globals)
Nftee.model_rebuild(_types_namespace=_module_globals)
NfteeContract.model_rebuild(_types_namespace=_module_globals)
NfteeVoucher.model_rebuild(_types_namespace=_module_globals)
Nftees.model_rebuild(_types_namespace=_module_globals)
NmrPrice.model_rebuild(_types_namespace=_module_globals)
NmrReturnStats.model_rebuild(_types_namespace=_module_globals)
Notification.model_rebuild(_types_namespace=_module_globals)
NumeraiTutorials.model_rebuild(_types_namespace=_module_globals)
Overview.model_rebuild(_types_namespace=_module_globals)
Payout.model_rebuild(_types_namespace=_module_globals)
PayoutSelection.model_rebuild(_types_namespace=_module_globals)
PipelineStatus.model_rebuild(_types_namespace=_module_globals)
QrBoject.model_rebuild(_types_namespace=_module_globals)
QuestProgress.model_rebuild(_types_namespace=_module_globals)
Ranks.model_rebuild(_types_namespace=_module_globals)
Reports.model_rebuild(_types_namespace=_module_globals)
Reps.model_rebuild(_types_namespace=_module_globals)
Returns.model_rebuild(_types_namespace=_module_globals)
ReturnsValue.model_rebuild(_types_namespace=_module_globals)
RootMutationType.model_rebuild(_types_namespace=_module_globals)
RootQueryType.model_rebuild(_types_namespace=_module_globals)
Round.model_rebuild(_types_namespace=_module_globals)
RoundDetails.model_rebuild(_types_namespace=_module_globals)
RoundModelPerformance.model_rebuild(_types_namespace=_module_globals)
RoundPayoutMultiplier.model_rebuild(_types_namespace=_module_globals)
ScheduledStakeTxn.model_rebuild(_types_namespace=_module_globals)
Scope.model_rebuild(_types_namespace=_module_globals)
SeasonAccountPerformance.model_rebuild(_types_namespace=_module_globals)
SeasonAccountSummary.model_rebuild(_types_namespace=_module_globals)
SeasonLeaderboardEntry.model_rebuild(_types_namespace=_module_globals)
Session.model_rebuild(_types_namespace=_module_globals)
SignalsLeaderboardEntry.model_rebuild(_types_namespace=_module_globals)
SignalsOverview.model_rebuild(_types_namespace=_module_globals)
SignalsTutorials.model_rebuild(_types_namespace=_module_globals)
Sso.model_rebuild(_types_namespace=_module_globals)
StakeTxn.model_rebuild(_types_namespace=_module_globals)
StakeValue.model_rebuild(_types_namespace=_module_globals)
StakedAccountsCount.model_rebuild(_types_namespace=_module_globals)
StakedModelsCount.model_rebuild(_types_namespace=_module_globals)
SubmissionScore.model_rebuild(_types_namespace=_module_globals)
SupportRequest.model_rebuild(_types_namespace=_module_globals)
SwReturns.model_rebuild(_types_namespace=_module_globals)
SwReturnsValue.model_rebuild(_types_namespace=_module_globals)
SymbolPriceConversion.model_rebuild(_types_namespace=_module_globals)
TierLeaderboard.model_rebuild(_types_namespace=_module_globals)
TitleInfo.model_rebuild(_types_namespace=_module_globals)
Tournament.model_rebuild(_types_namespace=_module_globals)
TypedMedalCounts.model_rebuild(_types_namespace=_module_globals)
UserPayouts.model_rebuild(_types_namespace=_module_globals)
UserScore.model_rebuild(_types_namespace=_module_globals)
V2ChangeStakeRequest.model_rebuild(_types_namespace=_module_globals)
V2Diagnostics.model_rebuild(_types_namespace=_module_globals)
V2DiagnosticsEras.model_rebuild(_types_namespace=_module_globals)
V2LeaderboardEntry.model_rebuild(_types_namespace=_module_globals)
V2NmrTransfer.model_rebuild(_types_namespace=_module_globals)
V2Overview.model_rebuild(_types_namespace=_module_globals)
V2RoundModelPerformance.model_rebuild(_types_namespace=_module_globals)
V2Stake.model_rebuild(_types_namespace=_module_globals)
V2Submission.model_rebuild(_types_namespace=_module_globals)
V3StakeAuthorization.model_rebuild(_types_namespace=_module_globals)
V3StakeClaim.model_rebuild(_types_namespace=_module_globals)
V3StakeConfig.model_rebuild(_types_namespace=_module_globals)
V3StakeRound.model_rebuild(_types_namespace=_module_globals)
V3StakeWallet.model_rebuild(_types_namespace=_module_globals)
V3UserProfile.model_rebuild(_types_namespace=_module_globals)
W9Info.model_rebuild(_types_namespace=_module_globals)
WalletTxn.model_rebuild(_types_namespace=_module_globals)
KaggleProfileDataInput.model_rebuild(_types_namespace=_module_globals)
