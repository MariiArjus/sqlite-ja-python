import tkinter as tk
from tkinter import messagebox
import sqlite3

def loe_andmed():
    """Värskendab nimekirja andmetega andmebaasist."""
    lb.delete(0, tk.END)
    conn = sqlite3.connect('filmid.db')
    c = conn.cursor()
    c.execute("SELECT id, pealkiri FROM filmid")
    for rida in c.fetchall():
        lb.insert(tk.END, f"{rida[0]} | {rida[1]}")
    conn.close()

def kustuta_kirje():
    """Kustutab valitud kirje andmebaasist."""
    try:
        # 1. Võtame nimekirjast valitud rea
        valitud_indeks = lb.curselection()
        if not valitud_indeks:
            messagebox.showwarning("Hoiatus", "Vali esmalt kirje, mida soovid kustutada!")
            return
        
        tekst = lb.get(valitud_indeks)
        id_kustutamiseks = tekst.split(" | ")[0]
        pealkiri = tekst.split(" | ")[1]

        # 2. Küsime kinnitust
        vastus = messagebox.askyesno("Kinnita kustutamine", f"Kas oled kindel, et soovid kustutada filmi: {pealkiri}?")
        
        if vastus:
            # 3. Teostame kustutamise
            conn = sqlite3.connect('filmid.db')
            c = conn.cursor()
            c.execute("DELETE FROM filmid WHERE id=?", (id_kustutamiseks,))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Tehtud", "Kirje on andmebaasist eemaldatud.")
            loe_andmed() # Värskendame vaadet

    except Exception as e:
        messagebox.showerror("Viga", f"Kustutamisel tekkis viga: {e}")

# --- GUI ---
root = tk.Tk()
root.title("Andmete kustutamine")
root.geometry("300x350")

tk.Label(root, text="Vali kustutatav film:", font=("Arial", 10, "bold")).pack(pady=5)

# Nimekiri
lb = tk.Listbox(root, width=40, height=10)
lb.pack(padx=10, pady=5)

# Kustutamise nupp
btn_kustuta = tk.Button(root, text="Kustuta valitud kirje", 
                        fg="white", bg="red", # Teeme nupu punaseks, et hoiatada
                        command=kustuta_kirje)
btn_kustuta.pack(pady=20)

# Laeme andmed sisse
loe_andmed()

root.mainloop()