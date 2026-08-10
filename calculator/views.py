from django.shortcuts import render


def index(request):
    tools = [
        {
            'name': 'Compound Interest',
            'url': 'calculator:compound',
            'icon': '📈',
            'description': 'Calculate wealth growth with compounding over time',
            'color': '#10b981',
            'tag': 'Growth',
        },
        {
            'name': 'SIP Calculator',
            'url': 'calculator:sip',
            'icon': '💰',
            'description': 'Estimate returns on systematic monthly investments',
            'color': '#3b82f6',
            'tag': 'Planning',
        },
        {
            'name': 'CAGR Calculator',
            'url': 'calculator:cagr',
            'icon': '📊',
            'description': 'Measure your investment\'s compounded annual growth rate',
            'color': '#8b5cf6',
            'tag': 'Analysis',
        },
        {
            'name': 'ROI Calculator',
            'url': 'calculator:roi',
            'icon': '🎯',
            'description': 'Calculate return on investment and annualized gains',
            'color': '#f59e0b',
            'tag': 'Returns',
        },
        {
            'name': 'EMI Calculator',
            'url': 'calculator:emi',
            'icon': '🏦',
            'description': 'Compute loan EMI with full amortization schedule',
            'color': '#ef4444',
            'tag': 'Loans',
        },
        {
            'name': 'SWP Calculator',
            'url': 'calculator:swp',
            'icon': '💸',
            'description': 'Plan sustainable monthly withdrawals from your corpus',
            'color': '#06b6d4',
            'tag': 'Retirement',
        },
    ]
    return render(request, 'calculator/index.html', {'tools': tools})


def compound(request):
    result = None
    form_data = {}
    yearly_data = []

    if request.method == 'POST':
        try:
            principal = float(request.POST.get('principal', 0))
            rate = float(request.POST.get('rate', 0))
            years = int(request.POST.get('years', 0))
            frequency = int(request.POST.get('frequency', 12))

            if principal <= 0 or rate < 0 or years <= 0:
                raise ValueError('Invalid inputs')

            form_data = request.POST
            r = rate / 100
            n = frequency
            t = years

            for yr in range(1, t + 1):
                amount = principal * (1 + r / n) ** (n * yr)
                yearly_data.append({
                    'year': yr,
                    'amount': round(amount, 2),
                    'interest': round(amount - principal, 2),
                })

            final_amount = principal * (1 + r / n) ** (n * t)
            result = {
                'principal': principal,
                'final_amount': round(final_amount, 2),
                'total_interest': round(final_amount - principal, 2),
                'rate': rate,
                'years': years,
                'multiplier': round(final_amount / principal, 2),
            }
        except (ValueError, ZeroDivisionError, TypeError):
            result = {'error': 'Please enter valid positive numbers.'}

    return render(request, 'calculator/compound.html', {
        'result': result,
        'form_data': form_data,
        'yearly_data': yearly_data,
    })


def sip(request):
    result = None
    form_data = {}
    yearly_data = []

    if request.method == 'POST':
        try:
            monthly = float(request.POST.get('monthly', 0))
            rate = float(request.POST.get('rate', 0))
            years = int(request.POST.get('years', 0))

            if monthly <= 0 or rate < 0 or years <= 0:
                raise ValueError('Invalid inputs')

            form_data = request.POST
            i = rate / 12 / 100
            n = years * 12

            if i > 0:
                fv = monthly * (((1 + i) ** n - 1) / i) * (1 + i)
            else:
                fv = monthly * n

            total_invested = monthly * n

            for yr in range(1, years + 1):
                m = yr * 12
                if i > 0:
                    val = monthly * (((1 + i) ** m - 1) / i) * (1 + i)
                else:
                    val = monthly * m
                invested = monthly * m
                yearly_data.append({
                    'year': yr,
                    'invested': round(invested, 2),
                    'value': round(val, 2),
                    'gains': round(val - invested, 2),
                })

            result = {
                'monthly': monthly,
                'rate': rate,
                'years': years,
                'total_invested': round(total_invested, 2),
                'total_returns': round(fv - total_invested, 2),
                'final_value': round(fv, 2),
                'wealth_gained': round(((fv - total_invested) / total_invested) * 100, 1),
            }
        except (ValueError, ZeroDivisionError, TypeError):
            result = {'error': 'Please enter valid positive numbers.'}

    return render(request, 'calculator/sip.html', {
        'result': result,
        'form_data': form_data,
        'yearly_data': yearly_data,
    })


def cagr(request):
    result = None
    form_data = {}

    if request.method == 'POST':
        try:
            beginning = float(request.POST.get('beginning', 0))
            ending = float(request.POST.get('ending', 0))
            years = float(request.POST.get('years', 0))

            if beginning <= 0 or ending <= 0 or years <= 0:
                raise ValueError('Invalid inputs')

            form_data = request.POST
            cagr_val = ((ending / beginning) ** (1 / years) - 1) * 100
            absolute_return = ((ending - beginning) / beginning) * 100
            gain = ending - beginning

            result = {
                'beginning': beginning,
                'ending': ending,
                'years': years,
                'cagr': round(cagr_val, 2),
                'absolute_return': round(absolute_return, 2),
                'gain': round(gain, 2),
                'positive': gain >= 0,
            }
        except (ValueError, ZeroDivisionError, TypeError):
            result = {'error': 'Please enter valid positive numbers.'}

    return render(request, 'calculator/cagr.html', {
        'result': result,
        'form_data': form_data,
    })


def roi(request):
    result = None
    form_data = {}

    if request.method == 'POST':
        try:
            initial = float(request.POST.get('initial', 0))
            final = float(request.POST.get('final', 0))
            period = float(request.POST.get('period', 1))

            if initial <= 0 or period <= 0:
                raise ValueError('Invalid inputs')

            form_data = request.POST
            net_profit = final - initial
            roi_val = (net_profit / initial) * 100
            annualized_roi = ((final / initial) ** (1 / period) - 1) * 100

            result = {
                'initial': initial,
                'final': final,
                'period': period,
                'net_profit': round(net_profit, 2),
                'roi': round(roi_val, 2),
                'annualized_roi': round(annualized_roi, 2),
                'positive': net_profit >= 0,
            }
        except (ValueError, ZeroDivisionError, TypeError):
            result = {'error': 'Please enter valid positive numbers.'}

    return render(request, 'calculator/roi.html', {
        'result': result,
        'form_data': form_data,
    })


def emi(request):
    result = None
    form_data = {}
    schedule = []

    if request.method == 'POST':
        try:
            principal = float(request.POST.get('principal', 0))
            rate = float(request.POST.get('rate', 0))
            tenure = int(request.POST.get('tenure', 0))

            if principal <= 0 or rate < 0 or tenure <= 0:
                raise ValueError('Invalid inputs')

            form_data = request.POST
            r = rate / 12 / 100
            n = tenure * 12

            if r > 0:
                emi_val = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
            else:
                emi_val = principal / n

            total_payment = emi_val * n
            total_interest = total_payment - principal

            balance = principal
            for yr in range(1, tenure + 1):
                yr_interest = 0
                yr_principal_paid = 0
                for _ in range(12):
                    if balance <= 0:
                        break
                    interest_part = balance * r
                    principal_part = emi_val - interest_part
                    yr_interest += interest_part
                    yr_principal_paid += principal_part
                    balance = max(0, balance - principal_part)
                schedule.append({
                    'year': yr,
                    'principal_paid': round(yr_principal_paid, 2),
                    'interest_paid': round(yr_interest, 2),
                    'balance': round(balance, 2),
                })

            result = {
                'principal': principal,
                'rate': rate,
                'tenure': tenure,
                'emi': round(emi_val, 2),
                'total_payment': round(total_payment, 2),
                'total_interest': round(total_interest, 2),
                'interest_pct': round((total_interest / total_payment) * 100, 1),
            }
        except (ValueError, ZeroDivisionError, TypeError):
            result = {'error': 'Please enter valid positive numbers.'}

    return render(request, 'calculator/emi.html', {
        'result': result,
        'form_data': form_data,
        'schedule': schedule,
    })


def swp(request):
    result = None
    form_data = {}
    yearly_data = []

    if request.method == 'POST':
        try:
            corpus = float(request.POST.get('corpus', 0))
            withdrawal = float(request.POST.get('withdrawal', 0))
            rate = float(request.POST.get('rate', 0))
            years = int(request.POST.get('years', 0))

            if corpus <= 0 or withdrawal <= 0 or years <= 0:
                raise ValueError('Invalid inputs')

            form_data = request.POST
            r = rate / 12 / 100
            balance = corpus
            total_withdrawn = 0
            sustainable = True
            depletion_year = None

            for yr in range(1, years + 1):
                yr_withdrawn = 0
                for _ in range(12):
                    if balance <= 0:
                        sustainable = False
                        if depletion_year is None:
                            depletion_year = yr
                        break
                    balance = balance * (1 + r) - withdrawal
                    yr_withdrawn += withdrawal
                    total_withdrawn += withdrawal

                yearly_data.append({
                    'year': yr,
                    'balance': round(max(balance, 0), 2),
                    'withdrawn': round(yr_withdrawn, 2),
                })

                if balance <= 0 and depletion_year is None:
                    depletion_year = yr
                    sustainable = False

            result = {
                'corpus': corpus,
                'withdrawal': withdrawal,
                'rate': rate,
                'years': years,
                'total_withdrawn': round(total_withdrawn, 2),
                'final_balance': round(max(balance, 0), 2),
                'sustainable': sustainable,
                'depletion_year': depletion_year,
            }
        except (ValueError, ZeroDivisionError, TypeError):
            result = {'error': 'Please enter valid positive numbers.'}

    return render(request, 'calculator/swp.html', {
        'result': result,
        'form_data': form_data,
        'yearly_data': yearly_data,
    })
