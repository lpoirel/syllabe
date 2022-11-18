import os
import time

from runner import Runner


class CLI(Runner):
    def print(self, text):
        print(text, end="", flush=True)

    def pause(self, duration):
        time.sleep(duration)

    def clear(self):
        print("\n")
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
