#Source : youtube, google, chatgpt (assez compris, mais pas la totalité + impossible que je le refasse sans les sources)

from tkinter import *
from tkinter import messagebox
import hashlib
"------------------------------------------------------------------------------------------------------------------"
gui = Tk()
gui.title("Password")
gui.geometry("390x300")
"------------------------------------------------------------------------------------------------------------------"
def exigences():
    messagebox.showinfo(title="Éxigences", message=
"""- 8 caractères
- une lettre majuscule
- une lettre minuscule
- un chiffre
- un caractère spécial""")
"------------------------------------------------------------------------------------------------------------------"
def check_passw():
    mdp = entry_mdp.get()
    if len(mdp) >= 8:
        minuscule = False
        majuscule = False
        num = False
        carac = False

        for char in mdp:
            if char.isdigit():
                num = True
            if char.islower():
                minuscule = True
            if char.isupper():
                majuscule = True
            if not char.isalnum():
                carac = True

        if minuscule and majuscule and num and carac:

            messagebox.showinfo(title="OK", message="Mot de passe accepté")

        else:
            messagebox.showerror(title="ERREUR", message="Répondez aux exigences.")
    else:
        messagebox.showerror(title="ERREUR", message="8 caractères minimum.")
"------------------------------------------------------------------------------------------------------------------"
def crypt_passw():
    mdp = entry_mdp.get()
    mdp_encode = mdp.encode()
    mdp_hash = hashlib.sha256(mdp_encode)
    mdp_hex = mdp_hash.hexdigest()
    messagebox.showinfo(title="Mot de passe crypté", message=mdp_hex)
"------------------------------------------------------------------------------------------------------------------"
txt = Label(gui, text="Entrez un mot de passe", font=("arial",15,"bold"), fg="black")
txt.place(x=90, y=30)

entry_mdp = Entry(gui, font=("arial",10))
entry_mdp.place(x=125, y=100, height=30, width=120)

ok = Button(gui, text="OK", fg="black", font=("arial",10), bg="#84E3EC", command=check_passw)
ok.place(x=260, y=100, height=30, width=30)

info = Button(gui, text="Éxigences du mot de passe", fg="black", font=("arial",10), bg="#84E3EC", command=exigences)
info.place(x=100, y=60, height=30, width=200)

crypt_button = Button(gui, text="Cryptage", fg="black", font=("arial",10), bg="grey", command=crypt_passw)
crypt_button.place(x=125, y=138, height=25, width=90)
"------------------------------------------------------------------------------------------------------------------"
gui.mainloop()
