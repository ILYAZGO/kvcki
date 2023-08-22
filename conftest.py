import pytest
#import requests
#from utils.create_delete_user import create_user, delete_user
from utils.variables import *

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):

    width = [1366, 1920, 1440, 1536, 1600]
    height = [768, 1080, 900, 864, 900]


    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

