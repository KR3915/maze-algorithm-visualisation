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
main.geometry("400x400")
main.resizable(False, False)
main.attributes('-topmost', True)  # Always on top

vcmd = (main.register(only_numbers), '%P')

# --- Window size label and entries ---
size_label = tk.Label(main, text="Window size (px):", bg="#E4E2E2")
size_label.pack(pady=(10, 0))

size_frame = tk.Frame(main, bg="#E4E2E2")
size_frame.pack()

width_label = tk.Label(size_frame, text="Width:", bg="#E4E2E2")
width_label.grid(row=0, column=0, sticky="e", padx=(0, 5))
width_entry = tk.Entry(size_frame, validate="key", validatecommand=vcmd)
width_entry.insert(0, str(config.get("width", 800)))
width_entry.grid(row=0, column=1, pady=(0, 5))

height_label = tk.Label(size_frame, text="Height:", bg="#E4E2E2")
height_label.grid(row=1, column=0, sticky="e", padx=(0, 5))
height_entry = tk.Entry(size_frame, validate="key", validatecommand=vcmd)
height_entry.insert(0, str(config.get("height", 800)))
height_entry.grid(row=1, column=1, pady=(0, 5))

# ------ rows ---------
col_label = tk.Label(main, text="Rows:", bg="#E4E2E2")
col_label.pack()
col_entry = tk.Entry(main, validate="key", validatecommand=vcmd)
col_entry.insert(0, str(config.get("rows", 20)))
col_entry.pack(pady=(5, 0))
# --------cols------------
row_label = tk.Label(main, text="Cols:", bg="#E4E2E2")
row_label.pack()
row_entry = tk.Entry(main, validate="key", validatecommand=vcmd)
row_entry.insert(0, str(config.get("cols", 20)))
row_entry.pack(pady=(5, 0))
#----------density----------
density_label = tk.Label(main, text="Obstacle density (%):", bg="#E4E2E2")
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
        int(width_entry.get()),
        int(height_entry.get()),
        int(density_scale.get())
    )
)
save_button.pack(pady=(10, 0))

main.mainloop()