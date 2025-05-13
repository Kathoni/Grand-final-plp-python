from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Transaction, Budget

def dashboard(request):
    transactions = Transaction.objects.all().order_by('-date')
    total_spent = sum(t.amount for t in transactions)
    budgets = Budget.objects.all()
    budget_total = sum(b.limit for b in budgets)
    budget_remaining = budget_total - total_spent

    return render(request, 'finance/dashboard.html', {
        'transactions': transactions,
        'total_spent': total_spent,
        'budget_remaining': budget_remaining,
    })
