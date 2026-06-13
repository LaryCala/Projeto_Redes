import socket
import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12000))
nome = input("Digite seu nome: ") #Recebe o nome do usuário, assim pode diferenciar cada um
print("Digite '/sair' para encerrar.")
client.send(("ENTROU: " + nome).encode("utf-8")) #Envia uma mensagem a todos dentro do servidor sobre quem entrou, o servidor precisa tratar essas mensagens diferente

while True:
   msg_para_enviar = input("Digite uma mensagem: ") #Recebe a mensagem do usuário
   agora = datetime.datetime.now() #Pega o horário atual
   horario = agora.strftime("%H:%M") # Formato Hora:Minutos

   if msg_para_enviar == "/sair":
    client.send(("SAIU: " + nome).encode("utf-8"))#Avisa que o usuário saiu do servidor para os outros
    print("Encerrando conexão...")
    client.close()
    break #Se o cliente digitar "/sair", ele encerra a conexão
   
   mensagem = "[" + horario + "] " + nome + ": " + msg_para_enviar
   client.send(mensagem.encode("utf-8"))

   msg_recebida_bytes = client.recv(1024)
   msg_recebida_str = msg_recebida_bytes.decode("utf-8")
   print(msg_recebida_str)
