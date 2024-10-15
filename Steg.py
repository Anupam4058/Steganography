import streamlit as st
import os
hexEnd = b'\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82'

def MsgEmbed(itext):
    global message 
    message = bytes(itext, 'utf-8') 
    with open("The jump.png",'ab') as f:
        f.write(message)
    return "Your message has been embeded"
def MsgRead():
    with open("The jump.png","rb") as r:
        content = r.read()
        offset = content.index(hexEnd)
        r.seek(offset + len(hexEnd))
        return r.read().decode("utf-8")
def MsgDelete():
    try:
        with open("The jump.png","rb+") as r:
            r.seek(-len(hexEnd),2)
            checkString = r.read()
            if(checkString != hexEnd):
                global message
                r.seek(-(len(message)),2)
                r.truncate()
                return "Message Deleted"
            else:
                return "No recent message to delete, embed a message using MsgEmbed or clear message with MsgClear."
    except Exception:
        return "No recent message to delete, embed a message using MsgEmbed or clear message with MsgClear."
def MsgClear():
    with open("The jump.png","rb+") as r:
        content = r.read()
        offset = content.index(hexEnd)
        r.seek(offset + len(hexEnd))
        start = r.seek(offset + len(hexEnd))
        end = r.seek(-1,2)+1
        r.seek(-(end-start),2)
        r.truncate()
    return "Message has been cleared"
    
def DestroyIMG():
    with open("The jump.png","rb+") as r:
        r.truncate()
    return "The image along with it's contents has been destroyed!"

finalText = "Let's get embedding"
col1, col2, col3,col4,col5 = st.columns(5)
with st.container():
    try:
        st.image("The jump.png")
    except:
        st.warning("The image is either destroyed or doesn't exist", icon="⚠️")
text = st.text_area(label = "Enter your message to embed", placeholder = "What's the message boss")
if st.button("Embed"):
    finalText = MsgEmbed(text)
with col1:
    if st.button("Read"):
        finalText = MsgRead()
# with col2:
#     if st.button("Delete"):
#         finalText = MsgDelete()
with col2:
    if st.button("Clear"):
        finalText = MsgClear()
with col3:
    if st.button("Destroy"):
        finalText = DestroyIMG()
st.success(finalText)