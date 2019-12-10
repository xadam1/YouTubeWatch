import proxy
import link
import video
from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Firefox(proxy.get_tor_profile())

    links = link.load("links.txt")

    video.watch_video(driver, links[1])

    # for i in range(5):
    #     driver.get("http://www.icanhazip.com")
    #     print("CURRENT IP: ", end="")
    #     print(proxy.getIP(driver.page_source))
    #     proxy.switchIP()
    #     time.sleep(5)

    driver.quit()
