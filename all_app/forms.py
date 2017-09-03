from django import forms
from .models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'uk-input uk-width-1-2', 'style': 'width: 100%; margin: 20px 0px; border-radius: 10px;'}))
    #url = forms.URLField(label='Your website', required=False)
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'uk-input uk-width-1-2', 'style' : 'width: 100%; margin: 20px 0px; border-radius: 10px;'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class' : 'uk-input uk-width-1-2', 'style' : 'width: 100%; margin: 20px 0px; border-radius: 10px;'}))
    def save(self, commit=True):
        user = super(UpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    class Meta:
        model = User
        fields = ("username", "email", "password")
        
class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'uk-input uk-width-1-2', 'style': 'width: 100%; margin: 20px 0px; border-radius: 10px;'}))
    #url = forms.URLField(label='Your website', required=False)
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class' : 'uk-input uk-width-1-2', 'style' : 'width: 100%; margin: 20px 0px; border-radius: 10px;'}))
    class Meta:

        fields = ("username", "password")
