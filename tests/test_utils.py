"""Unit tests for ml_engineering.utils module."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from ml_engineering.utils import (
    compute_basic_stats,
    load_config,
    validate_dataframe,
)

# ── load_config ────────────────────────────────────────────────────────────────


class TestLoadConfig:
    def test_loads_valid_yaml(self, tmp_path: Path) -> None:
        config_file = tmp_path / "test.yaml"
        config_file.write_text("model:\n  lr: 0.01\n  epochs: 10\n")
        result = load_config(config_file)
        assert result == {"model": {"lr": 0.01, "epochs": 10}}

    def test_raises_file_not_found(self, tmp_path: Path) -> None:
        with pytest.raises(FileNotFoundError, match="Config file not found"):
            load_config(tmp_path / "nonexistent.yaml")

    def test_returns_dict(self, tmp_path: Path) -> None:
        config_file = tmp_path / "cfg.yaml"
        config_file.write_text("key: value\n")
        result = load_config(config_file)
        assert isinstance(result, dict)


# ── validate_dataframe ─────────────────────────────────────────────────────────


class TestValidateDataframe:
    @pytest.fixture
    def sample_df(self) -> pd.DataFrame:
        return pd.DataFrame({"age": [25, 30, 35], "score": [0.8, 0.9, 0.7]})

    def test_passes_with_valid_df(self, sample_df: pd.DataFrame) -> None:
        result = validate_dataframe(sample_df, ["age", "score"])
        assert result is sample_df

    def test_raises_on_missing_columns(self, sample_df: pd.DataFrame) -> None:
        with pytest.raises(ValueError, match="Missing required columns"):
            validate_dataframe(sample_df, ["age", "score", "missing_col"])

    def test_raises_on_nulls_by_default(self) -> None:
        df = pd.DataFrame({"age": [25, None, 35], "score": [0.8, 0.9, 0.7]})
        with pytest.raises(ValueError, match="Null values found"):
            validate_dataframe(df, ["age"])

    def test_allows_nulls_when_flag_set(self) -> None:
        df = pd.DataFrame({"age": [25, None, 35]})
        result = validate_dataframe(df, ["age"], allow_nulls=True)
        assert len(result) == 3

    def test_empty_required_columns(self, sample_df: pd.DataFrame) -> None:
        result = validate_dataframe(sample_df, [])
        assert result is sample_df


# ── compute_basic_stats ────────────────────────────────────────────────────────


class TestComputeBasicStats:
    def test_returns_correct_keys(self) -> None:
        series = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
        stats = compute_basic_stats(series)
        assert set(stats.keys()) == {"mean", "std", "min", "max", "median"}

    def test_correct_mean(self) -> None:
        series = pd.Series([10.0, 20.0, 30.0])
        stats = compute_basic_stats(series)
        assert stats["mean"] == pytest.approx(20.0)

    def test_correct_min_max(self) -> None:
        series = pd.Series([5.0, 1.0, 9.0, 3.0])
        stats = compute_basic_stats(series)
        assert stats["min"] == 1.0
        assert stats["max"] == 9.0

    def test_correct_std_is_population_std(self) -> None:
        series = pd.Series([1.0, 2.0, 3.0, 4.0])
        stats = compute_basic_stats(series)
        # np.std uses ddof=0 (population); sample std (ddof=1) would be ~1.29
        assert stats["std"] == pytest.approx(1.118033988749895)

    def test_correct_median(self) -> None:
        series = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
        stats = compute_basic_stats(series)
        assert stats["median"] == pytest.approx(3.0)

    def test_raises_on_non_numeric(self) -> None:
        series = pd.Series(["a", "b", "c"])
        with pytest.raises(TypeError, match="Expected numeric series"):
            compute_basic_stats(series)

    def test_single_element_series(self) -> None:
        series = pd.Series([42.0])
        stats = compute_basic_stats(series)
        assert stats["mean"] == 42.0
        assert stats["std"] == 0.0

    def test_all_values_are_floats(self) -> None:
        series = pd.Series([1, 2, 3])
        stats = compute_basic_stats(series)
        assert all(isinstance(v, float) for v in stats.values())

    def test_large_series(self) -> None:
        rng = np.random.default_rng(42)
        series = pd.Series(rng.standard_normal(100_000))
        stats = compute_basic_stats(series)
        assert abs(stats["mean"]) < 0.1  # should be near 0 for large N
