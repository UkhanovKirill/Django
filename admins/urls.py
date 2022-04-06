from django.urls import path
from admins.views import index, UserAdminListView, UserAdminCreateView, UserAdminUpdateView, UserAdminDeleteView, CategoryAdminListView, ProductAdminListView, admin_product_card

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserAdminListView.as_view(), name='admin_users'),
    path('users-create/', UserAdminCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserAdminUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserAdminDeleteView.as_view(), name='admin_users_delete'),
    path('users-category/', CategoryAdminListView.as_view(), name='admin_category'),
    path('users-product/', ProductAdminListView.as_view(), name='admin_product'),
    path('users-product-card/<int:pk>', admin_product_card, name='admin_product_card'),
]
