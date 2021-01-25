from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/iframe-training')

# find and grab the iframe element
iframe = browser.find_element_by_css_selector("iframe")

# dig inside the iframe element for the paragraph that contains page text
browser.switch_to.frame(iframe)
welcome_text = browser.find_element_by_css_selector("div#block-ec928cee802cf918d26c div p")

assert welcome_text.text == "Welcome to the Training Ground. The ability find the right Web Elements is crucial to automation, " + \
                            "and a competent engineer can navigate the DOM swiftly and efficiently. Use this space to practice finding " + \
                            "different kinds of elements using CSS Selectors, XPATH, and other methods."

# hop out of the iframe and grab the title of the page
browser.switch_to.default_content()
title_text = browser.find_element_by_css_selector("div#block-5d3de848045889000188d389 div p")

assert title_text.text == " Training Ground for IFrames and traditional frames"
