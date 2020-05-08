from django.shortcuts import render, redirect, get_object_or_404

from .forms import *

from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def display_products(request):
    items= products.objects.all()
    context = {
        'items':items,
        'header':'products',
    }
    return render(request, 'index.html',context)

def display_customers(request):
    items= customers.objects.all()
    context = {
        'items':items,
        'header':'customers',
    }
    return render(request, 'index.html',context)


def display_orders(request):
    items= orders.objects.all()
    context = {
        'items':items,
        'header':'orders',
    }
    return render(request, 'index.html',context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})

def add_products(request):
    return add_item(request,productsForm)

def add_customers(request):
    return add_item(request,customersForm)

def add_orders(request):
    return add_item(request,ordersForm)



def edit_products(request, pk):
    item = get_object_or_404(products,pk=pk)

    if request.method == "POST":
        form = productsForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = productsForm(instance=item)
        return render(request, 'edit_item.html', {'form' : form})



def edit_customers(request, pk):
    item = get_object_or_404(customers,pk=pk)

    if request.method == "POST":
        form = customersForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = customersForm(instance=item)
        return render(request, 'edit_item.html', {'form' : form})


def edit_orders(request, pk):
    item = get_object_or_404(orders,pk=pk)

    if request.method == "POST":
        form = ordersForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ordersForm(instance=item)
        return render(request, 'edit_item.html', {'form' : form})


def delete_products(request, pk):

    template = 'index.html'
    products.objects.filter(pk=pk).delete()

    items = products.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_customers(request, pk):

    template = 'index.html'
    customers.objects.filter(pk=pk).delete()

    items = customers.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_orders(request, pk):

    template = 'index.html'
    orders.objects.filter(pk=pk).delete()

    items = orders.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
