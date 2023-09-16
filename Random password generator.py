from tkinter import *
from random import randint

root = Tk()
root.geometry("500x300")

def rand1():
	pas_entry.delete(0, END)
	pas_length = int(entry.get())
	password = ''

	for x in range(pas_length):
		password += chr(randint(33,126))

	pas_entry.insert(0, password)

def clipper():
	root.clipboard_clear()
	root.clipboard_append(pas_entry.get())

lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

entry = Entry(lf, font=("Lexend", 24))
entry.pack(pady=20, padx=20)

pas_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pas_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Strong Password", command=rand1)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboad", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
