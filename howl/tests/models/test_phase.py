from unittest import TestCase

from howl.models.phase import BoundaryDate, PhaseBoundary


class TestQuarter(TestCase):

    def setUp(self):
        self.start = BoundaryDate()

    def test_quarter_init(self):
        self.assertEqual(
            PhaseBoundary({"startDate": self.start}),
            PhaseBoundary({"startDate": self.start}),
        )

    def test_repr(self):
        self.assertEqual(
            repr(PhaseBoundary({"startDate": self.start})),
            "{'startDate': {'date': None, 'definite': False}}",
        )