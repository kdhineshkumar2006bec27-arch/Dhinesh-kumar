def convert_to_military_time(time_str):
    time_str = time_str.strip()
    period = time_str[-2:].upper()
    time_digits = time_str[:-2].strip()
    time_parts = time_digits.split(':')
    hours = int(time_parts[0])
    minutes = time_parts[1]
    seconds = time_parts[2]
    if period == "AM":
        if hours == 12:
            hours = 0
    elif period == "PM":
        if hours != 12:
            hours += 12
    if hours < 10:
        hours_str = "0" + str(hours)
    else:
        hours_str = str(hours)
        
    return f"{hours_str}:{minutes}:{seconds}"
print(convert_to_military_time("12:05:00AM"))  
print(convert_to_military_time("07:15:45PM"))  
