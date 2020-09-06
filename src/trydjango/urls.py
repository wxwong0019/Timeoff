"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from page.views import homepage_view, about_view
from Timeoff.views import (
    timeoff_create_view, 
    dynamic_lookup_view,
    timeoff_delete_view,
    timeoff_list_view,
)
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage_view),
    path('about/', about_view),
    path('timeoff/', include('Timeoff.urls')),
    # path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('teacherapply/', user_views.teacherapply, name='teacherapply'),
    path('nonteacherapply/', user_views.nonteacherapply, name='nonteacherapply'),
    path('supervisorapply/', user_views.supervisorapply, name='supervisorapply'),
    path('login_success/', user_views.login_success, name='login_success'),    
    path('success/', user_views.success, name='success'),
    path('managerlistview/', user_views.managerlistview, name='managerlistview'),
    path('<int:myid>/managerapprove/', user_views.managerapprove, name='managerapprove'),
    path('vplistview/', user_views.vplistview, name='vplistview'),
    path('<int:myid>/vpapprove/', user_views.vpapprove, name='vpapprove'),
    path('plistview/', user_views.plistview, name='plistview'),
    path('<int:myid>/papprove/', user_views.papprove, name='papprove'),
    path('plistviewdecided/', user_views.plistviewdecided, name='plistviewdecided'),
    path('<int:myid>/papprovedecided/', user_views.papprovedecided, name='papprovedecided'),
    path('userlistview/', user_views.userlistview, name='userlistview'),
    path('<int:myid>/userdetailview/', user_views.userdetailview, name='userdetailview'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






