from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from datetime import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from products.models import Product, ProductCategory


date = datetime.now()


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop - Admin', 'date': date}
    return render(request, 'admins/admin.html', context)


class CommonMixin(SuccessMessageMixin):
    title = None
    date = datetime.now()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CommonMixin, self).get_context_data(object_list=None, **kwargs)
        context['title'] = self.title
        context['date'] = self.date
        return context


class UserAdminListView(CommonMixin, ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'GeekShop - Админка'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminListView, self).dispatch(request, *args, **kwargs)


class UserAdminCreateView(CommonMixin, CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    success_message = 'Пользователь создан!'
    title = 'GeekShop - Админка'


class UserAdminUpdateView(CommonMixin, UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    success_message = 'Изменения внесены!'
    title = 'GeekShop - Админка'


class UserAdminDeleteView(CommonMixin, DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    title = 'GeekShop - Админка'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.success_url)





@user_passes_test(lambda u: u.is_staff)
def admin_category(request):
    categories = ProductCategory.objects.all()
    context = {'title': 'GeekShop - Admin-Category', 'categories': categories, 'date': date}
    return render(request, 'admins/admin-category.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product(request):
    products = Product.objects.all()
    context = {'title': 'GeekShop - Admin-Category', 'products': products, 'date': date}
    return render(request, 'admins/admin-products.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_card(request, pk):
    product = Product.objects.get(id=pk)
    context = {'title': 'GeekShop - Admin-Category', 'product': product, 'date': date}
    return render(request, 'products/includes/card.html', context)
