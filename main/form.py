from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegister(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label='username', min_length=6, max_length=8, help_text="use your student id as your username")
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()
        for c in username:
            if c.isalpha():
                raise ValidationError("User name should be you student id")
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']