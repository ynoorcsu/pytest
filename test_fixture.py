#! venv/bin/python

import os
import sqlite3
import pytest
from selenium import webdriver as web
     
@pytest.fixture(scope='function')
def db(tmpdir):
    file = os.path.join(tmpdir.strpath, "test.db")
  
    conn = sqlite3.connect(file)
    conn.execute("CREATE TABLE info (id, title, text)")  
    yield conn  

    conn.close()  

@pytest.mark.parametrize("id,title,text", [
    (1, "House Stark", "Winter is coming"),
    (2, "House Lannister", "A lannister always pays his debt"),
    (3, "House Tully", "Family, duty, honor")
])
def test_parametrized_entry_creation(id, title, text, db):  
    query = ("INSERT INTO info "
             "(id, title, text)"
             "VALUES (?, ?, ?)")

    values = (id, title, text)

    db.execute(query, values)

def test_entry_creation(db):  
    query = ("INSERT INTO info "  
             "(id, title, text)"  
             "VALUES (?, ?, ?)")  
    values = (1,
              "PyTest",  
              "This is a info entry")  
    
    db.execute(query, values)  

@pytest.fixture
def webdriver(request):
    dir = os.path.dirname(__file__)
    driver_path = dir + "/chromedriver"
    driver = web.Chrome(driver_path)
    request.addfinalizer(driver.quit)
    return driver

def test_nix_website_title(webdriver):
    webdriver.get("https://nixos.org/nix/")
    assert 'Nix' in webdriver.title

def test_pytest_website_title(webdriver):
    webdriver.get("http://pytest.org/latest/")
    assert 'pytest' in webdriver.title

