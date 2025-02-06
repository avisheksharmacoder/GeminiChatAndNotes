import streamlit as st
from fpdf import FPDF
from pathlib import Path

# we set page configuration for Chat History page, with page title.
st.set_page_config(page_title="History", page_icon="👋")

# we set the sidebar message for History Tab in the app.
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


for p in prompts:
    expander = st.expander(p[1])
    expander.text_area(label="Edit answer", value=p[1] + "This is the best I can do")
    expander.checkbox("Choose to Download", key=p[0])


# To download the chats, we first generate the pdf. This button
# when clicked, generates the PDF from the gemini chats.
if st.button("Generate PDF"):
    pdf_writer = FPDF()
    pdf_writer.add_page()
    pdf_writer.set_font("Arial", size=15)
    pdf_writer.cell(200, 10, txt="Here are your chats", ln=1, align="C")

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
            label="Download Final File",
            data=pdf_chats_byte_stream,
            file_name=filename,
            mime="application/octet-stream",
        )
