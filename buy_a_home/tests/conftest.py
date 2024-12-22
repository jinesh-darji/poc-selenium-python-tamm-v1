import re

import pytest
import allure
from allure_commons.types import AttachmentType

from allure import MASTER_HELPER as ALLURE_HELPER

from framework.browser.Browser import Browser
from framework.utils.EnvReader import EnvReader
from framework.utils.Screenshooter import Screenshooter
from framework.configuration import config
from buy_a_home.configuration import config as project_config


@pytest.fixture(scope="function", autouse=True)
def browser(request, prepare_config):
    Browser.set_up_driver()
    Browser.set_url(EnvReader().get_env_config()['start_url'])
    Browser.get_driver().set_window_size(1920, 1080)
    tests_failed_before_function = request.session.testsfailed
    yield
    Screenshooter.set_session_screen_dir()
    if request.session.testsfailed != tests_failed_before_function:
        allure.attach('screenshot', open(Screenshooter.take_screenshot(), 'rb').read(), type=AttachmentType.JPG)
    Browser.quit()


@pytest.fixture(scope='function', autouse=True)
def allure_naming():
    """Using name of method as name of test in allure-report"""
    if ALLURE_HELPER._allurelistener:
        method_name = re.search("\.(?:.(?!\.))+$", str(ALLURE_HELPER._allurelistener.test.name)).group(0).\
            replace('.', '')
        ALLURE_HELPER._allurelistener.test.name = method_name


@pytest.fixture(scope="function", autouse=True)
def prepare_config():
    """Using config file for each journey"""
    for key, value in project_config.__dict__.items():
        config.__dict__[key] = value

