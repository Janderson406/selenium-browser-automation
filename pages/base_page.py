class BasePage(object):

    # BasePage does not have a URL because it's not a real page. It's an abstract class to be inherited from
    # We're making it a class attribute because if we tried to change its value later the url would be reassigned
    # to what it was inside of the init method
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
