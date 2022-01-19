import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('product:', productId)
    return JsonResponse('Item was added', safe=False)
