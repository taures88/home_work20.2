from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django import forms

from catalog.forms import StyleForm
from users.models import User


class UserRegisterForm(StyleForm, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        success_url = reverse_lazy('users:login')


class UserProfileForm(StyleForm, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'country', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
