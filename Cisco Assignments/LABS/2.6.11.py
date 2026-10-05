hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

timemin = (hour * 60 + mins + dura) % 60
timehour = (hour * 60 + mins + dura) // 60
print("The event ends at", timehour, "hours and", timemin, "minutes.")
print("the Event Ends at", timehour,":",timemin)
    