from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from customstaff.models import User, TeachingStaffDetail, NonTeachingStaffDetail, TeachingStaff, NonTeachingStaff, LeaveApplication,VicePrincipalDetail, Picker
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
		fields = ['sickleave', 'annualleave', 'compensatedleave', 'duration']

	# def clean(self):
 #    	modify = self.cleaned_data['duration']
 #    	if obj.user.teachertimeofftype == sickleave:
 #    		sickleave = sickleave - modify

	# 	return super(NonTeachingStaffUpdateForm, self).clean()

class TeacherApplyForm(forms.ModelForm):
	
	startdate = forms.DateField(label= 'From date',widget=DatePickerInput(
		options={
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'class': 'start-time',
			 'placeholder' : "Pick a Date!",
			 })
			)
						
	starttime = forms.TimeField(required=False, label= 'From Time',widget=TimePickerInput(
		options={"stepping" : 5,
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'class': 'starttime',
			 'placeholder' : "Pick a Time!",
			 })
			)

	enddate = forms.DateField(label= 'Thru Date',widget=DatePickerInput(
		options={
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'class': 'start-time',
			 'placeholder' : "Pick a Date!",
			 })
			)
						
	endtime = forms.TimeField(required=False ,label= 'Thru Time',widget=TimePickerInput(
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
		
	def clean_enddate(self):
		startdate = self.cleaned_data.get('startdate')
		enddate = self.cleaned_data.get('enddate')

		if startdate > enddate:
			raise forms.ValidationError("End date must be later than start date")
		else:
			return enddate

class NonTeacherApplyForm(forms.ModelForm):
	startdate = forms.DateField(label= 'From date',widget=DatePickerInput(
		options={
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'class': 'start-time',
			 'placeholder' : "Pick a Date!",
			 })
			)
						
	starttime = forms.TimeField(required=False, label= 'From Time',widget=TimePickerInput(
		options={"stepping" : 5,
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'class': 'starttime',
			 'placeholder' : "Pick a Time!",
			 })
			)

	enddate = forms.DateField(label= 'Thru Date',widget=DatePickerInput(
		options={
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'class': 'start-time',
			 'placeholder' : "Pick a Date!",
			 })
			)
						
	endtime = forms.TimeField(required=False, label= 'Thru Time',widget=TimePickerInput(
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
			'nonteachertimeofftype',
			'startdate',
			'starttime',
			'enddate',
			'endtime',
			'reason'
		]

class PickerForm(forms.ModelForm):
	pickuser = forms.ModelMultipleChoiceField(queryset = User.objects.all())
	class Meta:
			model = Picker
			fields = [
				'pickuser'
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
	# finalduration = DecimalField(_("Modified duration (hr for OT, else use days)"),max_digits = 4, decimal_places = 0, default = )
	class Meta:
		model = LeaveApplication
		fields = [
			'finalstatus',
			'finalduration',
			'finalcomment',
		]

