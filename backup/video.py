import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


def get_video_duration(driver):
    """
    @returns video duration and the duration (string) in seconds (int)
    """
    duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]
    duration = duration.text
    mins, seconds = duration.split(":")
    seconds = int(seconds) + int(mins) * 60
    return duration, seconds


def get_video_title(driver):
    """
    @returns video title as string
    """
    wait = WebDriverWait(driver, 10)
    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title yt-formatted-string"))).text
    return name


def watch_video(driver, url):
    """
    Function which gets all the info about video and plays it. Also displays current state.
    """
    driver.get(url)
    video_duration, video_seconds = get_video_duration(driver)
    video_title = get_video_title(driver)

    driver.find_element_by_id("movie_player").click()  # plays the vid
    time.sleep(1.5)
    print("Now Watching:\t{}".format(video_title))
    countdown(video_seconds, video_duration)
