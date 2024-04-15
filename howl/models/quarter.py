from .model import Model
from .phase import BoundaryDate


class Quarter(Model):
    """
    A specific part of the Phase.
    """
    startDate = None
    endDate = None
    created = None
    lastModified = None
    # symptoms = []

    def __init__(self, mapping=None, /, pk='', startDate : BoundaryDate = None, endDate : BoundaryDate = None, created=None, lastModified=None, **kwargs):
        if not mapping:
            mapping = {
                'pk': pk,
                'startDate': startDate,
                'endDate': endDate,
                'created': None,
                'lastModified': None,
            }
        return super().__init__(mapping)
