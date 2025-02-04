import streamlit as st

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
    expander.text_area(label="Edit answer", value=p[1] + "This is the besst I can do")
    expander.checkbox("Choose to Download", key=p[0])


# This button will download all chats into pdf format.
st.button("Download")
