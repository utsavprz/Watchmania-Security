from django import forms
from .models import Products 


# Create your forms here.
class productForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ('name','price','brand','category','description','search_tags','available','image')
