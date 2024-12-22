from django.urls import path
from .views import TableViewSet, CategoryViewSet, MenuViewSet, OrderViewSet, WaiterViewSet,ReceptionViewSet, login, register

urlpatterns = [
    path('tables/', TableViewSet.as_view({'get':'list','post':'create'})),
    path('tables/<int:pk>/',TableViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('category/', CategoryViewSet.as_view({'get':'list','post':'create'})),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('menus/', MenuViewSet.as_view({'get':'list','post':'create'})),
    path('menus/<int:pk>/', MenuViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('orders/', OrderViewSet.as_view({'get':'list','post':'create'})),
    path('orders/<int:pk>/',OrderViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('waiters/', WaiterViewSet.as_view({'get':'list','post':'create'})),
    path('waiters/<int:pk>/', WaiterViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('reception/', ReceptionViewSet.as_view({'get':'list','post':'create'})),
    path('reception/<int:pk>/', ReceptionViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('login/',login),
    path('register/',register, name='register')
]