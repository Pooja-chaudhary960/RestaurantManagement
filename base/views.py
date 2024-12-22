from django.shortcuts import render
from .models import Table, Category, Menu, Order, Waiter, Reception
from rest_framework.viewsets import ModelViewSet
from .serializer import TableSerializer, CategorySerializer, MenuSerializer, OrderSerializer, WaiterSerializer,ReceptionSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class WaiterViewSet(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer


class ReceptionViewSet(ModelViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer


@api_view(['POST'])
def login(request):
   email = request.data.get('email')
   password = request.data.get('password')
   hash_password = make_password(password)
   request.data['password'] = hash_password

   user = authenticate(uername=email,password=password)

   if user == None:
       return Response('Invalid credentials!')
   
   else:
       token,_ = Token.objects.get_or_create(user=user)
       return Response(token.key)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Data created!')
    else:
        return Response(serializer.errors)