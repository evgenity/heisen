from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from team.models import Person

class RegistrationForm(UserCreationForm):
    slack_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'slack_name','password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
