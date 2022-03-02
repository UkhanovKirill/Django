from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin.html', context)


def admin_users(request):
    users = User.objects.all()
    context = {'title': 'GeekShop - Admin', 'users': users}
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь создан!')
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'GeekShop - Admin', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


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
    context = {'title': 'GeekShop - Admin', 'form': form, 'select_user': select_user}
    return render(request, 'admins/admin-users-update-delete.html', context)
