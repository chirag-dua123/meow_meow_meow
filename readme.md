# AI Engineering Project

A collection of Python scripts and utilities for learning and practicing AI engineering concepts.  
This repository includes examples, a calculator CLI, word count utility, and test workflows.

---

## 📂 Project Structure

```
.
├── basics.py
├── calculator.py
├── wordcount.py
├── requirements.txt
├── pytest.ini
├── tests/
└── .github/workflows/pytest.yml
```

---

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-engineering.git
   cd ai-engineering
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   - Core dependencies: `pytest`
   - Optional (development): `black`, `ruff`

---

## ▶️ Usage

Run the scripts directly:

```bash
python basics.py
python calculator.py
python wordcount.py input.txt
```

Or use the module syntax:

```bash
python -m src.calculator
```

---

## 🧮 Calculator CLI

The calculator supports basic operations.  
Errors are raised as `Exception`s (not strings), so tests can assert on exceptions or values.

Example:

```bash
python calculator.py 5 3 add
```

---

## 🧪 Testing

Run all tests with:

```bash
pytest
```

Configuration is in `pytest.ini`.

---

## 🔄 Continuous Integration

GitHub Actions workflow is included at `.github/workflows/pytest.yml`.  
It runs:

```bash
pip install -r requirements.txt
pytest
```

on **Python 3.11**.

---

## 🎨 Code Style

- Consistent formatting enforced with `black` and `ruff`.
- Each file includes module docstrings.
- `if __name__ == "__main__":` used consistently.

---

##Commands

python -m src.calculator
python -m src.wordcount input.txt
pytest
