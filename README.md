# 📈 InvestIQ — Django Investment Calculator Suite

> A professional-grade, full-stack investment toolkit built with Django and Python. Six powerful calculators to plan, analyze, and grow your wealth — all server-side, no database, no external APIs.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?style=flat-square&logo=django)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)
![No DB](https://img.shields.io/badge/Database-None-lightgrey?style=flat-square)

---

## 🧮 Calculators

| Tool | Formula | Use Case |
|------|---------|---------|
| **Compound Interest** | A = P(1 + r/n)^(nt) | Grow a lump-sum investment |
| **SIP** | FV = M × [(1+i)^n − 1]/i × (1+i) | Monthly systematic investing |
| **CAGR** | (End/Begin)^(1/years) − 1 | Measure investment growth rate |
| **ROI** | (Final − Initial) / Initial × 100 | Evaluate investment performance |
| **EMI** | P × r × (1+r)^n / [(1+r)^n − 1] | Loan repayment planning |
| **SWP** | Balance = Balance×(1+r) − Withdrawal | Retirement withdrawal sustainability |

---

## ✨ Features

- 🏗 **Full Django MVC** — Views, Templates, URL routing, static files
- 📊 **Interactive Charts** — Chart.js visualizations for all tools
- 📋 **Amortization Tables** — Year-by-year or month-by-month breakdowns
- 🌙 **Dark Theme** — Professional dark UI with CSS variables
- 📱 **Responsive** — Mobile-friendly layout
- ⚡ **Zero Runtime Dependencies** — No database, no external APIs
- 🐍 **Pure Python Math** — All calculations done server-side

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/cedricevan98/InvestIQ.git
cd InvestIQ

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

# 3. Install Django
pip install -r requirements.txt

# 4. Run the development server
python manage.py runserver

# 5. Open http://localhost:8000
```

---

## 🗂 Project Structure

```
InvestIQ/
├── manage.py
├── requirements.txt
├── investiq/                  # Django project
│   ├── settings.py            # No DB — stateless design
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── calculator/                # Main app
    ├── views.py               # All 6 calculator views
    ├── urls.py
    ├── templates/calculator/
    │   ├── base.html          # Dark theme layout
    │   ├── index.html         # Dashboard
    │   ├── compound.html
    │   ├── sip.html
    │   ├── cagr.html
    │   ├── roi.html
    │   ├── emi.html
    │   └── swp.html
    └── static/calculator/
        └── css/style.css      # Full dark theme CSS
```

---

## 🛠 Tech Stack

- **Backend**: Python 3.10+, Django 4.2
- **Frontend**: Django Templates, HTML5, CSS3 (zero frameworks)
- **Charts**: Chart.js 4.4 (CDN)
- **Fonts**: Inter (Google Fonts CDN)
- **Database**: None

---

## 📐 Architecture Decisions

- **No database** — All calculations are pure math (stateless). No models, no migrations.
- **No external APIs** — Inputs come from the user, calculations run in Django views.
- **Server-side math** — Python handles all financial formulas in `views.py`.
- **Chart.js CDN** — Charts rendered client-side from data embedded in templates.
- **Django templates** — Classic server-rendered HTML, no SPA complexity.

---

## 📜 License

MIT © [Cedric Evan](https://github.com/cedricevan98)
