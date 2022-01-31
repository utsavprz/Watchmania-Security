from tokenize import Token
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from accounts.models import User_Address
from cart.models import Order
from django.contrib.auth.decorators import login_required

import requests

from product.models import Category

# Create your views here. 
@login_required
def checkout(request):
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

    addressExists = False
    if (User_Address.objects.filter(user_info = customer.id).exists()):
        addressData = User_Address.objects.filter(user_info = customer.id)[0]
        addressExists=True
    else:
        addressExists=False

    # checkout operation for COD
    if request.method == 'POST':
        ShippingData = request.POST 
        user_info = customer
        order = order.id
        phone = ShippingData.get('phone')
        email = ShippingData.get('email')
        city = ShippingData.get('city')
        address = ShippingData.get('address')
        street = ShippingData.get('street')
        postalcode = ShippingData.get('postalcode')
        description = ShippingData.get('description')
        
        if ShippingData.get('PaymentMethod') == "Cash on Delivery":
            print(ShippingData)
            return redirect('index')

    

    context={
        'allcategory':allcategory,
        'items':items,
        'order':order,
        'customer':customer,
        'addressExists':addressExists,
        'addressData':addressData,
        
    }
    return render(request,'checkout.html',context)

# def KhaltiRequestView(request):
#     return render(request,'khaltirequest.html')

def KhaltiVerifyView(request):
    customer = request.user
    token = request.GET.get("token")
    amount = request.GET.get("amount")
    o_id = request.GET.get("order_id") 

    print(token ,amount,o_id)

    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
    "token": token,
    "amount": amount
    }
    headers = {
    "Authorization": "Key test_secret_key_90007f7bfd9d46ca9e8c7ce8d2802119"
    }

    order = Order.objects.get(id=o_id)
    response = requests.post(url, payload, headers = headers)
    response_dict = response.json()

    if response_dict.get("idx"):
        success = True
        order.complete = True
        order.payment_method = "Khalti"
        order.save()
        
    else:
        success = False

    data={
        "success":success
    }
    return JsonResponse(data)

def paymentSuccess(request):
    return render(request,'PaymentSuccess.html')
