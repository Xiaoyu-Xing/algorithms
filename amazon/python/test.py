import schedule
import time
from datetime import datetime


class ScheduledJobController:
    def __init__(self):
        self.sequence = 0

    def get_and_update_sequence(self):
        print(f"Current job sequence {self.sequence}, time {datetime.now()}")
        ret = self.sequence
        self.sequence += 1
        return ret

    def __repr__(self):
        return str(self.get_and_update_sequence())


if __name__ == '__main__':
    controller = ScheduledJobController()
    schedule.every(10).seconds.do(print, controller)
    schedule.run_all()

    while controller.sequence <= 2:

        schedule.run_pending()
        time.sleep(1)
