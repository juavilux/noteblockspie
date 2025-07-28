import tkinter as tk
from tkinter import filedialog, font

# Funções do bloco de notas
def abrir_arquivo():
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
    if caminho:
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
        texto.delete("1.0", tk.END)
        texto.insert(tk.END, conteudo)

def salvar_arquivo():
    caminho = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])
    if caminho:
        with open(caminho, "w", encoding="utf-8") as f:
            conteudo = texto.get("1.0", tk.END)
            f.write(conteudo)

def mudar_fonte(nome_fonte):
    fonte_atual.config(family=nome_fonte)

def zoom_in():
    tamanho = fonte_atual.cget("size")
    fonte_atual.config(size=tamanho + 2)

def zoom_out():
    tamanho = fonte_atual.cget("size")
    if tamanho > 6:
        fonte_atual.config(size=tamanho - 2)

# Criação da janela
janela = tk.Tk()
janela.title("NoteBlocksPie")

# Fonte padrão
fonte_atual = font.Font(family="Arial", size=14)

# Área de texto
texto = tk.Text(janela, bg="black", fg="red", font=fonte_atual, insertbackground="red", undo=True)
texto.pack(fill="both", expand=True)

# Menu
menu = tk.Menu(janela)
janela.config(menu=menu)

arquivo_menu = tk.Menu(menu, tearoff=0)
arquivo_menu.add_command(label="Abrir", command=abrir_arquivo)
arquivo_menu.add_command(label="Salvar", command=salvar_arquivo)
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=janela.quit)
menu.add_cascade(label="Arquivo", menu=arquivo_menu)

fonte_menu = tk.Menu(menu, tearoff=0)
# Lista de fontes fixas
fontes = ["Arial", "Courier New", "Times New Roman", "Helvetica", "Comic Sans MS"]
for f in fontes:
    fonte_menu.add_command(label=f, command=lambda f=f: mudar_fonte(f))

fonte_menu.add_separator()
fonte_menu.add_command(label="Zoom +", command=zoom_in)
fonte_menu.add_command(label="Zoom -", command=zoom_out)

menu.add_cascade(label="Fonte", menu=fonte_menu)

# Inicia o app
janela.mainloop()
