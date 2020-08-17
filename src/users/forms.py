from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from customstaff.models import User, TeachingStaffDetail, NonTeachingStaffDetail, TeachingStaff, NonTeachingStaff, LeaveApplication



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
		model = TeachingStaffDetail
		fields = ['sickleave', 'casualleave']

class NonTeachingStaffUpdateForm(forms.ModelForm):

	class Meta:
		model = NonTeachingStaffDetail
		fields = ['sickleave', 'annualleave']

class TeacherApplyForm(forms.ModelForm):

	class Meta:
		model = LeaveApplication
		fields = [
			'teachertimeofftype',
			'startdate',
			'enddate',
			'reason'
		]
	# def clean_duration(self, *arg, **kwarg):
	# 	start_date = self.cleaned_data["startdate"]
	# 	end_date = self.cleaned_data["enddate"]
	# 	duration = end_date - start_date
	# 	# if not email.endswith("edu"):
	# 	# 	raise forms.ValidationError("this is not email")
	# 	# else:
	# 	return duration

class NonTeacherApplyForm(forms.ModelForm):

	class Meta:
		model = LeaveApplication
		fields = [
			'nonteachertimeofftype',
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
