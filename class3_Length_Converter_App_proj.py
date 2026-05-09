'''Length Converter App
Write a Python program to create an application length in inches as input from the user and return the value of 
that length in centimeters using the Python Tkinter library'''

import tkinter as tk

def convert_to_cm():
    try:
        # Get user input from the entry widget
        inches = float(entry_inches.get())
        
        # Perform conversion (1 inch = 2.54 cm)
        cm = inches * 2.54
        
        # Display the result formatted to 2 decimal places
        label_result.config(text=f"Result: {cm:.2f} cm", fg="black")
    except ValueError:
        # Handle cases where input is not a valid number
        label_result.config(text="Please enter a valid number", fg="red")

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("300x200")

# Create and place UI elements
tk.Label(root, text="Enter length in inches:", font=("Arial", 10)).pack(pady=10)

entry_inches = tk.Entry(root)
entry_inches.pack(pady=5)

convert_btn = tk.Button(root, text="Convert", command=convert_to_cm, bg="lightblue")
convert_btn.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 10, "bold"))
label_result.pack(pady=10)

# Run the application
root.mainloop()
