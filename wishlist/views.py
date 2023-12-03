from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from products.models import Product


@login_required
def view_wishlist(request):
    """ A view that renders the cart contents page """
    user = request.user
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    products = Wishlist.objects.filter(user=user)
    wishlist_data = {
        'user_id': user.id,
        'wishlist_id': wishlist.id,
        'products': products,
        'created_at': wishlist.created_at,
    }
    return render(request, 'wishlist/wishlist.html', wishlist_data)


@login_required
def add_to_wishlist(request, product_id):
    user = request.user
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    product = get_object_or_404(Product, pk=product_id)

    # Check if the product is already in the wishlist
    if product in wishlist.products.all():
        messages.warning(request, 'This item is already in your wishlist.')
    else:
        wishlist.products.add(product)
        wishlist.save()
        messages.success(request, 'Item added to wishlist successfully.')

    wishlist_data = {
        'user_id': user.id,
        'wishlist_id': wishlist.id,
        'products': wishlist.products.all(),
        'created_at': wishlist.created_at,
    }
    return redirect('product_detail', product_id=product.id)

def remove_from_wishlist(request, product_id):
    user = request.user
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    product = get_object_or_404(Product, pk=product_id)

    wishlist.products.remove(product)
    wishlist.save()

    wishlist_data = {
        'user_id': user.id,
        'wishlist_id': wishlist.id,
        'products': wishlist.products.all(),
        'created_at': wishlist.created_at,
    }

    return render(
        request, 'wishlist/wishlist.html', {'wishlist_data': wishlist_data})
