from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.models import User
from common.views import CommonContextMixin
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from products.models import Product, ProductCategory


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop - Admin', 'date': datetime.now()}
    return render(request, 'admins/admin.html', context)


class UserAdminListView(CommonContextMixin, ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'GeekShop - Админка'


class UserAdminCreateView(CommonContextMixin, CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    success_message = 'Пользователь создан!'
    title = 'GeekShop - Админка'


class UserAdminUpdateView(CommonContextMixin, UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    success_message = 'Изменения внесены!'
    title = 'GeekShop - Админка'


class UserAdminDeleteView(CommonContextMixin, DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    title = 'GeekShop - Админка'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.success_url)


class CategoryAdminListView(CommonContextMixin, ListView):
    model = ProductCategory
    template_name = 'admins/admin-category.html'
    title = 'GeekShop - Admin-Category'


class ProductAdminListView(CommonContextMixin, ListView):
    model = Product
    template_name = 'admins/admin-products.html'
    title = 'GeekShop - Admin-Product'


@user_passes_test(lambda u: u.is_staff)
def admin_product_card(request, pk):
    product = Product.objects.get(id=pk)
    context = {'title': 'GeekShop - Admin-Category', 'product': product, 'date': date}
    return render(request, 'products/includes/card.html', context)
