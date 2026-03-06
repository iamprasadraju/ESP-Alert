import time

import network
from machine import mem32

import config
import rtc_ntp

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

rtc_ntp.setup_hourly_alarm()
