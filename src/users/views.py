from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import(
	TeachingStaffUpdateForm,
	NonTeachingStaffUpdateForm,
	UserRegisterForm,
	UserUpdateForm, 
	ProfileUpdateForm,
	ApplyForm,
	) 
# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'account created for {username}! Start requesting your timeoff')
			return redirect('login')



	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':	
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
								   request.FILES,	
								   instance=request.user.profile)
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

def teachingstaff(request):
	if request.method == 'POST':
		form = TeachingStaffUpdateForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Teacher timeoff applied')
			return redirect('profile')



	else:
		form = TeachingStaffUpdateForm()

	return render(request, 'users/teachingstaff.html', {'form': form})

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

def apply(request):
	if request.method == 'POST':
		form = ApplyForm(request.POST)
		if form.is_valid():
			a_form = form.save(commit=False)
			a_form.user = request.user
			a_form.save()
			messages.success(request, f'Teacher timeoff applied')

			return redirect('apply')
	else:
		form = ApplyForm()
		
	return render(request, "users/apply.html", {'form': form})

