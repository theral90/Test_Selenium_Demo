import random
import pytest

from test_selenium_demo.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures('setup')
class TestCreateAccount:

    def test_create_account_passed(self):
        email = str(random.randint(0, 10000)) + 'rr@example.com'
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, 'rr@example.com')

        assert my_account_page.is_logout_link_displayed()

