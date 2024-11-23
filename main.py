from comandos import *
from historico import *

historico = []
contador = 0 # Contador de comandos

while True:
    shell = input('unix-shell> ').strip() # Entrada de comandos

    if shell == 'exit':
        break
    elif shell == 'history':
        printarHistorico(historico)
    elif shell == '!!':
        contador += 1
        comando = executarUltimoComando(historico)
        adicionarComandoHistorico(historico, contador, comando)
    elif shell.startswith('!'):
        try:
            contador += 1
            indice = int(shell[1:])
            comando = executarIndiceComando(historico, indice)
            adicionarComandoHistorico(historico, contador, comando)
        except ValueError:
            print('índice não informado')
    else:
        contador += 1
        adicionarComandoHistorico(historico, contador, shell)
        executarComando(shell)