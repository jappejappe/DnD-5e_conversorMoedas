import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

materiais = [
    "Cobre",
    "Prata",
    "Electro",
    "Ouro",
    "Platina"
]

def converter_moeda(moeda_origem, moeda_destino, quantidade):
    valores_em_cobre = {
        'cobre': 1,
        'prata': 10,
        'electro': 50,
        'ouro': 100,
        'platina': 1000
    }
    
    origem = moeda_origem.lower()
    destino = moeda_destino.lower()
    
    total_em_cobre = quantidade * valores_em_cobre[origem]
    
    resultado = int(total_em_cobre // valores_em_cobre[destino])
    resto_em_cobre = total_em_cobre % valores_em_cobre[destino]
    sobra_moeda_origem = resto_em_cobre // valores_em_cobre[origem]

    messagebox.showinfo("Resultado", f"Você possui {resultado} moedas de {moeda_destino.capitalize()}.\nSobraram {sobra_moeda_origem} moedas de {moeda_origem.capitalize()}.")
    return resultado

#######################################################################################################
#### INTERFACE GRÁFICA
root = tk.Tk()
root.geometry("400x550")
root.title("Conversor de Moedas D&D 5E")

try:
    caminho_tema = resource_path("azure.tcl")
    root.tk.call("source", caminho_tema)
    root.tk.call("set_theme", "dark")
except tk.TclError:
    print("Aviso: Tema azure.tcl não encontrado. O app rodará com o tema padrão.")

def change_theme():
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        root.tk.call("set_theme", "light")
    else:
        root.tk.call("set_theme", "dark")

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

header_frame = ttk.Frame(main_frame)
header_frame.pack(fill="x", pady=(0, 20)) 

header_frame.columnconfigure(0, weight=1)

# Título
title_label = ttk.Label(header_frame, text="Moedas D&D", font=("Segoe UI", 20, "bold"))
title_label.grid(row=0, column=0, sticky="w")

# Botão de tema
theme_button = ttk.Label(header_frame, text="◐", cursor="hand2", font=("Segoe UI", 20, "bold"))
theme_button.grid(row=0, column=1, sticky="e") 
theme_button.bind("<Button-1>", lambda e: change_theme())

# Grupo: Moeda de origem
frame_origem = ttk.LabelFrame(main_frame, text=" Moeda de Origem ", padding=15)
frame_origem.pack(fill="x", pady=(0, 15))

ttk.Label(frame_origem, text="Tipo de moeda que possui:").pack(anchor="w", pady=(0, 5))
combo_origem = ttk.Combobox(frame_origem, values=materiais, state="readonly")
combo_origem.current(0)
combo_origem.pack(fill="x", pady=(0, 15))

ttk.Label(frame_origem, text="Quantidade:").pack(anchor="w", pady=(0, 5))
amount_var = tk.IntVar(value=0)
amount = ttk.Spinbox(frame_origem, from_=0, to=99999, increment=1, textvariable=amount_var)
amount.pack(fill="x")

# Grupo: Moeda de destino
frame_destino = ttk.LabelFrame(main_frame, text=" Moeda de Destino ", padding=15)
frame_destino.pack(fill="x", pady=(0, 25))

ttk.Label(frame_destino, text="Converter para:").pack(anchor="w", pady=(0, 5))
combo_destino = ttk.Combobox(frame_destino, values=materiais, state="readonly")
combo_destino.current(0)
combo_destino.pack(fill="x")

# Botão de conversão
btn_converter = ttk.Button(
    main_frame,
    text="Converter",
    style="Accent.TButton",
    command=lambda: converter_moeda(combo_origem.get(), combo_destino.get(), amount_var.get())
)

btn_converter.pack(fill="x", ipady=5) 

root.mainloop()
#######################################################################################################