import re, sys

def leArquivo():
    arquivo = open(sys.argv[1], "r")
    automato = []
    for linha in arquivo:
        automato.append(linha)
    arquivo.close()
    return automato

def RemoveCaracteres(automato):
    ##Remove os caracteres "{" e ajusta na lista
    primeira_linha = automato[0]
    #print("Antes")
    #print(automato[0])
    #Ignora o estado final e a fnc de transicao na montagem da lista
    regex = re.compile(r'\{[^\}]*\}')
    #print(regex)
    dados = re.findall(regex, primeira_linha)
    result = []
    #print(dados)
    for elemento in dados:
        result.append(elemento.strip("{}").replace(" ", "").split(","))
        #print(result)
    return result

def recuperaEstadoInicio(automato):
    primeira_linha = automato[0]
    regex = re.compile(r"Z|,\sq\w*,\s{")
    dado = re.findall(regex, primeira_linha)
    estado_inicial = [elemento.strip(",{ ") for elemento in dado]
    print("Estado Inicial:" + str(estado_inicial))
    return estado_inicial

def listaTransicao(automato):
    lista_transicao = []
    for i in range(1, len(automato)):
        automato[i] = automato[i].strip("\n").replace(" ", "").split(",")
        lista_transicao.append(automato[i])
    print('Lista de Transição' + str(lista_transicao))
    return lista_transicao

def lePalavra(estado_inicial,lista_transicao,estados_finais):
    palavra = sys.argv[2]
    estado_atual = estado_inicial[0]

    for letra in palavra:
        validacao = False
        for regra in lista_transicao:
            lista_entrada, lista_letra, lista_saida = regra
            if (str(lista_entrada) == estado_atual) and (str(lista_letra)==letra):
                estado_atual = str(lista_saida)
                break

    if estado_atual in estados_finais:
        print("------------------------------------")
        print("Palavra Reconhecida")
        print("------------------------------------")

    else:
        print("------------------------------------")
        print("Palavra não reconhecida")
        print("------------------------------------")
            #print("Lista Entrada:" + str(lista_entrada))
            #print("lista_letra:" + str(lista_letra))
            #print("lista_saida:" + str(lista_saida))
        #return false


def main():
    automato = leArquivo()
    dados = RemoveCaracteres(automato)
    #Recupera estados finais
    estados_finais=dados[2]
    estado_inicio= recuperaEstadoInicio(automato)
    lista_transicao = listaTransicao(automato)
    print("Estados Finais:" + str(estados_finais))
    validade = lePalavra(estado_inicio, lista_transicao,estados_finais)

    


if len(sys.argv) != 3:
    print("Tente: python3 automato.py <arquivo.txt> <palavra>")
else:
    print(main())