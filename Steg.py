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
        print(r.read().decode("utf-8"))
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
                print("No recent message to delete, embed a message using MsgEmbed or clear message with MsgClear.")
    except Exception:
        print("No recent message to delete, embed a message using MsgEmbed or clear message with MsgClear.")
def MsgClear():
    with open("The jump.png","rb+") as r:
        content = r.read()
        offset = content.index(hexEnd)
        r.seek(offset + len(hexEnd))
        start = r.seek(offset + len(hexEnd))
        end = r.seek(-1,2)+1
        r.seek(-(end-start),2)
        r.truncate()
    print("Message has been cleared")
    
def DestroyIMG():
    with open("The jump.png","rb+") as r:
        r.truncate()
    print("The image along with it's contents has been destroyed!")
