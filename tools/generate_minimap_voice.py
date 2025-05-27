from gtts import gTTS

tts = gTTS(text="MINIMAP LOOK MINIMAP", lang='en', slow=False)
tts.save("minimap_warning.mp3")

print("Alert voice saved as minimap_warning.mp3")
