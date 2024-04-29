import tkinter as tk
from PIL import Image, ImageTk
import os
import random 
from tkinter import filedialog
import shutil


random_displayed = False
choice_displayed = False
current_photo_labels = []

main_directory = os.path.dirname(__file__)
root = tk.Tk()
                 


def folder_existing():
    folder_location = f"{main_directory}/photos"
    if not os.path.exists(folder_location) :
        os.makedirs("photos")


def draw():
    global random_displayed
    global current_photo_labels
    photo_destruct()

    photo_folder = f"{main_directory}/photos"
    zdjecia = photos_in_directory()
    length = len(photos_in_directory())
    number = random.randrange(0, length)
    rand_photo = zdjecia[number]
    image = Image.open(f"{photo_folder}/{rand_photo}")
    image.thumbnail((700,700))
    photo = ImageTk.PhotoImage(image)
    current_photo_label = tk.Label(label_frame, image=photo)
    current_photo_label.image = photo
    current_photo_label.pack(pady=10)
    current_photo_labels.append(current_photo_label)

def exit_fullscreen(event):
    if event.keysym == 'Escape':
        root.attributes('-fullscreen', False)


def photos_in_directory():
    photo_folder = f"{main_directory}/photos"
    sciezka = []
    list = os.listdir(photo_folder)
    for item in list:
        if item.endswith(".jpg") or item.endswith(".png"):
            sciezka.append(item)

    return sciezka

def photo_choice():
    global current_photo_labels
    photo_destruct()
    photo_folder = f"{main_directory}/photos/"
    zdjecia = photos_in_directory()
    for file in zdjecia:
        image = Image.open(f"{photo_folder}/{file}")
        image.thumbnail((100,100))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(label_frame, image=photo)
        label.image = photo
        label.pack(side=tk.LEFT)
        current_photo_labels.append(label)

def photo_destruct():
    if current_photo_labels:
        for label in current_photo_labels:
            label.destroy()  

def import_file():
    filename_path = filedialog.askopenfilename(title="import file")
    photo_folder = f"{main_directory}/photos/"
    if filename_path and filename_path.endswith(".jpg") or filename_path.endswith(".png"):
        shutil.copy(filename_path, photo_folder)
    else:
        print("file does not fit the requirements or is not a photo")

        
def main():
    try:
        folder_existing()
        root.mainloop()
    except Exception as e:
        print("error: ", e)


root.attributes('-fullscreen', True)
root.title("Prosty interfejs")
root.bind('<Key>', exit_fullscreen)
#frame for buttons ->
button_frame = tk.Frame(root)
button_frame.pack()

#buttons ->
losuj_przycisk = tk.Button(button_frame, text="losuj zdjęcie", command=draw)
losuj_przycisk.pack(side=tk.LEFT ,pady=30)
pokaz_wybor = tk.Button(button_frame, text="pokaż zdjęcia do wyświetlenia", command=photo_choice)
pokaz_wybor.pack(side=tk.LEFT ,pady=30)
import_button = tk.Button(button_frame, text="Importuj plik", command=import_file)
import_button.pack(side=tk.LEFT, pady=30)

#frame for photos ->
label_frame = tk.Frame(root)
label_frame.pack()
main()
