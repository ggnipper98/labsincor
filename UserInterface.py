import tkinter as tk
from tkinter import filedialog, messagebox

import extractor

def select_file():
    # Abre um diálogo de seleção de arquivo e obtém o arquivo selecionado
    file_path = filedialog.askopenfilename()

    # Atualiza a etiqueta do caminho do arquivo com o arquivo selecionado
    file_label.config(text=file_path)

def process_file():
    # Obtém o caminho do arquivo da etiqueta do caminho do arquivo
    file_path = file_label.cget("text")

    # Realiza alguma ação no arquivo (por exemplo, lê o conteúdo)
    contents = extractor.extractor(file_path)

    # Exibe o conteúdo do arquivo na janela de texto
    text_window.insert(tk.END, contents + "\n" +  "\n" )

def clear_window():
    # Limpa o conteúdo da janela de texto
    text_window.delete(1.0, tk.END)

def copy_window():
    # Get the contents of the text window as a string
    contents = text_window.get(1.0, tk.END)[:-1]

    # Copy the contents to the clipboard
    tk.Tk().clipboard_append(contents)

def show_about():
    # Show an "About" message box
    messagebox.showinfo("Sobre", "Versão 1. acesse github.com/ggnipper98/labsincor para baixar, acessar o codigo fonte e ver os exames suportados. Reportar bugs ao email ")



# Create the main window
window = tk.Tk()

# Create a frame for the top menu
top_menu = tk.Frame(window)

# Create a button for showing the "About" message box
about_button = tk.Button(top_menu, text="Sobre", command=show_about)
about_button.pack(side=tk.LEFT)

# Add the top menu to the main window
top_menu.pack(side=tk.TOP, fill=tk.X)

# Configure the style of the about button
about_button.configure(background="#f0f0f0", foreground="#000000", font=("Arial", 10))


# Cria um botão para selecionar um arquivo
file_button = tk.Button(window, text="Selecionar arquivo", command=select_file)
file_button.pack()

# Cria uma etiqueta para exibir o caminho do arquivo
file_label = tk.Label(window, text="Nenhum arquivo selecionado")
file_label.pack()

# Cria um botão para processar o arquivo
process_button = tk.Button(window, text="Converter a texto", command=process_file)
process_button.pack()

# Cria uma janela de texto para exibir o conteúdo do arquivo
text_window = tk.Text(window)
text_window.pack()

# Create a button for copying the text window to the clipboard
copy_button = tk.Button(window, text="Copiar", command=copy_window)
copy_button.pack()


# Cria um botão para limpar a janela de texto
clear_button = tk.Button(window, text="Limpar", command=clear_window)
clear_button.pack()


# Inicia o loop de eventos do Tkinter
window.mainloop()