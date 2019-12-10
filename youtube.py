import time
from selenium import webdriver
from stem import Signal
from stem.control import Controller


def switchIP():
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)


def get_tor_profile():
    tor_profile = webdriver.FirefoxProfile()
    tor_profile.set_preference('network.proxy.type', 1)
    tor_profile.set_preference('network.proxy.socks', '127.0.0.1')
    tor_profile.set_preference('network.proxy.socks_port', 9150)
    return tor_profile


driver = webdriver.Firefox(get_tor_profile())

for i in range(5):
    driver.get("http://www.icanhazip.com")
    switchIP()
    time.sleep(5)
