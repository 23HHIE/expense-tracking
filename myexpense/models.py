

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.type} - ${self.fee}"


class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    # Define a method to enable the user to add or modify their budgets
    def set_budget(self, amount):
        self.amount = amount
        self.save()

    # Define a method to calculate the amount of the remaining budget
    def get_remaining_budget(self):
        # Fetch the current date
        today = now().date()
        # Fetch the first date of the current month
        start_day = today.replace(day=1)
        # Aggregate all the spending
        cost_this_month = Expense.objects.filter(

            user=self.user,
            payment_date__gte=start_day
        ).aggregate(total_expenses=models.Sum('fee'))['total_expenses'] or 0
        # Calculate the current budget remaining by subtracting the cost from the budget
        remaining_budget = self.amount - cost_this_month
        return round(remaining_budget, 2)

    def get_remaining_budget_percentage(self):
        remaining_budget = self.get_remaining_budget()
        if self.amount != 0:
            percentage = round((remaining_budget / self.amount) * 100, 2)
            return percentage
        else:
            return 0

    def __str__(self):
        return f"{self.user.username} - Budget: {self.amount}"
