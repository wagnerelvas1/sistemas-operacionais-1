import os
import shlex

def executarComando(comando): # Recebe a variável comando como parâmetro
    try:
        tokens = shlex.split(comando) # Divide o comando em tokens
        pid = os.fork() # Cria um novo processo
        if pid == 0: # Condição do processo filho
            os.execvp(tokens[0], tokens) # Executa o comando
        else: # Condição do processo pai
            os.wait() # Aguarda a execução do processo filho
    except FileNotFoundError: # Caso o comando não seja válido
        print(f'{comando}: comando não encontrado') # Printa a mensagem de erro
        os._exit(0) # Encerra o processo filho

def executarUltimoComando(historico): # Recebe o histórico como parâmetro
    if bool(historico): # Verifica se o histórico possui algum comando
        comando = historico[-1][2:].strip() # Guarda na variável comando o último comando do histórico
        executarComando(comando) # Executa o comando
        return comando # Retorna o comando
    else: # Caso o histórico esteja vazio
        print('nenhum comando no histórico') # Printa a mensagem informando

def executarIndiceComando(historico, indice): # Recebe o histórico e indice como parâmetro
    if bool(historico): # Verifica se o histórico possui algum comando
        try:
            indice = str(indice) # Transforma o índice em string
            for x in historico: # Loop que percorre o histórico
                if x[:len(indice)+1].strip() == indice: # Caso o número do comando no histórico seja igual ao índice
                    comando = x[len(indice)+1:].strip() # Guarda na variável comando 0 comando presente no histórico
            executarComando(comando) # Executa o comando
            return comando # Retorna o comando
        except: # Trata o erro no caso de índice não encontrado
            print('nenhum comando correspondente no histórico')
    else: # Caso o histórico esteja vazio, retorna uma mensagem
        print('nenhum comando no histórico')
