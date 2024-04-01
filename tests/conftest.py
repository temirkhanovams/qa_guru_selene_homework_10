from selene import browser
import pytest


@pytest.fixture(scope='function')
def browser_init():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1024
    browser.config.window_height = 780

    yield

    browser.quit()
