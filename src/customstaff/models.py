from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class MyUserManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		"""
		Creates and saves a superuser with the given email, date of
		birth and password.
		"""
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	USERNAME_FIELD = 'email'
	email = models.EmailField(verbose_name='email',max_length=255,unique=True)
	username = models.CharField(max_length= 100, default = '',unique=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	REQUIRED_FIELDS = ['username']
	objects = MyUserManager()

	class Types(models.TextChoices):
		TEACHINGSTAFF = 'teachingstaff', 'teachingstaff'
		NONTEACHINGSTAFF = 'nonteachingstaff', 'nonteachingstaff'

	base_type = Types.TEACHINGSTAFF
	
	type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=base_type)


	def get_absolute_url(self):
		return reverse("users:detail", kwargs={"username": self.username})

	def save(self, *args, **kwargs):
		if not self.id:
			self.type = self.base_type
		return super().save(*args, **kwargs)
		
	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin


class TeachingStaffManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type = User.Types.TEACHINGSTAFF)

class NonTeachingStaffManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type = User.Types.NONTEACHINGSTAFF)

class TeachingStaff(User):
	base_type = User.Types.TEACHINGSTAFF
	objects = TeachingStaffManager()

	class Meta:
		proxy = True

class TeachingStaffMore(models.Model):
	user = models.OneToOneField(TeachingStaff, on_delete=models.CASCADE)
	sickleave = models.DecimalField(_("Sick Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	# officialleave = models.DecimalField(_("Offical Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	casualleave = models.DecimalField(_("Casual Leave Available Days"),max_digits = 3, decimal_places = 2, default = 0)
	firstday = models.DateField(default=timezone.now())

class NonTeachingStaff(User):
	base_type = User.Types.NONTEACHINGSTAFF
	objects = NonTeachingStaffManager()
	
	class Meta:
		proxy = True

class NonTeachingStaffMore(models.Model):
	user = models.OneToOneField(NonTeachingStaff, on_delete=models.CASCADE)
	sickleave = models.DecimalField(_("Sick Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	# officialleave = models.DecimalField(_("Offical Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	annualleave = models.DecimalField(_("Annual Leave Available Days"),max_digits = 3, decimal_places = 2, default = 0)
	firstday = models.DateField(default=timezone.now())

class LeaveApplication(models.Model):
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

	pending = 'pending'
	approved = 'approved'
	denied = 'denied'

	STATUS_CHOICES = [
		(pending, 'pending'),
		(approved, 'approved'),
		(denied, 'denied'),
	]

	timeofftype = models.CharField(max_length= 10,choices = TIMEOFF_CHOICES, default=sickleave)
	startdate = models.DateTimeField(default=timezone.now())
	enddate = models.DateTimeField(default=timezone.now())
	reason = models.CharField(max_length= 200, default = '')
	firststatus = models.CharField(max_length= 10,choices = STATUS_CHOICES, default=pending)
	firstcomment = models.CharField(max_length= 200, default = '')
	finalstatus = models.CharField(max_length= 10,choices = STATUS_CHOICES, default=pending)
	finalcomment = models.CharField(max_length= 200, default = '')
	user = models.ForeignKey(User, on_delete=models.CASCADE)



		