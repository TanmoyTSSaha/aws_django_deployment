from django.shortcuts import render
from .forms import CRUDForm
from .models import CRUDModel

# Create your views here.
def CRUDView(request):
    template_name = "crud/home.html"
    product_form = CRUDForm()

    products = CRUDModel.objects.all()

    if request.method == "GET":
        context = {
            "products": products,
            "product_form": product_form,
        }
        return render(request, template_name, context)
    elif request.method == "POST":
        ProductName = request.POST.get("ProductName")
        ProductColor = request.POST.get("Color")
        ProductCategory = request.POST.get("Category")
        ProductPrice = request.POST.get("Price")

        print("PRODUCT DETAILS:: ", ProductName, " | ", ProductColor, " | ", ProductCategory, " | ", ProductPrice)

        try:
            CRUDModel.objects.create(
                ProductName = ProductName,
                Color = ProductColor,
                Category = ProductCategory,
                Price = ProductPrice
            ).save()

            print("Done with saving")
        except Exception as e:
            print("EXCEPTION:: ", e)

        context = {
            "products": products,
            "product_form": product_form,
        }
        return render(request, template_name, context)