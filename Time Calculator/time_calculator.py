def add_time(start, duration, starting_day=""):
  # Split start time into hours, minutes, and time period (AM or PM)
  split_start = start.split()
  start_time = split_start[0].split(":")
  start_time_period =  split_start[1]

  # Convert time to 24 hour format
  if start_time_period == "PM":
    hours = int(start_time[0]) + 12
    start_time[0] = str(hours)

  # Split duration into hours and minutes
  duration_time = duration.split(":")

  # Add start time and duration time
  new_hours = int(start_time[0]) + int(duration_time[0])
  new_minutes = int(start_time[1]) + int(duration_time[1])

  if new_minutes > 60:
    hours_add = new_minutes // 60
    new_minutes -= hours_add * 60
    new_hours += hours_add

  days_add = 0
  if new_hours > 24 :
    days_add = new_hours // 24
    new_hours -= days_add * 24

  # Find AM and PM
  # Convert to 12-hour clock format
  if new_hours > 0 and new_hours < 12 :
    start_time_period = "AM"
  elif new_hours == 12 :
    start_time_period = "PM"
  elif new_hours > 12 :
    start_time_period = "PM"
    new_hours -= 12
  else : # new_hour == 0
    start_time_period = "AM"
    new_hours += 12    

  if days_add > 0 :
    if days_add == 1 :
      days_later = " (next day)"
    else :
      days_later = " (" + str(days_add) + " days later)"
  else :
    days_later = ""

  week_days = ("Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday")
 
  if starting_day:
    weeks = days_add // 7
    index = week_days.index(starting_day.lower().capitalize()) + (days_add - 7 * weeks)
    if index > 6:
      index -= 7
    day = ", " + week_days[index]
  else:
    day = ""

  if new_minutes > 9:
    new_time = str(new_hours) + ":" + str(new_minutes) + " " + start_time_period + day + days_later
  else:
    new_time = str(new_hours) + ":" + ("0" + str(new_minutes)) + " " + start_time_period + day + days_later

  return new_time