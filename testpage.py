import logging
import time
import yaml
from selenium.webdriver.common.by import By
from BaseApp import BasePage


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationHelper(BasePage):

    def input_text_into_field(self, locator, word, description=None):
        """Метод ввода текста"""
        if description:
            element_name = description
        else:
            element_name = locator

        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        """Метод кликов по кнопкам"""
        if description:
            element_name = description
        else:
            element_name = locator

        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        """Метод отлова текста"""
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We found text {text} in field {element_name}")
        return text

    def get_property_from_element(self, locator, property, description=None):
        """Методо отлова свойств элемента"""
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.get_element_property(locator, property)
        if not field:
            return None
        try:
            field
        except:
            logging.exception(f"Exception while get property from {element_name}")
            return None
        return field

    """Ввод текста"""

    def input_login(self, word):
        self.input_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'],
                                   word, description="login")

    def input_passwd(self, word):
        self.input_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'],
                                   word, description="password")

    """Кликкеры кнопок"""

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'],
                          description="login button")

    def click_about_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_ABOUT_BTN'],
                          description="about button")

    """Отлов текста из источника"""

    def login_success(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_LOGIN_SUCCESS'],
                                          description="login success")

    def about_success(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ABOUT_SUCCESS'],
                                          description="about success")

    def get_login_error(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_LOGIN_FIELD'],
                                          description="error login field success")

    def get_height(self, property):
        return self.get_property_from_element(TestSearchLocators.ids['LOCATOR_ABOUT_CSS'],
                                              property, description="text height")

    """Вспомогательные инструменты"""

    def short_pause(self):
        time.sleep(1)
