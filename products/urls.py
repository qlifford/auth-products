from django.urls import path
from products.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name = 'register'),
    # path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', signout, name = 'logout'),


    path('', HomePage.as_view(), name='home-page'),
    path('product-create/', ProductCreate.as_view(), name='product-create'),
    path('product-detail/<str:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('product-update/<str:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('product-delete/<str:pk>/', ProductDelete.as_view(), name='product-delete'),
]
