from src.docking_station import DockingStation

class TestDockingStation:
    def test_release_bike(self):
        dock = DockingStation()
        assert dock.release_bike() == "bike"
