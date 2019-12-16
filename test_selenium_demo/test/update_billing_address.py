import random

import pytest

from test_selenium_demo.pages.billing_address_page import BillingAddressPage
from test_selenium_demo.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures('setup')
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        email = str(random.randint(0, 10000)) + 'rr@example.com'
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, 'rr@example.com')
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data('John', 'Doe')
        billing_address_page.select_country('Poland')
        billing_address_page.set_address('Kwiatowa 1', '00-001', 'Warsaw')
        billing_address_page.set_phone_number('111111111')
        billing_address_page.save_address()

        assert 'Address changed successfully' in billing_address_page.get_message_text()
