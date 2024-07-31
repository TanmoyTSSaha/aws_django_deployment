from django import forms

class CRUDForm(forms.Form):
    ProductName = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"bg-x-gray-900 border border-gray-40 text-gray-900 text-sm rounded-lg focus:border-none block min-w-80 max-w-96 p-2.5", "placeholder":"Enter the Product Name"}))
    Color = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"bg-x-gray-900 border border-gray-40 text-gray-900 text-sm rounded-lg focus:border-none block min-w-80 max-w-96 p-2.5", "placeholder":"Enter the Product Color"}))
    Category = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"bg-x-gray-900 border border-gray-40 text-gray-900 text-sm rounded-lg focus:border-none block min-w-80 max-w-96 p-2.5", "placeholder":"Enter the Product Category"}))
    Price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={"class":"bg-x-gray-900 border border-gray-40 text-gray-900 text-sm rounded-lg focus:border-none block min-w-80 max-w-96 p-2.5", "placeholder":"Enter the Product Price"}))