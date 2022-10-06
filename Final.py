####################### IMPORT ####################

from tkinter import *
from tkinter import filedialog as fd
import pyautogui as pag
import pyperclip
import time
from tkinter import messagebox as alert
import customtkinter as tk
import webbrowser

pag.useImageNotFoundException()
pag.FAILSAFE = False
##################################### Global Vars ############################################

file_path = ''
datalist = []
user = ''
passw = ''

######################################## Functions #######################################################

def ShowAlert():
    alert.showinfo(title= "Object Not Detected",message="Make sure the login area is visible on screen! Open the login screen and then click Ok!")   

############# CopyPasteUsername ###########
def CopyPasteUser():
        
        pyperclip.copy(user.strip())
        
        try:
            user_box = pag.locateCenterOnScreen('username.PNG')
            pag.moveTo(user_box)
            time.sleep(0.1)
            pag.click()
            time.sleep(0.1)
            pag.hotkey('ctrl','v')
            time.sleep(0.1)
            
        except Exception:
            
            ShowAlert()
            CopyPasteUser()

############# CopyPastePassword ###########
def CopyPastePass():
      
        
        pyperclip.copy(passw.strip())
        
        try:
            pass_box = pag.locateCenterOnScreen('password.PNG')
            pag.moveTo(pass_box)
            time.sleep(0.1)
            pag.click()
            time.sleep(0.1)
            pag.hotkey('ctrl','v')
            #paste_data = pyperclip.paste()
            #pag.typewrite(paste_data)
            
        except Exception:
            ShowAlert()

            CopyPastePass()
        
############# Press Login ###########
def login():   
        try:
            login_butt = pag.locateCenterOnScreen('login.PNG')
            pag.moveTo(login_butt)
            pag.click()
        
        except Exception:
            pass


def skip():
    user, passw = datalist.pop(0)
    current_acc.configure(text=user)
    current_pass.configure(text=passw)
############################# File processing #######################


def FileRead(file_path: str) -> list[tuple[str, str]]:
    """Reads file_path, returns list of (user, passwd) tuples."""
    with open(file_path) as data:
        
        datalist = data.readlines()
    return [
        (user, passwd)
        for user, passwd in zip(datalist[::2], datalist[1::2])
    ]
    

def OpenFile():
    """Asks user for a filename, read user/password data, and
    add all data from the file into datalist."""
    file_path = fd.askopenfilename()
    datalist.extend(FileRead(file_path))
    

def NextAccount():
    global user
    global passw
    user, passw = datalist.pop(0)
    current_acc.configure(text=user)
    current_pass.configure(text=passw)
    CopyPasteUser()
    CopyPastePass()
    login()


def Twit():
    webbrowser.open('https://twitter.com/Dragweeb')
  
    
    


######################################## GUI #######################################################


window = tk.CTk()
window.geometry('400x400+1090+213')
window.title("Val Booster Assist")

tk.set_appearance_mode("dark") 
tk.set_default_color_theme("dark-blue")



file_button = tk.CTkButton(window,text='Select Acc File', hover_color = 'green', command=OpenFile)
file_button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

next_acc = tk.CTkButton(window,text='Next', hover_color = 'green',command=NextAccount )
next_acc.place(relx = 0.5 , rely = 0.73, anchor = tk.CENTER)

skip_acc = tk.CTkButton(window, text='Skip', hover_color = 'red',command= skip)
skip_acc.place(relx = 0.5 , rely = 0.9, anchor = tk.CENTER)

current_acc = tk.CTkLabel(window, text = 'Current Username', bg_color= 'grey',compound='top')
current_acc.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

current_pass = tk.CTkLabel(window,text = 'Current Password',bg_color= 'grey', compound='top')
current_pass.place(relx=0.5, rely=0.6, anchor=tk.CENTER)



info_img = PhotoImage(file = 'info.png')
info_butt = tk.CTkButton(master = window,width = 5, image= info_img, text='', fg_color= '#212325', hover_color= '', command= Twit )
info_butt.place(x=0,y=0)

win_ico = PhotoImage(file = 'val_icon.png')
window.iconphoto(True,win_ico)

window.mainloop()