import pytest

@pytest.mark.xfail
def test_first():
    print("hello")

@pytest.mark.skip
def test_second():
    print("hi")

@pytest.mark.smoke
def test_Smoke():
    print("somke 1")