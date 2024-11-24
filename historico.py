def adicionarComandoHistorico(historico, contador, comando):
    if len(historico) >= 10: # Caso o histórico já possua 10 comandos armazenados
        historico.pop(0) # Remove o primeiro comando
    historico.append(f'{contador} {comando}') # E adiciona o comando recebido com o número do contador

def printarHistorico(historico):
    for x in reversed(historico): # Loop que percorre o histórico ao contrário
        print(x) # Printa cada comando em lop
