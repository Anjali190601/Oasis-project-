import tkinter as tk
import random

def generate_weather():
    cities = ["New York", "Tokyo", "London", "Mumbai", "Sydney"]
    weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]
    temperatures = list(range(-10, 40))

    city = random.choice(cities)
    condition = random.choice(weather_conditions)
    temp = random.choice(temperatures)

    output_label.config(text=f"City: {city}\nWeather: {condition}\nTemp: {temp}°C")

root = tk.Tk()
root.title("Weather Assumption App")
root.geometry("300x200")

title = tk.Label(root, text="Assumed Weather", font=("Helvetica", 16))
title.pack(pady=10)

generate_btn = tk.Button(root, text="Generate Weather", command=generate_weather)
generate_btn.pack(pady=5)

output_label = tk.Label(root, text="", font=("Helvetica", 12))
output_label.pack(pady=10)

root.mainloop()