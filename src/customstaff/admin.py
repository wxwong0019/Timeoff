from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from .models import User, TeachingStaffMore, NonTeachingStaffMore, TeachingStaff, NonTeachingStaff, LeaveApplication



admin.site.register(User)
admin.site.register(TeachingStaffMore)
admin.site.register(NonTeachingStaffMore)
admin.site.register(TeachingStaff)
admin.site.register(NonTeachingStaff)
admin.site.register(LeaveApplication)