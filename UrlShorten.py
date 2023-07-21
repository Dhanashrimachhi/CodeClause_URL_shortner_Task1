from tkinter import *
import pyshorteners
import pyperclip

root = Tk()
root.title('URL Shortner')
root.geometry('500x500')
root.config(background = "#1BB1B2")  

#Main function
def shorten():
    if shorty.get():
        shorty.delete(0, END)
    if my_entry.get():
        #Convert Url to Short
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        #Output to window
        shorty.insert(END, url)
        pyperclip.copy(url)

my_label = Label(root, text="URL Shortner",bg="#1BB1B2",fg="#020024", font=("Helvetica",34))
my_label.pack(pady=30)

my_entry = Entry(root, font=("Helvetica",24))
my_entry.pack(pady=20)

my_btn = Button(root, command=shorten , text="Shorten Link & Copy to Clipboard",bg="#131D32",fg="#fff",font=("Helvetica",15))
my_btn.pack(pady=20)

short_label = Label(root, text="Shortened Link" ,fg="#020024" ,bg="#1BB1B2", font=("Helvetica",18))
short_label.pack(pady=20)

shorty = Entry(root, font=("Helvetica",17),justify=CENTER, width=25,bd=0)#,bg="#1BB1B2", fg="#F9D949",  width=30,bd=0)
shorty.pack(pady=30)

root.mainloop()