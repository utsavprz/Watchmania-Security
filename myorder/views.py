from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cart.models import Delivery, Order, OrderItem
from myorder.models import MyOrder
from product.models import Category

# Create your views here.
@login_required
def myOrder(request):
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
    
    myorder = MyOrder.objects.filter(user_info = customer)
    items = OrderItem.objects.all()


    context={
        'allcategory':allcategory,
        'order':order,
        'customer':customer,
        'myorder':myorder, 
        'items':items,
    }
    return render(request,'myorder.html',context)
