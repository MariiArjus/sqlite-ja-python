import tkinter as tk
from tkinter import messagebox
import sqlite3

# --- 3. ANDMETE SISESTAMINE ANDMEBAASI ---
def salvesta_andmed():
    pealkiri = ent_pealkiri.get()
    aasta = ent_aasta.get()
    reiting = ent_reiting.get()

    # --- 2. VALIDEERIMINE ---
    if not pealkiri or not aasta or not reiting:
        messagebox.showwarning("Viga", "Kõik väljad peavad olema täidetud!")
        return

    try:
        aasta = int(aasta)
        reiting = float(reiting)
        
        if not (0 <= reiting <= 10):
            messagebox.showwarning("Viga", "Reiting peab olema vahemikus 0-10!")
            return
    except ValueError:
        messagebox.showerror("Viga", "Aasta ja reiting peavad olema numbrilised!")
        return

    # Andmebaasi toimingud
    try:
        conn = sqlite3.connect('filmid.db')
        c = conn.cursor()
        
        # Loome tabeli, kui seda veel pole
        c.execute('''CREATE TABLE IF NOT EXISTS filmid 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, pealkiri TEXT, aasta INTEGER, reiting REAL)''')
        
        # Kasutame parameetritega päringut (?) turvalisuse tagamiseks
        c.execute("INSERT INTO filmid (pealkiri, aasta, reiting) VALUES (?, ?, ?)", 
                  (pealkiri, aasta, reiting))
        
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Edu", "Andmed on edukalt salvestatud!")
        
        # --- 4. VÄLJADE TÜHJENDAMINE ---
        ent_pealkiri.delete(0, tk.END)
        ent_aasta.delete(0, tk.END)
        ent_reiting.delete(0, tk.END)
        
    except Exception as e:
        messagebox.showerror("Andmebaasi viga", f"Tekkis viga: {e}")

# --- 1. GRAAFILISE LIIDESE (GUI) LOOMINE ---
root = tk.Tk()
root.title("Filmi andmete sisestamine")
root.geometry("300x200")

# Sildid ja sisestusväljad kasutades .grid() meetodit
tk.Label(root, text="Filmi pealkiri:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
ent_pealkiri = tk.Entry(root)
ent_pealkiri.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Aasta:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
ent_aasta = tk.Entry(root)
ent_aasta.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Reiting (0-10):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
ent_reiting = tk.Entry(root)
ent_reiting.grid(row=2, column=1, padx=10, pady=5)

# Salvestamise nupp
btn_lisa = tk.Button(root, text="Lisa andmebaasi", command=salvesta_andmed)
btn_lisa.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()