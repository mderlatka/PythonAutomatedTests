from behave import *
from PageObject.Objects.BasePage import BasePage
from PageObject.Objects.HomePage import HomePage
from PageObject.Elements.HomePageElements import HomePageElements

@then('The title is shown on the page')
def page_title_is_present(context):
    #page = HomePage(context.driver)
    #assert page.title()
    assert context.home_page.title()

@then('the page title should be "{expected_title}"')
def verify_page_title(context, expected_title):
    #page = HomePage(context.driver)
    #assert page.title_text() == expected_title
    #page.assert_page_title(expected_title)
    assert context.home_page.title_text() == expected_title

#------------------------------------------------------#
@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    #page = BasePage(context.driver)
    #page.assert_current_url(expected_url)
    context.home_page.assert_current_url(expected_url)

#------------------------------------------------------------------------------
@then('main navigation bar should be visible')
def verify_main_nav_bar(context):
    #home_page = HomePage(context.driver)
    #assert home_page.main_nav_bar.is_displayed()
    assert context.home_page.main_nav_bar.is_displayed()
#-------------------------------------------------------------------------------------#

@then('on this bar "{element_name}" element should be visible')
def verify_element_on_main_nav_bar(context, element_name):

    #home_page = HomePage(context.driver)
    expected_elements = context.home_page.MAIN_NAV_BAR_ELEMENTS.keys()
    if element_name not in expected_elements:
        raise Exception("The passed in element is not in expected. Actual: {}, Expected: {}".format(element_name, expected_elements))

    element_data = context.home_page.MAIN_NAV_BAR_ELEMENTS.get(element_name)
    element_type = element_data['type']
    locator_value = element_data['locator']
    founded_element = context.home_page.find_element(element_type, locator_value)

    context.home_page.assert_is_element_visible(founded_element)

#--------------------------------------------------------------------------------------------------
@then('Footer should be visible')
def verify_footer(context):

    """expected_element = "footer"
    if footer != expected_element:
        raise Exception("The passed footer is not one of expected. Expected: {}, Actual: {}.".format(expected_element, footer))"""

    #page = HomePage(context.driver)
    #assert page.footer.is_displayed()
    assert  context.home_page.footer.is_displayed()
#--------------------------------------------------------------------------------

@then('"{footer_section}" section should be on page')
def verify_footer_section(context, footer_section):

    #home_page = HomePage(context.driver)
    expected_footer_section = context.home_page.FOOTER_SECTION.keys()

    if footer_section not in expected_footer_section:
        raise Exception("The passed footer is not one of expected. Expected: {}, Actual: {}.".format(expected_footer_section, footer_section))

    locator_data = context.home_page.FOOTER_SECTION.get(footer_section)
    locator_type = locator_data['type']
    locator_value = locator_data['locator']


    found_element = context.home_page.find_element(locator_type, locator_value)

    context.home_page.assert_is_element_visible(found_element)