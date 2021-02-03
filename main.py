"""Main entry point for application."""

import tkinter as tk
from tkinter import messagebox

def DoIt_Click():
    messagebox.showinfo("CLEEK!", "You clicked it!  You're doing great!")

def main():
    window = tk.Tk()
    window.geometry("320x240")

    label = tk.Label(text="Hello World!", font=("Consolas", 24))
    label.pack()

    button = tk.Button(text="Do It",command=DoIt_Click)
    button.pack()

    window.mainloop()

if __name__ == '__main__':
    main()
