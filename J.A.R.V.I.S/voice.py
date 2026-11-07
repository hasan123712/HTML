import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import numpy as np

# Initialize JARVIS voice
engine = pyttsx3.init()

engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)


# JARVIS SPEAKING FUNCTION
def speak(text):

    engine.say(text)
    engine.runAndWait()


# JARVIS LISTENING FUNCTION
def listen(duration=4):

    print("JARVIS: Listening...")

    try:

        recording = sd.rec(
            int(duration * 16000),
            samplerate=16000,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        audio_data = np.int16(recording * 32767)

        recognizer = sr.Recognizer()

        audio = sr.AudioData(
            audio_data.tobytes(),
            16000,
            2
        )

        text = recognizer.recognize_google(audio)

        print("YOU:", text)

        return text.lower()

    except sr.UnknownValueError:

        print("JARVIS: I couldn't understand that.")
        return ""

    except sr.RequestError:

        print("JARVIS: Speech recognition connection failed.")
        return ""

    except Exception as error:

        print("MICROPHONE ERROR:", error)
        return ""

    # WAKE WORD DETECTION

def wait_for_wake_word():

    print("JARVIS: Waiting for 'Hey JARVIS'...")

    while True:

        text = listen(duration=2)

        if "hey jarvis" in text or "hey, jarvis" in text:

            print("JARVIS: Wake word detected!")

            speak("Yes, how may I help you?")

            return