def adicionarComandoHistorico(historico, contador, shell):
    if len(historico) >= 10:
        historico.pop(0)
    historico.append(f'{contador} {shell}')

def printarHistorico(historico):
    for x in reversed(historico):
        print(x)
