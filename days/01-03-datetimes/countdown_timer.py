from datetime import datetime
import numpy as np
import time

LAST_DAY_OF_SCHOOL = datetime(2021, 6, 10, 11, 50, 0, 0)

def total_countdown():
    event_delta = LAST_DAY_OF_SCHOOL - datetime.now()
    while (event_delta.days + event_delta.seconds) > 0:
        hours, remaining_delta = divmod(event_delta.seconds, 3600)
        mins, secs = divmod(remaining_delta, 60)
        timer = f"\t{event_delta.days:02d} days {hours:02d} hours {mins:02d} minutes {secs:02d} seconds"
        print(timer, end="\r")
        time.sleep(1)
        event_delta = LAST_DAY_OF_SCHOOL - datetime.now()

    print("School's out for summer!")


def school_days():
    today = datetime.now()
    print(f"\tThere are {np.busday_count(today.date(), LAST_DAY_OF_SCHOOL.date()) -1} school days left in the 2020-2021 school year.")
    pass


print()
school_days()
print()
print("\tTime until school is out for summer 2021:", end="\n\n")
total_countdown()


