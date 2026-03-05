import urequests


def text_speech(text):
    t = text.replace(" ", "+")
    url = "http://tts-api.netlify.app/?text=" + t + "&lang=en"
    resp = urequests.get(url)
    with open("test.wav", "wb") as f:
        f.write(resp.content)
    resp.close()
    print("TTS downloaded!")
