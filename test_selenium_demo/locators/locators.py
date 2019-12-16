from selenium.webdriver.common.by import By


class BillingAddressLocators:

    addresses_link = (By.LINK_TEXT, 'Addresses')
    edit_link = (By.LINK_TEXT, 'Edit')
    first_name_input = (By.ID, 'billing_first_name')
    last_name_input = (By.ID, 'billing_last_name')
    country_select = (By.ID, 'billing_country')
    address_input = (By.ID, 'billing_address_1')
    postcode_input = (By.ID, 'billing_postcode')
    city_input = (By.ID, 'billing_city')
    phone_input = (By.ID, 'billing_phone')
    save_address_button = (By.XPATH, "//button[@value='Save address']")
    message_div = (By.XPATH, "//div[@class='woocommerce-message']")


class MyAccountPage:

    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    req_email_input = (By.ID, 'reg_email')
    req_password_input = (By.ID, 'reg_password')
    error_mag = (By.XPATH, "//ul[@class='woocommerce-error']//li")
    logout_link = (By.LINK_TEXT, 'Logout')
