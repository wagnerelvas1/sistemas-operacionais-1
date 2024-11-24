from comandos import *
from historico import *

historico = []
contador = 0

while True:
    shell = input('unix-shell> ').strip()

    if shell == 'exit':
        break
    elif not shell:
        pass
    elif shell == 'history':
        printarHistorico(historico)
    elif shell == '!!':
        comando = executarUltimoComando(historico)
        if comando != None:
            contador += 1
            adicionarComandoHistorico(historico, contador, comando)
    elif shell.startswith('!'):
        try:
            indice = int(shell[1:])
            comando = executarIndiceComando(historico, indice)
            if comando != None:
                contador += 1
                adicionarComandoHistorico(historico, contador, comando)
        except ValueError:
            print('índice inválido')
    else:
        contador += 1
        adicionarComandoHistorico(historico, contador, shell)
        executarComando(shell)