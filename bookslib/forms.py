from django import forms
from .models import User, Books


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=155, required=True)
    password = forms.CharField(max_length=155, widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    password2 = forms.CharField(max_length=55)

    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError("Passwords Doesn't Match")


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

