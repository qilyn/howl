import inspect


class UndefinedPropertyException(Exception):
    pass


class Model(dict):
    """
    Generic behaviour for all models.
    Written to provide some structure to a basic dictionary (and also kind of with Django in the back of my mind).
    """

    def __init__(self, mapping, /, **kwargs):
        return super().__init__(mapping)

    def __setitem__(self, key, value):
        if key not in inspect.getmembers_static():
            raise UndefinedPropertyException()
        return super().__setitem__(key, value)
