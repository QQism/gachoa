def estimate_time(content):
    word_count = len(content.split(' '))
    wpm = 200.0 # words per minute
    reading_time = word_count / wpm
    reading_seconds = int((reading_time % 1) * 60)
    reading_minutes = int(reading_time - (reading_time % 1))

    estimate_reading_time = ''
    if reading_minutes == 0:
        estimate_reading_time = str(reading_seconds) + ' sec'
    elif reading_seconds == 0:
        estimate_reading_time = str(reading_minutes) + ' min '
    else:
        estimate_reading_time = str(reading_minutes) + ' min ' + str(reading_seconds) + ' sec'

    return estimate_reading_time
