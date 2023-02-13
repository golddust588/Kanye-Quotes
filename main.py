from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])
    print(data)


window = Tk()
window.title("Kanye Says... Press me to know the truth!")
window.config(padx=50, pady=50)

canvas = Canvas(width=600, height=545)
background_img = PhotoImage(file="background.png")
canvas.create_image(300, 272, image=background_img)
quote_text = canvas.create_text(300, 272, text="Kanye Quote Goes HERE", width=500, font=("Arial", 30, "bold"),
                                fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
