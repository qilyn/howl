from unittest import TestCase

from howl.models.phase import BoundaryDate
from howl.models.quarter import Quarter


class TestQuarter(TestCase):

    def setUp(self):
        self.start = BoundaryDate()

    def test_quarter_init(self):
        self.assertEqual(
            Quarter({"startDate": self.start}),
            Quarter({"startDate": self.start}),
        )
