from django.shortcuts import render, redirect
from .models import food, order
from core.forms import listform
from django.contrib import messages


# Create your views here.


def base(request):
    Food = food.objects.all()
    return render(request, 'base.html', {'Food': Food})


def menu(request):
    Food = food.objects.all()
    return render(request, 'menu.html', {'Food': Food})


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    form = listform()
    if request.method == "POST":
        form = listform(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'contact.html', {'form': form})


def order_view(request, food_id):
    if request.POST:
        quantity = request.POST.get('quantity')
        username = request.POST.get('username')
        orderitem = order()
        Food = food.objects.get(pk=food_id)
        orderitem.Food = Food
        orderitem.quantity = quantity
        orderitem.name = username
        orderitem.save()
        return redirect('base')
    return render(request, 'detail.html')
