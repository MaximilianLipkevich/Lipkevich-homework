weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

weekdaysDict = {number + 1: day for (number, day) in enumerate(weekdays)}
reverseWeekdaysDict = {day: number + 1 for (number, day) in enumerate(weekdays)}

print(weekdaysDict)
print(reverseWeekdaysDict)