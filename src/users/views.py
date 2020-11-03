from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.core.mail import send_mail
from .filters import *
from .forms import *
from customstaff.models import *
from django.http import HttpResponse 
import csv
# Create your views here.
# def register(request):
# 	if request.method == 'POST':
# 		form = UserRegisterForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, f'account created for {username}! Start requesting your timeoff')
# 			return redirect('login')



# 	else:
# 		form = UserRegisterForm()

# 	return render(request, 'users/register.html', {'form': form})
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })

@login_required
def profile(request):

	test = LeaveApplication.objects.filter(user=request.user)
	if request.user.is_nonteacher:
		userid = NonTeachingStaffDetail.objects.get(user = request.user)
	elif request.user.is_supervisor:
		userid = SupervisorDetail.objects.get(user = request.user)
	elif request.user.is_viceprincipal:
		userid = VicePrincipalDetail.objects.get(user = request.user)
	else:
		userid = TeachingStaffDetail.objects.get(user = request.user)
	
	if request.user.is_nonteacher:
		myFilter = nonteacherLeaveApplicationFilter(request.GET, queryset=test)
		applicant = myFilter.qs
	else:
		myFilter = teacherLeaveApplicationFilter(request.GET, queryset=test)
		applicant = myFilter.qs
	
	context = {
		'applicant':applicant,
		'userid':userid,
		'myFilter' : myFilter
	}
	return render(request, 'users/profile.html', context)


def profiledetail(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)

	if request.method == 'POST':
		u_form = UserCancelForm(request.POST, instance=obj)
		if u_form.is_valid(): 
			if obj.finalstatus == "Pending" and obj.secondstatus == "Pending" and obj.firststatus == "Pending":

				obj.firststatus = "Canceled"
				obj.secondstatus = "Canceled"
				obj.finalstatus = "Canceled"
				u_form.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('alllistview')
	
	else:
		u_form = UserCancelForm(instance=obj)
	context = {
		'obj' : obj,
		'u_form' : u_form
	}
	return render(request, 'users/profiledetail.html', context)

def profileapprove(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)
	if request.method == 'POST':	
		u_form = ProfileApproveForm(request.POST,request.FILES)
								# instance=request.user)
		
		if u_form.is_valid():
			obj.firststatus = 'Pending'
			obj.secondstatus = 'Pending'
			obj.finalstatus = 'Pending'
			# u_form.save()
			obj.save()
			messages.success(request, f'Your file Has Been Updated')
			return redirect('profile')
	
	else:
		u_form = ProfileApproveForm()


		context = {
			'obj' : obj
		}
		return render(request, 'users/profileapprove.html', context)

@login_required
def login_success(request):
	"""
	Redirects users based on whether they are in the admins group
	"""
	if request.user.type == User.Types.NONTEACHINGSTAFF:
		# user is an admin
		messages.success(request, f'非教職員登入')
		return redirect("nonteacherapply")
	elif request.user.type == User.Types.SUPERVISOR:
		# user is an admin
		messages.success(request, f'主管登入')
		return redirect("supervisorapply")
	elif request.user.type == User.Types.VICEPRINCIPAL:
		# user is an admin
		messages.success(request, f'副校長登入')
		return redirect("teacherapply")
	elif request.user.type == User.Types.PRINCIPAL:
		# user is an admin
		messages.success(request, f'校長登入')
		return redirect("plistview")
	else:
		messages.success(request, f'教職員登入')
		return redirect("teacherapply")

@login_required
def nonteacherapply(request):
	userid = NonTeachingStaffDetail.objects.get(user = request.user)
	if request.method == 'POST':
		form = NonTeacherApplyForm(request.POST, request.FILES)
		print(request.POST['startdate'])
		if form.is_valid():


			a_form = form.save(commit=False)
			user = request.user
			startdate = form.cleaned_data.get('startdate')
			enddate = form.cleaned_data.get('enddate')
			starttime = form.cleaned_data.get('starttime')
			endtime = form.cleaned_data.get('endtime')
			reason = form.cleaned_data.get('reason')
			nonteachertimeofftype = form.cleaned_data.get('nonteachertimeofftype')
			stafftype = "Nonteacher"

	
			a_form = LeaveApplication.objects.create(startdate=startdate, enddate=enddate, starttime=starttime, endtime=endtime, nonteachertimeofftype=nonteachertimeofftype, reason=reason, user=user, stafftype=stafftype)
			a_form.save()			
			form.save_m2m()
			messages.success(request, f'Non Teacher timeoff applied')
			send_mail(
				'iLeave Confirmation' ,
				'Thank you '+request.user.username+ '! You application for '+request.POST['nonteachertimeofftype']+' is under proccess!',
				'test@gmail.com',
				['request.user.email'],
				)
			return redirect('success')
	else:
		form = NonTeacherApplyForm()
		
	return render(request, "users/apply.html", {'form': form, 'userid':userid})

@login_required
def teacherapply(request):
	if request.user.is_supervisor:
		userid = SupervisorDetail.objects.get(user = request.user)
	elif request.user.is_viceprincipal:
		userid = VicePrincipalDetail.objects.get(user = request.user)
	else:
		userid = TeachingStaffDetail.objects.get(user = request.user)
	if request.method == 'POST':
		form = TeacherApplyForm(request.POST, request.FILES)
		print(request.POST['startdate'])
		if form.is_valid():

			a_form = form.save(commit=False)
			user = request.user
			startdate = form.cleaned_data.get('startdate')
			enddate = form.cleaned_data.get('enddate')
			starttime = form.cleaned_data.get('starttime')
			endtime = form.cleaned_data.get('endtime')
			reason = form.cleaned_data.get('reason')
			teachertimeofftype = form.cleaned_data.get('teachertimeofftype')
			stafftype = "Teacher"

	
			a_form = LeaveApplication.objects.create(startdate=startdate, enddate=enddate, starttime=starttime, endtime=endtime, teachertimeofftype=teachertimeofftype, reason=reason, user=user, stafftype=stafftype)
			a_form.save()	

			messages.success(request, f'Teacher timeoff applied')

			send_mail(
				'iLeave Confirmation' ,
				'Thank you '+request.user.username+ '! You application for '+request.POST['teachertimeofftype']+' is under proccess!',
				'test@gmail.com',
				['request.user.email'],
				)

			return redirect('success')
			

		else:
			messages.warning(request, f'Start date/time must be less than or equal to End date/time!!!')
	else:
		form = TeacherApplyForm()
		
	return render(request, "users/apply.html", {'form': form, 'userid':userid})

@login_required
def supervisorapply(request, *args, **kwargs):
	if request.user.is_supervisor:
		userid = SupervisorDetail.objects.get(user = request.user)
	elif request.user.is_viceprincipal:
		userid = VicePrincipalDetail.objects.get(user = request.user)
	if request.method == 'POST':
		pickform = PickerForm(request.POST)
		form = GroupApplyForm(request.POST)
		userid = request.POST['pickuser']
		user = User.objects.filter(id=userid)
		# userid = list(User.objects.filter(username=request.POST['pickuser']).values('pickuser'))
		if form.is_valid() and pickform.is_valid():		
			f = form.save(commit=False)
			p = pickform.save(commit=False)
			startdate = form.cleaned_data.get('startdate')
			enddate = form.cleaned_data.get('enddate')
			starttime = form.cleaned_data.get('starttime')
			endtime = form.cleaned_data.get('endtime')
			reason = form.cleaned_data.get('reason')
			teachertimeofftype = 'Official Leave'
			nonteachertimeofftype = 'Official Leave'
			alluser = pickform.cleaned_data.get('pickuser')

			print(alluser)
			for stuff in alluser:
				if stuff.is_nonteacher:
					f = LeaveApplication.objects.create(startdate=startdate, enddate=enddate, starttime=starttime, endtime=endtime, teachertimeofftype=teachertimeofftype, reason=reason, user=stuff)
					f.save()			
					messages.success(request, f'Timeoff applied')
				elif stuff.is_viceprincipal or stuff.is_teacher or stuff.is_principal or stuff.is_supervisor:	
					f = LeaveApplication.objects.create(startdate=startdate, enddate=enddate, starttime=starttime, endtime=endtime, nonteachertimeofftype=nonteachertimeofftype, reason=reason, user=stuff)
					f.save()			
					messages.success(request, f'Timeoff applied')

				send_mail(
				'iLeave Confirmation' ,
				'Hello '+stuff.username+ '! ' + request.user.username + ' has submitted a group application for Official leave on your behalf and is now under proccess!' ,
				'test@gmail.com',
				[stuff.email],
				)
				send_mail(
					'iLeave Confirmation' ,
					'Thank you '+request.user.username+ '! You application for group application for Official leave is under proccess!',
					'test@gmail.com',
					[stuff.email],
					)
			return redirect('success')
	else:
		form = TeacherApplyForm()
		pickform = PickerForm()

	return render(request, "users/supervisorapply.html", {'form':form, 'pickform':pickform, 'userid':userid})

@login_required
def applyforapply(request, *args, **kwargs):
	if request.user.is_supervisor:
		userid = SupervisorDetail.objects.get(user = request.user)
	elif request.user.is_viceprincipal:
		userid = VicePrincipalDetail.objects.get(user = request.user)
	elif request.user.is_secretary:
		userid = NonTeachingStaffDetail.objects.get(user = request.user)
	if request.method == 'POST':
		pickform = PickerForm(request.POST)
		form = ApplyForForm(request.POST)
		userid = request.POST['pickuser']
		user = User.objects.filter(id=userid)
		# userid = list(User.objects.filter(username=request.POST['pickuser']).values('pickuser'))
		if form.is_valid() and pickform.is_valid():		
			f = form.save(commit=False)
			p = pickform.save(commit=False)
			startdate = form.cleaned_data.get('startdate')
			enddate = form.cleaned_data.get('enddate')
			starttime = form.cleaned_data.get('starttime')
			endtime = form.cleaned_data.get('endtime')
			reason = form.cleaned_data.get('reason')
			firststatus = 'Action Required'
			secondstatus = 'Action Required'
			finalstatus = 'Action Required'
			teachertimeofftype = 'Sick Leave'
			nonteachertimeofftype = 'Sick Leave'
			alluser = pickform.cleaned_data.get('pickuser')

			print(alluser)
			for stuff in alluser:
				if stuff.is_nonteacher:
					f = LeaveApplication.objects.create(startdate=startdate, enddate=enddate, starttime=starttime, endtime=endtime, firststatus=firststatus, secondstatus=secondstatus, finalstatus=finalstatus, teachertimeofftype=teachertimeofftype, reason=reason, user=stuff)
					f.save()			
					messages.success(request, f'Timeoff applied')
				elif stuff.is_viceprincipal or stuff.is_teacher or stuff.is_principal or stuff.is_supervisor:	
					f = LeaveApplication.objects.create(startdate=startdate, enddate=enddate, starttime=starttime, endtime=endtime, firststatus=firststatus, secondstatus=secondstatus, finalstatus=finalstatus, nonteachertimeofftype=nonteachertimeofftype, reason=reason, user=stuff)
					f.save()			
					messages.success(request, f'Timeoff applied')

				send_mail(
				'iLeave Confirmation' ,
				'Hello '+stuff.username+ '! ' + request.user.username + ' has submitted an application for Sick leave on your behalf!' ,
				'test@gmail.com',
				[stuff.email],
				)
				send_mail(
					'iLeave Confirmation' ,
					'Thank you '+request.user.username+ '! You application for group application for Sick leave on your behalf!',
					'test@gmail.com',
					[stuff.email],
					)
			return redirect('success')
	else:
		form = ApplyForForm()
		pickform = PickerForm()

	return render(request, "users/applyforapply.html", {'form':form, 'pickform':pickform, 'userid':userid})

@login_required
def incrementallview(request, *args, **kwargs):
	
	if request.method == 'POST':

		form = IncrementAllForm(request.POST)
		userall = User.objects.exclude(is_principal = True)
		# userid = list(User.objects.filter(username=request.POST['pickuser']).values('pickuser'))
		if form.is_valid():		
			f = form.save(commit=False)
						
			for stuff in userall:
				if stuff.is_supervisor and stuff.is_teacher:
					supervisordetail = SupervisorDetail.objects.get(user=stuff)

					num = supervisordetail.sickleave + supervisordetail.increment
					if (num > supervisordetail.maxsickleave):
						supervisordetail.sickleave = supervisordetail.maxsickleave
					else:
						supervisordetail.sickleave = num

					created_at = form.cleaned_data.get('created_at')

					f = IncrementAll.objects.create(created_at=created_at, added = supervisordetail.increment, user = stuff)
					supervisordetail.save()
					f.save()			
				elif stuff.is_viceprincipal and stuff.is_teacher:
					viceprincipaldetail = VicePrincipalDetail.objects.get(user=stuff)

					num = viceprincipaldetail.sickleave + viceprincipaldetail.increment
					if (num > viceprincipaldetail.maxsickleave):
						viceprincipaldetail.sickleave = viceprincipaldetail.maxsickleave
					else:
						viceprincipaldetail.sickleave = num

					created_at = form.cleaned_data.get('created_at')
					f = IncrementAll.objects.create(created_at=created_at, added = viceprincipaldetail.increment, user = stuff)
					viceprincipaldetail.save()
					f.save()			
					messages.success(request, f'Timeoff added for all users')
				elif stuff.is_nonteacher:
					nonteacherdetail = NonTeachingStaffDetail.objects.get(user=stuff)
					num = nonteacherdetail.sickleave + nonteacherdetail.increment
					if (num > nonteacherdetail.maxsickleave):
						nonteacherdetail.sickleave = nonteacherdetail.maxsickleave
					else:
						nonteacherdetail.sickleave = num

					created_at = form.cleaned_data.get('created_at')
					f = IncrementAll.objects.create(created_at=created_at, added = nonteacherdetail.increment, user = stuff)
					nonteacherdetail.save()
					f.save()			
					messages.success(request, f'Timeoff added for all users')
				elif stuff.is_teacher:
					teacherdetail = get_object_or_404(TeachingStaffDetail, user = stuff)

					num = teacherdetail.sickleave + teacherdetail.increment
					if (num > teacherdetail.maxsickleave):
						teacherdetail.sickleave = teacherdetail.maxsickleave
					else:
						teacherdetail.sickleave = num

					created_at = form.cleaned_data.get('created_at')
					f = IncrementAll.objects.create(created_at=created_at, added = teacherdetail.increment, user = stuff)
					teacherdetail.save()
					f.save()			
					messages.success(request, f'Timeoff added for all users')	

			return redirect('incrementallview')
	else:
		form = IncrementAllForm(request.POST)
		

	return render(request, "users/incrementall.html", {'form':form})

@login_required
def incrementlistview(req):

	queryset = IncrementAll.objects.all() # list of objects
	context = {
		"objec_list" : queryset
	}
	return render(req, "users/incrementlistview.html", context)


def success(req):
	obj = LeaveApplication.objects.all()
	context = {"object" : obj
	}
	return render(req,"users/success.html",context)

@login_required
def managerlistview(req):
	user_manager = req.user
	userid =  req.user.SupervisorDetail.overseeing.all()
	queryset = LeaveApplication.objects.filter(Q(user__id__in=userid.all()) | Q(pickmanager__id=user_manager.id))
	managerpicked = LeaveApplication.objects.filter(pickmanager__id=user_manager.id) # list of objects
	
	context = {
		"objec_list" : queryset,
		'user_manager' : user_manager,
		'managerpicked': managerpicked
	}
	return render(req, "users/managerlistview.html", context)

@login_required
def managerapprove(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)
	if request.method == 'POST':	
		u_form = FirstValidate(request.POST, instance=obj)
		if u_form.is_valid():
			u_form.save()
			messages.success(request, f'DONE')
			return redirect('success')
	else:
		u_form = FirstValidate(instance=obj)


		context = {
			'u_form':u_form,
			'obj' : obj
		}
	# context = {
	# 	"objec" : obj
	# }
	return render(request, "users/approve.html", context)

@login_required
def vplistview(req):
	user = VicePrincipalDetail.objects.get(user = req.user)
	userid =  req.user.VicePrincipalDetail.allvp.all()
	queryset = LeaveApplication.objects.exclude(user__id__in=userid.all()) # list of objects
	context = {
		"objec_list" : queryset,
		"user" : user
	}
	return render(req, "users/vplistview.html", context)

@login_required
def vpapprove(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)
	if request.method == 'POST':	
		u_form = SecondValidate(request.POST, instance=obj)
		if u_form.is_valid():
			u_form.save()
			messages.success(request, f'Saved')
			return redirect('vplistview')
	else:
		u_form = SecondValidate(instance=obj)


		context = {
			'u_form':u_form,
			'obj' : obj
		}
	return render(request, "users/vpapprove.html", context)

@login_required
def secretarylistview(req):
	queryset = LeaveApplication.objects.all() # list of objects
	context = {
		"objec_list" : queryset,
	}
	return render(req, "users/secretarylistview.html", context)

@login_required
def secretaryapprove(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)
	userid = obj.user
	if obj.user.is_nonteacher:
		applicant = NonTeachingStaffDetail.objects.get(user = userid)
	elif obj.user.is_supervisor:
		applicant = SupervisorDetail.objects.get(user = userid)
	elif obj.user.is_viceprincipal:
		applicant = VicePrincipalDetail.objects.get(user = userid)
	else:
		applicant = TeachingStaffDetail.objects.get(user = userid)
	if request.method == 'POST':	
		u_form = SecretaryValidate(request.POST, instance=obj)
		if u_form.is_valid():
			if obj.finalduration is None:
				modify = obj.duration
				u_form.save()
				obj.finalduration = modify
				obj.save()
				messages.success(request, f'non teacher DONE')

				send_mail(
				'iLeave Confirmation' ,
				'Hello '+obj.user.username+ 'your leave application status has been updated! Please sign in to review.',
				'test@gmail.com',
				[obj.user.email],
				)

				return redirect('secretarylistview')
			else:
				modify = obj.finalduration
				u_form.save()
				obj.finalduration = modify
				obj.save()
				messages.success(request, f'non teacher DONE')

				send_mail(
				'iLeave Confirmation' ,
				'Hello '+obj.user.username+ 'your leave application status has been updated! Please sign in to review.',
				'test@gmail.com',
				[obj.user.email],
				)

				return redirect('secretarylistview')
			
	else:
		u_form = SecretaryValidate(instance=obj)


		context = {
			'u_form':u_form,
			'obj' : obj,
			'applicant' : applicant
		}
	return render(request, "users/secretaryapprove.html", {
			'u_form':u_form,
			'obj' : obj,
			'applicant' : applicant
		})

@login_required
def plistview(req):
	queryset = LeaveApplication.objects.all() # list of objects
	context = {
		"objec_list" : queryset
	}
	return render(req, "users/plistview.html", context)

@login_required
def papprove(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)
	userid = obj.user
	if obj.user.is_nonteacher:
		applicant = NonTeachingStaffDetail.objects.get(user = userid)
	elif obj.user.is_supervisor:
		applicant = SupervisorDetail.objects.get(user = userid)
	elif obj.user.is_viceprincipal:
		applicant = VicePrincipalDetail.objects.get(user = userid)
	else:
		applicant = TeachingStaffDetail.objects.get(user = userid)

	if request.method == 'POST' :
		u_form = FinalValidate(request.POST, instance=obj)
		duration = u_form.data['finalduration']
		if u_form.is_valid() and obj.finalstatus == 'Approved':
						
			if u_form.is_valid() and obj.user.is_nonteacher:
				if obj.nonteacherchangetimeofftype is None:
					if obj.nonteachertimeofftype == 'Annual Leave':
						if obj.finalduration is None:
							modify = obj.duration
							applicant.annualleave = applicant.annualleave - abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')

							send_mail(
							'iLeave Confirmation' ,
							'Hello '+obj.user.username+ 'your leave application status has been updated! Please sign in to review.',
							'test@gmail.com',
							[obj.user.email],
							)

							return redirect('plistview')
						else:
							modify = obj.finalduration
							applicant.annualleave = applicant.annualleave - abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')

							send_mail(
							'iLeave Confirmation' ,
							'Hello '+obj.user.username+ 'your leave application status has been updated! Please sign in to review.',
							'test@gmail.com',
							[obj.user.email],
							)

							return redirect('plistview')

					elif obj.nonteachertimeofftype == 'Sick Leave':
						if obj.finalduration is None:
							modify = obj.duration
							applicant.sickleave = applicant.sickleave - abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')
						else:
							modify = obj.finalduration
							applicant.sickleave = applicant.sickleave - abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')
					elif obj.nonteachertimeofftype == 'Over Time':
						if obj.finalduration is None:
							modify = obj.duration
							applicant.compensatedleave = applicant.compensatedleave + abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')
						else:
							modify = obj.finalduration
							applicant.compensatedleave = applicant.compensatedleave + abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')
					else:
						u_form.save()
						messages.success(request, f'non teacher DONE')
						return redirect('plistview')
				elif obj.nonteacherchangetimeofftype == 'Annual Leave':  #change leave type for non teacher

					if obj.finalduration is None:
							modify = obj.duration
							applicant.annualleave = applicant.annualleave - abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')
					else:
						modify = obj.finalduration
						applicant.annualleave = applicant.annualleave - abs(modify)
						u_form.save()
						applicant.save()
						obj.finalduration = modify
						obj.save()
						messages.success(request, f'non teacher DONE')
						return redirect('plistview')
				elif obj.nonteacherchangetimeofftype == 'Over Time':  #change leave type for non teacher
				
					if obj.finalduration is None:
							modify = obj.duration
							applicant.compensatedleave = applicant.compensatedleave - abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')
					else:
						modify = obj.finalduration
						applicant.compensatedleave = applicant.compensatedleave - abs(modify)
						u_form.save()
						applicant.save()
						obj.finalduration = modify
						obj.save()
						messages.success(request, f'non teacher DONE')
						return redirect('plistview')
				elif obj.nonteacherchangetimeofftype == 'No Pay Leave':  #change leave type for non teacher
				
					if obj.finalduration is None:
							modify = obj.duration
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')
					else:
						modify = obj.finalduration
						u_form.save()
						applicant.save()
						obj.finalduration = modify
						obj.save()
						messages.success(request, f'non teacher DONE')
						return redirect('plistview')
			elif u_form.is_valid() and obj.user.is_teacher:
				if obj.teacherchangetimeofftype is None:	
					if obj.teachertimeofftype == 'Casual Leave':
						if obj.finalduration is None:
							modify = obj.duration
							applicant.casualleave = applicant.casualleave - abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')
						else:
							modify = obj.finalduration
							applicant.casualleave = applicant.casualleave - abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')

					elif obj.teachertimeofftype == 'Sick Leave':
						if obj.finalduration is None:
							modify = obj.duration
							applicant.sickleave = applicant.sickleave - abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')
						else:
							modify = obj.finalduration
							applicant.sickleave = applicant.sickleave - abs(modify)
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'non teacher DONE')
							return redirect('plistview')
					else:
						u_form.save()
						messages.success(request, f'teacher DONE')
						return redirect('plistview')
				elif obj.teacherchangetimeofftype == 'No Pay Leave':  #change leave type for non teacher
					if obj.finalduration is None:
							modify = obj.duration
							u_form.save()
							applicant.save()
							obj.finalduration = modify
							obj.save()
							messages.success(request, f'teacher DONE')
							return redirect('plistview')
					else:
						modify = obj.finalduration
						u_form.save()
						applicant.save()
						obj.finalduration = modify
						obj.save()
						messages.success(request, f'teacher DONE')
						return redirect('plistview')
		elif u_form.is_valid() and obj.finalstatus == 'Denied':	
			if u_form.is_valid():
				u_form.save()
				messages.success(request, f'LeaveApplication Denied')
				return redirect('plistview')
		elif u_form.is_valid() and obj.finalstatus == 'Pending':	
			if u_form.is_valid():
				u_form.save()
				messages.warning(request, f'Please select a Decision')
				return redirect(request.get_full_path())
		
	else:
		u_form = FinalValidate(instance=obj)


		# context = {
		# 	'u_form':u_form,
		# 	'obj' : obj, 
		# 	'applicant' : applicant
		# }
	return render(request, "users/papprove.html", {
													'u_form':u_form,
													'obj' : obj, 
													'applicant' : applicant})

@login_required
def plistviewdecided(req):
	queryset = LeaveApplication.objects.all() # list of objects
	context = {
		"objec_list" : queryset
	}
	return render(req, "users/plistviewdecided.html", context)

@login_required
def papprovedecided(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)
	userid = obj.user
	if obj.user.is_nonteacher:
		applicant = NonTeachingStaffDetail.objects.get(user = userid)
	elif obj.user.is_supervisor:
		applicant = SupervisorDetail.objects.get(user = userid)
	elif obj.user.is_viceprincipal:
		applicant = VicePrincipalDetail.objects.get(user = userid)
	else:
		applicant = TeachingStaffDetail.objects.get(user = userid)
	if request.method == 'POST' :
		u_form = CancelForm(request.POST, instance=obj)
		if u_form.is_valid() and obj.user.is_nonteacher:
			if obj.nonteachertimeofftype == 'Annual Leave':
				applicant.annualleave = applicant.annualleave + abs(obj.finalduration)
				obj.finalstatus = "Canceled"
				u_form.save()
				applicant.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('plistviewdecided')

			elif obj.nonteachertimeofftype == 'Sick Leave':
				applicant.sickleave = applicant.sickleave + abs(obj.finalduration)
				obj.finalstatus = "Canceled"
				u_form.save()
				applicant.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('plistviewdecided')
			elif obj.nonteachertimeofftype == 'Over Time':
				applicant.compensatedleave = applicant.compensatedleave - abs(obj.finalduration)
				obj.finalstatus = "Canceled"
				u_form.save()
				applicant.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('plistviewdecided')
			else:
				u_form.save()
				messages.success(request, f'non teacher DONE')
				return redirect('plistviewdecided')
		elif u_form.is_valid() and obj.user.is_supervisor:
			if obj.teachertimeofftype == 'Casual Leave':
				applicant.casualleave = applicant.casualleave + abs(obj.finalduration)
				obj.finalstatus = "Canceled"
				u_form.save()
				applicant.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('plistview')
			elif obj.teachertimeofftype == 'Sick Leave':
				applicant.sickleave = applicant.sickleave + abs(obj.finalduration)
				obj.finalstatus = "Canceled"
				u_form.save()
				applicant.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('plistview')
			else:
				u_form.save()
				messages.success(request, f'supervisor DONE')
				return redirect('plistview')	

		elif u_form.is_valid() and obj.user.is_viceprincipal:
			if obj.teachertimeofftype == 'Casual Leave':
				applicant.casualleave = applicant.casualleave + abs(obj.finalduration)
				obj.finalstatus = "Canceled"
				u_form.save()
				applicant.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('plistview')
			elif obj.teachertimeofftype == 'Sick Leave':
				applicant.sickleave = applicant.sickleave + abs(obj.finalduration)
				obj.finalstatus = "Canceled"
				u_form.save()
				applicant.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('plistview')
			else:
				u_form.save()
				messages.success(request, f'supervisor DONE')
				return redirect('plistview')		

		elif u_form.is_valid() and obj.user.is_teacher:
			if obj.teachertimeofftype == 'Casual Leave':
				applicant.casualleave = applicant.casualleave + abs(obj.finalduration)
				obj.finalstatus = "Canceled"
				u_form.save()
				applicant.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('plistview')
			elif obj.teachertimeofftype == 'Sick Leave':
				applicant.sickleave = applicant.sickleave + abs(obj.finalduration)
				obj.finalstatus = "Canceled"
				u_form.save()
				applicant.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('plistview')
			else:
				u_form.save()
				messages.success(request, f'supervisor DONE')
				return redirect('plistview')	
	else:
		u_form = CancelForm(instance=obj)
	return render(request, "users/papprovedecided.html", {
			'obj' : obj, 
			'applicant' : applicant,
			'u_form' : u_form
			})

@login_required
def userlistview(req):
	queryset = User.objects.exclude(is_principal = True) # list of objects
	
	# myFilter = teacherLeaveApplicationFilter(request.GET, queryset=queryset)
	# queryset = myFilter.qs

	context = {
		"objec_list" : queryset
	}
	return render(req, "users/userlistview.html", context)

@login_required
def userdetailview(request, myid):
	obj = get_object_or_404(User, id =myid)
	obj = User.objects.get(id=myid)

	if obj.is_nonteacher:
		applicant = LeaveApplication.objects.filter(user = obj)
	elif obj.is_supervisor:
		applicant = LeaveApplication.objects.filter(user = obj)
	elif obj.is_viceprincipal:
		applicant = LeaveApplication.objects.filter(user = obj)
	else:
		applicant = LeaveApplication.objects.filter(user = obj)

	return render(request, "users/userdetailview.html", {
			'obj' : obj, 
			'applicant' : applicant
			})
@login_required
def alllistview(req):
	# allteacher = User.objects.filter(is_teacher = True)
	# allnonteacher = User.objects.filter(is_nonteacher = True)

	# teacherqueryset = LeaveApplication.objects.filter(user = allteacher) # list of objects
	# nonteacherqueryset = LeaveApplication.objects.filter(user = allnonteacher)

	queryset = LeaveApplication.objects.all()
	myFilter = LeaveApplicationFilter(req.GET, queryset=queryset)

	queryset = myFilter.qs

	if req.method == 'POST':
		response = HttpResponse(content_type='text/csv') 
		response['Content-Disposition'] = 'attachment; filename="LeaveExport.csv"' 
		writer = csv.writer(response) 
		writer.writerow(['Apply Date/Time', 'Name', 'Leave Type', 'From Date', 'From Time', 'To Date', 'To Time', 'Supervisor Decision', 'Vice Principal Decision', 'Principal Decision', 'Remark']) 
		instance = queryset 
		for row in instance:
			if row.user.is_nonteacher:
				writer.writerow([row.created_at, row.user.username, row.nonteachertimeofftype, row.startdate, row.starttime, row.enddate, row.endtime, row.firststatus, row.secondstatus, row.finalstatus, row.finalcomment]) 
			else:
				writer.writerow([row.created_at, row.user.username, row.teachertimeofftype, row.startdate, row.starttime, row.enddate, row.endtime, row.firststatus, row.secondstatus, row.finalstatus, row.finalcomment]) 
		return response 
	context = {
		"myFilter" : myFilter,
		"objec_list" : queryset,
	}
	return render(req, "users/alllistview.html", context)


@login_required
def alldetailview(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)

	if request.method == 'POST':
		u_form = UserCancelForm(request.POST, instance=obj)
		if u_form.is_valid(): 
			if obj.finalstatus == "Pending" and obj.secondstatus == "Pending" and obj.firststatus == "Pending":

				obj.firststatus = "Canceled"
				obj.secondstatus = "Canceled"
				obj.finalstatus = "Canceled"
				u_form.save()
				obj.save()
				messages.success(request, f'non teacher DONE')
				return redirect('alllistview')
	
	else:
		u_form = UserCancelForm(instance=obj)
	context = {
		'obj' : obj,
		'u_form' : u_form
	}
	return render(request, 'users/alldetailview.html', context)

@login_required
def documentlistview(req):
	# allteacher = User.objects.filter(is_teacher = True)
	# allnonteacher = User.objects.filter(is_nonteacher = True)

	# teacherqueryset = LeaveApplication.objects.filter(user = allteacher) # list of objects
	# nonteacherqueryset = LeaveApplication.objects.filter(user = allnonteacher)

	queryset = LeaveApplication.objects.filter(Q(attachmentrequired=True) & Q(attachmentreceived=False))
	# myFilter = LeaveApplicationFilter(req.GET, queryset=queryset)

	# queryset = myFilter.qs

	context = {
		# "myFilter" : myFilter,
		"objec_list" : queryset,
	}
	return render(req, "users/documentlistview.html", context)


@login_required
def documentdetailview(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)

	if request.method == 'POST':
		u_form = DocumentForm(request.POST, instance=obj)
		if u_form.is_valid(): 	
			u_form.save()
			messages.success(request, f'non teacher DONE')
			return redirect('documentlistview')
	
	else:
		u_form = DocumentForm(instance=obj)
	context = {
		'obj' : obj,
		'u_form' : u_form
	}
	return render(request, 'users/documentdetailview.html', context)

@login_required
def calendarlistview(req):
	queryset = LeaveApplication.objects.filter(calendarcheck=False)
	# myFilter = LeaveApplicationFilter(req.GET, queryset=queryset)

	# queryset = myFilter.qs

	context = {
		# "myFilter" : myFilter,
		"objec_list" : queryset,
	}
	return render(req, "users/calendarlistview.html", context)

@login_required
def calendardetailview(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)

	if request.method == 'POST':
		u_form = CalendarForm(request.POST, instance=obj)
		if u_form.is_valid(): 	
			u_form.save()
			messages.success(request, f'non teacher DONE')
			return redirect('calendarlistview')
	
	else:
		u_form = CalendarForm(instance=obj)
	context = {
		'obj' : obj,
		'u_form' : u_form
	}
	return render(request, 'users/calendardetailview.html', context)

@login_required
def prependinglistview(req):
	queryset = LeaveApplication.objects.filter(finalstatus = 'Action Required') # list of objects
	context = {
		"objec_list" : queryset
	}
	return render(req, "users/prependinglistview.html", context)

@login_required
def prependingdetailview(request, myid):
	obj = get_object_or_404(LeaveApplication, id =myid)
	obj = LeaveApplication.objects.get(id=myid)
	if request.method == 'POST':	
		u_form = ProfileApproveForm(request.POST)
								# instance=request.user)
		
		if u_form.is_valid():
			obj.firststatus = 'Pending'
			obj.secondstatus = 'Pending'
			obj.finalstatus = 'Pending'
			# u_form.save()
			obj.save()
			messages.success(request, f'Success')
			return redirect('prependinglistview')
	
	else:
		u_form = ProfileApproveForm()


		context = {
			'obj' : obj
		}
		return render(request, 'users/prependingdetailview.html', context)
