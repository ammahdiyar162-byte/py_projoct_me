# Written by MohixCode / Mohammadreza Nouriyani

import tkinter as tk
import time
import random
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")

_photo_refs = []

def load_photo(path):
    try:
        img = tk.PhotoImage(file=path)
        _photo_refs.append(img)
        return img
    except Exception:
        return None

def create_glitch_window():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg="black")
    root.overrideredirect(True)

    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    glitch_colors = ["#00ffff", "#ff00ff", "#ffff00", "#ffffff", "#000000"]

    def glitch_frame():
        width = canvas.winfo_width() or root.winfo_screenwidth()
        height = canvas.winfo_height() or root.winfo_screenheight()
        canvas.delete("glitch")
        for _ in range(random.randint(8, 25)):
            y = random.randint(0, height)
            h = random.randint(2, 40)
            x = random.randint(-50, width)
            w = random.randint(100, width + 100)
            color = random.choice(glitch_colors)
            canvas.create_rectangle(x, y, x + w, y + h, fill=color, outline=color, tags="glitch")
        for _ in range(random.randint(3, 12)):
            x = random.randint(0, width)
            y = random.randint(0, height)
            size = random.randint(20, 120)
            color = random.choice(glitch_colors)
            canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline=color, tags="glitch")
        root.after(random.randint(50, 180), glitch_frame)

    label = tk.Label(root, text="System under maintenance... :)",
                     font=("Consolas", 16), bg="black", fg="#00ffff")
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    emojis_list = ["😈", "💀", "🔥", "😱", "👾", "💣", "🚨", "🤖", "⚠️", "🎭", "👻", "🦹"]

    def change_to_hacked():
        label.config(text="Your screen got hacked 😈🔥💀", fg="#ff0040")
        root.after(4500, show_emojis)

    def show_photos():
        width = canvas.winfo_width() or root.winfo_screenwidth()
        height = canvas.winfo_height() or root.winfo_screenheight()
        if not os.path.isdir(ASSETS_DIR):
            return
        all_imgs = sorted([os.path.join(ASSETS_DIR, f) for f in os.listdir(ASSETS_DIR)
                          if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))])
        by_name = {}
        if len(all_imgs) >= 3:
            for p in all_imgs:
                if "images_1" in p:
                    by_name["flag"] = p
                    break
            others = [p for p in all_imgs if "images_1" not in p]
            if len(others) >= 1:
                by_name["hoodie"] = others[0]
            if len(others) >= 2:
                by_name["mask"] = others[1]
        positions = [(width * 0.2, height * 0.5), (width * 0.5, height * 0.5), (width * 0.8, height * 0.5)]
        keys = ["hoodie", "mask", "flag"]
        for i, key in enumerate(keys):
            path = by_name.get(key)
            if not path or not os.path.isfile(path):
                continue
            img = load_photo(path)
            if img is None:
                continue
            x, y = positions[i][0], positions[i][1]
            canvas.create_image(x, y, image=img, tags="photo")
            if key == "flag":
                label.config(text="WE MAKE IRAN BETTER", fg="#ffffff", font=("Consolas", 24, "bold"))

    def show_emojis():
        width = canvas.winfo_width() or root.winfo_screenwidth()
        height = canvas.winfo_height() or root.winfo_screenheight()
        for _ in range(25):
            x = random.randint(50, max(100, width - 50))
            y = random.randint(50, max(100, height - 50))
            emoji = random.choice(emojis_list)
            size = random.randint(24, 72)
            canvas.create_text(x, y, text=emoji, font=("Segoe UI Emoji", size), fill=random.choice(glitch_colors), tags="emoji")

    root.after(5000, change_to_hacked)
    root.after(6000, show_photos)

    def close(_event=None):
        root.destroy()

    def block_key(event):
        return "break"

    root.bind("<Alt-F4>", close)
    root.bind("<Key>", block_key)
    root.bind("<KeyPress>", block_key)
    canvas.bind("<Key>", block_key)
    canvas.bind("<KeyPress>", block_key)
    label.bind("<Key>", block_key)
    label.bind("<KeyPress>", block_key)
    canvas.focus_set()

    root.update_idletasks()
    root.after(100, glitch_frame)
    root.after(200, root.focus_force)
    root.mainloop()

print("Screen will glitch in 3 seconds... Get ready!")
time.sleep(4)

create_glitch_window()
