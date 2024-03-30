from django.urls import path
from . import views

app_name = 'myexpense'
urlpatterns = [
    # landing page
    path('', views.LandingPage.as_view(), name='landing_page'),

    # expenses list
    path('details/', views.expense_list, name='expense_list'),
    # add expense page
    # path('add-expense/', views.add_expense, name='add_expense'),
    path('add/', views.add_expense, name='add_expense'),

    path('modify/<int:expense_id>/', views.modify_expense, name='modify_expense'),
    # delete expense
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),

    path('setbudget/<int:user_id>/', views.update_budget, name='update_budget'),

]
