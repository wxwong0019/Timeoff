import django_filters
from django import forms

from django_filters import *
from django_filters.widgets import *
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

from customstaff.models import *

class teacherLeaveApplicationFilter(django_filters.FilterSet):
	created_at = DateFilter(label= 'Date Created', lookup_expr='gte')
	class Meta:
		model = LeaveApplication
		fields = [
		'teachertimeofftype',
		'created_at'
		]


class nonteacherLeaveApplicationFilter(django_filters.FilterSet):
	created_at = DateFilter(label= 'Date Created', lookup_expr='gte')

	class Meta:
		model = LeaveApplication
		fields = [
		'nonteachertimeofftype',
		'created_at'
		]

class LeaveApplicationFilter(django_filters.FilterSet):
	created_at = DateFilter(label= 'Date Created', lookup_expr='gte')

	class Meta:
		model = LeaveApplication
		fields = [
		
		'alltimeofftype',
		'stafftype',
		'user',
		'created_at',
		'attachmentreceived',
		'attachmentrequired'
		]