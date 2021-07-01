import myresearch


def main():
    myresearch.init()
    print("Weather research for Seattle, 2014-2015")
    print()

    print("The hottest 5 days:")
    days = myresearch.hot_days()
    for i, day in enumerate(days[:5]):
        print(f"{i+1}. {day.actual_max_temp} F on {day.date}")
    print()

    print("The coldest 5 days:")
    days = myresearch.cold_days()
    for i, day in enumerate(days[:5]):
        print(f"{i+1}. {day.actual_min_temp} F on {day.date}")
    print()

    print("The wettest 5 days:")
    days = myresearch.wet_days()
    for i, day in enumerate(days[:5]):
        print(f"{i+1}. {day.actual_precipitation}\" on {day.date}")
    print()



if __name__ == "__main__":
    main()
