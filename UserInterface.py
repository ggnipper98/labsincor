import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import urllib.request

import extractor

def download_file(url):
    # Download the file from the web link
    response = urllib.request.urlopen(url)

    # Read the contents of the file
    file_contents = response.read()

    # Write the contents to a local file
    with open("downloaded_file.pdf", "wb") as f:
        f.write(file_contents)

def on_focus_in(event):
    # Delete the default text when the input field is clicked
    link_input.delete(0, tk.END)

def process_link():
    # Get the web link from the input field
    link = link_input.get()

    # Download the file from the web link
    download_file(link)

    # Process the downloaded file
    contents = extractor.extractor("downloaded_file.pdf")

    # Display the contents of the file in the text window
    text_window.insert(tk.END, contents + "\n" +  "\n")


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

def open_website():
    # Open the website in the default web browser
    webbrowser.open("https://github.com/ggnipper98/labsincor")

# Create the main window
window = tk.Tk()
window.title("LabsInCor")

# Create a frame for the top menu
top_menu = tk.Frame(window)

# Create a button for showing the "About" message box
about_button = tk.Button(top_menu, text="Sobre", command=show_about)
about_button.pack(side=tk.LEFT)

# Create the button
website_button = tk.Button(window, text="Visitar o site", command=open_website)


# Add the top menu to the main window
website_button.pack(side=tk.BOTTOM, fill=tk.X)
top_menu.pack(side=tk.TOP, fill=tk.X)

# Configure the button's style
website_button.configure(background="#f0f0f0", foreground="#000000", font=("Arial", 10))

# Configure the style of the about button
about_button.configure(background="#f0f0f0", foreground="#000000", font=("Arial", 10))


# Create an input field for the web link
link_input = tk.Entry(window)
link_input.insert(0, "Cole aqui o link para os exames")
link_input.configure(width=len("Cole aqui o link para os exames"),font=("Arial", 14), justify="center")  # <-- Set the default text
link_input.pack()

# Bind the on_focus_in function to the focus-in event
link_input.bind("<FocusIn>", on_focus_in)
# Create a button for processing the web link
process_button = tk.Button(window, text="Obter Exames do Link", command=process_link)
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