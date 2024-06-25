from howl.models.model import Model


class BoundaryDate:
    date = None
    definite = False

    def __init__(self, date=None, definite: bool = False):
        self.date = date
        self.definite = definite

    def __eq__(self, other):
        if isinstance(other, BoundaryDate):
            return other.date == self.date and other.definite == self.definite
        return False

    def __repr__(self):
        return repr({'date': self.date, 'definite': self.definite})


class PhaseBoundary(Model):
    """
    A PhaseBoundary is flexible and is positioned dynamically around its Quarter.

    PhaseBoundary.startDate = its lastPhase.quarter.endDate + 1
    PhaseBoundary.endDate = its quarter.endDate
    """
    startDate : BoundaryDate = None
    endDate : BoundaryDate = None
    nextPhase = None
    lastPhase = None
    # events = []

    def __init__(self, mapping=None, /, pk='', startDate : BoundaryDate = None, endDate : BoundaryDate = None, **kwargs):
        if not mapping:
            mapping = {
                'pk': pk,
                'startDate': startDate,
                'endDate': endDate,
                'nextPhase': None,
                'lastPhase': None,
            }
        return super().__init__(mapping)

    def __eq__(self, other):
        if isinstance(other, PhaseBoundary):
            return super().__eq__(other)

        return False