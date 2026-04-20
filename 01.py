import tkinter as tk
from tkinter import messagebox
import sqlite3

# --- ANDMETE SISESTAMINE ANDMEBAASI ---
def salvesta_andmed():
    pealkiri = ent_pealkiri.get()
    aasta = ent_aasta.get()
    hinnang = ent_hinnang.get()

    # --- VALIDEERIMINE ---
    if not pealkiri or not aasta or not hinnang:
        messagebox.showwarning("Viga", "Kõik väljad peavad olema täidetud!")
        return

    try:
        aasta = int(aasta)
        hinnang = float(hinnang)
        
        if not (0 <= hinnang <= 10):
            messagebox.showwarning("Viga", "Hinnang peab olema vahemikus 0-10!")
            return
    except ValueError:
        messagebox.showerror("Viga", "Aasta ja hinnang peavad olema numbrilised!")
        return

    # Andmebaasi toimingud
    try:
        conn = sqlite3.connect('raamatud.db')
        c = conn.cursor()
        
        # Loome tabeli, kui seda veel pole
        c.execute('''CREATE TABLE IF NOT EXISTS raamatud 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, pealkiri TEXT, aasta INTEGER, hinnang REAL)''')
        
        # Lisame andmed
        c.execute("INSERT INTO raamatud (pealkiri, aasta, hinnang) VALUES (?, ?, ?)", 
                  (pealkiri, aasta, hinnang))
        
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Edu", "Raamatu andmed on edukalt salvestatud!")
        
        # --- VÄLJADE TÜHJENDAMINE ---
        ent_pealkiri.delete(0, tk.END)
        ent_aasta.delete(0, tk.END)
        ent_hinnang.delete(0, tk.END)
        
    except Exception as e:
        messagebox.showerror("Andmebaasi viga", f"Tekkis viga: {e}")

# --- GRAAFILISE LIIDESE LOOMINE ---
root = tk.Tk()
root.title("Raamatu andmete sisestamine")
root.geometry("300x200")

# Sildid ja sisestusväljad
tk.Label(root, text="Raamatu pealkiri:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
ent_pealkiri = tk.Entry(root)
ent_pealkiri.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Ilmumisaasta:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
ent_aasta = tk.Entry(root)
ent_aasta.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Hinnang (0-10):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
ent_hinnang = tk.Entry(root)
ent_hinnang.grid(row=2, column=1, padx=10, pady=5)

# Salvestamise nupp
btn_lisa = tk.Button(root, text="Lisa andmebaasi", command=salvesta_andmed)
btn_lisa.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()