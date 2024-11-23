from historico import *

import os
import shlex

def executarComando(comando): # Função para executar comandos, utilizando o próprio comando como parametro
    try:
        tokens = shlex.split(comando) # Separando o comando em tokens
        pid = os.fork() # Criando processo filho
        if pid == 0: # Condição do processo filho
            os.execvp(tokens[0], tokens) # Executando comandos
        else: # Condição do processo pai
            os.wait()
    except FileNotFoundError: # Caso seja inserido um comando desconhecido, printa uma mesangem
        print(f'{comando}: comando não encontrado')
        os._exit(0)
    except IndexError:
        pass
        os._exit(0)

def executarUltimoComando(historico):
    if bool(historico):
        comando = historico[-1][2:].strip()
        executarComando(comando)
        return comando
    else:
        print('nenhum comando no histórico')

def executarIndiceComando(historico, indice):
    if bool(historico):
        try:
            indice = str(indice)
            for x in historico:
                if x.startswith(indice):
                    comando = x[len(indice)+1:]
            executarComando(comando)
            return comando
        except:
            print('nenhum comando correspondente no histórico')
    else:
        print('nenhum comando no histórico')
