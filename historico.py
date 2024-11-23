def adicionarComandoHistorico(historico, contador, comando):
    if len(historico) >= 10:
        historico.pop(0)
    historico.append(f'{contador} {comando}')

def printarHistorico(historico):
    for x in reversed(historico):
        print(x)
