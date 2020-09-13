from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from customstaff.models import User, TeachingStaffDetail, NonTeachingStaffDetail, TeachingStaff, NonTeachingStaff, LeaveApplication,VicePrincipalDetail, Picker, IncrementAll
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.core.exceptions import ValidationError
from django.contrib import messages

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
		fields = ['sickleave', 'annualleave', 'compensatedleave']

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
	
	# def clean_starttime(self):
	# 	if self.cleaned_data.get('starttime') != None and self.cleaned_data.get('endtime') != None:
	# 		starttime = self.cleaned_data.get('starttime')
	# 		endtime = self.cleaned_data.get('endtime')
	# 		startdate = self.cleaned_data.get('startdate')
	# 		enddate = self.cleaned_data.get('enddate')
	# 		if startdate.month == enddate.month and startdate.day == enddate.day:
	# 			if starttime.minute < endtime.minute or starttime.hour < endtime.hour:
	# 				return starttime
	# 		elif startdate.day < enddate.day or startdate.month < enddate.month:
	# 			return starttime
	# 		else:
	# 			raise ValidationError("End time must be later than start time")

	def clean(self):
		startdate = self.cleaned_data.get('startdate')
		enddate = self.cleaned_data.get('enddate')
		starttime = self.cleaned_data.get('starttime')
		endtime = self.cleaned_data.get('endtime')
		if starttime != None and endtime != None:
			
			if startdate.day < enddate.day and startdate.month == enddate.month:
				print('111111111')
				
			elif startdate.month < enddate.month:
				print('22222222')
				return endtime
			elif startdate.month == enddate.month and startdate.day == enddate.day:
				if starttime.minute  >=  endtime.minute and starttime.hour  >=  endtime.hour:
					raise ValidationError("End date must be later than start date")
				elif starttime.hour  >  endtime.hour:
					raise ValidationError("End date must be later than start date")
			else:
				print('4444444444')
				raise ValidationError("End date must be later than start date")
	
		elif starttime == None and endtime == None:
			if startdate.day <= endtime.hour and startdate.month == enddate.month:
				print('5555555')
				return endtime
			elif startdate.month < enddate.month:
				print('666666666')
				return endtime
			else:
				print('7777777')
				raise ValidationError("End date must be later than start date")
		else:
			raise ValidationError("End date must be later than start date")
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
	finalduration = forms.DecimalField(required=False,label =  "Modified duration (Optional)", widget=forms.TextInput(attrs={'placeholder' : "Hour for OT, Days for Leave"}) )
	class Meta:
		model = LeaveApplication
		fields = [
			'finalstatus',
			'finalcomment',
			'finalduration',
		]

class IncrementAllForm(forms.ModelForm):
	created_at = forms.DateField(label= 'Date Added',widget=DatePickerInput(
		options={
				"toolbarPlacement" : 'top',
				},
		attrs={
			 'placeholder' : "Pick a Date!",
			 })
			)
	class Meta:
			model = IncrementAll
			fields = [
				'created_at',

			]
class CancelForm(forms.ModelForm):
	finalcomment = forms.DecimalField(required=False,label =  "Cancel reason", widget=forms.TextInput(attrs={'placeholder' : "Reason"}) )
	class Meta:
		model = LeaveApplication
		fields = [
			'finalcomment',
		]
