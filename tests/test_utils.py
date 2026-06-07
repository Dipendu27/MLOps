import pandas as pd
import pytest

from ml_engineering.utils import compute_basic_stats, load_config, validate_dataframe


def test_load_config_reads_yaml(tmp_path):
    config_path = tmp_path / "config.yaml"
    config_path.write_text("""
project:
  name: demo
  seed: 42
""".lstrip())

    config = load_config(config_path)

    assert config == {"project": {"name": "demo", "seed": 42}}


def test_load_config_raises_for_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError, match="Config file not found"):
        load_config(tmp_path / "missing.yaml")


def test_validate_dataframe_returns_valid_dataframe():
    df = pd.DataFrame({"feature": [1, 2], "target": [0, 1]})

    validated = validate_dataframe(df, ["feature", "target"])

    assert validated is df


def test_validate_dataframe_raises_for_missing_columns():
    df = pd.DataFrame({"feature": [1, 2]})

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_dataframe(df, ["feature", "target"])


def test_validate_dataframe_raises_for_null_values():
    df = pd.DataFrame({"feature": [1, None], "target": [0, 1]})

    with pytest.raises(ValueError, match="Null values found"):
        validate_dataframe(df, ["feature", "target"])


def test_validate_dataframe_allows_null_values_when_requested():
    df = pd.DataFrame({"feature": [1, None], "target": [0, 1]})

    validated = validate_dataframe(df, ["feature", "target"], allow_nulls=True)

    assert validated is df


def test_compute_basic_stats_returns_descriptive_statistics():
    stats = compute_basic_stats(pd.Series([1, 2, 3, 4]))

    assert stats == {
        "mean": 2.5,
        "std": pytest.approx(1.11803398875),
        "min": 1.0,
        "max": 4.0,
        "median": 2.5,
    }


def test_compute_basic_stats_raises_for_non_numeric_series():
    with pytest.raises(TypeError, match="Expected numeric series"):
        compute_basic_stats(pd.Series(["a", "b"]))
