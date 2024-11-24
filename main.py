from comandos import *
from historico import *

historico = []
contador = 0

while True:
    shell = input('unix-shell> ').strip() # Entrada de comandos (.strip) serve para tirar espaços em branco descenecessários

    if shell == 'exit':
        break
    elif not shell: # Caso o usuário apenas pressione enter, não causará erros
        pass
    elif shell == 'history':
        printarHistorico(historico)
    elif shell == '!!':
        comando = executarUltimoComando(historico) # Armazena na variável "comando" o comando retornado pela função
        if comando != None: # Caso a função não retorne um comando (None), o valor não será armazenado no histórico
            contador += 1 # Incrementa o número do contador
            adicionarComandoHistorico(historico, contador, comando) # Adiciona o número e comando no histórico
    elif shell.startswith('!'):
        try:
            indice = int(shell[1:]) # Guarda na variável "indice" o número informado pelo usuário
            comando = executarIndiceComando(historico, indice) # Armazena na variável "comando" o comando retornado pela função
            if comando != None: # Caso a função não retorne um comando (None), o valor não será armazenado no histórico
                contador += 1 # Incrementa o número do contador
                adicionarComandoHistorico(historico, contador, comando) # Adiciona o número e comando no histórico
        except ValueError: # Caso o usuário não informe um número, o erro será tratado, imprimindo uma mensagem
            print('índice inválido')
    else:
        contador += 1 # Incrementa o número do contador 
        adicionarComandoHistorico(historico, contador, shell) # Adiciona o número e comando no histórico (mesmo que inválido)
        executarComando(shell) # Executa o comando inserido pelo usuário
        