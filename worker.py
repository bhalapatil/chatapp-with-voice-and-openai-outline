from openai import OpenAI
import requests

openai_client = OpenAI()


def speech_to_text(audio_binary):
    base_url = "https://sn-watson-stt.labs.skills.network"
    api_url=base_rl+ '/speech-to-text/api/v1/recognize'

    params = {

        'model' : 'en-US_Multimedia',
    }

    #set up the body of HTTP request

    body = audio_binary
    response = requests.post(api_url,params=params,data=audio_binary).json()

    test ='null'
    while bool(response.get('results')):
        print('speech to text response', respone)
        test = response.get('results').pop().get('alternatives').pop().get('transcript')
        print('recognised text ' : text)
        return text

def text_to_speech(text, voice=""):
    return None


def openai_process_message(user_message):
    return None
