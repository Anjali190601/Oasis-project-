import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        if height <= 0 or weight <= 0:
            raise ValueError("Positive values only")
        bmi = weight / ((height / 100) ** 2)
        bmi_result.set(f"{bmi:.2f}")
        category.set(get_bmi_category(bmi))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers for height and weight.")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

root = tk.Tk()
root.title("Colorful BMI Calculator")
root.geometry("420x450")
root.configure(bg="#FFFAF0")

style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", font=("Comic Sans MS", 12), background="#FFFAF0", foreground="#333")
style.configure("TEntry", font=("Comic Sans MS", 12))
style.configure("TButton", font=("Comic Sans MS", 12, "bold"), background="#ff69b4", foreground="white")
style.map("TButton", background=[("active", "#ff1493")])

title_label = tk.Label(root, text="BMI Calculator", font=("Comic Sans MS", 24, "bold"), bg="#FFFAF0", fg="#8A2BE2")
title_label.pack(pady=20)

frame = tk.Frame(root, bg="#FFF0F5", bd=2, relief="ridge")
frame.pack(pady=10, padx=20, fill="x")

tk.Label(frame, text="Height (cm):", font=("Comic Sans MS", 12), bg="#FFF0F5").grid(row=0, column=0, padx=10, pady=15, sticky="e")
height_entry = ttk.Entry(frame, width=20)
height_entry.grid(row=0, column=1, pady=15, padx=10)

tk.Label(frame, text="Weight (kg):", font=("Comic Sans MS", 12), bg="#FFF0F5").grid(row=1, column=0, padx=10, pady=15, sticky="e")
weight_entry = ttk.Entry(frame, width=20)
weight_entry.grid(row=1, column=1, pady=15, padx=10)

calculate_btn = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_btn.pack(pady=15)

result_frame = tk.Frame(root, bg="#E6E6FA", bd=2, relief="ridge")
result_frame.pack(pady=10, padx=20, fill="x")

bmi_result = tk.StringVar()
category = tk.StringVar()

tk.Label(result_frame, text="Your BMI:", font=("Comic Sans MS", 13, "bold"), bg="#E6E6FA", fg="#00008B").grid(row=0, column=0, pady=10, padx=10, sticky="e")
tk.Label(result_frame, textvariable=bmi_result, font=("Comic Sans MS", 13), bg="#E6E6FA", fg="#00008B").grid(row=0, column=1, pady=10, padx=10, sticky="w")

tk.Label(result_frame, text="Category:", font=("Comic Sans MS", 13, "bold"), bg="#E6E6FA", fg="#00008B").grid(row=1, column=0, pady=10, padx=10, sticky="e")
tk.Label(result_frame, textvariable=category, font=("Comic Sans MS", 13), bg="#E6E6FA", fg="#00008B").grid(row=1, column=1, pady=10, padx=10, sticky="w")

footer = tk.Label(root, text="Stay Healthy", font=("Comic Sans MS", 10, "italic"), bg="#FFFAF0", fg="#808080")
footer.pack(pady=10)

root.mainloop()