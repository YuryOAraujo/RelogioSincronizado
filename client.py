import tkinter as tk
from tkinter import ttk
import socket
from tkinter import messagebox

client_socket = None

# Realiza conexão com o servidor, em caso de sucesso atualiza a hora. Em caso de falha, exibe uma caixa informando que houve um erro na conexão.
def get_server_time():
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        # Área de Texto para exibir a hora
        global server_time_label
        server_time_label = ttk.Label(window, text="", foreground="#0f0", background="#222", font=("DS-Digital", 100, "bold"), anchor="center")
        server_time_label.pack(fill="both", expand=True)
        connect_button.destroy()
        update_server_time()
    except:
        messagebox.showerror("Erro de Conexão", "Não foi possível obter conexão com o servidor")

# Função que altera o texto do relógio
def update_server_time():
    server_time = client_socket.recv(1024).decode()
    hour =  server_time.split(' ')[3]
    server_time_label.config(text=hour)
    window.after(1000, update_server_time) # Atualizado a cada segundo

# Encerra o socket do cliente
def close_connection():
    global client_socket
    if client_socket:
        client_socket.close()

# Responsável por encerrar a conexão ao clicar no botão de fechar (X)
def close_window():
    close_connection()
    window.destroy()

def start_app():
    global HOST, PORT, connect_button, window
    HOST = 'localhost'
    PORT = 5000

    window = tk.Tk()
    window.title("Relógio Sincronizado - Cliente")
    window.geometry("500x200")
    window.configure(bg="#222")
    window.resizable(False, False)

    connect_button = ttk.Button(window, text="Conectar", command=get_server_time)
    connect_button.pack(padx=10, pady=80)

    window.protocol("WM_DELETE_WINDOW", close_window)
    window.mainloop()

start_app()
