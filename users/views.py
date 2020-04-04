from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from users.forms import UserForm, ProfileForm
from users.models import Profile

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learming_logs_app:index'))

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу.
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learming_logs_app:index'))

    context = {'form' : form}
    return render(request, 'users/register.html', context)

@login_required
@transaction.atomic
def update_profile(request):
    # if request.method == 'POST':
    #     user_form = UserForm(request.POST, instance=request.user)
    #     profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         profile_form.save()
    #         return HttpResponseRedirect(reverse('users:update_profile'))
    # else:
    #     user_form = UserForm(instance=request.user)
    #     profile_form = ProfileForm(instance=request.user.profile)
    # return render(request, 'users/profile.html', {
    #     'user_form': user_form,
    #     'profile_form': profile_form
    # })
    profile = request.user.profile
    return render(request, 'users/profile.html', {
        'image': profile.avatar,
    })