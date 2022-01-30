days_of_the_week = [
  'Sunday',
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday',
]

def add_time(start, duration, *args):
  
  [start_time, start_meridiem] = start.split(" ")
  [start_hour, start_minute] = start_time.split(":")
  [duration_hour, duration_minute] = duration.split(":")

  next_days = 0

  total_minute = int(start_minute) + int(duration_minute)
  total_hour = int(start_hour) + int(duration_hour)
  if total_minute > 60:
    total_hour = total_hour + 1
    total_minute = total_minute % 60
  if total_minute < 10:
    total_minute = f"0{total_minute}"
    
  if total_hour >= 12:
    t, r = divmod(total_hour, 12)
    total_hour = r if r else total_hour // t

    if start_meridiem == "PM":
      next_days = ((t-1) // 2) + 1
    else:
      next_days = t // 2

    if t > 0 and t % 2 != 0:
      start_meridiem = "AM" if start_meridiem == "PM" else "PM"

  new_time = str(total_hour) + ":" +str(total_minute) + f" {start_meridiem}"

  if args:
    day = args[0].title()
    if next_days > 0:
      index = days_of_the_week.index(day)
      index += next_days % 7
      if index > 6:
        index = index - 7
      day = days_of_the_week[index]

    new_time += f", {day}"

  if next_days == 1:
    new_time += " (next day)"
  elif next_days > 1:
    new_time += f" ({next_days} days later)"

  return new_time
