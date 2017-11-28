from selenium.webdriver.common.by import By

class HomePageElements:

    MAIN_NAVIGATION_BAR = By.CSS_SELECTOR, 'div.c_header__inner'

    MAIN_NAV_BAR_ELEMENTS = {

        'logo site': {'type': 'css selector', 'locator': 'div.c_header__logo-container'},
        'categories': {'type': 'id', 'locator': 'dropdownButton'},
        'search for courses form': {'type': 'css selector', 'locator': 'form#searchbox'},
        'Udemy for business': {'type': 'link text', 'locator': 'Udemy for Business'},
        'Teach on Udemy': {'type': 'css selector', 'locator': 'div.dropdown--instructor > div:nth-child(1)'},
        'Cart icon': {'type': 'css selector', 'locator': 'div.styles--dropdown--29tlt'},
        'Log in': {'type': 'css selector', 'locator': 'div.dropdown:nth-child(4)'},
        'Sign up': {'type': 'css selector', 'locator': 'div.dropdown:nth-child(5)'}
    }

    FOOTER = By.TAG_NAME, 'footer'

    FOOTER_SECTION = {'upper footer' : {'type': 'css selector', 'locator': 'footer > div.container-fluid:nth-child(2)'},
                      'bottom footer' : {'type': 'css selector', 'locator': 'footer > div.container-fluid:nth-child(4)'}
                      }