import proxy
import links
from IPAddressError import IPAddressError
import threading
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Watcher(threading.Thread):
    """
    Class Watcher works on a base of thread
    Represents a browser
    """

    video_links = links.load("links.txt")
    ip_addresses = set()

    def __init__(self):
        threading.Thread.__init__(self)
        self.driver = webdriver.Firefox(proxy.get_tor_profile())
        self.driver.minimize_window()
        self.ip = ""

    def run(self):
        """
        Basically main function
        Runs infinitely. Each cycle a driver gets new IP address.
        """
        while True:
            try:
                self.set_ip()

                if self.ip in self.ip_addresses:
                    raise IPAddressError

                self.ip_addresses.add(self.ip)
                self.watch_video(self.video_links[randint(0, len(self.video_links) - 1)])

            # Occurs if the IP address is already being used
            except IPAddressError:
                print("New IP Address Needed", end="\t")

            # Occurs if the same video is played too frequently.
            # Throws method set_ip()
            except IndexError:
                print("RIP ANTIBOT", end="\t")
                self.driver.quit()
                self.driver = webdriver.Firefox(proxy.get_tor_profile())
                self.driver.minimize_window()
            except Exception as e:
                print(e, end="\t")
            finally:
                self.ip_addresses.discard(self.ip)
                print(f"{self.ip} ended.\n")

            time.sleep(randint(8, 13))
            proxy.switchIP()

    def get_video_duration(self):
        """

        @return: video duration and the duration (string) in seconds (int)
        """

        duration = self.driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]
        duration = duration.text
        mins, seconds = duration.split(":")
        seconds = int(seconds) + int(mins) * 60
        return duration, seconds

    def get_video_title(self):
        """

        @return: video title as string
        """

        wait = WebDriverWait(self.driver, 10)
        name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title yt-formatted-string"))).text
        return name

    def watch_video(self, url):
        """
        Function which gets all the info about video and plays it. Also displays current state.
        """

        self.driver.get(url)
        video_duration, video_seconds = self.get_video_duration()

        self.driver.find_element_by_id("movie_player").click()  # plays the vid
        time.sleep(1.5)
        print(f"{self.ip} \t\t {self.get_video_title()} \t\t {video_duration}\n")
        time.sleep(video_seconds)
        # self.countdown(video_seconds, video_duration)

    def set_ip(self):
        """
        Sets current ip address
        Throws IndexError if antispam bot pops out
        """

        self.driver.get("http://www.icanhazip.com")
        tmp = str(self.driver.page_source).split("<pre>")
        ip = tmp[1].split("</pre>")[0]
        ip = ip.rsplit(".", 1)[0]
        self.ip = ip

    @staticmethod
    def countdown(t, duration):
        """
        Simple countdown-timer on 't' amount of seconds
        """
        while t:
            mins, secs = divmod(t, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            print("Remaining:\t\t", time_format, "/", duration, end='\r')
            time.sleep(1)
            t -= 1
