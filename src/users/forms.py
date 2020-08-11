from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from customstaff.models import User, TeachingStaffMore, NonTeachingStaffMore, TeachingStaff, NonTeachingStaff, LeaveApplication



# class UserRegisterForm(UserCreationForm):
# 	email = forms.EmailField()

# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'email',
# 			'password1',
# 			'password2',
# 		]
		
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
		model = TeachingStaffMore
		fields = ['sickleave', 'casualleave']

class NonTeachingStaffUpdateForm(forms.ModelForm):

	class Meta:
		model = NonTeachingStaffMore
		fields = ['sickleave', 'annualleave']

class ApplyForm(forms.ModelForm):
	class Meta:
		model = LeaveApplication
		fields = [
			'timeofftype',
			'startdate',
			'enddate',
			'reason'
		]

class FirstValidate(forms.ModelForm):
	class Meta:
		model = LeaveApplication
		fields = [
			'firststatus',
			'firstcomment'
		]

class FinalValidate(forms.ModelForm):
	class Meta:
		model = LeaveApplication
		fields = [
			'finalstatus',
			'finalcomment'
		]
