from src.bike import *
from unittest.mock import Mock

class TestBike:
    def test_responds_to_is_working(self):
        bike = Mock()
        bike.is_working()
        bike.is_working.assert_called()

        