from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def genItemsList(cart):
    cart_items = cartItems(cart)
    item_list = ""
    for item in cart_items:
        item_list += str(item.name)
        item_list += ","
    return item_list


def cartItems(cart):
    items = []
    for item in cart:
        items.append(Product.objects.get(id=item))
    return items

def priceCart(cart):
    cart_items = cartItems(cart)
    price =0
    for item in cart_items:
        price += item.price
    return price


def catalog(request):
    if 'cart' not in request.session:
        request.session['cart'] = []

    cart = request.session['cart']
    request.session.set_expiry(0)
    store_items = Product.objects.all()
    context = {'store_items':store_items, 'cart_size':len(cart)}

    if request.method == 'POST':
        cart.append(int(request.POST['obj_id']))
        return redirect('catalog')
    return render(request, 'catalog.html', context)

def cart(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    context = {'cart':cart, 'cart_size': len(cart), 'cart_items': cartItems(cart),
               'total_price': priceCart(cart)}
    return render(request, "cart.html", context)

def removefromcart(request):
    request.session.set_expiry(0)
    obj_to_remove = int(request.POST['obj_id'])
    obj_index = request.session['cart'].index(obj_to_remove)
    request.session['cart'].pop(obj_index)
    return redirect('cart')

def checkout(request):
    request.session.set_expiry(0)
    cart = request.session['cart']
    context = {'cart':cart, 'cart_size':len(cart), 'total_price': priceCart(cart)}
    return render(request, 'checkout.html', context)

def completeOrder(request):
    request.session.set_expiry(0)
    cart = request.session['cart']
    order= Order()
    order.first_name = request.POST['first_name']
    order.last_name = request.POST['last_name']
    order.address = request.POST['address']
    order.city = request.POST['order']
    order.payment_method = request.POST['payment']
    order.payment_data = request.POST['payment_data']
    order.items = genItemsList(cart)
    request.session['cart'] = []
    return render(request, 'complete_order.html', None)

def adminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            return render(request, 'admin_login', {'login':False})

    return render(request, 'admin_login.html', None)

@login_required
def adminDashboard(request):
    orders = Order.objects.all()
    context = {'orders':orders}
    return render(request, 'admin_panel.html', context)

