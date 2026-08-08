"""
Session 01: Time Value of Money
Run with: python Session_01/main.py
"""

import numpy as np
from scipy.optimize import brentq

#-----------------------------------------
# 1. FUTURE VALUE
#-----------------------------------------
def future_value(pv, r, n):
    """
    Compute future value of a present amount

    Parameters:
    pv : float - present value (today's amount)
    r  : float - periodic interest rate (e.g. 0.08 for 8%)
    n  : int   - number of periods

    Returns:
    float - future value
    """
    return pv * (1 + r) ** n

#-----------------------------------------
# 2. PRESENT VALUE
#-----------------------------------------
def present_value(fv, r, n):
    """
    Discount a future amount back to today.

    Parameters:
    fv : float - future value
    r  : float - discount rate per period
    n  : int   - number of periods

    Returns:
    float - present value
    """
    return fv / ((1 + r) ** n)

#-----------------------------------------
# 3. NET PRESENT VALUE
#-----------------------------------------
def npv(rate, cash_flows):
    """
    Compute Net Present Value of a series of cash flows.

    Parameters:
    rate       : float      - discount rate per period
    cash_flows : list/array - cash flows indexed by period
                              cash_flows[0] is period 0 (today, usually negative)
                              cash_flows[1] is period 1, etc.

    Returns:
    float - npv
    """
    cash_flows = np.array(cash_flows)
    periods = np.arange(len(cash_flows))
    return np.sum(cash_flows / (1 + rate) ** periods)

#-----------------------------------------
# 4. INTERNAL RATE OF RETURN
#-----------------------------------------
def irr(cash_flows):
    """
    Computer Internal Rate of Return numerically

    Uses Brent's method to find the root of NPV(r) = 0.
    Assumes cash_flows contains at least one sign change.

    Parameters:
    cash_flows : list/array - cash flows by period (period 0 first)

    Returns:
    float - IRR, or None if no solution found
    """
    try:
        result = brentq(lambda r:npv(r, cash_flows), a=-0.999, b=10.0)
        return result
    except ValueError:
        return None

#-----------------------------------------
# 5. ANNUITY PRESENT VALUE
#-----------------------------------------
def pv_annuity(cf, r, n):
    """
    Present value of an annuity (equal cash flows for n periods)

    Parameters:
    cf : float - cash flow per period
    r  : float - discount rate per period
    n  : int   - number of periods

    Returns:
    float - present value of the annuity
    """
    return cf * (1 - (1 + r) ** (-n)) / r

#-----------------------------------------
# 6. FUTURE VALUE OF ANNUITY
#-----------------------------------------
def fv_annuity(cf, r, n):
    """
    Future value of an annuity - total accumulation from regular investments.

    Answers: 'If I invest CF every period at rate r for n periods,
    how much will I have at the end?'

    Common uses: retirement saving, sinking funds, recurring investments.

    Parameters:
    cf : float - cash flow per period (regular investment amount)
    r  : float - periodic rate (match period to cf: monthyly cf -> monthly r)
    n  : int   - number of periods

    Returns:
    float - accumulated future value

    Note:
    Period consistency is critical:
        Monthly contribution -> r = annual_rate / 12, n in months
        Annual contribution  -> r = annual_rate     , n in years
    """
    return cf * ((1 + r) ** n - 1) / r

#-----------------------------------------
# 7. PERPETUITY PRESENT VALUE
#-----------------------------------------
def pv_perpetuity(cf, r):
    """
    Present value of a perpetuity (equal cash flows forever).

    Parameters:
    cf : float - cash flow per period
    r  : float - discount rate per period

    Returns:
    float - present value of the perpetuity
    """
    return cf / r

#-----------------------------------------
# DEMO
#-----------------------------------------
def main():
    print('=' * 50)
    print('SESSION 01: Time Value of Money')
    print('=' * 50)

    # --- Future Value ---
    print('\n--- Future Value ---')
    pv = 100  # present value
    r = 0.08  # rate per-period (e.g. year)
    n = 3     # period (year)

    fv = future_value(pv, r, n)
    print(f'  PV = ${pv}, rate = {r*100:.2f}%/year, periods = {n} years')
    print(f'  FV = ${fv:.2f}')

    # --- Present Value ---
    print('\n--- Present Value ---')
    pv_back = present_value(fv, r, n)
    print(f'  FV = ${fv:.2f}, rate = {r*100:.2f}%/year, periods = {n} years')
    print(f'  PV = ${pv_back:.2f} (should equal ${pv})')

    # --- NPV ---
    print('\n --- Net Present Value ---')
    cash_flows = [-1000, 300, 200, 500, 200, 800]
    discount_rate = 0.10
    project_npv = npv(discount_rate, cash_flows)
    print(f'  Cash flows    : ${cash_flows}')
    print(f'  Discount rate : {discount_rate*100:.2f}%')
    print(f'  NPV           : ${project_npv:.2f}')
    decision = 'ACCEPT' if project_npv > 0 else 'REJECT'
    print(f'  Decision      : {decision}')

    # --- IRR ---
    print('\n--- Internal Rate of Return ---')
    project_irr = irr(cash_flows)
    hurdle_rate = 0.10
    if project_irr is not None:
        print(f'  IRR = {project_irr*100:.2f}%')
        print(f'  Hurdle rate = {hurdle_rate*100:.2f}%')
        decision = 'ACCEPT' if project_irr > hurdle_rate else 'REJECT'
        print(f'  Decission   = {decision}')
    else:
        print(f'  IRR cold not be computed (check cash flow signs).')

    # --- Annuity ---
    print('\n--- Annuity ---')
    cf = 500          # current value
    r_ann = 0.06      # annual discount rate per-year
    n_ann = 10        # duration in years
    ann_pv = pv_annuity(cf, r_ann, n_ann)
    print(f'  CF = ${cf}/period, rate = {r_ann*100:.2f}%, periods = {n_ann}')
    print(f'  PV of annuity = ${ann_pv:.2f}')

    # --- Future Value of Annuity ---
    print('\n--- Future Value of Annuity ---')
    monthly_cf     = 1_000_000
    annual_return  = 0.08
    years          = 10
    r_monthly      = annual_return / 12
    n_months       = years * 12
    accumulated    = fv_annuity(cf=monthly_cf, r=r_monthly, n=n_months)
    total_invested = monthly_cf * n_months
    print(f'  Monthly investment    : Rp{monthly_cf:,.2f}')
    print(f'  Annual return         : {annual_return*100:.2f}%')
    print(f'  Duration              : {years} years ({n_months} months)')
    print(f'  Total invested        : Rp{total_invested:,.2f}')
    print(f'  Accumulated value     : Rp{accumulated:,.2f}')
    print(f'  Gain from compounding : Rp{accumulated - total_invested:,.2f}')

    # --- Perpetuity ---
    print('\n--- Perpetuity ---')
    perp_pv = pv_perpetuity(cf, r_ann)
    print(f'  CF = ${cf}/period, rate = {r_ann*100:.2f}%, forever')
    print(f'  PV of perpetuity = ${perp_pv:.2f}')
    print(f'  (Annuity converges to perpetuity as n -> ∞)')

    print('\n' + '=' * 50)
    print('End of Session 01 demo.')
    print('Proceed to exercise.py')
    print('=' * 50)


if __name__ == '__main__':
    main()



