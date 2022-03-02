from django.urls import path
from admins.views import index, admin_users, admin_users_create, admin_users_update, admin_users_delete, admin_category, admin_product, admin_product_card

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:pk>', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:pk>', admin_users_delete, name='admin_users_delete'),
    path('users-category/', admin_category, name='admin_category'),
    path('users-product/', admin_product, name='admin_product'),
    path('users-product_card/<int:pk>', admin_product_card, name='admin_product_card'),
]
