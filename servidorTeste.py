import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 12000))
server.listen()

print("Servidor aguardando conexão...")

cliente, endereco = server.accept()

print(endereco)

while True:
    mensagem = cliente.recv(1024)

    if not mensagem:
        break

    texto = mensagem.decode("utf-8")

    print(texto)

    cliente.send(texto.encode("utf-8"))
