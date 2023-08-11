from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from cart.models import Delivery, Order, OrderItem
from checkout.models import ShippingAddress
from myorder.models import MyOrder
from product.models import Category

@login_required (login_url="login")
def orderedItems(request,order_id):
    allcategory = Category.objects.all()
    customer = request.user

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }

    items = OrderItem.objects.filter(order=order_id)

    context={
        'allcategory':allcategory,
        'order':order,
        'customer':customer,
        'items':items,
        'order_id':order_id,
    }


    return render(request,'orderitems.html',context)


# Create your views here.
@login_required (login_url="login")
def myOrder(request):
    allcategory = Category.objects.all()
    customer = request.user

    # ShippingAddress.objects.

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }
    
    myorder = MyOrder.objects.filter(user_info = customer)


    context={
        'allcategory':allcategory,
        'order':order,
        'customer':customer,
        'myorder':myorder, 
    }
    return render(request,'myorder.html',context)
