import streamlit as st
from fpdf import FPDF
from pathlib import Path
import os
import sqlite3


# we set page configuration for Chat History page, with page title.
st.set_page_config(page_title="History", page_icon="👋")

# we set the sidebar message for History Tab in the app.
st.sidebar.success("Download your Chats")

# We check database file is present or not. If file is not available
# then this variable is set to False. Else set to True.
db_file_present: bool = False


# All code related to database.
# We have to create a database file to store the prompts.
# and responses.
# We check if sqlite db is in the folder or not.
def sqlite_db_exists(filename: str, folder_path: str) -> bool:
    file_path = Path(folder_path + "\\" + filename)
    print(file_path)
    return file_path.exists()


# This is the sqlite database file name.
db_filename = "chat.db"

# we bind the database that is already created from the GemChatApp file.
# We find the current directory of the active python file.
current_dir = Path.cwd()

# We generate the sqlite database file location.
db_dir = str(current_dir) + "\\sqlite_db\\"

# To check if the database file already exists in the folder or not.
if sqlite_db_exists(db_filename, db_dir):
    print("Databse file exists")
    db_file_present = True
else:
    print("Databse file not found")
    db_file_present = False


# The header for the History Page.
st.header("Your Gemini Chat History")

# The subheading for the History Page.
st.write("All your prompts and responses with Gemini will appear here !")

# We read the database and render the chats below in expanders.
# User can edit the chats as per their usage.
# test button to show streamlit expanders.
if st.button("Generate Expanders"):
    # To generate the database file path and connect to the database.
    db_filepath = Path(db_dir + "\\" + db_filename)

    # To connect to the database and create the database connection.
    sqlite_db_conn = sqlite3.connect(db_filepath)

    # To generate the sqlite database cursor to execute queries.
    sqlite_db_cursor = sqlite_db_conn.cursor()

    # To get all the records from the sql table Chat.
    sqlite_db_cursor.execute(
        """
        SELECT * FROM Chat
        """
    )

    # fetch all the records from the cursor.
    chats = sqlite_db_cursor.fetchall()

    # render the expanders for every chat. The user can see the contents of the chat
    # and decide whether to redit the content or not.
    for row in chats:
        expander = st.expander(row[1])
        expander.text_area(label="Edit answer", value=row[2])
        expander.checkbox("Choose to Download", key=row[0])


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
