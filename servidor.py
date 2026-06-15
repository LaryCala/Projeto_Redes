import socket
import threading

clientes = []

def gerenciamento_cliente(conexao_cliente, endereco_cliente):
    print(f"(NOVA CONEXÃO) {endereco_cliente} conectado!")
    conectado = True

    while conectado:
        try:
            #Recebe a mesnagem do cliente
            mensagem = conexao_cliente.recv(1024).decode('utf-8')
            if not mensagem:
                break
            if mensagem.startswith("ENTROU:"):
                print(f"[SISTEMA] {mensagem}")

            elif mensagem.startswith("SAIU:"):
                print(f"[SISTEMA] {mensagem}")

            else:
                print(f"{mensagem}")

            for cliente in clientes:
                if cliente != conexao_cliente:
                    cliente.send(mensagem.encode('utf-8'))

            # Reposta do servidor
            #resposta = f"Mensagem recebida com sucesso!"
            #conexao_cliente.send(resposta.encode('utf-8'))

        except ConnectionAbortedError:
            # Caso o cliente feche a janela abruptamente
            break
    
    print(f"(DESCONECTADO) {endereco_cliente} encerrou a conxeão. ")
    conexao_cliente.close()

def iniciar_servidor():

    HOST = "localhost"
    PORTA = 12000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORTA))
    servidor.listen()
    print(f"(LIGADO) Servidor escutando em {HOST}:{PORTA}...")

    while True:
        conexao_cliente, endereco_cliente = servidor.accept()
        clientes.append(conexao_cliente)

        thread = threading.Thread(target=gerenciamento_cliente, args=(conexao_cliente, endereco_cliente))
        thread.start()
        
        print(f"(CONEXÕES ATIVAS) {threading.active_count() - 1}")

if __name__ == "__main__":
    print("(INICIANDO) O servidor está ligando...")
    iniciar_servidor()
