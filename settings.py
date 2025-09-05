import os
import tkinter as tk
import commentjson as json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load current config values
config_path = os.path.join(BASE_DIR, 'config.jsonc')
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
else:
    config = {
        "rows": 20,
        "cols": 20,
        "width": 800,
        "height": 800,
        "obstacle_density": 20
    }

def save_settings(rows, cols, width, height, obstacle_density):
    config = {
        "rows": rows,
        "cols": cols,
        "width": width,
        "height": height,
        "obstacle_density": obstacle_density
    }
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)

def close_window():
    main.destroy()

def only_numbers(P):
    return P.isdigit() or P == ""

main = tk.Tk()
main.title("Settings")
main.config(bg="#E4E2E2")
main.geometry("400x250")

vcmd = (main.register(only_numbers), '%P')

col_label = tk.Label(main, text="rows:", bg="#E4E2E2")
col_label.pack()
col_entry = tk.Entry(main, validate="key", validatecommand=vcmd)
col_entry.insert(0, str(config.get("rows", 20)))
col_entry.pack(pady=(5, 0))

row_label = tk.Label(main, text="cols:", bg="#E4E2E2")
row_label.pack()
row_entry = tk.Entry(main, validate="key", validatecommand=vcmd)
row_entry.insert(0, str(config.get("cols", 20)))
row_entry.pack(pady=(5, 0))

density_label = tk.Label(main, text="obstacle density (%):", bg="#E4E2E2")
density_label.pack()
density_scale = tk.Scale(
    main,
    from_=0,
    to=100,
    resolution=1,
    orient=tk.HORIZONTAL,
    bg="#E4E2E2",
    length=350
)
density_scale.set(int(config.get("obstacle_density", 20)))
density_scale.pack()

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
        int(density_scale.get())
    )
)
save_button.pack(pady=(10, 0))

main.mainloop()