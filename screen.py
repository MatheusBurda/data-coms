import tkinter as tk
from crypt import encrypt
from binary import string_to_binary
from linecode import encode
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plotar_grafico(mensagem):
    valores_y = []

    for char in mensagem:
        number = int(char) - 1
        valores_y.append(number)

    tempos_x = np.arange(len(valores_y))

    # Criar figura do Matplotlib
    figura = Figure(figsize=(15, 2), dpi=50)
    subplot = figura.add_subplot(111)

    # Plotar gráfico de escada
    subplot.plot(tempos_x, valores_y, drawstyle='steps-post', marker='o')
    subplot.set_xlabel('Tempo')
    subplot.set_ylabel('Valores')
    subplot.set_title('Gráfico Stair')

    # Criar canvas do Matplotlib para Tkinter
    canvas = FigureCanvasTkAgg(figura, master=janela)
    canvas.draw()

    # Posicionar o canvas na janela do Tkinter
    canvas.get_tk_widget().place(relx=0.5, rely=0.6, anchor=tk.CENTER)


def limpar():
    mensagem_entry.delete(0, tk.END)
    valor1_entry.delete(0, tk.END)
    valor2_entry.delete(0, tk.END)
    valor3_entry.delete(0, tk.END)


def enviar_mensagem():
    mensagem = mensagem_entry.get()
    
    mensagem = encrypt(mensagem)
    valor1_entry.insert(0, mensagem)

    mensagem = string_to_binary(mensagem)
    valor2_entry.insert(0, mensagem)

    mensagem = encode(mensagem)
    valor3_entry.insert(0, mensagem)

    plotar_grafico(mensagem)


# Criar janela principal
janela = tk.Tk()
janela.title("Exemplo de Janela")
janela.geometry("700x450")
janela.resizable(False, False)  # Impede a janela de ser redimensionada


# Criar rótulo e campo de entrada de texto para a mensagem
mensagem_label = tk.Label(janela, text="Mensagem:")
mensagem_label.pack()
mensagem_entry = tk.Entry(janela, width=100)
mensagem_entry.pack()

# Criar rótulos e campos de entrada de texto para os valores
valor1_label = tk.Label(janela, text="Mensagem Criptografada:")
valor1_label.pack()
valor1_entry = tk.Entry(janela, width=100)
valor1_entry.pack()

valor2_label = tk.Label(janela, text="Mensagem em Binário:")
valor2_label.pack()
valor2_entry = tk.Entry(janela, width=100)
valor2_entry.pack()

valor3_label = tk.Label(janela, text="Mensagem em Código de Linha:")
valor3_label.pack()
valor3_entry = tk.Entry(janela, width=100)
valor3_entry.pack()


# Criar botões de enviar e limpar
enviar_button = tk.Button(janela, text="Enviar", command=enviar_mensagem)
enviar_button.place(relx=1.0, rely=1.0, anchor=tk.SE)

limpar_button = tk.Button(janela, text="Limpar", command=limpar)
limpar_button.place(relx=0.0, rely=1.0, anchor=tk.SW)

# Iniciar o loop principal da janela
janela.mainloop()
