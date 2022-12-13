import pytest


@pytest.mark.order(3)
def test_login_testCase01():
    print("Login test case 01 Executed")


@pytest.mark.order(1)
def test_login_testCase02():
    print("Login test case 02 Executed")


@pytest.mark.order(2)
def test_login_testCase03():
    print("Login test case 03 Executed")