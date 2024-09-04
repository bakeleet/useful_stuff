from subprocess import check_output

def get_uptime_array():
    return check_output(["uptime"]).split()  # whitespaces as a delimiter

def str2dict(str):
    return {'hour': int(str.split(':')[0]), 'minute': int(str.split(':')[1])}

def dict2str(dict):
    if len(str(dict['minute'])) == 1:
        return "{0}:0{1}".format(dict['hour'], dict['minute'])
    else:
        return "{0}:{1}".format(dict['hour'], dict['minute'])

def get_current_time_str():
    uptime_cmd_output = get_uptime_array()
    return uptime_cmd_output[0]

def get_current_time_dict():
    return str2dict(get_current_time_str())

def get_up_time_str():
    uptime_cmd_output = get_uptime_array()
    up_time = uptime_cmd_output[2]
    if up_time.find(",") >= 0:
        up_time = up_time[:-1]  # removing comma (",") in the end if it exists
    elif uptime_cmd_output[3].find("hour") >= 0 or uptime_cmd_output[3].find("hrs") >= 0:
        up_time = dict2str({'hour': up_time, 'minute': 0})
    elif uptime_cmd_output[3].find("min") >= 0:
        up_time = dict2str({'hour': 0, 'minute': up_time})
    return up_time

def get_up_time_dict():
    return str2dict(get_up_time_str())

def how_much_work_time_left(up_time):
    left_hour = 8 - up_time['hour']
    left_minute = 0 - up_time['minute']
    if left_hour > 0 and left_minute != 0:
        left_hour -= 1
        left_minute += 60
    return {'hour': left_hour, 'minute': left_minute}

def calculate_home_time(current_time, up_time):
    home_hour = current_time['hour'] + (7 - up_time['hour'])
    home_minute = current_time['minute'] + (60 - up_time['minute'])
    if home_minute >= 60:
        home_hour += 1
        home_minute -= 60
    return {'hour': home_hour, 'minute': home_minute}

def format_hours_minutes_str(time):
    hour_str = "hours" if time['hour'] != 1 else "hour"
    minute_str = "minutes" if time['minute'] != 1 else "minute"
    return {'hour': hour_str, 'minute': minute_str}

def format_time_str(time):
    time_str = format_hours_minutes_str(time)
    if time['hour'] == 0:
        return "only {0} {1}".format(time['minute'], time_str['minute'])
    elif time['minute'] == 0:
        return "{0} {1}".format(time['hour'], time_str['hour'], time['minute'], time_str['minute'])
    else:
        return "{0} {1} and {2} {3}".format(time['hour'], time_str['hour'], time['minute'], time_str['minute'])

def whenhome(up_time):
    if up_time['hour'] >= 8:
        up_time_str = format_time_str(up_time)
        print("GO HOME!\nIt's {0} and you're working {1}.".format(get_current_time_str(), up_time_str))
    else:
        current_time = get_current_time_dict()
        home_time = calculate_home_time(current_time, up_time)
        left_time = how_much_work_time_left(up_time)
        work_time_str = format_time_str(up_time)
        left_time_str = format_time_str(left_time)
        print("Stay up to {0}!\nYou are {1} at work, so {2} left.".format(dict2str(home_time), work_time_str, left_time_str))

if __name__ == '__main__':
    whenhome(get_up_time_dict())
