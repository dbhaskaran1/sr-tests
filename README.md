# sr-tests
Tests for SmartResponseMar2017

Clone the repo

pip install -r requirements

#also download the Selenium webdriver for the browser you want to run and place it in a dir on your PATH.

cd frontend_tests

pytest #to run the tests

*Sample output should look like this.

$ pytest
=================================================================== test session starts ====================================================================

platform darwin -- Python 2.7.10, pytest-3.0.7, py-1.4.32, pluggy-0.4.0
rootdir: /Users/dbhaskaran/src/sr-tests/frontend_tests, inifile:

collected 4 items

test_login.py ....

================================================================ 4 passed in 20.00 seconds =================================================================

$
