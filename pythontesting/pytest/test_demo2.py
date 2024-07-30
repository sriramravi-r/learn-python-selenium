import pytest


@pytest.mark.skip
def test_third():
    assert "hi" == "hello"

def test_fourth(setup):
    print("four")

@pytest.mark.smoke
def test_Smoke(setup):
    print("somke 2")