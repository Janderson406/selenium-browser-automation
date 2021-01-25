from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/trial-of-the-stones")

# Riddle of Stone
stone_input_locator = "//input[@id='r1Input']"
stone_button_locator = "//button[@id='r1Btn']"

stone_input_elem = browser.find_element_by_xpath(stone_input_locator)
stone_button_elem = browser.find_element_by_xpath(stone_button_locator)

stone_input_elem.send_keys("rock")
stone_button_elem.click()

password_locator = "//div[@id='passwordBanner']/h4"
password_elem = browser.find_element_by_xpath(password_locator)
stone_password = password_elem.get_attribute('innerHTML')

# # print("password: " + stone_password)

# Riddle of Secrets
secret_input_locator = "//input[@id='r2Input']"
secret_button_locator = "//button[@id='r2Butn']"

secret_input_elem = browser.find_element_by_xpath(secret_input_locator)
secret_button_elem = browser.find_element_by_xpath(secret_button_locator)

secret_input_elem.send_keys(stone_password)
secret_button_elem.click()

# Riddle of The Two Merchants (looked for name and then found wealth amount)
merchant_1_locator = "//b[contains(text(),'Jessica')]/../../p"
merchant_2_locator = "//b[contains(text(),'Bernard')]/../../p"

merchant_1_elem = browser.find_element_by_xpath(merchant_1_locator)
merchant_2_elem = browser.find_element_by_xpath(merchant_2_locator)

merchant_1_wealth = merchant_1_elem.get_attribute('innerHTML')
merchant_2_wealth = merchant_2_elem.get_attribute('innerHTML')

# # print("Jessica: $" + merchant_1_wealth)
# # print("Barnard: $" + merchant_2_wealth)

merchant_input_locator = "//input[@id='r3Input']"
merchant_button_locator = "//button[@id='r3Butn']"

merchant_input_elem = browser.find_element_by_xpath(merchant_input_locator)
merchant_button_elem = browser.find_element_by_xpath(merchant_button_locator)

if merchant_2_wealth > merchant_1_wealth:
    merchant_input_elem.send_keys("Barnard")
else:
    merchant_input_elem.send_keys("Jessica")

merchant_button_elem.click()

# Check Answers
check_answers_button_locator = "//button[@id='checkButn']"
check_answers_response_locator = ""

check_answers_button_elem = browser.find_element_by_xpath(check_answers_button_locator)
check_answers_button_elem.click()

trial_complete_locator = "//div[@id='trialCompleteBanner']/h4"
trial_complete_elem = browser.find_element_by_xpath(trial_complete_locator)

assert trial_complete_elem.get_attribute('innerHTML') == "Trial Complete"
