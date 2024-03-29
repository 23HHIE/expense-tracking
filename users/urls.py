from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from django.contrib.auth import views as authentication_view

app_name = 'users'
urlpatterns = [
    # signup page
    path('register/', views.register, name='register'),
    # login page
    path('login/', authentication_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    # logout page
    path('logout/', authentication_view.LogoutView.as_view(next_page='/wisespend/'), name='logout'),
    # decorator
    path('profile/', views.profile, name='profile')
]
