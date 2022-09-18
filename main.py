# standard lib
from time import sleep

# https://pypi.org/project/webdriver-manager/
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from screeninfo import get_monitors

"""
TODO
[ ] send opener message to new match list
[ ] add nlp chatbot for replies
[ ] add attractiveness decision network for swipe rule
[ ] log success of openers 
[ ] log general metrics, no. matches, etc.
[ ] nudge dead matches after x interval
"""

TINDER_LOGIN_XPATH = "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]"
"""
FACEBOOK_LOGIN_XPATH = (
    "/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button"
)"""
FACEBOOK_LOGIN_XPATH = (
    "/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button"
)
FACEBOOK_LOGIN_CONFIRMATION_XPATH = "/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]"


class TinderBot:
    def __init__(self):
        last_monitor = self.get_last_monitor_position()
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        self.set_window_position(last_monitor.x, last_monitor.y)

    def get_last_monitor_position(self):
        monitors = get_monitors()
        last_monitor = monitors[-1]

        return last_monitor

    def set_window_position(self, x, y):
        self.driver.set_window_position(x, y)

    def login_to_tinder(self):

        # open tinder in browser
        self.driver.get("https://tinder.com/")
        sleep(2)

        # click login button
        login = self.driver.find_element(By.XPATH, TINDER_LOGIN_XPATH,)
        login.click()
        sleep(1)

        # choose facebook auth
        self.driver.find_element(
            By.XPATH, FACEBOOK_LOGIN_XPATH,
        )
        login.click()
        sleep(5)


# def login_to_tinder(driver):


def main():

    bot = TinderBot()
    bot.login_to_tinder()


if __name__ == "__main__":
    main()
