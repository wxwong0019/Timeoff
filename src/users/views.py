from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import(
	TeachingStaffUpdateForm,
	NonTeachingStaffUpdateForm,
	# UserRegisterForm,
	UserUpdateForm, 
	ProfileUpdateForm,
	TeacherApplyForm,
	NonTeacherApplyForm,
	SecondValidate,
	FirstValidate,
	FinalValidate,
	PickerForm,
	IncrementAllForm
	) 
from customstaff.models import (
	User, 
	TeachingStaffDetail, 
	NonTeachingStaffDetail, 
	TeachingStaff, 
	NonTeachingStaff, 
	LeaveApplication, 
	SupervisorDetail, 
	VicePrincipalDetail, 
	PrincipalDetail,
	Picker,
	IncrementAll
	)
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
def profile(request):
	# if request.method == 'POST':	
	# 	u_form = UserUpdateForm(request.POST,)
	# 							# instance=request.user)
	# 	p_form = ProfileUpdateForm(request.POST,
	# 							   request.FILES,)	
	# 							   # instance=request.user.profile)
	# 	if u_form.is_valid() and p_form.is_valid():
	# 		u_form.save()
	# 		p_form.save()
	# 		messages.success(request, f'Your Account Has Been Updated')
	# 		return redirect('profile')
	# else:
		applicant = LeaveApplication.objects.filter(user=request.user)
		if request.user.is_nonteacher:
			userid = NonTeachingStaffDetail.objects.get(user = request.user)
		elif request.user.is_supervisor:
			userid = SupervisorDetail.objects.get(user = request.user)
		elif request.user.is_viceprincipal:
			userid = VicePrincipalDetail.objects.get(user = request.user)
		else:
			userid = TeachingStaffDetail.objects.get(user = request.user)

		context = {
			'applicant':applicant,
			'userid':userid,
		}
		return render(request, 'users/profile.html', context)

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
	if request.method == 'POST':
		form = NonTeacherApplyForm(request.POST)


		print(request.POST['startdate'])
		if form.is_valid():
			a_form = form.save(commit=False)
			a_form.user = request.user
			a_form.save()

			messages.success(request, f'Non Teacher timeoff applied')

			return redirect('success')
	else:
		form = NonTeacherApplyForm()
		
	return render(request, "users/apply.html", {'form': form})

@login_required
def teacherapply(request):
	if request.method == 'POST':
		form = TeacherApplyForm(request.POST)

		print(request.POST['startdate'])
		if form.is_valid():
			a_form = form.save(commit=False)
			a_form.user = request.user
			a_form.save()

			messages.success(request, f'Teacher timeoff applied')
			return redirect('success')
		else:
			messages.warning(request, f'Start date/time must be less than or equal to End date/time!!!')
	else:
		form = TeacherApplyForm()
		
	return render(request, "users/apply.html", {'form': form})

@login_required
def supervisorapply(request, *args, **kwargs):
	# userid = get_object_or_404(User, user__id__inbn = request.POST.get('user'))
	if request.method == 'POST':
		# start_date=request.POST['startdate']
		# end_date =request.POST['enddate']
		pickform = PickerForm(request.POST)
		form = TeacherApplyForm(request.POST)
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
			teachertimeofftype = form.cleaned_data.get('teachertimeofftype')
			alluser = pickform.cleaned_data.get('pickuser')
			print(alluser)
			for stuff in alluser:
				f = LeaveApplication.objects.create(startdate=startdate, enddate=enddate, starttime=starttime, endtime=endtime, teachertimeofftype=teachertimeofftype, reason=reason, user=stuff)
				f.save()			
				messages.success(request, f'supervisor timeoff applied')				
			return redirect('success')
	else:
		form = TeacherApplyForm()
		pickform = PickerForm()

	return render(request, "users/apply.html", {'form':form, 'pickform':pickform})


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
					supervisordetail.sickleave = supervisordetail.sickleave + supervisordetail.increment
					created_at = form.cleaned_data.get('created_at')

					f = IncrementAll.objects.create(created_at=created_at, added = supervisordetail.increment, user = stuff)
					supervisordetail.save()
					f.save()			
				elif stuff.is_viceprincipal and stuff.is_teacher:
					viceprincipaldetail = VicePrincipalDetail.objects.get(user=stuff)
					viceprincipaldetail.sickleave = viceprincipaldetail.sickleave + viceprincipaldetail.increment
					created_at = form.cleaned_data.get('created_at')
					f = IncrementAll.objects.create(created_at=created_at, added = viceprincipaldetail.increment, user = stuff)
					viceprincipaldetail.save()
					f.save()			
					messages.success(request, f'Timeoff added for all users')
				elif stuff.is_nonteacher:
					nonteacherdetail = NonTeachingStaffDetail.objects.get(user=stuff)
					nonteacherdetail.sickleave = nonteacherdetail.sickleave + nonteacherdetail.increment
					created_at = form.cleaned_data.get('created_at')
					f = IncrementAll.objects.create(created_at=created_at, added = nonteacherdetail.increment, user = stuff)
					nonteacherdetail.save()
					f.save()			
					messages.success(request, f'Timeoff added for all users')
				elif stuff.is_teacher:
					teacherdetail = get_object_or_404(TeachingStaffDetail, user = stuff)
					teacherdetail.sickleave = teacherdetail.sickleave + teacherdetail.increment
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

	userid =  req.user.SupervisorDetail.overseeing.all()
	queryset = LeaveApplication.objects.filter(user__id__in=userid.all()) # list of objects
	context = {
		"objec_list" : queryset
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
	userid =  req.user.VicePrincipalDetail.allvp.all()
	queryset = LeaveApplication.objects.exclude(user__id__in=userid.all()) # list of objects
	context = {
		"objec_list" : queryset
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
			messages.success(request, f'DONE')
			return redirect('success')
	else:
		u_form = SecondValidate(instance=obj)


		context = {
			'u_form':u_form,
			'obj' : obj
		}
	return render(request, "users/vpapprove.html", context)

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
	# supervisor = SupervisorDetail.objects.get(user = userid)
	# viceprincipal = VicePrincipalDetail.objects.get(user = userid)
	# teacher = TeachingStaffDetail.objects.get(user = userid)

	if request.method == 'POST' :
		u_form = FinalValidate(request.POST, instance=obj)
		duration = u_form.data['finalduration']
		if u_form.is_valid() and obj.finalstatus == 'Approved':
						
						if u_form.is_valid() and obj.user.is_nonteacher:
								if obj.nonteachertimeofftype == 'Annual Leave':
									if obj.finalduration is None:
										modify = obj.duration
										applicant.annualleave = applicant.annualleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
									else:
										modify = obj.finalduration
										applicant.annualleave = applicant.annualleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')

								elif obj.nonteachertimeofftype == 'Sick Leave':
									if obj.finalduration is None:
										modify = obj.duration
										applicant.sickleave = applicant.sickleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
									else:
										modify = obj.finalduration
										applicant.sickleave = applicant.sickleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
								elif obj.nonteachertimeofftype == 'Over Time':
									if obj.finalduration is None:
										modify = obj.duration
										applicant.compensatedleave = applicant.compensatedleave + abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
									else:
										modify = obj.finalduration
										applicant.compensatedleave = applicant.compensatedleave + abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
								else:
									u_form.save()
									messages.success(request, f'non teacher DONE')
									return redirect('plistview')

						elif u_form.is_valid() and obj.user.is_supervisor:
								if obj.teachertimeofftype == 'Casual Leave':
									if obj.finalduration is None:
										modify = obj.duration
										applicant.casualleave = applicant.casualleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
									else:
										modify = obj.finalduration
										applicant.casualleave = applicant.casualleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
								elif obj.teachertimeofftype == 'Sick Leave':
									if obj.finalduration is None:
										modify = obj.duration
										applicant.sickleave = applicant.sickleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
									else:
										modify = obj.finalduration
										applicant.sickleave = applicant.sickleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
								else:
									u_form.save()
									messages.success(request, f'supervisor DONE')
									return redirect('plistview')	

						elif u_form.is_valid() and obj.user.is_viceprincipal:
								if obj.teachertimeofftype == 'Casual Leave':
									if obj.finalduration is None:
										modify = obj.duration
										applicant.casualleave = applicant.casualleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
									else:
										modify = obj.finalduration
										applicant.casualleave = applicant.casualleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
								elif obj.teachertimeofftype == 'Sick Leave':
									if obj.finalduration is None:
										modify = obj.duration
										applicant.sickleave = applicant.sickleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
									else:
										modify = obj.finalduration
										applicant.sickleave = applicant.sickleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')	
								else:
									u_form.save()
									messages.success(request, f'viceprincipal DONE')
									return redirect('plistview')		

						elif u_form.is_valid() and obj.user.is_teacher:
								if obj.teachertimeofftype == 'Casual Leave':
									if obj.finalduration is None:
										modify = obj.duration
										applicant.casualleave = applicant.casualleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
									else:
										modify = obj.finalduration
										applicant.casualleave = applicant.casualleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')

								elif obj.teachertimeofftype == 'Sick Leave':
									if obj.finalduration is None:
										modify = obj.duration
										applicant.sickleave = applicant.sickleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
									else:
										modify = obj.finalduration
										applicant.sickleave = applicant.sickleave - abs(modify)
										u_form.save()
										applicant.save()
										messages.success(request, f'non teacher DONE')
										return redirect('plistview')
								else:
									u_form.save()
									messages.success(request, f'teacher DONE')
									return redirect('plistview')
		elif u_form.is_valid() and obj.finalstatus == 'Denied':	
			if u_form.is_valid():
				u_form.save()
				messages.success(request, f'LeaveApplication Denied')
				return redirect('plistview')
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

	return render(request, "users/papprovedecided.html", {
			'obj' : obj, 
			'applicant' : applicant
			})

@login_required
def userlistview(req):
	queryset = User.objects.exclude(is_principal = True) # list of objects
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
