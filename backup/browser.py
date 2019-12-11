import threading
from selenium import webdriver
from stem import Signal
from stem.control import Controller
import time
import proxy
import link


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting " + self.name)
        watch()
        print("Exiting " + self.name)
        self.join()


def watch():
    driver = webdriver.Firefox(proxy.get_tor_profile())
    driver.get("http://www.icanhazip.com")
    secs = 10
    print("Started watching", secs)
    time.sleep(secs)
    print("Done", secs)
    driver.quit()


threads = set()
for i in range(3):
    thread = MyThread(f"Thread-{i}")
    threads.add(thread)
    thread.start()
    time.sleep(5)
    proxy.switchIP()


print("Exiting Main Thread")
