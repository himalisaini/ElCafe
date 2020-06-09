from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import RegisterForm , UserUpdateForm , ProfileUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Account created successfully!')
            return redirect('login')

    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request,'users/register.html',context)


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profilemodel)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Account updated successfully!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form':user_form,
        'p_form': profile_form
    }
    return render(request,'users/profile.html',context)








#testuser data15032