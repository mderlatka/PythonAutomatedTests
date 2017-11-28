from behave import *

@when("I click on the '{element}' element")
def click_on_main_nav_element(context, element):
    element_data = context.home_page.MAIN_NAV_BAR_ELEMENTS.get(element)
    element_type = element_data['type']
    locator_value = element_data['locator']
    founded_element = context.home_page.find_element(element_type, locator_value)
    founded_element.click()