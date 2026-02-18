"""
Numerai Round Performance - Configuration and Models

Pydantic models for configuration, results, and per-tournament payout formula classes.
"""

from abc import abstractmethod
from pathlib import Path
from typing import Literal, Optional

import yaml
from loguru import logger
from pydantic import BaseModel, Field, field_validator

from numerai_client import Tournament


class FormulaBase(BaseModel):
    """Abstract base for tournament payout formulas.

    Each tournament has its own score fields, column headers, and payout calculation.
    """

    @property
    @abstractmethod
    def column_headers(self) -> tuple[str, str]:
        """Display names for the two score columns in table output."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Human-readable formula description for logging."""

    @property
    @abstractmethod
    def cache_score_columns(self) -> tuple[str, str]:
        """Parquet column names for the two score values."""

    @property
    @abstractmethod
    def score_display_names(self) -> tuple[tuple[str, ...], tuple[str, ...]]:
        """submissionScores displayName lookup tuples for (score1, score2)."""

    @abstractmethod
    def extract_scores(self, model_dict: dict) -> tuple[Optional[float], Optional[float]]:
        """Extract the two score values from a GraphQL model dict."""

    @property
    @abstractmethod
    def multiplier1(self) -> float:
        """Multiplier for the first score (used in vectorized calculation)."""

    @property
    @abstractmethod
    def multiplier2(self) -> float:
        """Multiplier for the second score (used in vectorized calculation)."""

    @abstractmethod
    def calculate_return(
        self, s1: Optional[float], s2: Optional[float], pf: float
    ) -> Optional[float]:
        """Calculate % return on stake from two scores and payout factor."""


class ClassicFormula(FormulaBase):
    """Classic tournament: clip(pf * (mmc_mult * MMC + corr_mult * CORR20), clip_min, clip_max)"""

    mmc_multiplier: float = 2.25
    corr_multiplier: float = 0.75
    clip_min: float = -0.05
    clip_max: float = 0.05

    @property
    def multiplier1(self) -> float:
        return self.mmc_multiplier

    @property
    def multiplier2(self) -> float:
        return self.corr_multiplier

    @property
    def column_headers(self) -> tuple[str, str]:
        return ("MMC20", "CORR20")

    @property
    def description(self) -> str:
        return (
            f"clip(pf * ({self.mmc_multiplier}*MMC + {self.corr_multiplier}*CORR20), "
            f"{self.clip_min}, {self.clip_max})"
        )

    @property
    def cache_score_columns(self) -> tuple[str, str]:
        return ("mmc", "v2_corr20")

    @property
    def score_display_names(self) -> tuple[tuple[str, ...], tuple[str, ...]]:
        return (("mmc", "canon_mmc"), ("v2_corr20", "canon_corr"))

    def extract_scores(self, model_dict: dict) -> tuple[Optional[float], Optional[float]]:
        return model_dict.get("mmc"), model_dict.get("v2Corr20")

    def calculate_return(
        self, s1: Optional[float], s2: Optional[float], pf: float
    ) -> Optional[float]:
        if s1 is None or s2 is None:
            return None
        raw = pf * (self.mmc_multiplier * s1 + self.corr_multiplier * s2)
        clipped = max(self.clip_min, min(self.clip_max, raw))
        return clipped * 100


class CryptoFormula(FormulaBase):
    """Crypto tournament: clip(pf * (mmc_mult * MMC + corr_mult * CORR), clip_min, clip_max)"""

    mmc_multiplier: float = 0.5
    corr_multiplier: float = 0.05
    clip_min: float = -0.05
    clip_max: float = 0.05

    @property
    def multiplier1(self) -> float:
        return self.mmc_multiplier

    @property
    def multiplier2(self) -> float:
        return self.corr_multiplier

    @property
    def column_headers(self) -> tuple[str, str]:
        return ("MMC20", "CORR")

    @property
    def description(self) -> str:
        return (
            f"clip(pf * ({self.mmc_multiplier}*MMC + {self.corr_multiplier}*CORR), "
            f"{self.clip_min}, {self.clip_max})"
        )

    @property
    def cache_score_columns(self) -> tuple[str, str]:
        return ("mmc", "corr")

    @property
    def score_display_names(self) -> tuple[tuple[str, ...], tuple[str, ...]]:
        return (("mmc", "canon_mmc"), ("corr",))

    def extract_scores(self, model_dict: dict) -> tuple[Optional[float], Optional[float]]:
        return model_dict.get("mmc"), model_dict.get("corr")

    def calculate_return(
        self, s1: Optional[float], s2: Optional[float], pf: float
    ) -> Optional[float]:
        if s1 is None or s2 is None:
            return None
        raw = pf * (self.mmc_multiplier * s1 + self.corr_multiplier * s2)
        clipped = max(self.clip_min, min(self.clip_max, raw))
        return clipped * 100


class SignalsFormula(FormulaBase):
    """Signals tournament: clip(pf * (alpha_mult * ALPHA + mpc_mult * MPC), min, max)"""

    alpha_multiplier: float = 0.3
    mpc_multiplier: float = 0.8
    clip_min: float = -0.017
    clip_max: float = 0.017

    @property
    def multiplier1(self) -> float:
        return self.alpha_multiplier

    @property
    def multiplier2(self) -> float:
        return self.mpc_multiplier

    @property
    def column_headers(self) -> tuple[str, str]:
        return ("ALPHA", "MPC")

    @property
    def description(self) -> str:
        return (
            f"clip(pf * ({self.alpha_multiplier}*ALPHA + {self.mpc_multiplier}*MPC), "
            f"{self.clip_min}, {self.clip_max})"
        )

    @property
    def cache_score_columns(self) -> tuple[str, str]:
        return ("alpha", "mpc")

    @property
    def score_display_names(self) -> tuple[tuple[str, ...], tuple[str, ...]]:
        return (("alpha",), ("mpc",))

    def extract_scores(self, model_dict: dict) -> tuple[Optional[float], Optional[float]]:
        return model_dict.get("alpha"), model_dict.get("mpc")

    def calculate_return(
        self, s1: Optional[float], s2: Optional[float], pf: float
    ) -> Optional[float]:
        if s1 is None or s2 is None:
            return None
        raw = pf * (self.alpha_multiplier * s1 + self.mpc_multiplier * s2)
        clipped = max(self.clip_min, min(self.clip_max, raw))
        return clipped * 100


class FormulasConfig(BaseModel):
    """Per-tournament formula configuration."""

    classic: ClassicFormula = Field(default_factory=ClassicFormula)
    crypto: CryptoFormula = Field(default_factory=CryptoFormula)
    signals: SignalsFormula = Field(default_factory=SignalsFormula)


class AppConfig(BaseModel):
    """Application configuration loaded from YAML with CLI overrides"""

    tournament: Tournament = Tournament.CLASSIC
    formulas: FormulasConfig = Field(default_factory=FormulasConfig)
    method: Literal["rounddetails", "permodel", "both"] = "rounddetails"
    model_regex: Optional[str] = None
    sort_by: Literal["return_pct", "mmc20", "corr20", "model_name"] = "return_pct"
    sort_desc: bool = True
    max_models: int = 100
    parquet_path: Path = Field(default=Path("round_details.parquet"))
    position_metric: Literal["return_pct", "score1", "score2"] = "return_pct"

    @field_validator("tournament", mode="before")
    @classmethod
    def parse_tournament(cls, v: object) -> Tournament:
        if isinstance(v, Tournament):
            return v
        if isinstance(v, int):
            return Tournament(v)
        if isinstance(v, str):
            return Tournament[v.upper()]
        raise ValueError(f"Invalid tournament: {v}. Use classic/signals/crypto or 8/11/12")

    def get_formula(self) -> FormulaBase:
        """Return the formula for the current tournament."""
        return getattr(self.formulas, self.tournament.name.lower())

    def get_parquet_path(self) -> Path:
        """Return tournament-specific parquet path, e.g. round_details_classic.parquet"""
        stem = self.parquet_path.stem
        suffix = self.parquet_path.suffix
        return self.parquet_path.with_name(f"{stem}_{self.tournament.name.lower()}{suffix}")


class ModelResult(BaseModel):
    """Performance result for a single model in a round"""

    model_name: str
    score1: Optional[float] = None
    score2: Optional[float] = None
    payout_factor: float
    return_pct: Optional[float] = None
    rank: Optional[int] = None
    total_models: Optional[int] = None


DEFAULT_CONFIG_PATH = Path(__file__).parent / "round_config.yaml"


def load_config(config_path: Path = DEFAULT_CONFIG_PATH) -> AppConfig:
    """Load configuration from YAML file, falling back to defaults"""
    if config_path.exists():
        logger.info(f"Loading config from {config_path}")
        with open(config_path) as f:
            data = yaml.safe_load(f) or {}
        return AppConfig(**data)
    logger.info("No config file found, using defaults")
    return AppConfig()
