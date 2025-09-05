import os
import tkinter as tk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def close_window():
    main.destroy()


main = tk.Tk()
main.title("Settings")
main.config(bg="#E4E2E2")
main.geometry("200x200")

# Use a Label instead of a Text widget
text_label = tk.Label(master=main, text="Your text here", bg="#E4E2E2", fg="#000", wraplength=791, justify="left")
text_label.place(x=1, y=1, width=120, height=120)

# Example text content (replace with your actual text)
example_text = "red: start\nblue: end\nwhite: obstacle\nE: eraser\nC: clear\n"
text_label.config(text=example_text)

button = tk.Button(master=main, text="OK")
button.config(bg="#E4E2E2", fg="#000", command=close_window)
button.place(x=50, y=100, height=40)


main.mainloop()