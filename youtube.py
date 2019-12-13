import proxy
from Watcher import Watcher
import time
from random import randint

if __name__ == "__main__":
    for _ in range(5):
        proxy.switchIP()
        watcher = Watcher()
        watcher.start()
        time.sleep(randint(5, 10))
