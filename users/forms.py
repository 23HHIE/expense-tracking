from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core import validators


class NewUserForm(UserCreationForm):
    common_attrs = {'class': 'border-0 focus:outline-none'}
    email = forms.EmailField(required=True,
                            validators=[validators.validate_email],
                            widget=forms.EmailInput(attrs=common_attrs))
                             
    min_length = 2
    max_length = 30
    message_lt_min = f"At least {min_length} characters."
    message_ht_max = f"At most{max_length} characters."
    
    name_message='The username only accepts letters!'
    username = forms.CharField(required=True,
                                validators=[
                                            validators.MinLengthValidator(min_length, message_lt_min),
                                            validators.MaxLengthValidator(max_length, message_ht_max),
                                widget=forms.TextInput(attrs=common_attrs))
    # encrypt password input
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs=common_attrs))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs=common_attrs))
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


