import sys
# import logging

from pprint import PrettyPrinter

from core.product.models import Product

# logger = logging.getLogger(__name__)
dumper = PrettyPrinter(indent=4, stream=sys.stderr).pprint


class CartItem:
   
    def __init__(self, product, quantity=1):
       self.product = product
       self.quantity = int(quantity)

    def as_dict(self):
        return {
            'product_id': self.product.id,
            'quantity': str(self.quantity)
        }

    @property
    def total(self):
        """Return the total price (with VAT)"""
        return self.product.price * self.quantity
    
class Cart:

    def __init__(self, session, session_key='cart'):
        self._items = {}
        self.session = session
        self.session_key = session_key

        if self.session_key in self.session:
            cart = self.session[self.session_key]
            cart_keys = cart.keys()
            products_in_cart = Product.objects.filter(pk__in=cart_keys)

            for product in products_in_cart:
                item = cart[str(product.id)]
                self._items[product.id] = CartItem(product, item['quantity'])

    @property
    def items(self):
        return self._items.values()

    @property
    def serialize_cart(self):
        cart = {}
        for item in self.items:
            product_id = str(item.product.id)
            cart[product_id] = item.as_dict()
        return cart

    def update_session(self):
        self.session[self.session_key] = self.serialize_cart
        self.session.modified = True

    @property
    def products(self):
        return [item.product for item in self.items]

    def add(self, product):
        if product in self.products:
            self._items[product.id].quantity += 1
        else:
            self._items[product.id] = CartItem(product)

        self.update_session()

    def clear(self):
        self._items = {}
        self.update_session()

    @property
    def total(self):
        return sum([item.total for item in self.items])
