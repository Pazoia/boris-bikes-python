from src.bike import *

class TestBike:
    def test_bike_is_working(self):
        bike = Bike()
        assert bike.is_working() == True