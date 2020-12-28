import os

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import ProductForm
from .models import Product, Order, Category, ProductSlider
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


@login_required(login_url="/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product:e-market")


@login_required(login_url="/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("product:cart_detail")


@login_required(login_url="/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product:cart_detail")


@login_required(login_url="/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("product:cart_detail")


@login_required(login_url="/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("product:cart_detail")


@login_required(login_url="/")
def cart_detail(request):
    return render(request, 'product/cart_details.html')


class EmarketView(View):
    def get(self, request):
        products = Product.objects.filter().order_by('-id')
        categories = Category.objects.filter()
        sliders = ProductSlider.objects.all()
        context = {
            'products': products,
            'categories': categories,
            'sliders': sliders
        }
        return render(request, 'product/e_market.html', context)


class ProductByCategory(View):
    def get(self, request, pk):
        products = Product.objects.filter(category_id=pk).order_by('-id')
        # categories = Category.objects.filter().order_by('-id')
        context = {
            'products': products,
            # 'categories': categories
        }
        return render(request, 'product/product_by_cat.html', context)

#
# To view the cart detail page use the below code
#
# {% load cart_tag %}
#
# Total Length :: {{request.session.cart|length}}
#
# Cart Detail:
#
# {% for key,value in request.session.cart.items %}
# {{value.name}} {{value.price}} {{value.quantity}} {{value.image}} Total {{ value.price|multiply:value.quantity }}
#
# {% endfor %}


class AddProductView(View):
    def get(self, request):
        form = ProductForm()
        context = {
            'status': 'active',
            'form': form,
        }
        return render(request, 'product/add_product.html', context)

    def post(self, request):
        form = ProductForm(request.POST or None, request.FILES or None)
        if request.method == 'POST':

            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user;
                obj.save()
                form = ProductForm()
                messages.success(request, "Successfully created")

        return render(request, 'product/add_product.html', {'form': form})


class MyShopProductView(View):
    def get(self, request):
        products = Product.objects.filter(user_id=request.user.id)
        context = {
            'products': products
        }
        return render(request, 'product/my_shop.html', context)


class EditProductView(View):
    def get(self, request, pk):
        data = Product.objects.get(pk=pk)
        form = ProductForm(instance=data)
        context = {
            'sttus': 'active',
            'data': data,
            'form': form,
            'id': data.id,
        }
        return render(request, 'product/edit.html', context)


class UpdateProductView(View):
    def post(self, request):
        id = request.POST.get('id')
        product = Product.objects.get(id=id)
        form = ProductForm(request.POST, request.FILES or None, instance=product)
        context = {
            'status': 'active',
            'form': form,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Data updated successful', extra_tags='success')
        else:
            return render(request, 'product/edit.html', context)
        return redirect('product:my-shop')


class DeleteProductView(View):
    def get(self, request, pk):
        id = request.POST.get('id')
        product = Product.objects.get(id=pk)
        product.delete()
        messages.success(request, 'Data updated successful', extra_tags='success')
        return redirect('product:my-shop')


class DetailProductView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        user = User.objects.get(pk=product.user_id)

        context = {
            'product': product,
            'user': user
        }
        return render(request, 'product/product_details.html', context)


class SellerContactView(View):
    def get(self, request, pk):

        return render(request, 'product/seller_contact.html')


class OrderSubmit(View):
    def post(self, request):
        name = request.POST.getlist('name[]')
        price = request.POST.getlist('price[]')
        qty = request.POST.getlist('qty[]')
        subtotal = request.POST.get('subtotal')

        datalen = len(name)
        i = 0
        while i < datalen:
            data = Order()
            data.name = name[i]
            data.price = price[i]
            data.qty = qty[i]
            data.user_id = request.user.id
            data.status = 1
            data.save()
            i += 1
        cart = Cart(request)
        cart.clear()
        response = {
            'success': 'Success! '
        }
        return JsonResponse(response)


class ProductSearchView(View):
    def post(self, request):
        name = request.POST.get('name')
        products = Product.objects.filter(name=name)
        context = {
            'products': products
        }
        return render(request, 'product/product_search.html', context)