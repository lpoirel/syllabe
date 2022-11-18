import time
import tkinter as tk

from runner import Runner


class GUI(Runner):
    def __init__(self, config):

        try:
            from ctypes import windll

            windll.shcore.SetProcessDpiAwareness(1)
        except ImportError:
            pass

        super().__init__(config)
        root = tk.Tk()
        root.title("syllabes")
        root.state("zoomed")

        self.displayed_text = tk.StringVar()

        tk.Label(
            root,
            textvariable=self.displayed_text,
            justify="left",
            anchor=tk.W,
            width=80,
            font=("Arial", config["font_size"]),
        ).pack()
        self.root = root

    def print(self, text):
        self.displayed_text.set(self.displayed_text.get() + text)
        self.root.update()

    def pause(self, duration):
        time.sleep(duration)

    def clear(self):
        self.displayed_text.set("")
        self.root.update()
