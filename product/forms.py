from django import forms
from .models import Brand, Category, Products 


# Create your forms here.
class productForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ('name','price','brand','category','description','search_tags','available','image')

class categoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__' 

class brandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__' 


