from model import Tamagotchi
from view import Visual
import tkinter as tk
import os
import threading


window = tk.Tk()
window.title("Tamagotchi")
window.geometry("250x250")
window.minsize(240, 240)
window.maxsize(260, 260)

tamagotchi = Tamagotchi()
icons = Visual()

# Initial Frame
tamagotchi_frame = tk.Frame(window)

Logo = tk.Label(tamagotchi_frame, text=icons.logo, font=("Courier", 5))
Logo.pack()

design_label = tk.Label(tamagotchi_frame, text=icons.tamagotchi[1], font=("Courier", 2))
design_label.pack()

status_label = tk.Label(tamagotchi_frame, text=tamagotchi.get_status())
status_label.pack()

feed_button = tk.Button(tamagotchi_frame, text="Feed", command=lambda: show_food_menu())
play_button = tk.Button(tamagotchi_frame, text="Play", command=tamagotchi.play)
sleep_button = tk.Button(tamagotchi_frame, text="Zzz", command=tamagotchi.sleep_prog)

feed_button.place(x=30, y=200)
play_button.place(x=97, y=200)
sleep_button.place(x=160, y=200)


# Food Frame
food_frame = tk.Frame(window)

hamburguer = tk.Label(food_frame, text=icons.food[0], font=("Courier", 1))
cake = tk.Label(food_frame, text=icons.food[1], font=("Courier", 1))
lasagna = tk.Label(food_frame, text=icons.food[2], font=("Courier", 1))

option1 = tk.Button(food_frame, text="Hamburguer", command=lambda: button1_click())
option2 = tk.Button(
    food_frame, text="Cake", command=lambda: show_tamagotchi(option2["text"])
)
option3 = tk.Button(
    food_frame, text="Lasagna", command=lambda: show_tamagotchi(option3["text"])
)

hamburguer.place(x=150, y=38)
cake.place(x=150, y=98)
lasagna.place(x=150, y=158)
option1.place(x=30, y=40)
option2.place(x=30, y=100)
option3.place(x=30, y=160)


# Show init Frame Function
def show_tamagotchi(food_option):
    tamagotchi_frame.place(x=0, y=0, width=250, height=250)
    food_frame.place_forget()
    tamagotchi.feed(food_option)
    print("Tamagotchi alimentado con", food_option)


# Show food Frame Function
def show_food_menu():
    tamagotchi_frame.place_forget()
    food_frame.place(x=0, y=0, width=250, height=250)
    print("Menú Comida Abierto")


# Update Status
def update_tamagotchi():
    tamagotchi.update()
    status_label.config(text=tamagotchi.get_status())
    window.after(2000, update_tamagotchi)


update_tamagotchi()


# Principal animation
def animate(index):
    design_label.config(text=icons.tamagotchi[index])
    index = (index + 1) % len(icons.tamagotchi)
    window.after(500, animate, index)


animate(0)


# Button function
def play_alert_sound():
    script = 'osascript -e "beep"'
    os.system(script)


def button1_click():
    threading.Thread(target=play_alert_sound()).start()
    threading.Thread(show_tamagotchi(option1["text"])).start()


tamagotchi_frame.place(x=0, y=0, width=250, height=250)


window.mainloop()
