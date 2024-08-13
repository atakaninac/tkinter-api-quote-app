import tkinter as tk
import requests



#Getting the Quote from API
def get_data():
    data = requests.get(url="https://zenquotes.io/api/random").json()

    label_author.config(text=data[0]["a"])
    canvas.itemconfig(quote_text, text=data[0]["q"])


#Window
window = tk.Tk()
window.title("Quote of the Day")
window.config(padx=50, pady=50, bg="#379777")
window.resizable(False, False)

#Canvas
canvas = tk.Canvas(width=300, height=414, highlightthickness=0, bg="#379777")
img = tk.PhotoImage(file="./bubble.png")
canvas.create_image(150, 207, image=img)
quote_text = canvas.create_text(150, 207, text="Press the Button Below for Quote of The Day", width=250, font=("Arial", 22))

canvas.grid(row=0, column=0)

#Button
img1 = tk.PhotoImage(file="./author.png")
button = tk.Button(image=img1, highlightthickness=0, borderwidth=0, height=170, width=170, bg="#379777", command=get_data)

button.grid(row=1, column=0)

#Label
label_author = tk.Label(text="", font=("Arial", 22), bg="#379777")
label_author.grid(row=2, column=0)










window.mainloop()