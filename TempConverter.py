import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    temp = float(entry_temp.get())
    if conversion_var.get() == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(temp)
        label_result.config(text=f"{temp}°C is equal to {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(temp)
        label_result.config(text=f"{temp}°F is equal to {result:.2f}°C")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create a frame for the input and dropdown
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, padx=10, pady=10)

# Temperature input
label_temp = ttk.Label(frame, text="Enter temperature:")
label_temp.grid(row=0, column=0, padx=5, pady=5)

entry_temp = ttk.Entry(frame)
entry_temp.grid(row=0, column=1, padx=5, pady=5)

# Conversion direction dropdown
conversion_var = tk.StringVar(value="Celsius to Fahrenheit")
dropdown_conversion = ttk.Combobox(frame, textvariable=conversion_var, state="readonly")
dropdown_conversion['values'] = ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
dropdown_conversion.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Convert button
button_convert = ttk.Button(frame, text="Convert", command=convert_temperature)
button_convert.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Result label
label_result = ttk.Label(frame, text="")
label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()