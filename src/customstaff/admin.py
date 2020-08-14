from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User, TeachingStaffMore, NonTeachingStaffMore, TeachingStaff, NonTeachingStaff, LeaveApplication
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'username', 'is_admin', 'is_staff')
	search_fields = ('email', 'username')
	readonly_field = ()

	fieldsets = ()
	filter_horizontal = ()
	list_filter = ()

admin.site.register(User, CustomUserAdmin)
admin.site.register(TeachingStaffMore)
admin.site.register(NonTeachingStaffMore)
admin.site.register(TeachingStaff)
admin.site.register(NonTeachingStaff)
admin.site.register(LeaveApplication)