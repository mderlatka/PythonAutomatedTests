from selenium import webdriver
from PageObject.Objects.HomePage import HomePage
from PageObject.Objects.BasePage import BasePage


def before_all(context):
    context.driver = webdriver.Firefox()
    context.home_page = HomePage(context)
    context.base_page = BasePage(context)


def after_all(context):
    context.driver.close()