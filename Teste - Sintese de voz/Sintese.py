import pyttsx3

engine = pyttsx3.init()  # object creation

# RATE
rate = engine.getProperty("rate")  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty("rate", 200)  # setting up new voice rate

# VOLUME
volume = engine.getProperty("volume")  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty("volume", 1.0)  # setting up volume level  between 0 and 1

# VOICE
# getting details of current voice
# changing index, changes voices. o for male
 # changing index, changes voices. 1 for female
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}:")
    print(f" - ID: {voice.id}")
    print(f" - Name: {voice.name}")
    print(f" - Languages: {voice.languages}")
    print(f" - Gender: {voice.gender}")
    print(f" - Age: {voice.age}")
    print()
engine.setProperty('voice', voices[1].id)

engine.say("Perona? BAGULHO BOM MESMO :)")  # adding things to say
engine.say("My current speaking rate is " + str(rate))
engine.runAndWait()
engine.stop()

# Saving Voice to a file
# On Linux, make sure that 'espeak-ng' is installed
engine.save_to_file("""Spooky, scary skeletons
Send shivers down your spine
Shrieking skulls will shock your soul
Seal your doom tonight
Spooky, scary skeletons
Speak with such as screech
You'll shake and shudder in surprise
When you hear these zombies shriek

We're so sorry, skeletons
You're so misunderstood
You only want to socialize
(But I don't think we should)
'Cause spooky, scary skeletons
Shout startling, shrilly screams
They'll sneak from their sarcophagus
And just won't leave you be

Spirits, supernatural
Are shy, what's all the fuss?
Bags of bones seem so unsafe
It's semi-serious!
Spooky, scary skeletons
Are silly all the same
They'll smile and scrabble slowly by
And drive you so insane!

Sticks and stones will break your bones
They seldom let you snooze
Spooky, scary skeletons
Will wake you with a boo!""", "test.mp3")
engine.runAndWait()