# from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, reverse

from core.product.models import Product

from .cart import Cart


# @login_required(login_url='/')
# def view_cart(request, template='cart_view.html'):
#     cart = Cart(request.session)

#     title_view = 'Empty cart' if cart.is_empty() else 'Cart'
#     template = 'client/cart/%s' % template

#     return render(request, template, {
#         'title': title_view,
#         'cart_items': cart.items,
#         'cart': cart
#     })


# @user_passes_test(check_merchant_scope, login_url='/')
# @login_required(login_url='/')
def add(request, company_id, product_id=None, quantity=1):
    """Add a product to the cart."""
    product = Product.objects.get(id=product_id)
    company_id = product.company.id
    quantity = request.POST.get('product_qty') or int(quantity)

    cart = Cart(request.session)
    cart.add(product, quantity)
    return redirect('company:detail', company_id)



# @user_passes_test(check_merchant_scope, login_url='/')
# @login_required(login_url='/')
# def remove_product(request, product_id, quantity=None):
#     """remove_product."""
#     c = Cart(request.session)
#     # TODO: It's not neccessary this query, use only the id
#     p = Product.objects.get(id=product_id)

#     c.remove(p, quantity)

#     return redirect(view_cart)


# @user_passes_test(check_merchant_scope, login_url='/')
# @login_required(login_url='/')
# def remove_product_item(request, product_id):
#     """remove_product_item."""
#     c = Cart(request.session)
#     p = Product.objects.get(id=product_id)

#     c.remove_item(p)

#     return redirect(view_cart)


# @login_required(login_url='/')
# def checkout(request):
#     """checkout."""
#     cart = Cart(request.session)
#     create_order(request.user, cart)
#     # TODO: Say to the end user that a a checkout has been successfully
#     cart.clear()
#     return redirect(list_products)
