<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=ML%20Engineering%20Master%20Roadmap&fontSize=36&fontColor=ffffff&fontAlignY=38&desc=120%20Days%20%7C%207%20Phases%20%7C%20Production-Grade%20ML%20Systems&descAlignY=58&descSize=16&descColor=a0c4ff" />

<br/>

<!-- Live progress badges -->
![Day](https://img.shields.io/badge/Day-4%2F120-0f2027?style=for-the-badge&logo=calendar&logoColor=white)
![Phase](https://img.shields.io/badge/Phase_1-MLOps_%26_Production-203a43?style=for-the-badge&logo=docker&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-79_Passing-2c5364?style=for-the-badge&logo=pytest&logoColor=white)
![Coverage](https://img.shields.io/badge/Coverage-93%25-00b894?style=for-the-badge&logo=codecov&logoColor=white)

<br/>

![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS_SageMaker-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apache-kafka&logoColor=white)

</div>

---

## 👋 What This Is

This repository is a **live, public learning system** — built one day at a time, committed every evening, and documented with measurable outcomes.

The goal: bridge the gap between data science and **production ML engineering** through 120 days of structured, industry-level practice across 7 phases, 12+ projects, and 40+ tools.

Every commit is dated. Every deliverable has a benchmark. Every phase has a definition of done.

> **Open to ML Engineering, ML Platform, and Applied AI roles globally.**
> Resume · [LinkedIn](https://www.linkedin.com/in/dipendu-mukherjee-4199a8226/) · [Portfolio](https://dipendu-mukherjee-portfolio.vercel.app/)

---

## 📊 Live Progress

| # | Phase | Days | Status | Key Outcome |
|---|-------|------|--------|-------------|
| 1 | 🔧 MLOps & Production Engineering | 1–20 | 🔄 **In Progress** | Production-grade MLOps on existing repo |
| 2 | 🔄 Advanced Data Engineering | 21–38 | ⏳ Upcoming | Real-time streaming + lakehouse + orchestration |
| 3 | ☁️ Cloud ML Engineering | 39–58 | ⏳ Upcoming | AWS SageMaker, FastAPI serving, Ray distributed |
| 4 | 🤖 Advanced LLM Engineering | 59–78 | ⏳ Upcoming | Agents, evals, guardrails, DPO alignment |
| 5 | 🔬 Specialized ML Domains | 79–96 | ⏳ Upcoming | GNNs, time-series, multimodal, RL, federated |
| 6 | ⚖️ Responsible AI & ML Security | 97–108 | ⏳ Upcoming | Explainability, fairness, adversarial, DP |
| 7 | 🏗️ ML System Design & Capstone | 109–120 | ⏳ Upcoming | Recsys + fraud system + capstone + portfolio |

---

## 🚀 Quick Start

```bash
# Clone and install in under 60 seconds
git clone https://github.com/Dipendu27/ml-engineering-master
cd ml-engineering-master

pip install -e ".[dev]"   # installs package + all dev dependencies
make test                  # runs full pytest suite
make lint                  # black + isort + flake8
```

**Requirements:** Python 3.10+, pip, git. No other setup needed for Phase 1.

---

## 🗂️ Repository Structure

```
ml-engineering-master/
│
├── src/
│   └── ml_engineering/         # Installable Python package
│       ├── __init__.py
│       ├── preprocessing.py    # 5 data preprocessing functions
│       ├── features.py         # 4 feature engineering functions
│       ├── model.py            # MLModel class — train/predict/evaluate/save/load
│       └── utils.py            # Shared utilities (config, logging, validation)
│
├── tests/
│   ├── conftest.py             # Session-scoped fixtures, shared test data
│   ├── test_preprocessing.py   # 20 tests — edge cases, null handling, encoding
│   ├── test_features.py        # 26 tests — parametrized, BMI, rolling stats
│   ├── test_model.py           # 25 tests — predict, evaluate, save/load
│   ├── test_model_mock.py      # 8 tests — pytest-mock, logger spy, pickle patch
│   └── test_utils.py           # 8 tests — config loading, validation
│
├── configs/
│   └── base.yaml               # Project-wide YAML config (seed, paths, hyperparams)
│
├── notebooks/                  # Exploration notebooks (not production code)
├── scripts/
│   ├── train.py                # CLI training entry point
│   └── predict.py              # CLI inference entry point
│
├── docs/                       # Architecture diagrams + daily notes
├── data/
│   ├── raw/                    # Immutable source data (DVC tracked from Day 10)
│   ├── processed/              # Transformed data
│   └── external/               # Third-party datasets
│
├── artifacts/                  # Model artifacts (MLflow tracked from Day 5)
├── .github/
│   └── workflows/              # CI/CD (GitHub Actions — added Day 13)
│
├── pyproject.toml              # Package metadata + dependency pinning
├── Makefile                    # make test | make lint | make train | make clean
├── .pre-commit-config.yaml     # black · isort · flake8 on every commit
└── .flake8                     # Linting config (max-line 88, E203/W503 ignored)
```

---

## ✅ Phase 1 — MLOps & Production Engineering (Days 1–20)

> Retrofitting production scaffolding onto an existing ML project: packaging, testing, experiment tracking, data versioning, CI/CD, and model monitoring.

### Completed

| Day | Deliverable | Measurable Outcome |
|-----|-------------|--------------------|
| 1–2 | Production repo structure | Installable package · pre-commit hooks · Makefile |
| 3 | Preprocessing + feature modules | `preprocessing.py` (5 functions) · `features.py` (4 functions) |
| 4 | Model class + full test suite | `MLModel` · 79 tests · 93% coverage · pytest-mock |

### Upcoming

| Day | Topic | Tools |
|-----|-------|-------|
| 5–7 | MLflow experiment tracking | mlflow · SQLite backend · autologging |
| 8–9 | MLflow Model Registry | MlflowClient · staging transitions |
| 10–12 | DVC data & model versioning | dvc · dvc.yaml · remote storage |
| 13–15 | CI/CD with GitHub Actions | ci.yml · cd.yml · Docker buildx |
| 16–17 | Drift detection | Evidently AI · DataDriftPreset · PSI alerting |
| 18–20 | RAG evaluation | RAGAS · faithfulness · CI regression gate |

---

## 🧪 Test Suite — Day 4 Snapshot

```
tests/test_features.py        .......................... (26 tests)
tests/test_model.py           .......................... (25 tests)
tests/test_model_mock.py      ........           (8 tests)
tests/test_preprocessing.py   .................. (20 tests)
tests/test_utils.py           ........           (8 tests)

79 passed · 0 failed · 0 skipped
Coverage: 93% across src/ml_engineering/
```

**Testing patterns used:**
- `conftest.py` session-scoped fixtures (dataset created once, shared across all tests)
- `@pytest.mark.parametrize` for table-driven tests (thresholds, metrics, age buckets)
- `pytest-mock` for isolating behavior (mocking pickle, spying on logger, patching estimator)
- `tmp_path` fixture for filesystem tests with automatic cleanup
- Edge cases: empty DataFrames, mismatched lengths, unfitted model, negative values

---

## 🛠️ Tools Across All 120 Days

<details>
<summary><b>Phase 1–2 · MLOps + Data Engineering</b></summary>

| Category | Tools |
|----------|-------|
| Packaging | `pyproject.toml` · `setuptools` · `pre-commit` |
| Testing | `pytest` · `pytest-cov` · `pytest-mock` · `Great Expectations` |
| Experiment Tracking | `MLflow` · `SQLite backend` · autologging |
| Data Versioning | `DVC` · `dvc.yaml` · S3 remote |
| CI/CD | `GitHub Actions` · `Docker buildx` |
| Monitoring | `Evidently AI` · `DataDriftPreset` |
| Evaluation | `RAGAS` · faithfulness · context recall |
| Streaming | `Apache Kafka` · `confluent-kafka` · `Kafka UI` |
| Feature Store | `Feast` · Redis online store · Parquet offline |
| Transformation | `dbt` · `DuckDB` · 3-layer model architecture |
| Lakehouse | `Delta Lake` · time travel · schema evolution |
| Orchestration | `Apache Airflow` · sensors · SLA monitoring |

</details>

<details>
<summary><b>Phase 3–4 · Cloud ML + LLM Engineering</b></summary>

| Category | Tools |
|----------|-------|
| Cloud Training | `AWS SageMaker` · `boto3` · `S3` · `ECR` |
| ML Pipelines | `SageMaker Pipelines` · `ConditionStep` |
| Serving | `FastAPI` · `BentoML` · `uvicorn` · `Pydantic` |
| Distributed | `Ray Train` · `Ray Tune` · ASHA scheduler |
| Containers | `Docker` · `Kubernetes (kind)` · `HPA` |
| LLM Agents | `LangGraph` · `CrewAI` · `LangChain` |
| Observability | `LangSmith` · traces · feedback labels |
| Prompt Optimization | `DSPy` · `BootstrapFewShot` · `MIPRO` |
| Safety | `NeMo Guardrails` · `Llama Guard` · `Outlines` |
| Alignment | `TRL (DPO)` · `PEFT` · `bitsandbytes` |

</details>

<details>
<summary><b>Phase 5–7 · Specialized + Responsible AI + System Design</b></summary>

| Category | Tools |
|----------|-------|
| Graph ML | `PyTorch Geometric` · GCN · GAT · `NetworkX` |
| Time Series | `pytorch-forecasting` · TFT · N-BEATS · `sktime` |
| Multimodal | `CLIP` · `LLaVA` · `transformers` · `torchvision` |
| Reinforcement Learning | `Stable-Baselines3` · PPO · SAC · `Gymnasium` |
| Federated Learning | `Flower (flwr)` · FedAvg · `Opacus` DP-SGD |
| Explainability | `SHAP` · `LIME` · `Captum` · Integrated Gradients |
| Fairness | `Fairlearn` · `AI Fairness 360` · GridSearch |
| Adversarial ML | `ART` · FGSM · PGD · `TextAttack` |
| Differential Privacy | `Opacus` · DP-SGD · PATE · privacy budgets |
| System Design | `FAISS` · `LightGBM` · `Faust` · `Locust` |
| Monitoring | `Prometheus` · `Grafana` · `Evidently AI` |

</details>

---

## 📈 Roadmap at a Glance

```
Phase 1  ████░░░░░░░░░░░░░░░░░░░░░░░░░░  Day 4/20   MLOps
Phase 2  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Day 0/18   Data Engineering
Phase 3  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Day 0/20   Cloud ML
Phase 4  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Day 0/20   LLM Engineering
Phase 5  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Day 0/18   Specialized ML
Phase 6  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Day 0/12   Responsible AI
Phase 7  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Day 0/12   System Design
```

---

## 📝 Daily Log

<details>
<summary><b>Phase 1 — MLOps & Production Engineering (click to expand)</b></summary>

### Day 4 — pytest for ML Code: Model, Fixtures & Mocks
**Date:** _(fill in your date)_
- Built `MLModel` class: `train()`, `predict()`, `predict_proba()`, `evaluate()`, `save()`, `load()`
- Created `conftest.py` with 6 session-scoped shared fixtures
- Wrote `test_model.py` — 25 tests covering all methods and edge cases
- Wrote `test_model_mock.py` — 8 tests using `pytest-mock` (logger spy, pickle patch, estimator mock)
- Total: **79 tests · 93% coverage**

### Day 3 — pytest for ML Code: Preprocessing & Feature Engineering
**Date:** _(fill in your date)_
- Built `preprocessing.py` — 5 functions: remove_duplicates, handle_missing_values, normalize_features, clip_outliers, encode_categorical
- Built `features.py` — 4 functions: create_age_buckets, compute_rolling_stats, compute_bmi, flag_high_risk
- Wrote 46 tests with `@pytest.mark.parametrize` and shared fixtures

### Day 1–2 — Repo Structure & Python Packaging
**Date:** _(fill in your date)_
- Migrated to `src/` layout with `pyproject.toml`
- Configured pre-commit hooks: black, isort, flake8
- Wrote `Makefile` with `test`, `lint`, `train`, `clean` targets
- 8 initial utility tests passing

</details>

---

## 🤝 Connect

I post daily progress on LinkedIn — technical write-ups with benchmarks, architecture decisions, and lessons learned.

If you're hiring for **ML Engineering**, **ML Platform**, **MLOps**, or **Applied AI** roles — I'd love to connect.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dipendu-mukherjee-4199a8226/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Dipendu27)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-111827?style=for-the-badge&logo=vercel&logoColor=white)](https://dipendu-mukherjee-portfolio.vercel.app/)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=100&section=footer" />

<sub>Updated daily · Last updated: Day 4 · Phase 1: MLOps & Production Engineering</sub>

</div>
