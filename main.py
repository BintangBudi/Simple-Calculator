import tkinter as tk

def calculate_discount():
    # Retrieve user input values as floats
    price = float(entry_price.get())
    discount = float(entry_discount.get())
    
    # Calculate final price after discount
    final_price = price - (price * (discount / 100))
    
    # Update the result label
    label_result.config(text=f"Final Price: Rp. {final_price:.2f}")

# 1. Main Window Setup
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("320x260")

# 2. Original Price Section
label_price = tk.Label(root, text="Original Price:")
label_price.pack(pady=(15, 2))

entry_price = tk.Entry(root, justify="center")
entry_price.pack(pady=2)

# 3. Discount (%) Section
label_discount = tk.Label(root, text="Discount (%):")
label_discount.pack(pady=(10, 2))

entry_discount = tk.Entry(root, justify="center")
entry_discount.pack(pady=2)

# 4. Calculate Button
btn_calculate = tk.Button(root, text="Calculate", command=calculate_discount)
btn_calculate.pack(pady=15)

# 5. Final Price Result Display
label_result = tk.Label(root, text="Final Price: Rp. 0.00", font=("Arial", 10))
label_result.pack(pady=5)

# Run GUI Event Loop
root.mainloop()