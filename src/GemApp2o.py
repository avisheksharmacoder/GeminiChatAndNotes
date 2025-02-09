import streamlit as st
import google.generativeai as genai
import dotenv
import os
from pathlib import Path
from datetime import datetime
from pony import orm
from fpdf import FPDF


# response text.
gemini_response: str = ""

# response text splits for better UI.
response_splits = ["random", "_______"]

# response augmentation configurations.
response_configs = {
    "KISAS": "Keep it short and simple",
    "EIFPs": "Explain in points",
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


# Prompt augmentation.
# Prompt augmentation options column.
col1, col2 = st.columns(2)

# prompt augmentation 1.
# keep reply short and simple checkbox.
if col1.checkbox("Keep it short and simple "):
    # add it to the prompt, if checked.
    gemini_prompt += "\n" + response_configs["KISAS"]


# Prompt augmentation part 2.
# Explain in points.
if col2.checkbox("Explain in few points"):
    # add it to the prompt, if checked.
    gemini_prompt += "\n" + response_configs["EIFPs"]


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
    response_splits = gemini_response.split(".", 1)
    st.success(response_splits[0])

st.write(response_splits[1])

# we generate the pdf here silenty, using the current
# prompt, response and current date time, for the user to download
# just this prompt and response.
pdf_writer = FPDF()
pdf_writer.add_page()
pdf_writer.set_font("Arial", size=15)
pdf_writer.cell(200, 10, txt="Gemini Chats", ln=1, align="C")

# show the prompt,
pdf_writer.cell(200, 10, txt=gemini_prompt.capitalize(), ln=1, align="L")

# show the response.
pdf_writer.multi_cell(
    200,
    10,
    txt=gemini_response,
    align="L",
)

# This is the name of the pdf file, that will be saved.
filename = "tests.pdf"

# We temporarily write the file into local storage, then later
# reload the pdf file in rb format.
pdf_writer.output(filename)

# Once the pdf file is generated, open the file in rb format and
# generate the final download button, for the user to download
# the pdf file from the browser, to a specific PC location.
with open(Path("../src/" + filename), "rb") as pdf_raw:
    pdf_chats_byte_stream = pdf_raw.read()

    # we generate the final download button.
    st.download_button(
        label="Download into PDF",
        data=pdf_chats_byte_stream,
        file_name=filename,
        mime="application/octet-stream",
        icon="✔",
    )


# token details.
st.write("Your prompt token size is ", len(gemini_prompt.split(" ")))
st.write("Your prompt response size is ", len(gemini_response.split(" ")))
