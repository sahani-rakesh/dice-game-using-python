import random  # Importing random module for generating random dice faces
from tkinter import *  # Importing Tkinter for GUI
import pygame  # Importing pygame to play sound on button click

pygame.mixer.init()  # Initializing the mixer module of pygame

def play_sound():
    """Loads and plays a sound when called."""
    pygame.mixer.music.load("sound\click.mp3")
    pygame.mixer.music.play()

def rolldice():
    """Selects a random dice face and updates the label, then plays sound."""
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']  # Unicode characters for dice faces
    label.configure(text=random.choice(dice))  # Updating the label with a random dice face
    play_sound()  # Playing sound on roll

# Creating the main window
root = Tk()
root.title("Roll Dice")  # Setting window title
root.geometry("600x600")  # Defining window size

# Creating and placing the label for displaying dice face
label = Label(root, font=('arial', 250, 'bold'), text='')
label.pack()

# Creating and placing the button to roll the dice
button = Button(root, font=('arial', 25, 'bold'), text='Roll Dice', command=rolldice)
button.pack()

# Running the GUI event loop
root.mainloop()
