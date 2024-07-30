import pytest


@pytest.mark.usefixtures("setup")
class Testcommanfixture:
    def test_one(self):
        print("first test")
    def test_second(self):
        print("second test")