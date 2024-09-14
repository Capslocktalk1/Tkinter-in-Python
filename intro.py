from tkinter import *
window = Tk()
window.title('Tkinter sample window')

window.geometry('300x300')

greeting = Label(text = "Hello" , fg = "black" , bg = 'blue')
greeting.pack

bt = Button(text="click me", bg="black", fg='white', width=20)
bt.pack(pady=5)

input1 = Entry(bg="red" , fg='white')
input1.pack(pady=10)

window.mainloop()