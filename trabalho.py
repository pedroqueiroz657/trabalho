import tkinter as tk
from tkinter import messagebox
import os

def extract_radicals(words):
    radicals = set()
    for word in words:
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                radicals.add(word[i:j])
    return list(radicals)

def classify_message(message):
    palavras_improprias = ['arromb', 'put', 'caralh',]
    elogios = ['ótimo', 'ótima', 'maravilhoso', 'maravilhosa', 'excelente', 'fantástico', 'esplêndido', 'incrível',
               'perfeito', 'fenomenal', 'formidável', 'excepcional', 'brilhante', 'sensacional', 'impressionante',
               'extraordinário', 'supremo', 'sublime', 'magnífico', 'notável', 'fabuloso', 'genial', 'único', 'grande',
               'admirável']

    elogio_radicals = extract_radicals(elogios)

    for palavra in palavras_improprias:
        if palavra in message.lower():
            return "impropria"

    for radical in elogio_radicals:
        if radical in message.lower():
            return "elogio"

    return "reclamacao"

def save_message(message, classification):
    filename = f"{classification}s.txt"
    with open(filename, "a") as file:
        file.write(message + "\n")

def classify_and_save_message():
    message = message_entry.get()
    classification = classify_message(message)
    save_message(message, classification)
    messagebox.showinfo("Mensagem Registrada", "Mensagem registrada com sucesso!")

root = tk.Tk()
root.title("Registro de Mensagens")

message_label = tk.Label(root, text="Digite sua mensagem:")
message_label.pack()

message_entry = tk.Entry(root, width=50)
message_entry.pack()

classify_button = tk.Button(root, text="Registrar Mensagem", command=classify_and_save_message)
classify_button.pack()

exit_button = tk.Button(root, text="Sair", command=root.destroy)
exit_button.pack()

root.mainloop()
