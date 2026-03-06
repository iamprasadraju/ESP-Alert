import time

import network
import urequests
from machine import DAC, Pin, mem32

RTC_CNTL_BROWN_OUT_REG = 0x3FF480D4
mem32[RTC_CNTL_BROWN_OUT_REG] = 0
print("brownout disabled!")

# --------- CONFIG ----------
WIFI_SSID = "Prasad"
WIFI_PASSWORD = "qwertyuiop"
DAC_PIN = 25  # Connect your speaker here

# --------- CONNECT WIFI ---------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print("Connecting to WiFi...")
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
print("\nConnected:", wlan.ifconfig())

# --------- DAC SETUP ----------
dac = DAC(Pin(DAC_PIN))


# --------- FETCH TTS FUNCTION ----------
def text_speech(text):
    t = text.replace(" ", "+")
    url = "http://tts-api.netlify.app/?text=" + t + "&lang=en"
    resp = urequests.get(url)
    with open("test.wav", "wb") as f:
        f.write(resp.content)
    resp.close()
    print("TTS downloaded!")


# --------- TEST ---------
text_speech("Hello! This is a TTS test.")
