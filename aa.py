import tkinter as tk
from tkinter import ttk

def calculate_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    interest = (principal * rate * time) / 100
    result_label.config(text=f"Simple Interest: {interest}")

# Create the main window
root = tk.Tk()
root.title("Simple Interest Calculator")

# Create and place the principal amount entry
ttk.Label(root, text="Principal Amount:").grid(column=0, row=0, padx=10, pady=5)
principal_entry = ttk.Entry(root)
principal_entry.grid(column=1, row=0, padx=10, pady=5)

# Create and place the rate of interest entry
ttk.Label(root, text="Rate of Interest (%):").grid(column=0, row=1, padx=10, pady=5)
rate_entry = ttk.Entry(root)
rate_entry.grid(column=1, row=1, padx=10, pady=5)

# Create and place the time period entry
ttk.Label(root, text="Time Period (years):").grid(column=0, row=2, padx=10, pady=5)
time_entry = ttk.Entry(root)
time_entry.grid(column=1, row=2, padx=10, pady=5)

# Create and place the calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Create and place the result label
result_label = ttk.Label(root, text="Simple Interest: ")
result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()

