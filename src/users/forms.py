from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, TeachingStaff, NonTeachingStaff, Apply


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password1',
			'password2',
		]
		
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = [
			'image',
		]


class TeachingStaffUpdateForm(forms.ModelForm):

	class Meta:
		model = TeachingStaff
		fields = ['sickleave', 'officialleave', 'casualleave']

class NonTeachingStaffUpdateForm(forms.ModelForm):

	class Meta:
		model = NonTeachingStaff
		fields = ['sickleave', 'officialleave', 'annualleave']

class ApplyForm(forms.ModelForm):
	class Meta:
		model = Apply
		fields = [
			'timeofftype',
			'startdate',
			'enddate'
		]
