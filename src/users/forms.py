from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from customstaff.models import User, TeachingStaffDetail, NonTeachingStaffDetail, TeachingStaff, NonTeachingStaff, LeaveApplication,VicePrincipalDetail
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

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
TIME_FORMAT = '%I:%M %p'

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
	
	# startdate = forms.DateField(label='Starting Date',
	# 		 widget=forms.TextInput(     
	# 		 attrs={
	# 		 'type': 'date',
	# 		 'class': 'startdate',
	# 		 } 
	# 		))

	startdate = forms.DateField(label= 'Starting Date',widget=DatePickerInput(
		options={
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'class': 'start-time',
			 'placeholder' : "Pick a Date!",
			 })
			)
						
	starttime = forms.TimeField(label= 'Starting Time',widget=TimePickerInput(
		options={"stepping" : 5,
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'class': 'starttime',
			 'placeholder' : "Pick a Time!",
			 })
			)

	enddate = forms.DateField(label= 'Ending Date',widget=DatePickerInput(
		options={
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'class': 'start-time',
			 'placeholder' : "Pick a Date!",
			 })
			)
						
	endtime = forms.TimeField(label= 'Ending Time',widget=TimePickerInput(
		options={"stepping" : 5,
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'class': 'starttime',
			 'placeholder' : "Pick a Time!",
			 })
			)
	
	reason	= forms.CharField(
		widget=forms.Textarea(
			attrs={
				"cols" : 50,
				"rows" : 3
		}))		 
	class Meta:
		model = LeaveApplication
		fields = [
			'teachertimeofftype',
			'startdate',
			'starttime',
			'enddate',
			'endtime',
			'reason'
		]
		
				# 'startdate': forms.DatePickerInput(options={
				# 		 "format": "MM/DD/YYYY", # moment date-time format
				# 		 "showClose": True,
				# 		 "showClear": True,
				# 		 "showTodayButton": False,
				# 		 "stepping": 30,
				# 		 }
				# 	)}
				
			# {'enddate': DatePickerInput(options={
			# 		 "format": "MM/DD/YYYY", # moment date-time format
			# 		 "showClose": True,
			# 		 "showClear": True,
			# 		 "showTodayButton": False,
			# 		 "stepping": 30})
			# 		}
	# def clean(self):
	# 	startdate = self.cleaned_data.get('startdate')
	# 	enddate = self.cleaned_data.get('enddate')

	# 	if enddate <= startdate:
	# 		raise forms.ValidationError("End date must be later than start date")
	# 	return super(TeacherApplyForm, self).clean()

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

class SecondValidate(forms.ModelForm):
	class Meta:
		model = LeaveApplication
		fields = [
			'secondstatus',
			'secondcomment'
		]

class FinalValidate(forms.ModelForm):
	class Meta:
		model = LeaveApplication
		fields = [
			'finalstatus',
			'finalcomment'
		]
