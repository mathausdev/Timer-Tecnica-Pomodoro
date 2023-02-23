import tkinter as tk
import time
import threading
from datetime import datetime, timedelta

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
        
        self.schedule_button = tk.Button(self.master, text="Schedule a future timer", command=self.schedule_timer)
        self.schedule_button.pack(pady=10)

    def start_timer(self):
        try:
            time_in_minutes = int(self.entry.get())
            self.button.config(state=tk.DISABLED)
            threading.Thread(target=self.countdown
