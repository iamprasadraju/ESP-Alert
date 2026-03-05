import time

import network
from machine import mem32

import rtc_ntp
import tts
import config

# Disable brownout
RTC_CNTL_BROWN_OUT_REG = 0x3FF480D4
mem32[RTC_CNTL_BROWN_OUT_REG] = 0
print("brownout disabled!")


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print("Connecting to WiFi...")
    wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
print("\nConnected:", wlan.ifconfig())



TIMEZONE_OFFSET = 19800

month = {
    1: "JAN",
    2: "FEB",
    3: "MAR",
    4: "APR",
    5: "MAY",
    6: "JUN",
    7: "JUL",
    8: "AUG",
    9: "SEP",
    10: "OCT",
    11: "NOV",
    12: "DEC",
}

rtc_ntp.sync_time()
rtc_ntp.set_local_time(TIMEZONE_OFFSET)

print("Date Month Year Hour:Minutes:Seconds")

# Example usage
tts.text_speech("It is 3 o'clock")

"""
    while True:
        t = time.localtime()
        print("{} {} {} {:02d}:{:02d}:{:02d}".format(t[2], t[1], t[0], t[3], t[4], t[5]))
        time.sleep(1)

"""
