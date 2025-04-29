import pytest
import time

from selenium.webdriver.common.by import By

BROWSER_LINK = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestAbs():
    def test_add_to_basket_btn(self, browser):
        # Arrange
        browser.get(BROWSER_LINK)

        # Act
        add_to_basket_btn = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
        #time.sleep(10)
        
        # Assert
        assert add_to_basket_btn is not None, "Add to basket button not found"