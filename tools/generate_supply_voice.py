from gtts import gTTS

# Change this text if you want a different message
text = "Supply block incoming. Build now."

# Generate the mp3
tts = gTTS(text=text, lang='en', slow=False)
tts.save("supply_warning.mp3")

print("Voice alert saved as supply_warning.mp3")
