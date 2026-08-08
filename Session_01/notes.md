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

## 4. Internal Rate of Return (IRR)

**Concept:**
IRR answers: *"What actual return does this investment generate?"*

It is the discount rate that makes $NPV = 0$ - the breakeven rate.
No closed-form solution exists; IRR is found numerically by itteration.

$$\text{Solve for } r \text{ where} \quad \sum_{t=0}^{n} \frac{CF_t}{(1 + r)^{t}} = 0$$

**Decision rule:**

| Condition | Decision |
|-----------|----------|
| $IRR \>$ hurdle rate | Accept |
| $IRR \<$ rrudle rate | Reject |

The **hurdle rate** is the minimum return your organisation requires
(also called the required rate of return of cost of capital).

**Real-world example:**
Using the same flood risk platform above:

$$CF = [-200{,}000,\ 60{,}000, \80{,}000, \90{,}000, \100{,}000] \quad \Rightarrow \quad IRR \approx 22.8\%$$

If the company's hurdle rate is 10%, IRR of 22.8% comfortably clears it.
The platform is a viable investment.

**Important limitation:**
IRR can give misleading results when cash flows change sign more than once (e.g., a project requiring major reinvestment mid-life, commin in mining and energy). Always cross-check IRR with NPV.

**Analogy:**
IRR is a root-finding problem -- identical in structure to finding 
the depth of a reflector by iterating on velocity in seismic processing,
or finding the equilibirum temperature in a radiative balance model.
`scipy.optimize.brentq` handles this the same way in both cases.

```python
cash_flows = [-200_000, 60_000, 80_000, 90_000, 100_000]
irr(cash_flows)
# returns: 0.2281 -> 22.81%
```

$\rightarrow$ Function: `irr(cash_flows)`
Internally uses `scipy.optimize.brentq` to find the root of $NPV = 0$.

---

## 5. Annuity (PV)

**Concept:**
An annuity is a series of equal cash flows paid at regular intervals
for a fixed number of periods.

$$PV_{\text{annuity}} = CF \times \frac{1 - (1 + r)^{-n}}{r}$$

**Real-world example:**
A government signs a 10-year contract to pay a climate monitoring
company $80,000 per year. The company's discount rate is 6%.
What is that contract worth today?

$$PV_{\text{annuity}} = 80{,}000 \times \frac{1 - (1.06)^(-10)}{0.06} = 80{,}000 \times 7.3601 = \$588{,}808$$

The company can use this to decide the minimum contract value they would accept upfront as a lump sum instead.

**In main.py:**
```python
pv_annuity(cf=80_000, r=0.06, n=10)
# returns: 588,808.15
```

$\rightarrow$ Function: `pv_annuity(cf, r, n)`

---

## 6. Future Value of Annuity (FVA)

**Concept:**
The PV annuity asks: "what is a stream of future payments worth today?"
The FV annuity asks the opposite: "if I invest regularly, how much will
I accumulate by a future date?"

$$FVA = CF \times \frac{(1 + r)^{n}}{r}$$

This is one of the most widely used formulas in investment management.

**Real-world example -- personal:**
You invest Rp1,000,000.00 per month into a mutual fund (reksa dana)
with an annual return of 8% for 10 years (120 months).

$$r = \frac{0.08}{12} = 0.00\overline{6} \quad (\text{monthly rate}), \qquad n = 120$$

$$FVA = 1{,}000{,}000 \times \frac{(1.00667)^{120} - 1}{0.00667} \approx \text{Rp}182{,}946{,}000$$

You contributed Rp120,000,000.00 in total.
The extra ~Rp63 million is compounding -- money earning money.

**Real-world example -- institutional:**
Investment managers use FVA in several contexts:
- **Defined contribution pension funds** -- projecting how much a member accumulates from monthly contributions over a working career
- **Sinking funds** -- a company sets aside fixed quarterly payments to retire a bond at maturity
- **Liability-Driven Investment (LDI)** -- matching accumulated assets against known future obligations (pension payouts, insurance claims)
- **Project finance** -- modelling debt service reserve accounts built up from regular project revenues.

**Analogy:**
FVA is the discrete integral of a constant signal multiplied by an exponentially growing kernel --
structurally similar to computing the cumulative response of a system to a repeated forcing,
as in climate forcing accumulation over time.

**In main.py:**
```python
fv_annuity(cf=1_000_000, r=0.08/12, n=120)
# returns: 182,946,026.85
```

$\rightarrow$ Function: `fv_annuity(cf, r, n)`
Note: always match the period of $r$ and $n$. Monthly contributions $\rightarrow$ monthly rate $= r_{\text{annual}} / 12$, $n$ in months.

---




