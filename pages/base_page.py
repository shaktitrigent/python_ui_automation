from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

class BasePage:

    base_url = "https://demoqa.com"
    _handles = None

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_title(self):
        return self.driver.title

    def open_url(self, path):
        self.driver.get(self.base_url + path)

    def find_element(self, locator):
        return self.driver.find_element(locator[0], locator[1])

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, input_text):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(input_text)

    def drop_down_select(self, locator, index_value):
        Select(self.find_element(locator)).select_by_index(index_value)

    def double_click_base(self, locator):
        ActionChains(self.driver).double_click(self.find_element(locator)).perform()

    def right_click_base(self, locator):
        ActionChains(self.driver).context_click(self.find_element(locator)).perform()

    def click_base(self, locator):
        ActionChains(self.driver).click(self.find_element(locator)).perform()

    def backward(self):
        self.driver.back()

    def get_number_of_handles(self):
        self.update_window_handles()
        return len(self._handles)

    def update_window_handles(self):
        self._handles = self.driver.window_handles

    def switch_to_window_handle(self, index):
        self.driver.switch_to.window(self._handles[index])

    def switch_to_frame(self, locator):
        self.driver.switch_to.frame(self.find_element(locator))

    def close(self):
        self.driver.close()