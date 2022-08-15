import pytest
# from api.scraper import FBScraper  #i need to provide the full path when using docker
from scraper import FBScraper

fbc = FBScraper()

def test_highest_comment():
    assert(fbc.highcomments()>0)

    
def test_highest_like():
    assert(fbc.highlikes()>0)