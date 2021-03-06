from django.urls import path

from admins.views.main import IndexTemplateView
from admins.views.users import UserListView, UserCreateView, UserUpdateView, UserDeleteView
from admins.views.categories import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from admins.views.products import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from admins.views.orders import OrderListView, OrderUpdateView, OrderDeleteView, OrderCreateView

app_name = 'admins'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),

    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),

    path('categories/', CategoryListView.as_view(), name='admin_categories'),
    path('categories-create/', CategoryCreateView.as_view(), name='admin_categories_create'),
    path('categories-update/<int:pk>', CategoryUpdateView.as_view(), name='admin_categories_update'),
    path('categories-delete/<int:pk>', CategoryDeleteView.as_view(), name='admin_categories_delete'),

    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products-delete/<int:pk>', ProductDeleteView.as_view(), name='admin_products_delete'),

    path('orders/', OrderListView.as_view(), name='admin_orders'),
    path('orders-create/', OrderCreateView.as_view(), name='admin_orders_create'),
    path('orders-update/<int:pk>', OrderUpdateView.as_view(), name='admin_orders_update'),
    path('orders-delete/<int:pk>', OrderDeleteView.as_view(), name='admin_orders_delete'),
]
