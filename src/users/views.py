from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import(
	TeachingStaffUpdateForm,
	NonTeachingStaffUpdateForm,
	# UserRegisterForm,
	UserUpdateForm, 
	ProfileUpdateForm,
	ApplyForm,
	FirstValidate
	) 
from customstaff.models import LeaveApplication
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
	if request.method == 'POST':	
		u_form = UserUpdateForm(request.POST,)
								# instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
								   request.FILES,)	
								   # instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your Account Has Been Updated')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)


		context = {
			'u_form':u_form,
			'p_form':p_form,
		}
	return render(request, 'users/profile.html', context)



def nonteachingstaff(request):
	if request.method == 'POST':
		form = NonTeachingStaffUpdateForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Teacher timeoff applied')
			return redirect('profile')
	else:
		form = NonTeachingStaffUpdateForm()
	return render(request, 'users/nonteachingstaff.html', {'form': form})

def teacherapply(request):
	if request.method == 'POST':
		form = ApplyForm(request.POST)
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
		form = ApplyForm()
		
	return render(request, "users/apply.html", {'form': form})

def success(req):
	obj = LeaveApplication.objects.get(id=1)
	context = {"object" : obj
	}
	return render(req,"users/success.html",context)

def managerlistview(req):
	queryset = LeaveApplication.objects.all() # list of objects
	context = {
		"objec_list" : queryset
	}
	return render(req, "users/managerlistview.html", context)

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

# def managerapprove(request, myid):
# 	if request.method == 'POST':	
# 		u_form = FirstValidate(request.POST,instance=request.myid)
# 		if u_form.is_valid():
# 			u_form.save()
# 			messages.success(request, f'Your Account Has Been Updated')
# 			return redirect('profile')
# 	else:
# 		u_form = FirstValidate(instance=request.user)


# 		context = {
# 			'u_form':u_form,
# 		}
# 	return render(request, 'users/approve.html', context)
