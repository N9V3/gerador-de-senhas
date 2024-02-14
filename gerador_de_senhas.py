import tkinter as tk
from tkinter import messagebox
import string as st
import numpy as np
import pyperclip

def criar_senha():
    algarismos = ""
    if incluir_letras.get():
        algarismos += st.ascii_letters
    if incluir_numeros.get():
        algarismos += st.digits
    if incluir_especiais.get():
        algarismos += st.punctuation

    if not algarismos:
        messagebox.showwarning(lang_dict["Warning"], lang_dict["Select_character_type"])
        return

    senha = np.random.choice(list(algarismos), tamanho_senha.get())
    senha_gerada.set(''.join(senha))
    btn_criar_senha.config(state=tk.DISABLED)  # Desabilita o botão "Criar Senha"
    btn_copiar_senha.config(state=tk.NORMAL)  # Habilita o botão "Copiar Senha"

def refazer_senha():
    criar_senha()

def copiar_senha():
    pyperclip.copy(senha_gerada.get())
    messagebox.showinfo(lang_dict["Title"], lang_dict["Password_Copied"])

def habilitar_btn_criar_senha():
    btn_criar_senha.config(state=tk.NORMAL)
    btn_copiar_senha.config(state=tk.DISABLED)

def change_language(lang):
    global lang_dict
    if lang == "Português":
        lang_dict = {
            "Title": "Gerador de Senhas",
            "Letters": "Letras",
            "Numbers": "Números",
            "Specials": "Especiais",
            "Password_Size": "Tamanho da Senha:",
            "Create_Password": "Criar Senha",
            "Recreate_Password": "Refazer Senha",
            "Copy_Password": "Copiar Senha",
            "Password_Copied": "Senha copiada para a área de transferência.",
            "Warning": "Escolha seu idioma",
            "Select_character_type": "Selecione pelo menos um tipo de caractere para a senha."
        }
    elif lang == "English":
        lang_dict = {
            "Title": "Password Generator",
            "Letters": "Letters",
            "Numbers": "Numbers",
            "Specials": "Specials",
            "Password_Size": "Password Size:",
            "Create_Password": "Create Password",
            "Recreate_Password": "Recreate Password",
            "Copy_Password": "Copy Password",
            "Password_Copied": "Password copied to clipboard.",
            "Warning": "Choose your language",
            "Select_character_type": "Select at least one character type for the password."
        }
    elif lang == "Español":
        lang_dict = {
            "Title": "Generador de Contraseñas",
            "Letters": "Letras",
            "Numbers": "Números",
            "Specials": "Especiales",
            "Password_Size": "Tamaño de la Contraseña:",
            "Create_Password": "Crear Contraseña",
            "Recreate_Password": "Rehacer Contraseña",
            "Copy_Password": "Copiar Contraseña",
            "Password_Copied": "Contraseña copiada al portapapeles.",
            "Warning": "Seleccione su idioma",
            "Select_character_type": "Seleccione al menos un tipo de carácter para la contraseña."
        }
    
    root.title(lang_dict["Title"])
    lbl_tamanho_senha.config(text=lang_dict["Password_Size"])
    btn_criar_senha.config(text=lang_dict["Create_Password"])
    btn_refazer_senha.config(text=lang_dict["Recreate_Password"])
    btn_copiar_senha.config(text=lang_dict["Copy_Password"])
    lbl_warning.config(text=lang_dict["Warning"])
    update_button_text()

def update_button_text():
    btn_letras.config(text=lang_dict["Letters"])
    btn_numeros.config(text=lang_dict["Numbers"])
    btn_especiais.config(text=lang_dict["Specials"])

# Configurações da janela que abre
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("320x350")  # Definindo o tamanho da janela

# Variáveis para controlar a seleção dos tipos de caracteres
incluir_letras = tk.BooleanVar()
incluir_numeros = tk.BooleanVar()
incluir_especiais = tk.BooleanVar()

# Variável para armazenar o tamanho da senha
tamanho_senha = tk.IntVar()
tamanho_senha.set(16)  # Tamanho padrão da senha

# Dicionário de idiomas
lang_dict = {
    "Title": "Gerador de Senhas",
    "Letters": "Letras",
    "Numbers": "Números",
    "Specials": "Especiais",
    "Password_Size": "Tamanho da Senha:",
    "Create_Password": "Criar Senha",
    "Recreate_Password": "Refazer Senha",
    "Copy_Password": "Copiar Senha",
    "Password_Copied": "Senha copiada para a área de transferência.",
    "Warning": "Escolha seu idioma",
    "Select_character_type": "Selecione pelo menos um tipo de caractere para a senha."
}

# Frame para organizar os widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Botões para selecionar os tipos de caracteres
btn_letras = tk.Checkbutton(frame, text=lang_dict["Letters"], variable=incluir_letras)
btn_letras.pack(side=tk.LEFT, padx=5)
btn_numeros = tk.Checkbutton(frame, text=lang_dict["Numbers"], variable=incluir_numeros)
btn_numeros.pack(side=tk.LEFT, padx=5)
btn_especiais = tk.Checkbutton(frame, text=lang_dict["Specials"], variable=incluir_especiais)
btn_especiais.pack(side=tk.LEFT, padx=5)

# Slider para selecionar o tamanho da senha
lbl_tamanho_senha = tk.Label(root, text=lang_dict["Password_Size"])
lbl_tamanho_senha.pack()
slider_tamanho_senha = tk.Scale(root, from_=8, to=24, orient=tk.HORIZONTAL, variable=tamanho_senha, length=200)
slider_tamanho_senha.pack()

# Botão para criar senha
btn_criar_senha = tk.Button(root, text=lang_dict["Create_Password"], command=criar_senha)
btn_criar_senha.pack(pady=5)

# Botão para refazer senha
btn_refazer_senha = tk.Button(root, text=lang_dict["Recreate_Password"], command=refazer_senha)
btn_refazer_senha.pack(pady=5)

# Label para exibir a senha gerada
senha_gerada = tk.StringVar()
lbl_senha = tk.Label(root, textvariable=senha_gerada, font=("Helvetica", 12), wraplength=300)
lbl_senha.pack(pady=10)

# Botão para copiar senha
btn_copiar_senha = tk.Button(root, text=lang_dict["Copy_Password"], command=copiar_senha, state=tk.DISABLED)
btn_copiar_senha.pack(pady=5)

# Label para exibir avisos
lbl_warning = tk.Label(root, text=lang_dict["Warning"], fg="black")
lbl_warning.pack()

# Botões para seleção de idioma
language_frame = tk.Frame(root)
language_frame.pack(pady=10)

languages = ["Português", "English", "Español"]
selected_language = tk.StringVar()
for lang in languages:
    tk.Radiobutton(language_frame, text=lang, variable=selected_language, value=lang, command=lambda l=lang: change_language(l)).pack(side=tk.LEFT, padx=5)

root.mainloop()
