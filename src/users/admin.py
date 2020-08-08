from django.contrib import admin

# Register your models here.
from .models import Profile, TeachingStaff, NonTeachingStaff, Apply

admin.site.register(Profile)
admin.site.register(TeachingStaff)
admin.site.register(NonTeachingStaff)
admin.site.register(Apply)


