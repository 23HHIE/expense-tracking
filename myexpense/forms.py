from django import forms

from .models import Expense, Budget


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['type', 'fee', 'payment_date']


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount']


class UpdateBudgetForm(forms.Form):
    budgetAmount = forms.DecimalField(label='Budget Amount', max_digits=10, decimal_places=2)