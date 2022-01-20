from django.shortcuts import render
from cart.models import Order

from product.models import Category

# Create your views here.
def checkout(request):
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
    return render(request,'checkout.html',context)