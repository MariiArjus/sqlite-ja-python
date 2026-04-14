import tkinter as tk
from tkinter import messagebox
import sqlite3

def kuva_andmed():
    listbox.delete(0, tk.END)
    
    try:
        conn = sqlite3.connect('raamatud.db')
        c = conn.cursor()
        
        c.execute("SELECT id, pealkiri, aasta, hinnang FROM raamatud")
        tulemused = c.fetchall()
        
        for rida in tulemused:
            tekst = f"{rida[0]}. {rida[1]} ({rida[2]}) - Hinnang: {rida[3]}"
            listbox.insert(tk.END, tekst)
            
        conn.close()
        
    except Exception as e:
        messagebox.showerror("Viga", f"Andmete lugemisel tekkis viga: {e}")

root = tk.Tk()
root.title("Raamatukogu andmete kuvamine")
root.geometry("400x300")

tk.Label(root, text="Raamatukogu sisu:", font=("Arial", 12, "bold")).pack(pady=10)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(padx=10, pady=5)

btn_loe = tk.Button(root, text="Uuenda andmeid", command=kuva_andmed)
btn_loe.pack(pady=10)

kuva_andmed()

root.mainloop()
