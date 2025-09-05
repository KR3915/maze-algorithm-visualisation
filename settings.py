import os
import tkinter as tk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def close_window():
    main.destroy()

def validate_input(P):
    if P == "":
        return True
    try:
        value = int(P)
        return 1 <= value <= 100
    except ValueError:
        return False

main = tk.Tk()
main.title("Settings")
main.config(bg="#E4E2E2")
main.geometry("200x200")

vcmd = (main.register(validate_input), '%P')

label1 = tk.Label(main, text="Value 1 (1-100):", bg="#E4E2E2")
label1.pack(pady=(20, 0))
entry1 = tk.Entry(main, validate="key", validatecommand=vcmd)
entry1.pack(pady=(0, 10))

label2 = tk.Label(main, text="Value 2 (1-100):", bg="#E4E2E2")
label2.pack()
entry2 = tk.Entry(main, validate="key", validatecommand=vcmd)
entry2.pack(pady=(0, 10))

close_button = tk.Button(main, text="Close", command=close_window)
close_button.pack(pady=(10, 0))

main.mainloop()