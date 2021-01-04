import pytest
from delivery.app import create_app


@pytest.fixture(scope="module")  #scope options -> "function" => creates a new app for each test and delete it by the end of that test
def app():                       #              ->  "module"  => creates one app and run all the test on that app.   
    """Instance of Main flask app""" 
    return create_app() # this is the reason that we install our project
