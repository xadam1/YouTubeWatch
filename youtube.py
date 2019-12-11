import proxy
import link
import video
from selenium import webdriver
import threading
import time

if __name__ == "__main__":
    # driver = webdriver.Firefox(proxy.get_tor_profile())

    links = link.load("links.txt")

    # video.watch_video(driver, links[1])

    # for i in range(5):
    #     driver.get("http://www.icanhazip.com")
    #     print("CURRENT IP: ", end="")
    #     print(proxy.getIP(driver.page_source))
    #     proxy.switchIP()
    #     time.sleep(5)

    # driver.quit()

    class MyThread(threading.Thread):
        def __init__(self, name, count):
            threading.Thread.__init__(self)
            self.name = name
            self.count = count

        def run(self):
            print("Starting " + self.name)
            driver = webdriver.Firefox(proxy.get_tor_profile())
            video.watch_video(driver, links[self.count])
            driver.quit()
            print("Exiting " + self.name)
            # self.join()


    threads = set()
    for i in range(3):
        thread = MyThread(f"Thread-{i}", i)
        threads.add(thread)
        thread.start()
        time.sleep(5)
        proxy.switchIP()
