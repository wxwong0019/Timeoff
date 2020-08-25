from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import datetime 

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
	is_teacher = models.BooleanField('teacher status', default=False)
	is_nonteacher = models.BooleanField('Non teaching staff status', default=False)
	is_supervisor = models.BooleanField('Supervisor status', default=False)
	is_viceprincipal = models.BooleanField('Viceprincipal status', default=False)
	is_principal = models.BooleanField('Principal status', default=False)

	REQUIRED_FIELDS = ['username']
	objects = MyUserManager()


	class Types(models.TextChoices):
		TEACHINGSTAFF = 'teachingstaff', 'teachingstaff'
		NONTEACHINGSTAFF = 'nonteachingstaff', 'nonteachingstaff'
		SUPERVISOR = 'supervisor', 'supervisor'
		VICEPRINCIPAL = 'viceprincipal', 'viceprincipal'
		PRINCIPAL = 'principal', 'principal'
	
	base_type = Types.NONTEACHINGSTAFF
	
	type = models.CharField(_("Types"), max_length=50, choices=Types.choices)

	def save(self, *args, **kwargs):
			if self.type == User.Types.TEACHINGSTAFF:
				self.is_teacher = True
				self.is_nonteacher = False
				self.is_supervisor = False
				self.is_viceprincipal = False
				self.is_principal = False
			elif self.type == User.Types.NONTEACHINGSTAFF:
				self.is_teacher = False
				self.is_nonteacher = True
				self.is_supervisor = False
				self.is_viceprincipal = False
				self.is_principal = False
			elif self.type == User.Types.SUPERVISOR:
				self.is_teacher = True
				self.is_nonteacher = False
				self.is_supervisor = True
				self.is_viceprincipal = False
				self.is_principal = False
			elif self.type == User.Types.VICEPRINCIPAL:
				self.is_teacher = True
				self.is_nonteacher = False
				self.is_supervisor = False
				self.is_viceprincipal = True
				self.is_principal = False
			elif self.type == User.Types.PRINCIPAL:
				self.is_teacher = True
				self.is_nonteacher = False
				self.is_supervisor = False
				self.is_viceprincipal = False
				self.is_principal = True
			return super(User, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("users:detail", kwargs={"username": self.username})
		
	def __str__(self):
		return self.username

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
class SupervisorManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type = User.Types.SUPERVISOR)

class VicePrincipalManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type = User.Types.VICEPRINCIPAL)

class PrincipalManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type = User.Types.PRINCIPAL)

class TeachingStaff(User):
	base_type = User.Types.TEACHINGSTAFF
	objects = TeachingStaffManager()

	class Meta:
		proxy = True

	def save(self, *args, **kwargs):
		if not self.pk:
			self.type = self.base_type
		return super().save(*args, **kwargs)

class NonTeachingStaff(User):
	base_type = User.Types.NONTEACHINGSTAFF
	objects = NonTeachingStaffManager()
	
	class Meta:
		proxy = True

	def save(self, *args, **kwargs):
		if not self.pk:
			self.type = self.base_type
		return super().save(*args, **kwargs)

class Supervisor(User):
	base_type = User.Types.SUPERVISOR
	objects = SupervisorManager()

	class Meta:
		proxy = True

	def save(self, *args, **kwargs):
		if not self.pk:
			self.type = self.base_type
		return super().save(*args, **kwargs)

class VicePrincipal(User):
	base_type = User.Types.VICEPRINCIPAL
	objects = VicePrincipalManager()

	class Meta:
		proxy = True

	def save(self, *args, **kwargs):
		if not self.pk:
			self.type = self.base_type
		return super().save(*args, **kwargs)

class Principal(User):
	base_type = User.Types.PRINCIPAL
	objects = PrincipalManager()

	class Meta:
		proxy = True

	def save(self, *args, **kwargs):
		if not self.pk:
			self.type = self.base_type
		return super().save(*args, **kwargs)

class TeachingStaffDetail(models.Model):
	user = models.OneToOneField(TeachingStaff, on_delete=models.CASCADE)
	sickleave = models.DecimalField(_("Sick Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	# officialleave = models.DecimalField(_("Offical Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	casualleave = models.DecimalField(_("Casual Leave Available Days"),max_digits = 3, decimal_places = 2, default = 0)
	firstday = models.DateField(default=timezone.now())

	is_teacher = models.BooleanField('teacher status', default=True)
	is_viceprincipal = models.BooleanField('Viceprincipal status', default=False)
	is_principal = models.BooleanField('Principal status', default=False)


class NonTeachingStaffDetail(models.Model):
	user = models.OneToOneField(NonTeachingStaff, on_delete=models.CASCADE)
	sickleave = models.DecimalField(_("Sick Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	# officialleave = models.DecimalField(_("Offical Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	annualleave = models.DecimalField(_("Annual Leave Available Days"),max_digits = 3, decimal_places = 2, default = 0)
	firstday = models.DateField(default=timezone.now())

	is_nonteacher = models.BooleanField('Non teaching staff status', default=True)

class SupervisorDetail(models.Model):
	user = models.OneToOneField(Supervisor, on_delete=models.CASCADE, null=True, blank=True, related_name='SupervisorDetail')
	overseeing = models.ManyToManyField(NonTeachingStaff, related_name='overseeing')
	sickleave = models.DecimalField(_("Sick Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	# officialleave = models.DecimalField(_("Offical Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	annualleave = models.DecimalField(_("Annual Leave Available Days"),max_digits = 3, decimal_places = 2, default = 0)
	firstday = models.DateField(default=timezone.now())

	is_supervisor = models.BooleanField('Supervisor status', default=True)
	is_teacher = models.BooleanField('Teacher status', default=True)

class VicePrincipalDetail(models.Model):
	user = models.OneToOneField(VicePrincipal, on_delete=models.CASCADE,null=True, blank=True, related_name='VicePrincipalDetail')
	sickleave = models.DecimalField(_("Sick Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	# officialleave = models.DecimalField(_("Offical Leave Available Days"),max_digits = 4, decimal_places = 1, default = 0)
	annualleave = models.DecimalField(_("Annual Leave Available Days"),max_digits = 3, decimal_places = 2, default = 0)
	firstday = models.DateField(default=timezone.now())
	is_teacher = models.BooleanField('teacher status', default=True)
	is_viceprincipal = models.BooleanField('VicePrincipal status', default=True)
	allvp = models.ManyToManyField(VicePrincipal, related_name='allvp')

class PrincipalDetail(models.Model):
	user = models.OneToOneField(Principal, on_delete=models.CASCADE,null=True, blank=True, related_name='PrincipalDetail')
	is_teacher = models.BooleanField('teacher status', default=True)
	is_principal = models.BooleanField('Principal status', default=True)

class LeaveApplication(models.Model):
	sickleave = 'SL'
	officialleave = 'OL'
	casualleave = 'CL'
	annualleave = 'AL'
	specialtuberculosisleave = 'TB'
	maternalleave = 'ML'
	paternityleave = 'PL'
	studyleave = 'ST'
	jurorsorwitnesses = 'JK'
	leaveforspecialevents = 'LS'
	overtime = 'OT'
	others = 'O'

	TEACHER_TIMEOFF_CHOICES = [
		(sickleave, 'Sick Leave'),
		(officialleave, 'Official Leave'),
		(casualleave, 'Casual Leave'),
		(specialtuberculosisleave, 'Special Tuberculosis Leave'),
		(maternalleave, 'Maternal Leave'),
		(paternityleave, 'Paternity Leave'),
		(studyleave, 'Study Leave'),
		(jurorsorwitnesses, 'Jurors or Witnesses'),
		(leaveforspecialevents, 'Leave for Special Events'),
		(others, 'Others'),
	]

	NONTEACHER_TIMEOFF_CHOICES = [
		(sickleave, 'Sick Leave'),
		(officialleave, 'Official Leave'),
		(annualleave, 'Annual Leave'),
		(overtime, 'Over Time'),		
		(specialtuberculosisleave, 'Special Tuberculosis Leave'),
		(maternalleave, 'Maternal Leave'),
		(paternityleave, 'Paternity Leave'),
		(jurorsorwitnesses, 'Jurors or Witnesses'),
		(others, 'Others'),
	]

	pending = 'Pending'
	approved = 'Approved'
	denied = 'Denied'

	STATUS_CHOICES = [
		(pending, 'pending'),
		(approved, 'approved'),
		(denied, 'denied'),
	]

	teachertimeofftype = models.CharField(_("Teacher Type of Leave"),max_length= 10,choices = TEACHER_TIMEOFF_CHOICES, default=sickleave)
	nonteachertimeofftype = models.CharField(_("Non Teacher Type of Leave"),max_length= 10,choices = NONTEACHER_TIMEOFF_CHOICES, default=sickleave)
	startdate = models.DateTimeField(default=timezone.now())
	enddate = models.DateTimeField(default=timezone.now())
	duration = models.DurationField(default = datetime.timedelta)
	reason = models.CharField(max_length= 200, default = '')
	firststatus = models.CharField(max_length= 10,choices = STATUS_CHOICES, default=pending)
	firstcomment = models.CharField(max_length= 200, blank=True)
	secondstatus = models.CharField(max_length= 10,choices = STATUS_CHOICES, default=pending)
	secondcomment = models.CharField(max_length= 200, blank=True)
	finalstatus = models.CharField(max_length= 10,choices = STATUS_CHOICES, default=pending)
	finalcomment = models.CharField(max_length= 200, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	# is_teacher = models.BooleanField('teacher status', default=False)
	# is_nonteacher = models.BooleanField('Non teaching staff status', default=False)
	# is_supervisor = models.BooleanField('Supervisor status', default=False)
	# is_viceprincipal = models.BooleanField('Viceprincipal status', default=False)
	# is_principal = models.BooleanField('Principal status', default=False)
	# leaveoversee = models.ManyToManyField(Supervisor, related_name='leaveoversee')

	def __str__(self):
		return self.user.username

	def save(self, *args, **kwargs):
		start_date = self.startdate
		end_date = self.enddate
		self.duration = end_date - start_date
		return super(LeaveApplication, self).save(*args, **kwargs)



	def get_absolute_url(self):
		return  reverse("managerapprove", kwargs={"myid" : self.id})  #f"/timeoff/{self.id}"


		