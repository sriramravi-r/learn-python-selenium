import pytest

@pytest.mark.smoke
def test_fixture(setup):
    print("i will execute step after the setup is done")