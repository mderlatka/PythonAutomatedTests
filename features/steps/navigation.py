from PageObject import urlconfigs
from behave import *



@given('I am on the home page with "{language}" language set')
def main_page(context, language=None):
    available_languages = urlconfigs.URL_LANG_CONFIG.keys()
    if language not in available_languages:
        raise Exception("Passed in language is not available. List to choose {}.".format(available_languages))

    #context.driver = webdriver.Firefox()
    #home_page_url = HomePage(context.driver)
    if not language:
        lang_url = urlconfigs.URL_LANG_CONFIG.get('english')
    else:
        lang_url = urlconfigs.URL_LANG_CONFIG.get(language)
    lang_url = lang_url['url']
    full_url = context.home_page.url() + lang_url

    print("Navigating to the site: {}".format(full_url))

    context.driver.get(full_url)

#------------------------------------------------------#

@then('I should be on the Teach Online page')
def on_each_online_page(context):
    expected_url = context.teach_online_page.url()
    assert expected_url == context.driver.current_url

@then('I should be on the home page')
def on_each_online_page(context):
    expected_url = context.home_page.url()
    assert expected_url == context.driver.current_url