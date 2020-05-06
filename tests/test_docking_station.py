from src.docking_station import DockingStation
from unittest.mock import MagicMock

class TestDockingStation:
    def test_responds_to_release_bike(self):
        docking_station = DockingStation()
        docking_station.release_bike = MagicMock(side_effect=docking_station.release_bike)
        docking_station.release_bike()
        docking_station.release_bike.assert_called()

    def test_released_bike_is_working(self):
        docking_station = DockingStation()
        bike = docking_station.release_bike()
        assert bike.is_working() == True
