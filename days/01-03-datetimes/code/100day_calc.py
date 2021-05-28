from datetime import date, datetime, timedelta
import time

START_DATE = date(2021, 5, 25)
duration = timedelta(days=100)







def countdown():
    event_delta = LAST_DAY_OF_SCHOOL - datetime.now()
    print()
    print("\tTime until school is out for summer 2021:", end="\n\n")
    while event_delta.seconds >0:
        hours, remaining_delta = divmod(event_delta.seconds, 3600)
        mins, secs = divmod(remaining_delta, 60)
        timer = f"\t{event_delta.days:02d} days {hours:02d} hours {mins:02d} minutes {secs:02d} seconds"
        print(timer, end="\r")
        time.sleep(1)
        event_delta = LAST_DAY_OF_SCHOOL - datetime.now()

    print("School's out for summer!")
