import streamlit as st
from fpdf import FPDF


st.set_page_config(page_title="History", page_icon="👋")

st.sidebar.success("Download your Chats")

prompts = [
    (0, "What is pectin? "),
    (1, "What is protein? explain brief"),
    (2, "What is fat ??"),
]


def delete_record(i):
    return prompts.pop(i)


st.header("Your Gemini Chat History")


st.write("All your prompts and responses with Gemini will appear here !")


# We show the prompts as checkboxes.
# for p in prompts:
#     expander = st.expander(p)
#     expander.write(p + "This is the best I could come up with ")
#     expander.button("Delete", key=p + str(len(p)))

for p in prompts:
    expander = st.expander(p[1])
    expander.text_area(label="Edit answer", value=p[1] + "This is the best I can do")
    expander.checkbox("Choose to Download", key=p[0])


# This button will download all chats into pdf format.
if st.button("Generate PDF"):
    pdf_write = FPDF()
    pdf_write.add_page()
    pdf_write.set_font("Arial", size=15)
    pdf_write.cell(200, 10, txt="Here are your chats", ln=1, align="C")

    filename = "tests.pdf"

    pdf_write.output(filename)
