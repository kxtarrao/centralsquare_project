from color import Color
from day_of_week import DayOfWeek

from math import floor

# Determine the manufacture color of cars on a particular day ahead of initial day
# Input: Days away from initial day
# Output: Color of manufactured cars on input day
# Assumes: Initial Day = Monday = Red Car Day
def color_of_the_day(day_index):

    day_of_week = DayOfWeek(day_index % len(DayOfWeek) + 1)

    if day_of_week in [DayOfWeek.SATURDAY, DayOfWeek.SUNDAY]:
        return 'No Color'
    else:
        workday_index = day_index - 2*floor(day_index / len(DayOfWeek))
        color = Color(workday_index % len(DayOfWeek) + 1)
        return color.name.capitalize()