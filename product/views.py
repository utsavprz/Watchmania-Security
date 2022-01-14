from django.shortcuts import render

from product.models import Products

# Create your views here.
def searchResult(request):
    allproducts = Products.objects.all()

    item_name = request.GET.get('item_name')
    if item_name!= "" and item_name is not None:
        allproducts = allproducts.filter(description__icontains=item_name)

    context={
        'allproducts':allproducts,
        'item_name':item_name,
    }
    return render(request,'searchResult.html',context)