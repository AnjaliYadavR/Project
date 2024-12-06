from dotenv import load_dotenv
from pprint import pprint
import google.generativeai as genai
import os
import requests


def askQuery(query):
    genai.configure(api_key=os.getenv("API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(query)
    return response.text


# if __name__ == "__main__":
#     askQuery(input("Enter your query\n"))
