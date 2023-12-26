from configparser import ConfigParser

import google.generativeai as genai

config = ConfigParser()
config.read("credentials.ini")
API_KEY = config["API_KEY"]["google_api_key"]
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-pro")
chat = model.start_chat()


def response_generate(_question):
    res = chat.send_message(_question)
    return res.text
