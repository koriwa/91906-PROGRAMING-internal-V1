import tkinter as tk
from datetime import datetime, timedelta

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main app")

        self.timer_running = False
        self.start_time = None
        self.elapsed_time = timedelta()

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Helvetica", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, font=("Helvetica", 14), bg="#F44336", fg="white", padx=10, pady=5, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = datetime.now()
            self.update_timer()

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.elapsed_time += datetime.now() - self.start_time
            self.start_time = None

            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.timer_running:
            elapsed = self.elapsed_time + datetime.now() - self.start_time
            timer_str = str(elapsed).split('.')[0]  # Remove microseconds

            self.time_label.configure(text=timer_str)
            self.root.after(1000, self.update_timer)  # Update every second

root = tk.Tk()
timer_app = TimerApp(root)
root.mainloop()
