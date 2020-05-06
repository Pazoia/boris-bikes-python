from src.bike import *
from unittest.mock import MagicMock

class TestBike:
    def test_responds_to_is_working(self):
        bike = Bike()
        bike.is_working = MagicMock(side_effect=bike.is_working)
        bike.is_working()
        bike.is_working.assert_called()

        