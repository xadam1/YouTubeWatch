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


def getIP(source_code):
    tmp = str(source_code).split("<pre>")
    ip = tmp[1].split("</pre>")[0]
    return ip
