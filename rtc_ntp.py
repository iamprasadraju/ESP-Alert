import time

import machine
import ntptime
from machine import RTC, mem32

import config

ntptime.host = "time.nplindia.org"


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

    rtc = RTC()
    rtc.datetime((tm[0], tm[1], tm[2], tm[6], tm[3], tm[4], tm[5], 0))
