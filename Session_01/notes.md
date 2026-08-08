# Session 01: Time Value of Money

## Core Question
Why is $100 today worth more than $100 a year from now? 
Because money available today can be invested to earn a return. 
This seemingly simple idea is the foundation of almost every financial model.

---

## 1. Future Value (FV)

**Concept:**
If you invest money today, it grows over time. Future Value answers:
*"How much will my money be worth at a future date?"*

$$FV = PV \times (1 + r)^n$$

Where:
- $PV$ = Present Value, the amount you start with today
- $r$  = interest rate per period (e.g. 0.08 for 8%)
- $n$  = number of periods (years, months, etc.)
- $FV$ = Future Value, the amount you end up with

**Real-world example:**
A geothermal company sets aside $100,000 today into a reserve fund
earning 8% annually, to cover future decommissioning costs in 3 years.
How much will that fund be worth?

$$FV = \$100,000 \times (1.00 + 0.08)^3 = \$125,971.00$$

The company will have ~$126k available, enough to plan against.

**Analogy:**
This is exponential growth, the same equation as radioactive ingrowth of a daughter isotope,
or compound interest in a saving account. 
The rate $r$ plays the role of growth constant $\lambda$.

**In main.py**
```python
future_value(pv=100_000, r=0.08, n=3)
# returns: 125971.20
```

$\rightarrow$ Function: `future_value(pv, r, n)`

---

## 2. Present Value (PV)

**Concept**
The reverse of FV. Present Value answers:
*"What is a future cash flow worth in today's money?"*

$$PV = \frac{FV}{(1 + r)^{n}}$$

The interest rate $r$ used here is called the **discount rate**.
The process is called **discounting**.

**Real-world example:**
A carbon credit project is contractually guaranteed to pay $500,000 in 5 years.
An investor wants to buy that contract today.
If the discount rate is 7%, what should they pay?

$$PV = \frac{\$500{,}000}{(1.00 + 0.07)^{5}} = \$356{,}493$$

Paying more than ~$365k for that contract means the investor is not earning their required 7% return.

**Analogy:**
Discounting is mathematically identical to radioactive decay.
A future cash flow "decays" in value as you move it backward in time.
The discount rate is the decay constant: higher rate, faster decay, lower present value.

**In main.py:**
```python
present_value(fv=500_000, r=0.07, n=5)
# returns: 356,492.56
```

$\rightarrow$ Function: `present_value(fv, r, n)`

---

## 3. Net Present Value (NPV)

**Concept:**
Real projects involve multiple cash flows at different points in time --
an upfront cost, the a stream of revenues over years.
NPV sums all of them after discounting each to today.

$$NPV = \sum_{t=0}^{n} \frac{CF_t}{(1 + r)^{t}}$$

Where:
- $CF_t$ = cash flow at time $t$
  - Negative = money going out (investment, costs)
  - Positive = money coming in (revenue, savings)
- $t = 0$ is today -- no discounting needed
- $r$ = discount rate

**Decision rule:**

| NPV | Meaning | Decision |
|-----|---------|----------|
| $> 0$ | Investment creates value above required return | Accept |
| $< 0$ | Investment destroys value | Reject |
| $= 0$ | Investment excatly meets required return | Indifferent |

**Real-world example:**
A climate consultancy is evaluating whether to build a flood risk
assessment platform. Costs and projected revenues:

| Year | Cash Flow |
|------|-----------|
| 0 | -$200,000 (build the platform) |
| 1 | +$60,000 (early clients) |
| 2 | +$80,000 |
| 3 | +$90,000 |
| 4 | +$100,000 |

Discount rate: 10%

$$NPV = -200{,}000
+ \frac{60{,}000}{(1.10)^{1}}
+ \frac{80{,}000}{(1.10)^{2}}
+ \frac{90{,}000}{(1.10)^{3}}
+ \frac{100{,}000}{(1.10)^{4}}$$

$$NPV = \$-200{,}000 + \$54{,}545 + \$66{,}116 + \$67{,}618 + \$68{,}301 = +\$56{,}580 \quad \rightarrow \text{Accept}$$

**Analogy:**
NPV is a weighted sum where decays exponentially with time --
identical to computing the weighted mean of a geophysical signal
where older measurements carry less weight dur to instrument drift.

**In main.py:**
```python
cash_flows = [-200_000, 60_000, 80_000, 90_000, 100_000]
npv(rate=0.10, cash_flows=cash_flows)
# returns: 56,580.38
```

$\rightarrow$ Function: `npv(rate, cash_flows)`
Note: `cash_flows[0]` is period 0 (today). Pass the initial investment
as a negative number.

---


















