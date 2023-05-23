import time
import rumps

class PomodoroTimer(rumps.App):
    def __init__(self):
        self.pomodoro_length = 25
        self.timer = None
        self.reset_timer(None)

    @rumps.clicked("Start")
    def start_timer(self, _):
        if self.timer is None or not self.timer.is_alive():
            self.timer = rumps.Timer(self.update_timer, 1)
            self.timer.start()

    @rumps.clicked("Stop")
    def stop_timer(self, _):
        if self.timer is not None:
            self.timer.stop()

    @rumps.clicked("Reset")
    def reset_timer(self, _):
        super(PomodoroTimer, self).__init__("🍅")
        self.stop_timer(None)
        self.timer = None
        self.interval = self.pomodoro_length * 60

    def update_timer(self, _):
        self.interval -= 1
        if self.interval == 0:
            rumps.notification("Pomodoro Timer", "Time's up! 💪", "Take a break. ☕️")
            self.reset_timer(None)
        else:
            mins, secs = divmod(self.interval, 60)
            self.title = f"{mins:02d}:{secs:02d}"

if __name__ == '__main__':
    PomodoroTimer().run()

