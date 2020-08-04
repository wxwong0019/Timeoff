from django import forms

from .models import Timeoff


class TimeoffForm(forms.ModelForm):
	title		= forms.CharField(label='dis title', widget=forms.TextInput(attrs={'placeholder' : "enter yo"}))
	email 		=  forms.EmailField()
	description = forms.CharField(
		widget=forms.Textarea(
			attrs={
				"cols" : 120,
				"class": "new-class-nameetwo",
				"rows" : 20
		}))
	startdate	= forms.DateField()
	startsession= forms.TimeField()
	enddate		= forms.DateField()
	endsession	= forms.TimeField()	

	class Meta:
		model = Timeoff
		fields = [
			'title',
			'name',
			'description',
			'startdate',
			'startsession',
			'enddate',
			'endsession',
			'email',
		]
	# def clean_title(self, *arg, **kwarg):
	# 	title = self.cleaned_data.get("title")
	# 	if not "Ansin" in title:
	# 		raise forms.ValidationError("this is not Ansin")
	# 	else:
	# 		return title

	def clean_email(self, *arg, **kwarg):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("this is not email")
		else:
			return email


