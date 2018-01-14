import time
from PageObject.Elements.CommonElements import CommonElements
from PageObject.Elements.BasePageElements import BasePageElements

class BasePage(CommonElements):

    def __init__(self, context):
        self.driver = context.driver

    def url(self):
        return 'https://www.udemy.com'

    def title(self):
        return self.driver.find_element(*BasePageElements.TITLE)

    def title_text(self):
        return self.driver.title

    # --------------------------------------------------------------------------#

    def assert_page_title(self, expected_title):
        """
        Function to assert title of current page
        :param expected_title:
        :return:
        """
        actual_page_title = self.driver.title

        print("Actual title is: {}".format(actual_page_title))
        print("Expected title is: {}".format(expected_title))

        assert expected_title == actual_page_title, "The title is not as expected. Expected: {}, Actual:{}".format(
            expected_title, actual_page_title)
        print("Page title is as expected")

    # ----------------------------------------------------#

    def assert_current_url(self, expected_url):

        actual_page_url = self.driver.current_url

        if not expected_url.startswith('http') or not expected_url.startswith('https'):
            expected_url = 'https://' + expected_url + '/'

        assert actual_page_url.startswith(
            expected_url), "The current url is not as expected. Actual: {}, Expected: {}.".format(actual_page_url,
                                                                                                  expected_url)
        print("Page url is as expected")

    # -----------------------------------------------------#

    def find_element(self, locator_type, locator_value):
        """
        Finds element and returns the element object.
        :param locator_type: which attribute to use to locate element (example: id, class, xpath,....)
        :param the locator_value: example: the id, class, name, ....)
        """

        possible_locators = CommonElements.LOCATORS

        if locator_type not in possible_locators:
            raise Exception(
                'Provided locator attribute is not in approved attribute. Approved attributes: %s' % possible_locators)
        try:
            time.sleep(2)
            element = self.driver.find_element(locator_type, locator_value)
            return element
        except Exception as e:
            raise Exception(e)

    # -----------------------------------------------------------------------------------------#

    def assert_is_element_visible(self, element):
        """
        Function to assert if element is visible and returns True or False
        """
        if not element.is_displayed():
            raise AssertionError("Element is not visible")
