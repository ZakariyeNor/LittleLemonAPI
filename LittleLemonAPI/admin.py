from django.contrib import admin
from .models import Category, MenuItem, Cart, Order, OrderItem

# Register models into admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_filter = ('featured', 'category')
    search_fields = ('title',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'menuitem', 'price')
    search_fields = ('user__username', 'menuitem__title')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'delivery_crew', 'status', 'date')
    list_editable = ('delivery_crew', 'status')
    list_filter = ('status', 'date')
    search_fields = ('user__username',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'menuitem', 'price')
    search_fields = ('order__user__username', 'menuitem__title')
