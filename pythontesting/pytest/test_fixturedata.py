import pytest


@pytest.mark.usefixtures("dataload")
class Testexample:
    def test_editprofile(self,dataload):
        print(dataload)

    def test_crossBrowser(self,crossbrowser):
        print(crossbrowser)