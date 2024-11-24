import os
import shlex

def executarComando(comando):
    try:
        tokens = shlex.split(comando)
        pid = os.fork()
        if pid == 0:
            os.execvp(tokens[0], tokens)
        else:
            os.wait()
    except FileNotFoundError:
        print(f'{comando}: comando não encontrado')
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
                if x[:len(indice)+1].strip() == indice:
                    comando = x[len(indice)+1:].strip()
            executarComando(comando)
            return comando
        except:
            print('nenhum comando correspondente no histórico')
    else:
        print('nenhum comando no histórico')
