import socket
import time

#Configurações do servidor
HOST = 'localhost'
PORT = 5000

#Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print('Aguardando conexão do cliente...')

#Aceita a conexão do cliente
client_socket, addr = server_socket.accept()
print('Conexão estabelecida com', addr)

#Função para enviar o tempo atual ao cliente
def send_current_time():
    current_time = time.ctime(time.time())
    client_socket.send(current_time.encode())

#Envia o tempo atual a cada segundo
while True:
    send_current_time()
    time.sleep(1)

#Fecha a conexão
client_socket.close()
server_socket.close()