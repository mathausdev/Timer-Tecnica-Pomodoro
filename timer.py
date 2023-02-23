import tkinter as tk
import time
import threading

class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer")
        self.master.geometry("300x200")
        self.master.resizable(False, False)
        
        self.label1 = tk.Label(self.master, text="Enter time in minutes:")
        self.label1.pack(pady=10)
        self.entry = tk.Entry(self.master, width=10)
        self.entry.pack(pady=10)
        
        self.button = tk.Button(self.master, text="Start Timer", command=self.start_timer)
        self.button.pack(pady=10)
        
        self.label2 = tk.Label(self.master, text="")
        self.label2.pack(pady=10)
        
        self.label3 = tk.Label(self.master, text="")
        self.label3.pack(pady=10)

    def start_timer(self):
        try:
            time_in_minutes = int(self.entry.get())
            self.button.config(state=tk.DISABLED)
            threading.Thread(target=self.countdown, args=(time_in_minutes,)).start()
        except ValueError:
            self.label2.config(text="Invalid input. Please enter a valid integer.", fg="red")
            
    def countdown(self, time_in_minutes):
        start_time = time.time()
        end_time = start_time + (time_in_minutes * 60)
        while time.time() < end_time:
            remaining_time = int(end_time - time.time())
            mins, secs = divmod(remaining_time, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            self.label2.config(text=f"Time Remaining: {time_format}")
            time.sleep(1)
        self.label2.config(text="Time's up!", fg="red")
        self.button.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
