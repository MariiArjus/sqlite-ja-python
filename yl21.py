import tkinter as tk
from tkinter import messagebox
import sqlite3


def loe_andmed():
    lb.delete(0, tk.END)
    conn = sqlite3.connect('raamatud.db')
    c = conn.cursor()
    c.execute("SELECT * FROM raamatud")
    for rida in c.fetchall():
        lb.insert(tk.END, f"{rida[0]} | {rida[1]} | {rida[2]}")
    conn.close()

def vali_kirje(event):
    try:
        valitud = lb.get(lb.curselection())
        id_numbri = valitud.split(" | ")[0]
        
        conn = sqlite3.connect('raamatud.db')
        c = conn.cursor()
        c.execute("SELECT * FROM raamatud WHERE id=?", (id_numbri,))
        kirje = c.fetchone()
        conn.close()

        ent_id.config(state='normal')
        ent_id.delete(0, tk.END)
        ent_id.insert(0, kirje[0])
        ent_id.config(state='readonly')
        
        ent_pealkiri.delete(0, tk.END)
        ent_pealkiri.insert(0, kirje[1])
        
        ent_aasta.delete(0, tk.END)
        ent_aasta.insert(0, kirje[2])
    except:
        pass

def uuenda_andmeid():
    id_muudetav = ent_id.get()
    uus_pealkiri = ent_pealkiri.get()
    uus_aasta = ent_aasta.get()

    if not id_muudetav:
        messagebox.showwarning("Viga", "Vali esmalt raamat, mida muuta!")
        return

    conn = sqlite3.connect('raamatud.db')
    c = conn.cursor()
    c.execute("UPDATE raamatud SET pealkiri=?, aasta=? WHERE id=?", 
              (uus_pealkiri, uus_aasta, id_muudetav))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Edu", "Raamatu andmed uuendatud!")
    loe_andmed()

root = tk.Tk()
root.title("Raamatute muutmine")

lb = tk.Listbox(root, width=40)
lb.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
lb.bind('<<ListboxSelect>>', vali_kirje)

tk.Label(root, text="ID (lukus):").grid(row=1, column=0)
ent_id = tk.Entry(root, state='readonly')
ent_id.grid(row=1, column=1)

tk.Label(root, text="Pealkiri:").grid(row=2, column=0)
ent_pealkiri = tk.Entry(root)
ent_pealkiri.grid(row=2, column=1)

tk.Label(root, text="Ilmumisaasta:").grid(row=3, column=0)
ent_aasta = tk.Entry(root)
ent_aasta.grid(row=3, column=1)

tk.Button(root, text="Uuenda raamatut", command=uuenda_andmeid).grid(row=4, column=0, columnspan=2, pady=10)

loe_andmed()
root.mainloop()
loe_andmed()
root.mainloop()
