import openai
from openai import OpenAI
import speech_recognition as sr
import os

api_key = os.environ.get('KEY')
def ai(userquery):
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {
                    "role": "user",
                    "content": userquery
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        generated_texts = [choice.message.content for choice in response.choices]
        res = ''.join(generated_texts)
        print("Alpha : ",res)
        return res

    except Exception as e:
        print(e) 
