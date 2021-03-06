from django.shortcuts import render
from .models import Product, Category
from cart.forms import CartAddProductForm


def product(request):
    list_category = Category.objects.all()
    return render(request, 'category.html', context={'category': list_category})


def detail(request, category_id, product_id):
    products_code = Product.objects.get(id=product_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'product.html', context={'product': products_code, 'cart_product_form': cart_product_form})


def catalog(request, category_id):
    print(category_id)
    list_product = Product.objects.filter(category_id=category_id)
    return render(request, 'catalog/base.html', context={'product': list_product})
