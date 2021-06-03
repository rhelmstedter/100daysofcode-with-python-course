from datetime import datetime, date, timedelta
import time

LAST_DAY_OF_SCHOOL = datetime(2022, 6, 16, 13, 35)
BREAKS_2021 = [
    date(2021, 9, 6),
    date(2021, 9, 16),
    date(2021, 10, 25),
    date(2021, 10, 26),
    date(2021, 10, 27),
    date(2021, 10, 28),
    date(2021, 10, 29),
    date(2021, 11, 11),
    date(2021, 11, 24),
    date(2021, 11, 25),
    date(2021, 11, 26),
    date(2021, 12, 20),
    date(2021, 12, 21),
    date(2021, 12, 22),
    date(2021, 12, 23),
    date(2021, 12, 24),
    date(2021, 12, 25),
    date(2021, 12, 27),
    date(2021, 12, 28),
    date(2021, 12, 29),
    date(2021, 12, 30),
    date(2021, 12, 31),
    date(2021, 12, 31),
    date(2022, 1, 17),
    date(2022, 2, 18),
    date(2022, 2, 21),
    date(2022, 4, 4),
    date(2022, 4, 5),
    date(2022, 4, 6),
    date(2022, 4, 7),
    date(2022, 4, 8),
    date(2022, 4, 15),
    date(2022, 5, 30),
]


def countdown():
    event_delta = LAST_DAY_OF_SCHOOL - datetime.now()
    print()
    print("\tTime until school is out for summer 2021:", end="\n\n")
    while (event_delta.days + event_delta.seconds) > 0:
        hours, remaining_delta = divmod(event_delta.seconds, 3600)
        mins, secs = divmod(remaining_delta, 60)
        timer = f"\t{event_delta.days:02d} days {hours:02d} hours {mins:02d} minutes {secs:02d} seconds"
        print(timer, end="\r")
        time.sleep(1)
        event_delta = LAST_DAY_OF_SCHOOL - datetime.now()

    print("School's out for summer!")


def school_days_left():
    pass


if __name__ == "__main__":

    countdown()
