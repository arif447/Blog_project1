from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Login_app.forms import Signup_form, Change_form, profile_pic_Form

# Create your views here.
def Sign_up(request):
    form = Signup_form()
    if request.method == 'POST':
        form = Signup_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('Login_app:Login'))
    diction = {'form': form, }
    return render(request, 'Login_app/sign_up.html', context=diction)


def Login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    diction = {'form': form}
    return render(request, 'Login_app/log_in.html', context=diction)


@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_app:Sign_up'))


@login_required
def Profile_page(request):

    return render(request, 'Login_app/profile.html', context={})

@login_required
def change_user(request):
    current_user = request.user
    form = Change_form(instance=current_user)
    if request.method == 'POST':
        form = Change_form(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = Change_form(instance=current_user)
            return HttpResponseRedirect(reverse('Login_app:Profile_page'))
    diction = {'form': form}
    return render(request, 'Login_app/change_user.html', context=diction)
@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'Login_app/pass_change.html', context={'form': form, 'changed': changed})


@login_required
def add_profile_pic(request):
    form = profile_pic_Form()
    if request.method == 'POST':
        form = profile_pic_Form(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('Login_app:Profile_page'))
    diction = {'form': form}
    return render(request, 'Login_app/pictureForm.html', context=diction)


@login_required
def change_pro_pi(request):
    form = profile_pic_Form(instance=request.user.user_profile)
    if request.method == 'POST':
        form = profile_pic_Form(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Login_app:Profile_page'))
    return render(request, 'Login_app/pictureForm.html', context={'form': form})

