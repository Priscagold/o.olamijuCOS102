from tkinter import *
from tkinter import messagebox

def calculate_fee():
    try:
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for weight.")
        return

    location = location_var.get()

    if location == "Ibeju-Lekki":
        if weight >= 10:
            fee = 5000
        else:
            fee = 3500
    elif location == "Epe":
        if weight >= 10:
            fee = 10000
        else:
            fee = 5000
    else:
        fee = 0

    result_label.config(text="Delivery Fee: ₦" + str(fee))

# Window setup
window = Tk()
window.title("Delivery Fee Calculator")

Label(window, text="Package Weight (kg):").pack()
weight_entry = Entry(window)
weight_entry.pack()

Label(window, text="Select Location:").pack()
location_var = StringVar()
location_var.set("Ibeju-Lekki")
OptionMenu(window, location_var, "Ibeju-Lekki", "Epe").pack()

Button(window, text="Calculate", command=calculate_fee).pack()

result_label = Label(window, text="Delivery Fee: ₦0")
result_label.pack()

window.mainloop()
