from datetime import datetime

class TimerModel:

    timerName = ""
    dtStart = ""
    dtStop = ""
    dtDuration = 0

    def __init__(self, _timerName):
        self.timerName = _timerName

    def start(self):
        dtDir = self.get_current_dt()
        self.dtStart = dtDir["dtNow"]
        print("starting timer [" + self.timerName + "], dt [" + dtDir["dtNowStr"] + "]")

    def stop(self):
        dtDir = self.get_current_dt()
        self.dtStop = dtDir["dtNow"]
        print("stopping timer [" + self.timerName + "], dt [" + dtDir["dtNowStr"] + "]")

    def duration(self):
        difference = self.dtStart - self.dtStop
        duration_in_s = difference.total_seconds()
        self.dtDuration = duration_in_s
        print("timer duration [" + duration_in_s + " (s)]")

    def get_current_dt(self):
        dtNow = datetime.now()
        dtNowStr = dtNow.strftime("%Y-%m-%d %H-%M-%S")

        return {
            "dtNow": dtNow,
            "dtNowStr": dtNowStr,
        }