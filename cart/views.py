import json
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import JsonResponse
from cart.models import Order, OrderItem
from django.contrib.auth.models import User

from product.models import Category, Products

# Create your views here.

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    if(data['qty'] == "false"):
        pass
    else:
        qty = data['qty']

    customer = request.user
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user_info = customer, complete=False)

    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'addWithQty':
        orderItem.quantity = (orderItem.quantity + int(qty))
    elif action == 'deleteItem':
        orderItem.quantity = 0
    orderItem.save()


    if orderItem.quantity <=0:
        orderItem.delete()
    
    # return redirect ('index')

    return JsonResponse('HREER', safe=False)

def cartIndex(request):
    allcategory = Category.objects.all()

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user_info = customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }
    context={
        'allcategory':allcategory,
        'items':items,
        'order':order,
        
    }
    return render(request,'cart.html',context)



