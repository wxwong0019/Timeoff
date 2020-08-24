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
	) 
from customstaff.models import User, TeachingStaffDetail, NonTeachingStaffDetail, TeachingStaff, NonTeachingStaff, LeaveApplication, SupervisorDetail, VicePrincipalDetail
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
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)


		context = {
			'u_form':u_form,
			'p_form':p_form,
		}
		return render(request, 'users/profile.html', context)

@login_required
def login_success(request):
	"""
	Redirects users based on whether they are in the admins group
	"""
	if request.user.type == User.Types.NONTEACHINGSTAFF:
		# user is an admin
		messages.success(request, f'NOT a teacher')
		return redirect("nonteacherapply")
	else:
		messages.success(request, f'IS a teacher')
		return redirect("teacherapply")

@login_required
def nonteacherapply(request):
	if request.method == 'POST':
		form = NonTeacherApplyForm(request.POST)
		# start_date=request.POST['startdate']
		# end_date =request.POST['enddate']

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
		# start_date=request.POST['startdate']
		# end_date =request.POST['enddate']

		print(request.POST['startdate'])
		if form.is_valid():
			a_form = form.save(commit=False)
			a_form.user = request.user
			a_form.save()

			messages.success(request, f'Teacher timeoff applied')

			return redirect('success')
	else:
		form = TeacherApplyForm()
		
	return render(request, "users/apply.html", {'form': form})

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
	return render(request, "users/vpapprove.html", context)
