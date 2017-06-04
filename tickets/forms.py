from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . models import Ticket


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Authentication failed. Please try again.")
        return self.cleaned_data


class TicketForm(forms.ModelForm):

    OPEN_STATUS = 1
    REOPENED_STATUS = 2
    RESOLVED_STATUS = 3
    CLOSED_STATUS = 4
    DUPLICATE_STATUS = 5

    STATUS_CHOICES = (
        (OPEN_STATUS, 'Open'),
        (REOPENED_STATUS, 'Reopened'),
        (RESOLVED_STATUS, 'Resolved'),
        (CLOSED_STATUS, 'Closed'),
        (DUPLICATE_STATUS, 'Duplicate'),
    )

    status_choice = forms.ChoiceField(
        label="Ticket Status", choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control input-sm'})
    )
