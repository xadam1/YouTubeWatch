import time
from proxy import *
from link import *

if __name__ == "__main__":
    driver = webdriver.Firefox(get_tor_profile())

    links = load("links.txt")

    for i in range(5):
        driver.get("http://www.icanhazip.com")
        print("CURRENT IP: ", end="")
        print(getIP(driver.page_source))
        switchIP()
        time.sleep(5)
