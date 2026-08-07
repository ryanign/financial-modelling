# Financial Modelling with Python

A self-paced course bridging physical sciences expertise into financial risk,
portfolio construction, and climate-adjusted investing — built for the terminal.

*Curriculum designed with Claude (Anthropic). Scope may be ambitious, but the goal is to build real foundational fluency.*

## Introduction

Financial modelling is the practice of building quantitative representations
of how money moves through time, assets, and risk. It is the core language
of investment decisions, from valuing a single company to constructing a
portfolio that accounts for physical climate exposure.

This course is designed for practitioners with a physical sciences background
(geosciences, climate, environmental sciences) who already think quantitatively
but have no formal finance training. The translation is more direct than it
appears: discounting cash flows shares the same logic as radioactive decay,
portfolio variance is error propagation under a different name, and time series
analysis in finance draws from the same toolkit as geophysical signal processing.

The goal is not to replicate a finance degree. It is to build enough fluency
in financial concepts and tooling to work at the intersection of physical risk
and capital markets — a space where domain expertise in earth systems is
genuinely scarce and increasingly valued.

Each session is 1 hour: concept-first, then implementation in Python,
then a hands-on exercise. All work is done in the terminal.

## Track

Risk · Portfolio Construction · Climate-Adjusted Investing

## Stack

- Python 3.12
- venv + pip
- Terminal-first workflow

## Setup

```bash
git clone git@github.com:ryanign/financial-modelling.git
cd financial-modelling
python3.12 -m venv fm-py312
source fm-py312/bin/activate
pip install -r requirements.txt
python verify.py
```

## Sessions

| # | Title | Core Concept |
|---|-------|-------------|
| 01 | Time Value of Money | Cash flows, NPV, IRR |
| 02 | Financial Statements | Income statement, balance sheet, cash flow |
| 03 | Valuation I — DCF | Free cash flow, WACC, terminal value |
| 04 | Valuation II — Multiples | EV/EBITDA, P/E, sector comps |
| 05 | Risk & Return I | Volatility, distributions, Sharpe ratio |
| 06 | Risk & Return II — Climate | Physical risk, transition risk, stranded assets |
| 07 | Portfolio Construction | Weights, diversification, efficient frontier |
| 08 | Time Series & Market Data | Returns, autocorrelation, rolling stats |
| 09 | Automation & Tooling | Reusable model design, modular scripts |
| 10 | Capstone | Climate-adjusted portfolio risk tool |

## Repository Structure

```
financial-modelling/
├── readme.md
├── requirements.txt
├── verify.py
├── session_01/
│   ├── notes.md       # concept notes — read first
│   ├── main.py        # session walkthrough — run and study
│   └── exercise.py    # your exercise — attempt before checking solution
├── session_02/
│   └── ...
└── data/              # shared datasets (added as needed)
```





