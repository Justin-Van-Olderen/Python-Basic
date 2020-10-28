import time
import random

hour = random.randrange(0, 23)
minute = random.randrange(0, 60)
second = random.randrange(0, 60)


while (hour < 24):
    second += 1
    time.sleep(1)

    if (second >= 60):
        second = 0
        minute += 1

    if (minute >= 60):
        minute = 0
        hour += 1

    print(str(hour) + ":" + str(minute) + ":" + str(second))

    
