import tkinter
from tkinter import *
import webbrowser


#screen
screen=tkinter.Tk()
screen.geometry=("100x100")
screen.title("Titre de l'appli")
mainmenu = tkinter.Menu(screen)

#Label (corps de l'appli)
#'pack' pour importer le contenu
l1 = Label(text="Welcome" , font='Garamond' , bg='purple')
#"pady" pour descendre ou monter le contenu
#"side" pour mettre a droite ou a gauche le contenu
l1.pack(pady=50)

#Attribuer des fonctions aux boutons
def open():
    webbrowser.open_new("https://github.com/KhizarSAN")

def exit():
    quit()

#BOUTON
bouton2= Button(text="GITHUB", command=(open))
bouton2.pack(pady=100)

bouton1= Button(text="Close", command=(exit))
bouton1.pack(pady=200)

#Menu
first = tkinter.Menu(mainmenu)
first.add_radiobutton(label='Click')

#Mainmenu
mainmenu.add_cascade(label='Settings', menu=first)


#loop pour ne pas que ca ferme
screen.config(menu=mainmenu)
screen.mainloop()


