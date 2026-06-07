"""Core utility functions for the ML Engineering pipeline."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

logger = logging.getLogger(__name__)


def load_config(config_path: str | Path) -> dict[str, Any]:
    """Load a YAML configuration file.

    Args:
        config_path: Path to the YAML config file.

    Returns:
        Dictionary of configuration values.

    Raises:
        FileNotFoundError: If the config file does not exist.
    """
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with open(config_path) as f:
        config = yaml.safe_load(f)
    logger.info("Loaded config from %s", config_path)
    return config


def validate_dataframe(
    df: pd.DataFrame,
    required_columns: list[str],
    allow_nulls: bool = False,
) -> pd.DataFrame:
    """Validate a DataFrame has required columns and no unexpected nulls.

    Args:
        df: Input DataFrame to validate.
        required_columns: List of column names that must be present.
        allow_nulls: Whether to allow null values in required columns.

    Returns:
        The validated DataFrame (unchanged).

    Raises:
        ValueError: If required columns are missing or nulls found.
    """
    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if not allow_nulls:
        null_cols = [c for c in required_columns if df[c].isnull().any()]
        if null_cols:
            raise ValueError(f"Null values found in columns: {null_cols}")

    return df


def compute_basic_stats(series: pd.Series) -> dict[str, float]:
    """Compute descriptive statistics for a numeric Series.

    Args:
        series: A pandas Series of numeric values.

    Returns:
        Dictionary with mean, std, min, max, median.

    Raises:
        TypeError: If series is not numeric.
    """
    if not pd.api.types.is_numeric_dtype(series):
        raise TypeError(f"Expected numeric series, got {series.dtype}")

    return {
        "mean": float(np.mean(series)),
        "std": float(np.std(series)),
        "min": float(np.min(series)),
        "max": float(np.max(series)),
        "median": float(np.median(series)),
    }


def setup_logging(level: str = "INFO") -> None:
    """Configure root logger for the project.

    Args:
        level: Logging level string (DEBUG, INFO, WARNING, ERROR).
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
