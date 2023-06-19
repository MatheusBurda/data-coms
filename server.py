import socket
import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from binary import binary_to_string
from linecode import decode
from cryptog import decrypt


PORT = 17171            # The port used by the server

def receive_with_socket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        print("Awaiting connection...")

        server_socket.bind(('', PORT))
        server_socket.listen()
        conn, addr = server_socket.accept()

        with conn:
            print(f"Connected to client on {addr}")

            return conn.recv(1024).decode('utf-8')

def plot_graph(mensagem):
    global figure, canvas
    valores_y = []

    for char in mensagem:
        number = int(char) - 1
        valores_y.append(number)

    tempos_x = np.arange(len(valores_y))

    figure = Figure(figsize=(15, 5), dpi=70)
    subplot = figure.add_subplot(111)

    # Plotar gráfico de escada
    subplot.plot(tempos_x, valores_y, drawstyle='steps-post', marker='o')
    subplot.set_xlabel('Time')
    subplot.set_ylabel('Ternary Value')
    subplot.set_title('8B6T line coding graph')

    canvas = FigureCanvasTkAgg(figure, master=janela)
    canvas.draw()

    # Posicionar o canvas na janela do Tkinter
    canvas.get_tk_widget().place(relx=0.5, rely=0.6, anchor=tk.CENTER)


def clear_all():
    mensagem_entry.delete(0, tk.END)
    valor1_entry.delete(0, tk.END)
    valor2_entry.delete(0, tk.END)
    valor3_entry.delete(0, tk.END)
    for item in canvas.get_tk_widget().find_all():
       canvas.get_tk_widget().delete(item)


def receive():
    mensagem = receive_with_socket()
    plot_graph(mensagem)

    line_code = mensagem.replace('2', '+').replace('0', '-').replace('1', '0')

    valor3_entry.delete(0, 'end')
    valor3_entry.insert(0, line_code)

    mensagem = decode(mensagem)

    valor2_entry.delete(0, 'end')
    valor2_entry.insert(0, mensagem)
    mensagem = binary_to_string(mensagem)

    valor1_entry.delete(0, 'end')
    valor1_entry.insert(0, mensagem)
    mensagem = decrypt(mensagem)

    mensagem_entry.delete(0, 'end')
    mensagem_entry.insert(0, mensagem)




# Criar janela principal
janela = tk.Tk()
janela.title("Exemplo de Janela")
janela.geometry("900x650")
janela.resizable(False, False)  # Impede a janela de ser redimensionada

# Criar figure do Matplotlib
figure = Figure(figsize=(15, 5), dpi=70)
# Criar canvas do Matplotlib para Tkinter
canvas = FigureCanvasTkAgg(figure, master=janela)

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


# Criar botões de enviar e clear_all
enviar_button = tk.Button(janela, text="Receber", command=receive)
enviar_button.place(relx=1.0, rely=1.0, anchor=tk.SE)

clear_all_button = tk.Button(janela, text="clear_all", command=clear_all)
clear_all_button.place(relx=0.0, rely=1.0, anchor=tk.SW)

# Iniciar o loop principal da janela
janela.mainloop()
