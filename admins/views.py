from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


date = datetime.now()


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop - Admin', 'date': date}
    return render(request, 'admins/admin.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    users = User.objects.all()
    context = {'title': 'GeekShop - Admin', 'users': users, 'date': date}
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь создан!')
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'GeekShop - Admin', 'form': form, 'date': date}
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, pk):
    select_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=select_user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения внесены!')
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=select_user)
    context = {'title': 'GeekShop - Admin', 'form': form, 'select_user': select_user, 'date': date}
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))
