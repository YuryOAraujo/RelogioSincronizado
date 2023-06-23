import socket
import time
import threading

# Configurações do servidor
HOST = 'localhost'
PORT = 5000

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(0)

print('Aguardando conexões dos clientes...')

# Função para enviar o tempo atual ao cliente
def send_current_time(client_socket):
    while True:
        try:
            current_time = time.ctime(time.time())
            client_socket.send(current_time.encode())
        except ConnectionAbortedError:
            break
        except ConnectionResetError:
            print("Conexão com o cliente redefinida")
            break
        time.sleep(1)

# Função para lidar com cada cliente em uma nova thread
def handle_client(client_socket, client_address):
    print('Conexão estabelecida com', client_address)
    send_current_time(client_socket)
    client_socket.close()
    print('Conexão encerrada com', client_address)

# Aceita conexões dos clientes e cria uma nova thread para cada cliente
while True:
    try:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
    except KeyboardInterrupt:
        break

# Encerra o socket do servidor
server_socket.close()
