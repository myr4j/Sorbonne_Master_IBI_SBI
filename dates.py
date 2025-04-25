from datetime import datetime, timedelta
from collections import Counter
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