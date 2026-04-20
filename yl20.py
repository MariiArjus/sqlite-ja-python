import tkinter as tk
from tkinter import messagebox
import sqlite3

def kuva_andmed():
    # 1. Tühjendame Listboxi vanadest andmetest
    listbox.delete(0, tk.END)
    
    try:
        # 2. Ühendus andmebaasiga
        conn = sqlite3.connect('raamatud.db')
        c = conn.cursor()
        
        # 3. Päringu teostamine
        c.execute("SELECT id, pealkiri, aasta, hinnang FROM raamatud")
        tulemused = c.fetchall()
        
        # 4. Andmete lisamine Listboxi
        for rida in tulemused:
            tekst = f"{rida[0]}. {rida[1]} ({rida[2]}) - Hinnang: {rida[3]}"
            listbox.insert(tk.END, tekst)
            
        conn.close()
        
    except Exception as e:
        messagebox.showerror("Viga", f"Andmete lugemisel tekkis viga: {e}")

# --- GUI LOOMINE ---
root = tk.Tk()
root.title("Raamatukogu andmete kuvamine")
root.geometry("400x300")

# Silt
tk.Label(root, text="Raamatukogu sisu:", font=("Arial", 12, "bold")).pack(pady=10)

# Listbox andmete kuvamiseks
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(padx=10, pady=5)

# Nupp andmete uuendamiseks/lugemiseks
btn_loe = tk.Button(root, text="Uuenda andmeid", command=kuva_andmed)
btn_loe.pack(pady=10)

# Käivitame andmete lugemise kohe akna avanemisel
kuva_andmed()

root.mainloop()