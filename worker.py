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
    # set the prompt for the OpenAI Api
    prompt ="Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations "

    #call the OpenAI Api to process the prompt
    openai_response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role" : "system", "content" : promt},
                {"role" : "user" , "content" : user_message}
        ],
        max_tokens=4000
    )

    print("openai response",openai_response)

    #parse the response to get the response message from the pr
    response_text = openai_response.choices[0].message.content
    return response_text


    

