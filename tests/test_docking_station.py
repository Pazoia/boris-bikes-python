from src.docking_station import *
from unittest.mock import Mock

class TestDockingStation:

    def test_responds_to_release_bike(self):
        docking_station = Mock()
        docking_station.release_bike()
        docking_station.release_bike.assert_called()
        

    def test_released_bike_is_working(self):
        docking_station = DockingStation()
        bike = docking_station.release_bike()
        assert bike.is_working() == True
