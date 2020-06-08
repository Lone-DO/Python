import timeago, datetime

def ConvertTime(time):
    now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

    date = datetime.datetime.now() 

    return (timeago.format(date, now))