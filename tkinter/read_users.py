import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Filmid")


# Loo raam kerimisribaga
frame = tk.Frame(root)
frame.pack(pady=20, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Loo tabel (Treeview) andmete kuvamiseks
tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("first_name", "last_name", "email", "gender", "image"), show="headings")
tree.pack(fill=tk.BOTH, expand=True)


# Seosta kerimisriba tabeliga
scrollbar.config(command=tree.yview)


# Määra veergude pealkirjad ja laius
tree.heading("first_name", text="Eesnimi")
tree.heading("last_name", text="Perenimi")
tree.heading("email", text="Email")
tree.heading("phone", text="Telefon")
tree.heading("image", text="Pilt")

tree.column("first_name", width=150)
tree.column("last_name", width=150)
tree.column("email", width=160)
tree.column("phone", width=150)
tree.column("image", width=160)


# Käivita Tkinteri tsükkel
root.mainloop()