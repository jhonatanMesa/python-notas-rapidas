import tkinter as tk
from tkinter import filedialog, messagebox

def guardar():
    contenido = txt.get("1.0", tk.END).strip()
    if not contenido:
        messagebox.showinfo("Notas", "No hay contenido para guardar.")
        return
    ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Texto", "*.txt")])
    if ruta:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        messagebox.showinfo("Notas", "Nota guardada.")

root = tk.Tk()
root.title("Notas Rápidas")
root.geometry("500x400")

txt = tk.Text(root, wrap="word")
txt.pack(fill="both", expand=True, padx=8, pady=8)

btn = tk.Button(root, text="Guardar", command=guardar)
btn.pack(pady=6)

root.mainloop()
