import streamlit as st
import google.generativeai as genai
import dotenv
import os
from pathlib import Path


def env_path() -> str:
    """
    return .env file path.
    """
    return Path("./keys/.env")


# models names.
gemini_models = {
    "Gemini 1.5 Flash v2": "gemini-1.5-flash-002",
    "Gemini 2.0 Flash Experimental": "gemini-2.0-flash-exp",
}

print(tuple(gemini_models.keys())[1])
# load env file.
# dotenv.load_dotenv(dotenv_path=env_path())
# KEY = os.getenv("GEMINI_API_KEY")
# print(KEY)

# # configure gemini api.
# genai.configure(api_key=KEY)

# # load all models.
# # g_models = genai.list_models()
# # for model in g_models:
# #     print(model.name)

# # load 1.5 flash 002
# gemini_model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp")

# generate response
# response = gemini_model.generate_content(
#     "what is a gemini model? keep it short to 30 words"
# )
# print(response.text)
