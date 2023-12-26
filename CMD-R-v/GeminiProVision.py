from configparser import ConfigParser

import google.generativeai as genai
from PIL import Image

config = ConfigParser()
config.read("credentials.ini")
API_KEY = config["API_KEY"]["google_api_key"]
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-pro-vision")


def response_generate(_question, _location):
    res = None
    try:
        im = Image.open(_location)
        if _question == "":
            res = model.generate_content(im)
        else:
            res = model.generate_content([_question, im], stream=True)
        res.resolve()
    except Exception as e:
        print(f"{type(e).__name__}: {e.__dict__}")

    return res.text
