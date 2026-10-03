
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Product


def home(request):
    return render(request, 'index.html')



def admin_dashboard(request):
    return render(request, 'admin.html')
def admin_products(request):
    products = Product.objects.all()

    return render(
        request,
        'admin-products.html',
        {'products': products}
    )
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        available = request.POST.get('available') == 'on'
        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            available=available,
            image=image
        )

        return redirect('/admin-products/')

    return render(
        request,
        'add-product.html'
    )

def products(request):
    products = Product.objects.all()

    return render(
        request,
        'store/products.html',
        {'products': products}
    )


def cart(request):
    return render(
        request,
        'store/cart.html'
    )


def checkout(request):
    return render(
        request,
        'store/checkout.html'
    )


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/products/')

        return render(
            request,
            'store/login.html',
            {'error': 'Invalid username or password'}
        )

    return render(
        request,
        'store/login.html'
    )


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'store/register.html',
                {'error': 'Username already exists'}
            )

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('/login/')

    return render(
        request,
        'store/register.html'
    )

