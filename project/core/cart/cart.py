from core.product.models import Product


class CartItem:
    """CartItem model

    A representation of a cart item, with all his own attrs and
    methods.
    """
    def __init__(self, product, quantity=1):
        """CartItem constructor

        KEYWORD ARGUMENTS:
        product  -- The instance of a product
        quantity -- Quantity of products to add
        """
        self.product = product
        self.quantity = int(quantity)
        # self.price_with_vat = price_with_vat
        # self.price_without_vat = price_without_vat
        # self.amount = amount

    def as_dict(self):
        """Return a cart item as a dict"""
        return {
            'product_id': self.product.id,
            'quantity': str(self.quantity)
        }

    def unit_price_neto(self):
        """Return the unit price (without VAT)"""
        return self.product.retail_net_price()

    def unit_price_bruto(self):
        """Return the unit price (with VAT)"""
        return self.product.retail_gross_price()

    @property
    def subtotal(self):
        """Return the subtotal price (without VAT)"""
        return self.product.retail_net_price() * self.quantity

    @property
    def total(self):
        """Return the total price (with VAT)"""
        return self.product.retail_gross_price() * self.quantity


class Cart:
    """Cart model"""

    def __init__(self, session, session_key='cart'):
        """Cart constructor

        KEYWORD ARGUMENTS:
        session     --
        session_key --
        """
        self._items = {}
        self.session = session
        self.session_key = session_key

        if self.session_key in self.session:
            cart = self.session[self.session_key]
            cart_keys = cart.keys()
            products_in_cart = Product.objects.filter(pk__in=cart_keys)  # order_items

            for product in products_in_cart:
                item = cart[str(product.id)]
                self._items[product.id] = CartItem(product, item['quantity'])

    @property
    def items(self):
        return self._items.values()

    @property
    def serialize_cart(self):
        """Serialize the cart data and return it as a JSON object.

        EXAMPLE:
        {
            1: { 'product_id': 1, [...], 'quantity': 1 }
            2: { 'product_id': 2, [...], 'quantity': 2 }
            7: { 'product_id': 7, [...], 'quantity': 3 }
        }

        NOTES:
        Use the product.id as dict key.
        """
        cart = {}
        for item in self.items:
            product_id = str(item.product.id)
            cart[product_id] = item.as_dict()
        return cart

    def update_session(self):
        """Update the session with a serialized cart data"""
        self.session[self.session_key] = self.serialize_cart
        self.session.modified = True

    @property
    def products(self):
        """Return a list of products"""
        return [item.product for item in self.items]

    def add(self, product, quantity=1):
        """Add a product into the cart"""
        quantity = int(quantity)

        if quantity < 1:
            raise ValueError(
                'Quantity must be at least 1 to add an item to the cart')

        if product in self.products:
            # Increase the quantity if product exist
            self._items[product.id].quantity += quantity
        else:
            # if price is None:
            #     raise ValueError('Missing price of the product')
            # Create a new product
            self._items[product.id] = CartItem(product, quantity)

        self.update_session()

    def remove(self, product, quantity=None):
        """Removes the product from the cart"""
        # TODO: We can remove a product by id instead of object instance
        if product in self.products:
            if quantity:
                if self._items[product.id].quantity <= 1:
                    del self._items[product.id]
                else:
                    self._items[product.id].quantity -= 1

            else:
                del self._items[product.id]

            self.update_session()

    def clear(self):
        """Removes all items from the cart"""
        self._items = {}
        self.update_session()

    def is_empty(self):
        """"Check if the cart is empty"""
        return len(self._items) == 0

    @property
    def total_units(self):
        """Return the total units as a sum of quantities"""
        return sum([item.quantity for item in self.items])

    @property
    def subtotal(self):
        """Return the subtotal of the whole cart"""
        return sum([item.subtotal for item in self.items])

    @property
    def vat_details(self):
        """Return a sum of each vat present in the cart"""
        vat_list = []
        for item in self.items:
            if item.product.vat not in vat_list:
                vat_list.append(item.product.vat)

        vats = []
        for vat in vat_list:
            total_vat = sum([
                item.product.vat_amount(item.product.retail_net_price(),
                                        item.quantity) for item in self.items
                if item.product.vat == vat
            ])

            vats.append({'name': str(vat.name), 'total': str(total_vat)})

        return vats

        # Example: short form with compressed lists. Nice to know!
        # return [{
        #     'name': str(vat.name),
        #     'total': str(
        #         sum([item.total for item in self.items if item.product.vat == vat])
        #         )} for vat in vat_list]

    @property
    def total(self):
        """Return the total of the whole cart"""
        return sum([item.total for item in self.items])
