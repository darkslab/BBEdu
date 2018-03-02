from django.db.transaction import atomic
from django.db import IntegrityError
from decimal import Decimal
from . import items
from .items.base import Item
from .exceptions import ShoppingError, ItemError
from .base import Cart, LineItem


class CartHandle:
    def __init__(self, cart):
        self.__cart = cart
        self.__products = []
        self.__errors = []
        self.__is_modified = False

        if not self.__cart.is_current:
            raise ShoppingError("Only current carts are allowed")
        for line_item in self.__cart.line_items.all():
            if not hasattr(items, line_item.item_class):
                raise ShoppingError("Incorrect item class: %s" % line_item.item_class)
            try:
                getattr(items, line_item.item_class).instantiate_from_meta_data(line_item.meta_data)
            except ItemError as error:
                self.__errors.append(str(error))

            if len([ product for product in self.__products if product["item"] is not None and product["line_item"] is None ]) > 1:
                raise ShoppingError("Incorrect item instantiation from meta data")
            for product in self.__products:
                if product["item"] is not None and product["line_item"] is None:
                    product["line_item"] = line_item
                    break

        self.__is_modified = False
        if len(self.__errors):
            self.__is_modified = True
            self.save()

        # DARK_TODO  do something with self.__errors

    def add_item(self, item):
        self.__normalize_products(item.merge_into_items(self.__items()))
        self.__is_modified = True

    def remove_item(self, item):
        items = self.__items()
        if item not in items:
            return
        self.__normalize_products(item.separate_from_items(items))
        self.__is_modified = True

    def charge(self):
        # DARK_TODO  implement this!
        pass

    def save(self):
        if not self.__is_modified:
            return

        lock_safe = False
        try:
            with atomic(savepoint=False):
                if not self.__cart.is_current:
                    raise ShoppingError("Cannot save a non-current cart")
                self.__cart.discount = Decimal("0.00")
                items = self.__items()
                for item in items:
                    self.__cart.discount += item.cart_discount(items)
                if self.__cart.pk is None:
                    self.__cart.save()
                    lock_safe = True

                expired_line_items = [ product["line_item"] for product in self.__products if product["item"] is None ]
                expired_line_items.sort(key=lambda line_item: line_item.pk)
                for expired_line_item in expired_line_items:
                    expired_line_item.delete()

                existing_products = [ product for product in self.__products if product["item"] is not None and product["line_item"] is not None ]
                existing_products.sort(key=lambda existing_product: existing_product["line_item"].pk)

                new_products = [ product for product in self.__products if product["item"] is not None and product["line_item"] is None ]
                for new_product in new_products:
                    new_product["line_item"] = LineItem(cart=self.__cart)

                for products in (existing_products, new_products):
                    for product in products:
                        product["line_item"].item_class = product["item"].__class__.__name__
                        product["line_item"].meta_data = product["item"].meta_data()
                        product["line_item"].description = product["item"].description()
                        product["line_item"].price = product["item"].price()
                        product["line_item"].discount = product["item"].discount()
                        product["line_item"].refunded = Decimal("0.00")
                        product["line_item"].save()

                if not lock_safe:
                    self.__cart.save()
                    if not Cart.objects.filter(pk=self.__cart.pk, lock_version=self.__cart.lock_version).update(lock_version=(self.__cart.lock_version + 1)):
                        raise IntegrityError("Cart is stale")

            self.__is_modified = False
        except IntegrityError:
            raise ShoppingError("Could not save the cart")

        self.__products = [ product for product in self.__products if product["item"] is not None ]

    def __iter__(self):
        return ItemsIterator(self.__items())

    def __items(self):
        return [ product["item"] for product in self.__products if product["item"] is not None ]

    def __normalize_products(self, items):
        if not isinstance(items, list):
            raise ShoppingError("Cannot process Items")
        if len(items) != len(set(items)):
            raise ShoppingError("Item duplication is not supported")

        product_items = self.__items()
        for item in items:
            if not isinstance(item, Item):
                raise ShoppingError("Items have to be an Item subclass")
            if item not in product_items:
                self.__products.append({
                    "item": item,
                    "line_item": None,
                })
        for product in self.__products:
            if product["item"] is not None and product["item"] not in items:
                product["item"] = None

        expired_products = [ product for product in self.__products if product["item"] is None and product["line_item"] is not None ]
        valid_products = [ product for product in self.__products if product["item"] is not None ]

        valid_products.sort(key=lambda product: items.index(product["item"]))
        self.__products = valid_products + expired_products


class ItemsIterator:
    def __init__(self, items):
        self.__index = 0
        self.__items = items

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration
