import proxy
from Watcher import Watcher
import time
from random import randint

if __name__ == "__main__":
    while True:
        try:
            watchers_count = int(input("Number of bots: "))
            if watchers_count < 1:
                raise ValueError
            break
        except ValueError as e:
            print("Somár, číslo veď...")

    for _ in range(watchers_count):
        proxy.switchIP()
        watcher = Watcher()
        watcher.start()
        time.sleep(randint(5, 10))
