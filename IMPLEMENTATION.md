### 1. Connect with wifi

### 2. Sync the RTC using ntp -> set to local time in device

 Indian ntp ```time.nplindia.org```

### 3. Implement Text to Speech (Offline)
[microTTS](https://github.com/Voinic/microtts)
[google unofficial TTS](https://tts-api.netlify.app/)


### Beep for every hour

- fetch time from ntp when connected to wifi
- use: rtc_alarm
- use: deep sleep func to save battery


```text
      Boot
        ↓
    Connect WiFi
        ↓
     Sync NTP
        ↓
    Calculate time until next hour
        ↓
    Deep sleep until next hour
        ↓
    Wake → Beep
        ↓
    Deep sleep 1 hour
```
