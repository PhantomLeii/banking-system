from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput({'autocomplete': 'current-password', 'class': 'form-control'})
    )