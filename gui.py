from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x500")
window.configure(bg="#9B93EF")

canvas = Canvas(
    window,
    bg="#9B93EF",
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    375.0,
    273.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    480.0,
    261.0,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=290.0,
    y=166.0,
    width=380.0,
    height=188.0
)

canvas.create_text(
    300.0,
    182.0,
    anchor="nw",
    text="Enter your message.....",
    fill="#000000",
    font=("Actor Regular", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=550.0,
    y=390.0,
    width=124.0,
    height=38.0
)

canvas.create_text(
    280.0,
    20.0,
    anchor="nw",
    text="STEGANOGRAPHY",
    fill="#000000",
    font=("Goldman Bold", 20 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=76.0,
    y=221.0,
    width=120.0,
    height=21.0
)

canvas.create_rectangle(
    120.0,
    168.0,
    170.0,
    218.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    65.0,
    78.0,
    anchor="nw",
    text="Encrypt your message here",
    fill="#000000",
    font=("Exo2 Bold", 25 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=640.0,
    y=463.0,
    width=140.0,
    height=37.0
)

canvas.create_text(
    190.0,
    469.0,
    anchor="nw",
    text="To Decrypt your message click here -->>",
    fill="#000000",
    font=("Goldman Bold", 20 * -1)
)

window.resizable(False, False)
window.mainloop()
