from decimal import Decimal


class Item:
    def __init__(self, handle):
        """
        Subclasses have to call `self.handle().add_item(self)` to add itself to handle.
        Subclasses can raise ItemError with a translated message.
        ItemError can be raised before or after `self.handle().add_item(self)` is used.
        """
        self.__handle = handle

    @classmethod
    def instantiate_from_meta_data(cls, handle, meta_data):
        """
        Can raise ItemError with a translated message.
        """
        raise NotImplementedError("%s has to implement 'instantiate_from_meta_data' class method" % cls.__name__)

    def merge_into_items(self, items):
        """
        Has to add itself into items and return items. Itself may already exist in items.
        """
        raise NotImplementedError("%s has to implement 'merge_into_items' method" % type(self).__name__)

    def separate_from_items(self, items):
        """
        Has to remove itself from items and return items. Itself always exists in items.
        """
        raise NotImplementedError("%s has to implement 'separate_from_items' method" % type(self).__name__)

    def handle(self):
        return self.__handle

    def cart_discount(self, items):
        return Decimal("0.00")

    def meta_data(self):
        raise NotImplementedError("%s has to implement 'meta_data' method" % type(self).__name__)

    def description(self):
        raise NotImplementedError("%s has to implement 'description' method" % type(self).__name__)

    def price(self):
        raise NotImplementedError("%s has to implement 'price' method" % type(self).__name__)

    def discount(self):
        return Decimal("0.00")
