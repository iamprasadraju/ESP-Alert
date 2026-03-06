import time

import buzz
import machine
import ntptime
from machine import RTC

rtc = RTC()

ntptime.host = "time.nplindia.org"
TIMEZONE_OFFSET = 19800


def sync_time():
    try:
        ntptime.settime()
        print("NTP sync success")
    except:
        print("NTP sync failed")


def set_local_time(offset):
    utc = time.time()
    local = utc + offset
    tm = time.localtime(local)

    rtc.datetime((tm[0], tm[1], tm[2], tm[6], tm[3], tm[4], tm[5], 0))
    print("Local time set:", tm)


def next_hour_delay():
    t = rtc.datetime()

    minute = t[5]
    second = t[6]

    remaining_seconds = (60 - minute) * 60 - second
    return remaining_seconds * 1000


def hourly_task():
    print("Hourly task triggered!")
    buzz.beep()


def setup_hourly_alarm():
    if machine.reset_cause() != machine.DEEPSLEEP_RESET:
        sync_time()
        set_local_time(TIMEZONE_OFFSET)

        delay = next_hour_delay()
        print("Sleeping until next hour:", delay)

        machine.deepsleep(delay)

    else:
        hourly_task()

        machine.deepsleep(3600000)
