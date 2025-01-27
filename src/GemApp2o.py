import streamlit as st
import google.generativeai as genai
import dotenv
import os
from pathlib import Path


# response text.
gemini_response: str = ""

# response configurations.
response_configs = {
    "KISAS": False,
    "EIPs": False,
}

response_configs_values = {
    "KISAS": "Keep it short and simple",
    "EIPs": "Explain in points",
}

# models names.
gemini_models = {
    "1.5": "gemini-1.5-flash-002",
    "2.0": "gemini-2.0-flash-exp",
}


# return env path
def env_path() -> str:
    """
    return .env file path.
    """
    return Path("./keys/.env")


# laod the env file.
def api_key_from_env() -> str:
    dotenv.load_dotenv(dotenv_path=env_path())
    KEY = os.getenv("GEMINI_API_KEY")
    return KEY


# prompt with text
def ask_gemini_with_text(user_prompt, model_name) -> str:
    """
    call gemini API and get the response.
    """
    KEY = api_key_from_env()
    genai.configure(api_key=KEY)
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(user_prompt)
    return response.text


# prompt with image.
def ask_gemini_with_image() -> str:
    pass


# prompt with audio.
def ask_gemini_with_audio() -> str:
    pass


# Home page configurations for side bar.
# set page title and icon.
st.set_page_config(page_title="Gemini2.0", page_icon="👋")

# set page side bar message.
st.sidebar.success("Welcome to Gemini 2.0 chat")


# App heading.
st.header("Ask Gemini and Learn")


# checkbox for gemini 2.0 option.
gemini_model2_checked = st.checkbox(
    "Gemini 2.0 Flash Experimental",
    help="Generate the prompt using latest Gemini 2.0 model",
)


# gemini prompt text input.
gemini_prompt = st.text_input(
    label="Your query goes here",
    max_chars=500,
    help="Explain what you want, in simple words",
)


# keep reply short and simple checkbox.
if st.checkbox("Keep it short and simple "):
    response_configs["KISAS"] = True

    # add it to the prompt, if checked.
    gemini_prompt += response_configs_values["KISAS"]


# ask gemini button.
if st.button(label="Ask", type="primary"):
    if gemini_model2_checked:
        gemini_response = ask_gemini_with_text(
            gemini_prompt, model_name=gemini_models["2.0"]
        )
    else:
        gemini_response = ask_gemini_with_text(
            gemini_prompt, model_name=gemini_models["1.5"]
        )


# show the response.
st.write(gemini_response)


# show the download button.
st.button("Download into PDF", type="primary", icon="✔")


# token details.
st.write("Your prompt token size is ", len(gemini_prompt.split(" ")))
st.write("Your prompt response size is ", len(gemini_response.split(" ")))
