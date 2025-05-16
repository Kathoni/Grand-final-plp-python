# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Transaction
from .forms import CategoryForm, TransactionForm
from django.db.models import Sum


@login_required
def home(request):
    categories = Category.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    # Calculate total spent per category
    category_spending = {}
    for category in categories:
        total_spent = Transaction.objects.filter(user=request.user, category=category).aggregate(Sum('amount'))['amount__sum'] or 0
        category_spending[category.id] = total_spent

    context = {
        'categories': categories,
        'transactions': transactions,'category_spending': category_spending,
    }
    return render(request, 'budget/home.html', context)


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('budget:home')
    else:
        form = CategoryForm()
    return render(request, 'budget/add_category.html', {'form': form})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('budget:home')
    else:
        form = TransactionForm()
        form.fields['category'].queryset = Category.objects.filter(user=request.user)  # Limit categories to user's
    return render(request, 'budget/add_transaction.html', {'form': form})

@login_required
def edit_category(request, category_id):
  category = get_object_or_404(Category, pk=category_id, user=request.user)
  if request.method == 'POST':
      form = CategoryForm(request.POST, instance=category)
      if form.is_valid():
          form.save()
          return redirect('budget:home')
  else:
      form = CategoryForm(instance=category)
  return render(request, 'budget/edit_category.html', {'form': form})

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id, user=request.user)
    if request.method == 'POST':
        category.delete()
        return redirect('budget:home')
    return render(request, 'budget/delete_category.html', {'category': category})

@login_required
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('budget:home')
    else:
        form = TransactionForm(instance=transaction)
        form.fields['category'].queryset = Category.objects.filter(user=request.user)
    return render(request, 'budget/edit_transaction.html', {'form': form})

@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('budget:home')
    return render(request, 'budget/delete_transaction.html', {'transaction': transaction})
