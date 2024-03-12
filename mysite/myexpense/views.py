from datetime import datetime

from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required


class LandingPage(TemplateView):
    template_name = 'myexpense/landingpage.html'


@login_required()
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'myexpense/expenses.html', {'expenses': expenses})


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('myexpense:expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'myexpense/addexpense.html', {'form': form})


@login_required
def modify_expense(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == 'POST':
        expense.type = request.POST.get('type')
        expense.fee = request.POST.get('fee')
        payment_date_str = request.POST.get('payment_date')
        if payment_date_str:
            expense.date = datetime.strptime(payment_date_str, '%B %d, %Y').date()
        expense.save()
        return redirect('myexpense:expense_list')
    context = {'expense': expense}
    return render(request, 'myexpense/modifyexpense.html', context)


@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    context = {'expense': expense}
    if request.method == 'POST':
        expense.delete()
        return redirect('myexpense:expense_list')
    return render(request, 'myexpense/delete.html', context)
