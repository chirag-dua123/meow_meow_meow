# AI Engineering — Course Materials

This repository contains course materials, examples, and exercises for a 12-week AI Engineering course covering Python, data, classical ML, deep learning, deployment, and product skills.

## Course Overview

The course is a practical, project-first introduction to the tools and workflows used to build AI systems. Students will work through weekly modules, short assignments, and two major projects (vision and NLP), finishing with an end-to-end product and interview prep.

## Weekly Syllabus

- **Week 1 — Foundations:** Python, Git, CLI, HTTP/REST, SQL basics.
- **Week 2 — Data Wrangling:** Data cleaning, pandas, EDA, visualization, basic statistics.
- **Week 3 — Classical ML:** Linear & logistic regression, tree models, scikit-learn pipelines.
- **Week 4 — Model Quality:** Model evaluation, cross-validation, feature engineering, hyperparameter tuning.
- **Week 5 — PyTorch Basics:** Tensors, autograd, training loop.
- **Week 6 — Vision Project:** CNNs and transfer learning.
- **Week 7 — NLP Project:** Transformers and fine-tuning with Hugging Face.
- **Week 8 — MLOps Basics:** Docker, model serving with FastAPI, simple CI.
- **Week 9 — Cloud Deployment:** Deploy a model to AWS/GCP/Azure with cost-aware setup.
- **Week 10 — Data Engineering:** Intro to Spark and a simple batch pipeline.
- **Week 11 — Product Integration:** Minimal frontend + API + monitoring; assemble end-to-end product.
- **Week 12 — Capstone & Careers:** Interview prep, system design, portfolio polish, README and presentation.

## Learning Outcomes

- Build reproducible data workflows using Python and pandas.
- Train, evaluate, and tune classical and deep learning models.
- Implement training loops with PyTorch and fine-tune transformer models.
- Containerize and serve models with FastAPI and Docker.
- Deploy models to cloud providers and reason about cost.
- Integrate a minimal frontend with an API and add basic monitoring.
- Prepare a professional README, presentation, and interview-ready portfolio.

## Repository Structure

Top-level folders you will use:

- `src/` — course code, notebooks, and exercises.
- `data/` — sample datasets used in exercises and projects.
- `tests/` — unit tests and small CI examples.
- `docs/` — additional reading and reference notes.
- `docker/` — example Dockerfile(s) for serving and reproducible environments.

## Setup

1. Clone the repository:

```bash
git clone <repo-url>
cd ai_engineer
```

2. Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\Activate.ps1 or Activate.bat
pip install -r requirements.txt
```

## Running Examples & Exercises

- Run the calculator module:

```bash
python -m src.calculator
```

- Run the wordcount example on the provided `data/input.txt`:

```bash
python -m src.wordcount data/input.txt
```

## Tests

Run unit tests with:

```bash
pytest
```

CI is configured in `.github/workflows/pytest.yml`.

## Projects & Assessments

- Vision project (Week 6): image classification using transfer learning.
- NLP project (Week 7): transformer fine-tuning and evaluation.
- Capstone (Week 11–12): end-to-end product combining a minimal frontend, API, and monitoring; includes a README and short presentation.

Assessment artifacts to submit:

- Final project README (clear setup & run instructions).
- Notebook or script reproducing training & evaluation.
- Short slide deck or video walkthrough (5–10 minutes).

## Contributing & Style

- Follow PEP8; use `black` and `ruff` when available.
- Write tests for non-trivial functions in `tests/`.
- Use meaningful commit messages and feature branches.

## Support & Contact

If you have questions or find issues, open an issue in the repository or contact the course maintainer.

---

Updated core README with course syllabus and instructions.
