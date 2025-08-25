from django.urls import path
from . import views

urlpatterns = [
    # Group assignment
    path('assign-group/', views.Assign_group, name='assign-group'),

    # Categories
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),

    # Menu Items
    path('menuitems/', views.MenuListCreateView.as_view(), name='menuitem-list'),
    path('menuitems/<int:pk>/', views.MenuDetailView.as_view(), name='menuitem-detail'),

    # Cart
    path('cart/', views.CartListCreateView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', views.CartDetailView.as_view(), name='cart-detail'),

    # Orders
    path('orders/', views.OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),

    # Order Items
    path('order-items/', views.OrderItemListCreateView.as_view(), name='orderitem-list'),
    path('order-items/<int:pk>/', views.OrderItemDetailView.as_view(), name='orderitem-detail'),
]
