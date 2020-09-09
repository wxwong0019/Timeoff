from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User, TeachingStaffDetail, NonTeachingStaffDetail, SupervisorDetail,VicePrincipalDetail, LeaveApplication, IncrementAll
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'username', 'is_admin', 'is_staff')
	search_fields = ('email', 'username')
	readonly_field = ()

	fieldsets = ()
	filter_horizontal = ()
	list_filter = ()

admin.site.register(User, CustomUserAdmin)
admin.site.register(TeachingStaffDetail)
admin.site.register(NonTeachingStaffDetail)
admin.site.register(SupervisorDetail)
admin.site.register(LeaveApplication)
admin.site.register(VicePrincipalDetail)
admin.site.register(IncrementAll)