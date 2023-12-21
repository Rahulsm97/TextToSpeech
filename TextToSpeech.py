import pyttsx3

def get_available_voices():
    """
    Get a list of available voices.
    """
    voices = engine.getProperty('voices')
    return voices

def set_voice(voice_id):
    """
    Set the voice for speech synthesis.
    Args:
        voice_id (int): Index of the desired voice from the list of available voices.
    """
    voices = get_available_voices()
    engine.setProperty('voice', voices[voice_id].id)

def set_rate(rate):
    """
    Set the speech rate.
    Args:
        rate (int): Speech rate in words per minute.
    """
    engine.setProperty('rate', rate)

def set_pitch(pitch):
    """
    Set the speech pitch.
    Args:
        pitch (int): Speech pitch in Hz.
    """
    engine.setProperty('pitch', pitch)

def speak(text):
    """
    Convert text to speech.
    Args:
        text (str): The text to be spoken.
    """
    engine.say(text)
    engine.runAndWait()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get available voices and print them
voices = get_available_voices()
print("Available Voices:")
for i, voice in enumerate(voices):
    print(f"{i}. {voice.name}")

# Ask user to select a voice
voice_id = int(input("Select a voice by entering the corresponding index: "))
set_voice(voice_id)

# Ask user for speech rate a0nd pitch
rate = int(input("Enter speech rate (words per minute): "))
set_rate(rate)

pitch = int(input("Enter speech pitch (in Hz): "))
set_pitch(pitch)

# Ask user for text to convert to speech
text = input("Enter the text you want to convert to speech: ")

# Convert text to speech
speak(text)

# Clean up the engine resources
engine.quit()
