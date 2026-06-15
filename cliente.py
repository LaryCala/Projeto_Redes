import socket
import datetime
import threading  # Permite receber mensagens mesmo que não tenha enviado nenhuma

def receber_mensagens():  # Função responsável por "escutar" o servidor
    while True:
        try:
            msg_recebida_bytes = client.recv(1024)
            msg_recebida_str = msg_recebida_bytes.decode("utf-8")
            print(f"\n{msg_recebida_str}")

        except:
            print("Conexão encerrada.")
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12000))

nome = input("Digite seu nome: ")# Recebe o nome do usuário, assim pode diferenciar cada um
print("Digite '/sair' para encerrar.")

#Permite que o usuário receba mensagens de outros usuários assim que entrar no servidor
thread_recebimento = threading.Thread(
   target=receber_mensagens
)
thread_recebimento.start()

client.send(("ENTROU: " + nome).encode("utf-8"))# Envia uma mensagem a todos dentro do servidor sobre quem entrou, o servidor precisa tratar essas mensagens diferente

while True:
    # Recebe a mensagem do usuário
    msg_para_enviar = input("Digite uma mensagem: ")
    agora = datetime.datetime.now()  # Pega o horário atual
    horario = agora.strftime("%H:%M")  # Formato Hora:Minutos

    if msg_para_enviar == "/sair":
        # Avisa que o usuário saiu do servidor para os outros
        client.send(("SAIU: " + nome).encode("utf-8"))
        print("Encerrando conexão...")
        client.close()
        break  # Se o cliente digitar "/sair", ele encerra a conexão

    mensagem = "[" + horario + "] " + nome + ": " + msg_para_enviar
    client.send(mensagem.encode("utf-8"))
