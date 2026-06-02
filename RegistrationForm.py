import tkinter as tk
from tkinter import messagebox

def register():
    name = name1.get()
    surname = surname1.get()
    age = age1.get()
    email = email1.get()
    password = password1.get()
    gender = gender1.get()
    if gender == "":
        messagebox.showerror("Error", "Please select gender")
        return

    if not name or not surname or not age or not email or not password:
        messagebox.showerror("Error", "Fill all fields!")
        return

    with open("users.txt", "a") as file:
        data = name + "," + surname + "," + age + "," + email + "," + password + "," + gender + "\n"
        file.write(data)
    messagebox.showinfo("Success", "You have successfully registered!")

login_window = tk.Tk()
login_window.title("Registration")
login_window.geometry("400x350")
login_window.config(bg="#0f0f0f")

card = tk.Frame(login_window, bg="#121212")
card.place(relx=0.5, rely=0.5, anchor="center")

FirstLabel = tk.Label(
    card,
    text="Registration",
    bg="#121212",
    fg="white",
    font=("Segoe UI", 20, "bold")
)
FirstLabel.grid(row=0, column=0, columnspan=2, pady=15)

def create_label(text, row):
    tk.Label(
        card,
        text=text,
        bg="#121212",
        fg="#cfcfcf",
        font=("Segoe UI", 10)
    ).grid(row=row, column=0, sticky="w", padx=10, pady=5)

def create_entry(row, show=None):
    entry = tk.Entry(
        card,
        bg="#1e1e1e",
        fg="#e0e0e0",
        insertbackground="white",
        highlightbackground="#2ecc71",
        highlightcolor="#2ecc71",
        highlightthickness=1,
        relief="flat",
        font=("Segoe UI", 11),
        width=25,
        show=show
    )
    entry.grid(row=row, 
               column=1,
               padx=10,
               pady=5)
    return entry

create_label("Name", 1)
name1 = create_entry(1)

create_label("Surname", 2)
surname1 = create_entry(2)

create_label("Age", 3)
age1 = create_entry(3)

create_label("Email", 4)
email1 = create_entry(4)

create_label("Password", 5)
password1 = create_entry(5, show="•")

gender1 = tk.StringVar()
tk.Label(
    card,
    text="Gender",
    bg="#121212",
    fg="#cfcfcf",
    font=("Segoe UI", 10)
).grid(row=6, column=0, sticky="w", padx=10, pady=5)
tk.Radiobutton(
    card,
    text="Male",
    variable=gender1,
    value="Male",
    bg="#121212",
    fg="white",
    selectcolor="#0f0f0f"
).grid(row=6, column=1, sticky="w")

tk.Radiobutton(
    card,
    text="Female",
    variable=gender1,
    value="Female",
    bg="#121212",
    fg="white",
    selectcolor="#0f0f0f"
).grid(row=6, column=1, sticky="e")

tk.Button(
    card,
    text="Register",
    bg="#1e7f3f",
    fg="white",
    activebackground="#2ecc71",
    activeforeground="white",
    relief="flat",
    font=("Segoe UI", 11),
    cursor="hand2",
    width=25,
    command=register
).grid(row=7, column=0, columnspan=2, pady=15)

login_window.mainloop()