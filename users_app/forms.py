




from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile

#form ce mostenesc user creation form
class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:    #keeps the configuration in one place
		model = User    #lucram cu modelul user. cand facem form.save() se va salva in acest model
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:   
		model = User    
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']