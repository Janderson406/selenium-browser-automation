from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/trial-of-the-stones")

# Riddle of Stone
stone_input = browser.find_element_by_id('r1Input')
# the hash sign also works for identifying an id: 'button#r1Btn'
stone_answer_butn = browser.find_element_by_css_selector("button#r1Btn")
# there may be more than one h4 on the page
# so find h4 header under the div with the id of passwordBanner
stone_result = browser.find_element_by_css_selector("div#passwordBanner > h4")

# Riddle of Secrets
secrets_input = browser.find_element_by_css_selector("input[id='r2Input']")  # or "input#r2input"
secrets_answer_butn = browser.find_element_by_css_selector("button#r2Butn")

# Two Merchants
# Simple Approach: look for name using the wealth value
richest_merchant_name = browser.find_element_by_xpath("//p[text()='3000']/../span").text
merchant_input = browser.find_element_by_id('r3Input')
merchant_answer_butn = browser.find_element_by_css_selector('button#r3Butn')

check_butn = browser.find_element_by_css_selector("button[name='checkButn']")

complete_msg = browser.find_element_by_css_selector("div#trialCompleteBanner > h4")

#Run Script
stone_input.send_keys('rock')
stone_answer_butn.click()
password = stone_result.text

secrets_input.send_keys(password)
secrets_answer_butn.click()

merchant_input.send_keys(richest_merchant_name)
merchant_answer_butn.click()

check_butn.click()
assert complete_msg.text == "Trial Complete"
