import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import string
import secrets


# ----- Password Logic -----

def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        result_var.set("❌ Enter valid length")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    char_pool = ''
    if use_upper: char_pool += string.ascii_uppercase
    if use_lower: char_pool += string.ascii_lowercase
    if use_digits: char_pool += string.digits
    if use_symbols: char_pool += string.punctuation

    if not char_pool:
        result_var.set("⚠️ Select at least one character type")
        return

    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    result_var.set(password)
    strength_var.set("Strength: " + check_strength(password))

def check_strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if len(password) >= 12: score += 1

    if score <= 2: return "Weak"
    elif score == 3: return "Moderate"
    else: return "Strong"

def copy_password():
    pwd = result_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        root.update()  # now it stays on clipboard after the app closes
        messagebox.showinfo("Copied", "🔐 Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "❌ No password to copy.")

def save_password():
    pwd = result_var.get()
    if not pwd:
        messagebox.showwarning("Empty", "❌ No password to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(pwd + "\n")
        messagebox.showinfo("Saved", f"✅ Password saved to {file_path}")

# ----- GUI Setup -----

root = tk.Tk()
root.title("🌈 Fancy Password Generator")
root.geometry("450x520")
root.configure(bg="#1f1f2e")

# Custom Fonts
TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 12)
ENTRY_FONT = ("Consolas", 14, "bold")
BUTTON_FONT = ("Segoe UI", 10)

# Header Frame with shadow-like effect
header_frame = tk.Frame(root, bg="#27293d", bd=2, relief="ridge")
header_frame.pack(pady=15, padx=15, fill="x")

title = tk.Label(header_frame, text=" Secure Password Generator", font=TITLE_FONT, fg="#f1c40f", bg="#27293d")
title.pack(pady=10)

# Options Frame
option_frame = tk.Frame(root, bg="#1f1f2e")
option_frame.pack(pady=10)

tk.Label(option_frame, text="Password Length:", font=LABEL_FONT, bg="#1f1f2e", fg="white").grid(row=0, column=0, pady=5, sticky='w')
length_var = tk.StringVar(value="12")
length_entry = ttk.Entry(option_frame, textvariable=length_var, font=ENTRY_FONT, justify='center', width=10)
length_entry.grid(row=0, column=1, pady=5)

# Character Options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

check_frame = tk.Frame(root, bg="#1f1f2e")
check_frame.pack(pady=5)

def create_checkbox(text, variable, row, col):
    cb = tk.Checkbutton(check_frame, text=text, variable=variable, font=LABEL_FONT, bg="#1f1f2e", fg="white", activebackground="#1f1f2e", activeforeground="#16a085", selectcolor="#27293d")
    cb.grid(row=row, column=col, padx=15, pady=5, sticky='w')

create_checkbox("Include A-Z", upper_var, 0, 0)
create_checkbox("Include a-z", lower_var, 0, 1)
create_checkbox("Include 0-9", digit_var, 1, 0)
create_checkbox("Include Symbols", symbol_var, 1, 1)

# Result Display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Consolas", 16), bg="#1f1f2e", fg="#00e676", wraplength=420)
result_label.pack(pady=15)

# Strength Label
strength_var = tk.StringVar()
tk.Label(root, textvariable=strength_var, font=("Segoe UI", 11), bg="#1f1f2e", fg="#ffca28").pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#1f1f2e")
button_frame.pack(pady=10)

def styled_button(text, command, color):
    return tk.Button(button_frame, text=text, command=command, font=BUTTON_FONT, bg=color, fg="white", activebackground="#333", width=14, relief="raised", bd=2)

styled_button("Generate", generate_password, "#16a085").grid(row=0, column=0, padx=10, pady=5)
styled_button("Copy", copy_password, "#3498db").grid(row=0, column=1, padx=10, pady=5)
styled_button("Save", save_password, "#9b59b6").grid(row=1, column=0, columnspan=2, pady=5)

# Footer
tk.Label(root, text="✨ Designed for oasis", font=("Arial", 9), bg="#1f1f2e", fg="#95a5a6").pack(side="bottom", pady=10)

# Run GUI
root.mainloop()