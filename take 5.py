# Nayeer Ullah
# This program creates a GUI for Google Search using Tkinter.
# Perhaps not the sleekest solution, it was great to shake off the rust..Hopefully it works...

from tkinter import *
import webbrowser

root = Tk()
root.title("Google Search")
root.configure(bg="lightblue")
label1 = Label(root, text="What would you like to search for?", font=("Arial", 20, "bold"))
label1.grid(row=0, column=0)
entry = Entry(root, width=30)
entry.grid(row=0, column=1)

def search():
    url = entry.get()
    webbrowser.open("https://www.google.com/search?q=" + url)

button = Button(root, text='Search', command=search)
button.grid(row=1, column=0, columnspan=2, pady=10)

#user_input = input("Enter your Query: ") 
#webbrowser.open(user_input)

root.mainloop()