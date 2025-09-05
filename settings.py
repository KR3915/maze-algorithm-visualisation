import os
import tkinter as tk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def save_settings(rows, cols, width, height, obstacle_density):
    config = {
        "rows": rows,
        "cols": cols,
        "width": width,
        "height": height,
        "obstacle_density": obstacle_density
    }
    with open(os.path.join(BASE_DIR, 'config.jsonc'), 'w') as f:
        import commentjson as json
        json.dump(config, f, indent=4)

def close_window():
    main.destroy()

def only_numbers(P):
    return P.isdigit() or P == ""

main = tk.Tk()
main.title("Settings")
main.config(bg="#E4E2E2")
main.geometry("200x200")

vcmd = (main.register(only_numbers), '%P')

col_label = tk.Label(main, text="rows:", bg="#E4E2E2")
col_label.pack()
col_entry = tk.Entry(main, validate="key", validatecommand=vcmd)
col_entry.pack(pady=(20, 0))

row_label = tk.Label(main, text="cols:", bg="#E4E2E2")
row_label.pack()
row_entry = tk.Entry(main, validate="key", validatecommand=vcmd)
row_entry.pack(pady=(20, 0))

close_button = tk.Button(main, text="Close", command=close_window)
close_button.pack(pady=(10, 0))

save_button = tk.Button(
    main,
    text="Save",
    command=lambda: save_settings(
        int(col_entry.get()),
        int(row_entry.get()),
        800,
        800,
        0.2
    )
)
save_button.pack(pady=(10, 0))

main.mainloop()