from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ElementText(BasePage):
    elements_path = '/elements'
    text_loc = "/text-box"
    fullname_loc = (By.ID, "userName")
    email_loc = (By.ID, "userEmail")
    current_address_loc = (By.ID, "currentAddress")
    elements_permanent_address_loc = (By.ID, "permanentAddress")
    submit_button_loc = (By.ID, "submit")

    def __init__(self):
        super(ElementText, self).__init__()

    def open_text_area(self):
        self.open_url(self.text_loc)

    def enter_full_name(self):
        self.send_keys(self.fullname_loc, "Mohan H")

    def enter_email_id(self):
        self.send_keys(self.email_loc, "mohanh@gmail.com")

    def enter_current_address(self):
        self.send_keys(self.current_address_loc, "Bengaluru")

    def enter_permanent_address(self):
        self.send_keys(self.elements_permanent_address_loc, "Shivamogga")

    def enter_submit(self):
        self.click(self.submit_button_loc)

    def close_tab(self):
        self.close()


c1 = ElementText()
c1.open_text_area()
c1.enter_full_name()
c1.enter_email_id()
c1.enter_current_address()
c1.enter_permanent_address()
c1.enter_submit()