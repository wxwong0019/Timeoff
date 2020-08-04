from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Timeoff(models.Model):
	title		= models.CharField(max_length =50)
	name		= models.CharField(max_length =50, default="input")
	description	= models.TextField(blank=True, null=False, default='testing')
	startdate	= models.DateField(default='01-01-0001')
	startsession= models.TimeField(default=datetime.time(16, 00))
	enddate		= models.DateField(default='01-01-0001')
	endsession	= models.TimeField(default=datetime.time(16, 00))
	email 		= models.EmailField(default='default@test.edu')
	upload		= models.FileField()


	def get_absolute_url(self):
		return  reverse("timeoff:timeoff-detail", kwargs={"myid" : self.id})  #f"/timeoff/{self.id}"
