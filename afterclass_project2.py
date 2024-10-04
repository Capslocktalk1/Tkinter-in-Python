import tkinter as tk
import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(12):
        password += random.choice(characters)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

label = tk.Label(root, text="Generated Password:")
label.pack()

password_entry = tk.Entry(root, width=40)
password_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

root.mainloop()
