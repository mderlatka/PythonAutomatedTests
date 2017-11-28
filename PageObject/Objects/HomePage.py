from PageObject.Elements.HomePageElements import HomePageElements
from PageObject.Objects.BasePage import BasePage

class HomePage(BasePage, HomePageElements):

    #def __init__(self, driver):
        #self.driver = driver

    def url(self):
        return super(HomePage, self).url() + '/'

    #def title(self):
        #return self.driver.title()

    @property
    def footer(self):
        return self.driver.find_element(*HomePageElements.FOOTER)

    @property
    def main_nav_bar(self):
        return self.driver.find_element(*HomePageElements.MAIN_NAVIGATION_BAR)