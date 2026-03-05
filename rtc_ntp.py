import time

import machine
import network
import ntptime
from machine import RTC, mem32

import config

# Disable brownout
RTC_CNTL_BROWN_OUT_REG = 0x3FF480D4
mem32[RTC_CNTL_BROWN_OUT_REG] = 0

ssid = "Prasad"
password = "qwertyuiop"

ntptime.host = "time.nplindia.org"


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting WiFi...")
        wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

        timeout = 15
        while not wlan.isconnected() and timeout > 0:
            print(".", end="")
            time.sleep(1)
            timeout -= 1

        if not wlan.isconnected():
            print("WiFi failed. Restarting.")
            machine.reset()

    print("\nConnected:", wlan.ifconfig())


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
