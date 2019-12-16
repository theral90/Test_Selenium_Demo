import pytest

from test_selenium_demo.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures('setup')
class TestLogIn:

    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in('rr@example.com', 'rr@example.com')

        assert my_account_page.is_logout_link_displayed()


