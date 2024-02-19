miles = 10 * 0.6214
hours = (42 * 60 + 42) / 3600
pace = hours / miles
minutes_per_mile, seconds_per_mile = divmod(pace * 60, 1)
speed = miles / hours
print(f"Average pace: {int(minutes_per_mile)}:{int(seconds_per_mile):02d} per mile")
print(f"Average speed: {round(speed, 2)} miles per hour")
