import os
import shlex

def executarComando(shell): # Função para executar comandos, utilizando o próprio comando como parametro
    try:
        tokens = shlex.split(shell) # Separando o comando em tokens
        pid = os.fork() # Criando processo filho
        if pid == 0: # Condição do processo filho
            os.execvp(tokens[0], tokens) # Executando comandos
            os._exit(0)
        else: # Condição do processo pai
            os.wait()
    except FileNotFoundError: # Caso seja inserido um comando desconhecido, printa uma mesangem
        print(f'{shell}: comando não encontrado')
        os._exit(0)

def ultimoComando(historico):
    if bool(historico):
        executarComando(historico[-1][2:])
    else:
        print('nenhum comando no histórico')

def indiceComando(historico, indice):
    try:
        for x in historico:
            if x.startswith(str(indice)):
                comando = historico[historico.index(x)]
        executarComando(comando[2:].strip())
    except IndexError:
        print('nenhum comando correspondente no histórico')
