from django import forms
from .models import UserSignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserSignUp
        fields = ["full_name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "@gmail.com" in email:
            raise forms.ValidationError("Please only use gmail.com!")
        return email
