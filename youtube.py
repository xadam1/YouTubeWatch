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


def getIP(source_code):
    tmp = str(source_code).split("<pre>")
    ip = tmp[1].split("</pre>")[0]
    return ip


def load_links(path):
    file = open(path, 'r')
    contents = file.readlines()
    urls = []
    for link in contents:
        urls.append(link.strip('\n'))
    print("Loaded links: ", end="")
    print(urls)
    file.close()

    return urls


if __name__ == "__main__":
    # driver = webdriver.Firefox(get_tor_profile())

    links = load_links("links.txt")

    # for i in range(5):
    #     driver.get("http://www.icanhazip.com")
    #     print("CURRENT IP: ", end="")
    #     print(getIP(driver.page_source))
    #     switchIP()
    #     time.sleep(5)
