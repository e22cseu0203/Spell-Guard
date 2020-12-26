from textblob import TextBlob
from tkinter import *

def check():
    b = TextBlob(e.get())
    corrected_text = Label(root, text = str(b.correct()))
    corrected_text.pack()

root = Tk()
root.title('SpellCheck')
root.geometry('400x200')

head = Label(root, text='SpellCheck',font=('helvetica', 14 , 'bold'))
head.pack()
e = Entry(root, width=200,borderwidth=5)
e.pack()
b = Button(root, text = 'Check', font=('helvetica', 8 , 'bold'), fg = 'white', bg = 'brown', command = check)
b.pack()
root.mainloop()













































































































