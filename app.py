import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk

root = tk.Tk()
root.title("Bloc de Note")
root = Style(theme="lumen")

# Etiquette
label = ttk.Label(root, text="Bloc de Note", style="info.tLabel")
label.pack(pady=15)

# Champ pour ajoueter une note
note_entry = ttk.Entry(root, whidth=60)
note_entry.pack(pady=10)
