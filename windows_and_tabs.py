from selenium import webdriver

# setting up multiple browser instances for more than one window
browser1 = webdriver.Chrome()
# browser2 = webdriver.Chrome()

browser1.get('http://techstepacademy.com/training-ground')
# browser2.get('http://google.com')

# executing javascript for opening another tab
browser1.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
browser1.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
browser1.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
browser1.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')

# switch between tabs using the switch_to function



