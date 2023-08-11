import json
from multiprocessing import context
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import JsonResponse
from cart.models import Order, OrderItem
from cryptography.fernet import Fernet
from django.contrib.auth.models import User

from product.models import Category, Products


def encrypt_product_name(product_name):
    cipher_suite = Fernet(settings.ENCRYPTION_KEY)
    encrypted_name = cipher_suite.encrypt(product_name.encode())
    return encrypted_name

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    if 'qty' in data and data['qty'] != "false":
        qty = int(data['qty'])
    else:
        qty = 0

    customer = request.user
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user_info=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        if orderItem.quantity > 0:
            orderItem.quantity = 0
            orderItem.save()
        orderItem.delete() 
        return JsonResponse('Product updated successfully', safe=False)
    elif action == 'addWithQty':
        if qty > 0:
            orderItem.quantity += qty
    elif action == 'deleteItem':
        if orderItem.quantity > 0:
            orderItem.quantity = 0
            orderItem.save()
        orderItem.delete() 
        return JsonResponse('Product updated successfully', safe=False)

    if orderItem.quantity <= 0:
        print(orderItem)
        print('here')
        orderItem.delete()  # Delete the OrderItem if the quantity is <= 0
    else:
        orderItem.save()

    # Encrypt the product name using Fernet encryption and store it in encrypted_product field
    encrypted_product_name = encrypt_product_name(product.name)
    orderItem.encrypted_product = encrypted_product_name.decode()  # Convert bytes to string
    orderItem.save()

    return JsonResponse('Product updated successfully', safe=False)


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