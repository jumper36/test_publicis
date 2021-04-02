# coding=utf-8
"""Google Web Browsing feature tests."""
from pages.result import GoogleResultPage
from pages.search import GoogleSearchPage
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)

# Scenario

scenario('../features/searching.feature', 'Basic Google Search')


# Given Steps

@given('the Google home pages is displayed')
def google_home(browser):
    browser.get(GoogleSearchPage.URL)


# When Steps

@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_page = GoogleSearchPage(browser)
    search_page.load()
    search_page.search(phrase)


# Then Steps

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    result_page = GoogleResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(phrase) > 0
    assert result_page.search_input_value() == phrase



# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
#
# # Constants
#
# GOOGLE_HOME = 'https://www.google.com/'
#
#
# # Fixtures
#
# @scenario('../features/searching.feature', 'Basic Google Search')
# def test_basic_google_search():
#     pass
#
#
# @pytest.fixture
# def browser():
#     b = webdriver.Chrome(executable_path=r'/my/absolute/driver/path/chromedriver')
#     b.implicitly_wait(10)
#     yield b
#     b.quit()
#
#
# # Given Steps
#
# @given('the Google home page is displayed')
# def ddg_home(browser):
#     browser.get(GOOGLE_HOME)
#
#
# # When Steps
#
# @when(parsers.parse('the user searches for "{phrase}"'))
# def search_phrase(browser, phrase):
#     search_input = browser.find_element_by_id('search_form_input_homepage')
#     search_input.send_keys(phrase + Keys.RETURN)
#
#
# # Then Steps
#
# @then(parsers.parse('results are shown for "{phrase}"'))
# def search_results(browser, phrase):
#     # Check search result list
#     # (A more comprehensive test would check results for matching phrases)
#     # (Check the list before the search phrase for correct implicit waiting)
#     links_div = browser.find_element_by_id('links')
#     assert len(links_div.find_elements_by_xpath('//div')) > 0
#     # Check search phrase
#     search_input = browser.find_element_by_id('search_form_input')
#     assert search_input.get_attribute('value') == phrase
#
