from historico import *
from comandos import *

historico = []
contador = 0

while True:
    shell = input('unix-shell> ')

    if shell != '!!' and shell != 'history' and not shell.strip().startswith('!') :
        contador += 1
        adicionarComandoHistorico(historico, contador, shell)

    if shell.strip() == 'exit':
        break
    elif shell.strip() == '!!':
        ultimoComando(historico)
    elif shell.strip().startswith('!'):
        try:
            indice = int(shell[1:])
            indiceComando(historico, indice)
        except ValueError:
            print('índice não informado')
    elif shell.strip() == 'history':
        printarHistorico(historico)
    else:
        executarComando(shell)
