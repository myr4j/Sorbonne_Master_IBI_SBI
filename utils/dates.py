import calendar
from collections import Counter
from datetime import datetime, timedelta
from typing import Union



def mois_cine(date: Union[str | datetime]) -> int:

    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")

    day_of_week = date.weekday()

    # Calculate the start and end dates of the sem_cine
    if day_of_week < 2:  # Monday, Tuesday
        start_date = date - timedelta(days=(day_of_week + 5))  # Previous Wednesday
    else:
        start_date = date - timedelta(days=(day_of_week - 2))  # Current Wednesday

    # Store all dates from start_date to end_date in a list
    dates = [start_date + timedelta(days=i) for i in range(7)]

    # Count the occurrences of each month
    month_occurrences = Counter(date.month for date in dates)
    year_occurrences = Counter(date.year for date in dates)

    # Determine the month to which the sem_cine belongs
    month = month_occurrences.most_common(1)[0][0]
    year = year_occurrences.most_common(1)[0][0]
    # Return the result in the YYMM format
    return int(f"{year % 100:02}{month:02}")


def sem_cine_inv(
        date: datetime | str,
        date_separator: str = "-",
) -> int:

    if isinstance(date, str):
        date = datetime.strptime(date, f"%Y{date_separator}%m{date_separator}%d")

    week = week_number(date, date_separator)
    year = date.year
    month = date.month

    if week >= 52 and month == 1:
        year -= 1

    if week == 1 and month == 12:
        year += 1

    return year % 100 * 100 + week


def week_number(date: datetime | str, separator: str = "-") -> int:

    if isinstance(date, str):
        date = datetime.strptime(date, f"%Y{separator}%m{separator}%d")

    # Sets up january 1st and december 31st date times
    jan1st = datetime(year=date.year, month=1, day=1)
    dec31st = datetime(year=date.year, month=12, day=31)

    # Getting their day : iso-weekday monday = 1; sunday = 7
    jan1st_day = jan1st.isoweekday()
    dec31st_day = dec31st.isoweekday()

    # Gets to the closest wednesday from the january 1st.
    # It is actually the wednesday of the first vague of the year
    year_first_wed = jan1st
    sign = -1 if 3 <= jan1st_day <= 6 else 1
    while year_first_wed.isoweekday() != 3:
        year_first_wed += timedelta(days=1 * sign)

    # can be negative
    time_elapsed = date - year_first_wed

    # num is a number between 0 and 53 included
    # All the values between are good but the extreme must be checked
    if (num := time_elapsed.days // 7 + 1) == 53:
        # Only possible if the first or last day of year is Saturday
        return num if jan1st_day == 6 or dec31st_day == 6 else 1
    elif num == 0:  # time_elapsed is negative
        # Is equal to the last number of last year, which can be 52 or 53
        # 53 if Jan 1st is sunday => implies than last year Dec 31st is saturday therefore 53 weeks (see previous point)
        # 53 if Jan 1st is monday and last year is leap => implies than last year Jan 1st is saturday therefore 53 weeks (see previous point)
        # 52 for any other case
        return (
            53
            if (calendar.isleap(jan1st.year - 1) and jan1st_day == 1) or jan1st_day == 7
            else 52
        )
    else:
        return num
