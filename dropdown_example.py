from selenium import webdriver
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

sel = browser.find_element_by_id('sel1')
my_select = Select(sel)

welcome_text = browser.find_element_by_css_selector("div#block-ec928cee802cf918d26c")