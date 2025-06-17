import tkinter as tk
from tkinter import messagebox, filedialog
import random
import threading
import time
import pyautogui
from PIL import Image, ImageTk
import os
import ctypes

# --- Roast and Compliment Data ---
roasts = [
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You're not stupid; you just have bad luck thinking.",
    "You bring everyone so much joy… when you leave the room.",
    "You're proof that even evolution takes a break sometimes."
]

compliments = [
    "You're cooler than a snowman in a freezer.",
    "You're like a ray of sunshine in a dark room.",
    "You're smarter than Google and cuter than a cat meme.",
    "You make even Mondays feel like Fridays!"
]

therapist_responses = [
    "Tell me more about how that made your goldfish feel.",
    "Interesting... but have you tried yelling into a pillow?",
    "Maybe you're just tired. Or cursed.",
    "Sounds like a you problem."
]

# --- GUI Functions ---

def open_ai_roast_bot():
    win = tk.Toplevel()
    win.title("AI Roast Bot")
    win.geometry("400x200")
    tk.Label(win, text="Press to get roasted 👿", font=("Arial", 14)).pack(pady=10)
    label = tk.Label(win, text="", wraplength=300, font=("Arial", 12))
    label.pack(pady=10)
    tk.Button(win, text="Roast Me", command=lambda: label.config(text=random.choice(roasts))).pack()

def open_compliment_generator():
    win = tk.Toplevel()
    win.title("Compliment Generator")
    win.geometry("400x200")
    tk.Label(win, text="Press for a compliment 💖", font=("Arial", 14)).pack(pady=10)
    label = tk.Label(win, text="", wraplength=300, font=("Arial", 12))
    label.pack(pady=10)
    tk.Button(win, text="Compliment Me", command=lambda: label.config(text=random.choice(compliments))).pack()

def open_fake_therapist():
    win = tk.Toplevel()
    win.title("Fake Therapist")
    win.geometry("400x250")
    tk.Label(win, text="Fake Therapist 🤔", font=("Arial", 14)).pack(pady=10)
    entry = tk.Entry(win, width=40)
    entry.pack(pady=5)
    label = tk.Label(win, text="", wraplength=350)
    label.pack(pady=10)
    def reply():
        label.config(text=random.choice(therapist_responses))
    tk.Button(win, text="Ask", command=reply).pack()

def open_love_calculator():
    win = tk.Toplevel()
    win.title("Love Calculator")
    win.geometry("400x250")
    tk.Label(win, text="Name 1").pack()
    name1 = tk.Entry(win)
    name1.pack()
    tk.Label(win, text="Name 2").pack()
    name2 = tk.Entry(win)
    name2.pack()
    result = tk.Label(win, text="", font=("Arial", 14))
    result.pack(pady=10)
    def calc():
        score = random.randint(0, 100)
        result.config(text=f"Love Score: {score}% ❤️" if score > 50 else f"Love Score: {score}% 💔")
    tk.Button(win, text="Calculate", command=calc).pack(pady=5)

def open_meme_generator():
    win = tk.Toplevel()
    win.title("Meme Generator")
    win.geometry("500x600")
    canvas = tk.Canvas(win, width=400, height=400)
    canvas.pack()
    top_text = tk.Entry(win, width=50)
    bottom_text = tk.Entry(win, width=50)
    top_text.pack(pady=5)
    bottom_text.pack(pady=5)

    def load_image():
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not path:
            return
        img = Image.open(path).resize((400, 400))
        img_draw = ImageTk.PhotoImage(img)
        canvas.image = img_draw
        canvas.create_image(0, 0, anchor="nw", image=img_draw)
        canvas.create_text(200, 30, text=top_text.get(), fill="white", font=("Arial", 18, "bold"))
        canvas.create_text(200, 370, text=bottom_text.get(), fill="white", font=("Arial", 18, "bold"))

    tk.Button(win, text="Choose Image", command=load_image).pack()

def open_face_tracker():
    win = tk.Toplevel()
    win.title("Face Tracker")
    win.geometry("300x300")
    dot = tk.Label(win, text="😐", font=("Arial", 24))
    dot.place(x=150, y=150)

    def follow_mouse():
        while True:
            x, y = pyautogui.position()
            dot.place(x=x % 250, y=y % 250)
            time.sleep(0.1)

    threading.Thread(target=follow_mouse, daemon=True).start()

def start_auto_typer():
    def type_loop():
        phrases = ["I'm watching you...", "Did you hear that?", "Help me.", "You can't escape.","I'm coming for you.","behind you."]
        while True:
            time.sleep(random.randint(10, 20))
            pyautogui.write(random.choice(phrases), interval=0.05)
    threading.Thread(target=type_loop, daemon=True).start()
    messagebox.showinfo("Auto Typer", "Creepy typing will start randomly.")

def start_ghost_cursor():
    def move_mouse():
        while True:
            dx = random.randint(-10, 10)
            dy = random.randint(-10, 10)
            x, y = pyautogui.position()
            pyautogui.moveTo(x + dx, y + dy, duration=0.2)
            time.sleep(random.randint(5, 10))
    threading.Thread(target=move_mouse, daemon=True).start()
    messagebox.showinfo("Ghost Cursor", "Mouse will start moving randomly.")

def flash_webcam_light():
    win = tk.Toplevel()
    win.attributes('-fullscreen', True)
    win.configure(bg='white')
    def close_flash():
        win.destroy()
    win.after(500, close_flash)

def trigger_blue_screen():
    win = tk.Toplevel()
    win.attributes('-fullscreen', True)
    win.configure(bg='blue')
    tk.Label(win, text="💀 A problem has been detected...", font=("Consolas", 20), fg="white", bg="blue").pack(pady=100)
    tk.Label(win, text="If this is your first time seeing this...\nJust kidding. Press ESC to exit.", font=("Consolas", 16), fg="white", bg="blue").pack()

    def esc_exit(event):
        win.destroy()
    win.bind("<Escape>", esc_exit)

# --- Main Hub GUI ---
root = tk.Tk()
root.title("Fun Python Hub")
root.geometry("400x620")
root.configure(bg="#111")

tk.Label(root, text="🌀 Fun Hub", font=("Arial", 24), fg="cyan", bg="#111").pack(pady=20)

buttons = [
    ("AI Roast Bot", open_ai_roast_bot),
    ("Meme Generator", open_meme_generator),
    ("Compliment Generator", open_compliment_generator),
    ("Fake Therapist", open_fake_therapist),
    ("Love Calculator", open_love_calculator),
    ("Face Tracker", open_face_tracker),
    ("Auto Typer Prank", start_auto_typer),
    ("Ghost Cursor", start_ghost_cursor),
    ("Fake Webcam Flash", flash_webcam_light),
    ("Fake Blue Screen", trigger_blue_screen),
]

for (text, command) in buttons:
    tk.Button(root, text=text, font=("Arial", 14), width=30, height=2, command=command, bg="#222", fg="white", activebackground="#333").pack(pady=5)

root.mainloop()
