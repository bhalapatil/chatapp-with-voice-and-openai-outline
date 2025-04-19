from openai import OpenAI
import requests

openai_client = OpenAI()


def speech_to_text(audio_binary):
    base_url = "https://sn-watson-stt.labs.skills.network"
    api_url=base_url+ '/speech-to-text/api/v1/recognize'

    params = {

        'model' : 'en-US_Multimedia',
    }

    #set up the body of HTTP request

    body = audio_binary
    response = requests.post(api_url,params=params,data=audio_binary).json()

    test ='null'
    while bool(response.get('results')):
        print('speech to text response', response)
        text = response.get('results').pop().get('alternatives').pop().get('transcript')
        print('recognised text ' , text)
        return text

def text_to_speech(text, voice=""):
    base_url = "https://sn-watson-stt.labs.skills.network"
    api_url=base_url+ '/speech-to-text/api/v1/recognize'

    # add voice parameter in the api_url if the user has selected a particular voice
    if voice != "" and voice != "default":
        api_url += "&voice=" + voice

    #Set the headers for our HTTP request
    headers = {
        'Accept' : 'audio/wav' ,
        'Content-Type' : 'application/json',

    }

    #Set the body of the HTTP request
    json_data = {

        'text' :text
    }

    response = requests.post(api_url,headers=headers,json=json_data)
    print('text to speech response:' , response)
    return response.content

def openai_process_message(user_message):
    # set the prompt for the OpenAI Api
    prompt ="Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations "

    #call the OpenAI Api to process the prompt
    openai_response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role" : "system", "content" : prompt},
                {"role" : "user" , "content" : user_message}
        ],
        max_tokens=4000
    )

    print("openai response",openai_response)

    #parse the response to get the response message from the pr
    response_text = openai_response.choices[0].message.content
    return response_text


    

