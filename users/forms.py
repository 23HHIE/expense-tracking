from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'border-0 focus:outline-none'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'border-0 focus:outline-none'}))
    # encrypt password input
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'border-0 focus:outline-none'}))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'border-0 focus:outline-none'}))
    budget = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


