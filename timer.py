import tkinter as tk
import time


class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Timer")

        self.timer_running = False
        self.time_left = 0

        # Create widgets
        self.title_label = tk.Label(master, text="mathausdev", font=("Arial", 10))
        self.title_label.pack()

        self.timer_label = tk.Label(master, text="00:00:00", font=("Arial", 50))
        self.timer_label.pack()

        self.time_entry_label = tk.Label(master, text="Enter time (in minutes):")
        self.time_entry_label.pack()

        self.time_entry = tk.Entry(master)
        self.time_entry.pack()

        self.name_entry_label = tk.Label(master, text="Enter name:")
        self.name_entry_label.pack()

        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        # Bind the window's protocol "WM_DELETE_WINDOW" to the quit function
        master.protocol("WM_DELETE_WINDOW", self.quit)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            minutes = int(self.time_entry.get())
            seconds = minutes * 60
            self.time_left = seconds

            self.name = self.name_entry.get()
            self.master.title(self.name)

            self.start_button.config(text="Pause", command=self.pause_timer)

            self.countdown()

    def countdown(self):
        if self.timer_running:
            hours = self.time_left // 3600
            minutes = (self.time_left // 60) % 60
            seconds = self.time_left % 60
            self.timer_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

            if self.time_left == 0:
                self.timer_running = False
                self.master.title("Timer")
                self.start_button.config(text="Start", command=self.start_timer)
                self.bring_to_front()

            else:
                self.time_left -= 1
                self.master.after(1000, self.countdown)

    def pause_timer(self):
        self.timer_running = False
        self.start_button.config(text="Resume", command=self.resume_timer)

    def resume_timer(self):
        self.timer_running = True
        self.start_button.config(text="Pause", command=self.pause_timer)
        self.countdown()

    def bring_to_front(self):
        self.master.attributes("-topmost", 1)
        self.master.attributes("-topmost", 0)

    def quit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
