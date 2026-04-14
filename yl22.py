import tkinter as tk
from tkinter import messagebox
import sqlite3

def loe_andmed():
    lb.delete(0, tk.END)
    conn = sqlite3.connect('raamatud.db')
    c = conn.cursor()
    c.execute("SELECT id, pealkiri FROM raamatud")
    for rida in c.fetchall():
        lb.insert(tk.END, f"{rida[0]} | {rida[1]}")
    conn.close()

def kustuta_kirje():
    try:
        valitud_indeks = lb.curselection()
        if not valitud_indeks:
            messagebox.showwarning("Hoiatus", "Vali esmalt raamat, mida soovid kustutada!")
            return
        
        tekst = lb.get(valitud_indeks)
        id_kustutamiseks = tekst.split(" | ")[0]
        pealkiri = tekst.split(" | ")[1]

        vastus = messagebox.askyesno(
            "Kinnita kustutamine", 
            f"Kas oled kindel, et soovid kustutada raamatu: {pealkiri}?"
        )
        
        if vastus:
            conn = sqlite3.connect('raamatud.db')
            c = conn.cursor()
            c.execute("DELETE FROM raamatud WHERE id=?", (id_kustutamiseks,))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Tehtud", "Raamat on andmebaasist eemaldatud.")
            loe_andmed()

    except Exception as e:
        messagebox.showerror("Viga", f"Kustutamisel tekkis viga: {e}")

root = tk.Tk()
root.title("Raamatute kustutamine")
root.geometry("300x350")

tk.Label(root, text="Vali kustutatav raamat:", font=("Arial", 10, "bold")).pack(pady=5)

lb = tk.Listbox(root, width=40, height=10)
lb.pack(padx=10, pady=5)

btn_kustuta = tk.Button(root, text="Kustuta valitud raamat", 
                        fg="white", bg="red",
                        command=kustuta_kirje)
btn_kustuta.pack(pady=20)

loe_andmed()

root.mainloop()
