import os
hexEnd = b'\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82'
def MsgEmbed():
    global message 
    inputString = input("Give an input: ")
    message = bytes(inputString, 'utf-8') 
    with open("The jump.png",'ab') as f:
        f.write(message)

def MsgRead():
    with open("The jump.png","rb") as r:
        content = r.read()
        offset = content.index(hexEnd)
        r.seek(offset + len(hexEnd))
        if(r.read() == b''):
            print("No message to print")
        else:
            print(r.read())
def MsgDelete():
    try:
        with open("The jump.png","rb+") as r:
            r.seek(-len(hexEnd),2)
            checkString = r.read()
            if(checkString != hexEnd):
                global message
                r.seek(-(len(message)),2)
                r.truncate()
                print("Message Deleted")
            else:
                print("No message to delete, embed a message using MsgEmbed or clear messaeg with MsgClear.")
    except:
        print("You must embed a string to clear it.")
def MsgClear():
    with open("The jump.png","rb+") as r:
        r.seek(-len(hexEnd),2)
        checkString = r.read()
        if(checkString != hexEnd):
            content = r.read()
            offset = content.index(hexEnd)
            start = r.seek(offset + len(hexEnd))
            end = r.seek(-1,2)+1
            r.seek(-(end-start),2)
            r.truncate()
            print("Message has been cleared!")
        else:
            print("No Message to delete, embed a message using MsgEmbed")
MsgDelete()