from rest_framework import generics, filters
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import (
    CategorySerializer, MenuItemSerializer,
    CartSerializer, OrderSerializer,
    OrderItemSerializer
)

from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend



# Assign user to a group
@api_view(['POST', 'DELETE'])
@permission_classes([IsAdminUser])
def Assign_group(request):
    username = request.data.get('username')
    group_name = request.data.get('group')

    if not username or not group_name:
        return Response(
            {
                "Message": "Username and group are required"
            }, status=status.HTTP_400_BAD_REQUEST
        )
    
    user = User.objects.filter(username=username).first()
    group = Group.objects.filter(name=group_name).first()

    if not user or not group:
        return Response(
            {
                "Message": "Invalid user or group"
            }, status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'POST':
        group.user_set.add(user)
        return Response(
            {"Message": f"{username} added to {group_name}"}
        )
    elif request.method == 'DELETE':
        group.user_set.remove(user)
        return Response(
            {"Message": f"{username} removed from {group_name}"}
        )


""" GENERIC CLASS--BASED VIEWS """
# ----------------- Category Views -----------------
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    # Filtering, Searching and Ordering
    filter_backends = [
        DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter
    ]
    filterset_fields = ['slug', 'title']
    search_fields = ['slug', 'title']
    ordering_fields = ['slug', 'title']

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


# ----------------- MenuItem Views -----------------
class MenuListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]
    
    # Filtering, Searching and Ordering
    filter_backends = [
        DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter
    ]
    filterset_fields = [
        'category__id', 'featured', 'price'
    ]
    search_fields = ['title']
    ordering_fields = ['price', 'title']
    ordering = ['id']

class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]


# ----------------- Cart Views -----------------
class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# ----------------- Order Views -----------------
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    # Filtering & ordering
    filter_backends = [
        DjangoFilterBackend, filters.OrderingFilter
    ]
    filterset_fields = ['status', 'delivery_crew', 'user']
    ordering_fields = ['date', 'total', 'status']


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# ----------------- OrderItem Views -----------------
class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    # Filtering & ordering
    filter_backends = [
        DjangoFilterBackend, filters.OrderingFilter
    ]
    filterset_fields = ['menuitem', 'order']
    ordering_fields = ['price', 'quantity', 'unit_price']


class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



""" FUNCTION BASED--VIEWS """
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer, OrderSerializer, OrderItemSerializer

# ----------------- Category Views -----------------
@api_view(['GET', 'POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------- MenuItem Views -----------------
@api_view(['GET', 'POST'])
def menuitem_list_create(request):
    if request.method == 'GET':
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def menuitem_detail(request, pk):
    try:
        item = MenuItem.objects.get(pk=pk)
    except MenuItem.DoesNotExist:
        return Response({'error': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------- Cart Views -----------------
@api_view(['GET', 'POST'])
def cart_list_create(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cart_detail(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------- Order Views -----------------
@api_view(['GET', 'POST'])
def order_list_create(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------- OrderItem Views -----------------
@api_view(['GET', 'POST'])
def orderitem_list_create(request):
    if request.method == 'GET':
        items = OrderItem.objects.all()
        serializer = OrderItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def orderitem_detail(request, pk):
    try:
        item = OrderItem.objects.get(pk=pk)
    except OrderItem.DoesNotExist:
        return Response({'error': 'Order item not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""