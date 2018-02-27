class Item:
    def __init__(self, handle):
        self.__handle = handle

    @classmethod
    def instantiate_from_meta_data(cls, meta_data):
        raise NotImplementedError("%s has to implement 'instantiate_from_meta_data' class method" % cls.__name__)

    def merge_into_items(self, items):
        raise NotImplementedError("%s has to implement 'merge_into_items' method" % type(self).__name__)

    def separate_from_items(self, items):
        raise NotImplementedError("%s has to implement 'separate_from_items' method" % type(self).__name__)

    def handle(self):
        return self.__handle
