from testpage import OperationHelper as OH
import logging
import yaml

with open('testdata.yaml') as f:
    data = yaml.safe_load(f)


def test_step_1(browser):
    logging.info("Test 1 starting")
    testpage = OH(browser)
    testpage.go_to_site()
    testpage.input_login("test")
    testpage.input_passwd("test")
    testpage.click_login_button()
    assert testpage.get_login_error() == "401", "Test 1 FAIL"


def test_step_2(browser):
    logging.info("Test 2 starting")
    testpage = OH(browser)
    testpage.go_to_site()
    testpage.input_login(data['user_name'])
    testpage.input_passwd(data['user_pass'])
    testpage.click_login_button()
    testpage.short_pause()
    assert testpage.login_success() == f"Hello, {data['user_name']}", "Test 2 FAIL"


def test_step_3(browser):
    logging.info('Test 3 starting')
    testpage = OH(browser)
    testpage.click_about_button()
    testpage.short_pause()
    assert testpage.about_success() == "About Page", "Test 3 FAIL"


def test_step_4(browser):
    logging.info('Test 4 starting')
    testpage = OH(browser)
    assert testpage.get_height("font-size") == "32px", "Test 4 FAIL"
