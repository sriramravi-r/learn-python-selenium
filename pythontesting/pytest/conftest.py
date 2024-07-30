import pytest


@pytest.fixture
def setup(scope="class"):
    print("i will execute first")
    yield
    print("i will run after execute")

@pytest.fixture
def dataload():
    print("user profile data is being created")
    return ["sriram","shetty","sri@gmail.com"]

@pytest.fixture(params=[("chrome","firefox"),("sri","ram")])
def crossbrowser(request):
    return request.param
