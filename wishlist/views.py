from django.shortcuts import render, get_object_or_404
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
    wishlist.products.add(product) 
    wishlist.save()  
    wishlist_data = {
        'user_id': user.id,
        'wishlist_id': wishlist.id,
        'products': wishlist.products.all(),  
        'created_at': wishlist.created_at,
    }
    return render(request, 'wishlist/wishlist.html', {'wishlist_data': wishlist_data})


# @login_required
# @require_POST
# def add_to_wishlist(request, product_id):
#     user = request.user
#     wishlist, created = Wishlist.objects.get_or_create(user=user)
#     product = get_object_or_404(Product, pk=product_id)

    
#     wishlist.products.add(product)
#     wishlist.save()
#     messages.success(request, 'Item added to your wishlist.')

#     test = wishlist.products.all()

#     context = {
#       'wishlist': test,
#     }

#     return render(request, 'wishlist/wishlist.html', context)
    

# @login_required
# @require_POST
# def remove_from_wishlist(request, product_id):
#     user = request.user
#     wishlist, created = Wishlist.objects.get_or_create(user=user)
#     product = get_object_or_404(Product, pk=product_id)

    
#     wishlist.products.remove(product)
#     wishlist.save()
#     messages.success(request, 'Item removed from your wishlist.')

def remove_from_wishlist(request, product_id):
    user = request.user
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    product = get_object_or_404(Product, pk=product_id)

    wishlist.products.remove(product)
    wishlist.save()

    wishlist_data = {
        'user_id': user.id,
        'wishlist_id': wishlist.id,
        'product': product,
        'created_at': wishlist.created_at,
    }

    return render(request, 'wishlist/wishlist.html', {'wishlist_data': wishlist_data})
