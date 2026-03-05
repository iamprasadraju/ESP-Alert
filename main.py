import time

import rtc_ntp

TIMEZONE_OFFSET = 19800

month = {
    "1": "JAN",
    "2": "FEB",
}


rtc_ntp.connect_wifi()
rtc_ntp.sync_time()
rtc_ntp.set_local_time(TIMEZONE_OFFSET)


while True:
    t = time.localtime()
    print(t)
    print("{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5]))
    time.sleep(1)
