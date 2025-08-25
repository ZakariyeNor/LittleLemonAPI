from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, MenuItem, Cart, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']
    
    def validate_title(self, value):
        if Category.objects.filter(title__iexact=value).exists():
            raise serializers.ValidationError("This category already exists.")
        return value


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)       # Nested (read-only)
    category_id = serializers.IntegerField(write_only=True)  # Accepts ID on create/update

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']


class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)   # set from request.user
    menuitem = MenuItemSerializer(read_only=True)               # nested display
    menuitem_id = serializers.IntegerField(write_only=True)     # accept ID on POST

    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem', 'menuitem_id', 'quantity', 'unit_price', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menuitem', 'menuitem_id', 'quantity', 'unit_price', 'price']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)   # request.user
    order_items = OrderItemSerializer(source="orderitem_set", many=True, read_only=True)  

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date', 'order_items']
