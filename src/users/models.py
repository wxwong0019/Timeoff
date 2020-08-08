from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)



class TeachingStaff(models.Model):
	sickleave = models.DecimalField(max_digits = 3, decimal_places = 2)
	officialleave = models.DecimalField(max_digits = 3, decimal_places = 2)
	casualleave = models.DecimalField(max_digits = 3, decimal_places = 2)
	user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

class NonTeachingStaff(models.Model):
	sickleave = models.DecimalField(max_digits = 3, decimal_places = 2)
	officialleave = models.DecimalField(max_digits = 3, decimal_places = 2)
	annualleave = models.DecimalField(max_digits = 3, decimal_places = 2)
	user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

class Apply(models.Model):
	sickleave = 'SL'
	officialleave = 'OL'
	casualleave = 'CL'
	annualleave = 'AL'

	TIMEOFF_CHOICES = [
		(sickleave, 'sick leave'),
		(officialleave, 'official leave'),
		(casualleave, 'casual leave'),
		(annualleave, 'annual leave'),
	]
	timeofftype = models.CharField(max_length= 10,choices = TIMEOFF_CHOICES, default=sickleave)
	startdate = models.DateTimeField(default=timezone.now())
	enddate = models.DateTimeField(default=timezone.now())
	user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
