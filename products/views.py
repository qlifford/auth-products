from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Product

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout

class HomePage(ListView):
    model = Product

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ('name', 'desc', 'price','img')

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product

class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ('name', 'desc', 'price','img')


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('home-page')

def register(request):
    return render(request, 'registration/register.html', {'form': UserCreationForm})


def signout(request):
    logout(request)
    return render(request, 'registration/logout.html')

