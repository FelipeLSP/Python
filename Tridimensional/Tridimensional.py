import math

def soma_distancias(lista_das_coordenadas, referencia):

    soma = 0
    for i in range(0,len(lista_das_coordenadas)):

        distancia = math.sqrt( ((referencia[0] - lista_das_coordenadas[i][0]) ** 2) + ((referencia[1] - lista_das_coordenadas[i][1]) ** 2) + ((referencia[2] - lista_das_coordenadas[i][2]) ** 2))
        soma += distancia

    return round(soma, 2)

def deslocamento(lista_das_coordenadas, qtd_ciclos, diferencial_deslocamento, referencia_convertida):

    lista_coordenadas_depois_dos_deslocamentos = []
    soma_distancias_deslocadas = 0
    vetor_soma_distancias_deslocadas = []

    for i in range(1, qtd_ciclos+1):
        coordenadas_pos_deslocamento=[]
        for j in range(0, len(lista_das_coordenadas)):
            novo_ponto=[]
            for k in range(0, 3):
                if k == 2:
                    novo_ponto.append(round(lista_das_coordenadas[j][k] + (diferencial_deslocamento*i),2))
                else:
                    novo_ponto.append(round(lista_das_coordenadas[j][k] - (diferencial_deslocamento*i),2))

            coordenadas_pos_deslocamento.append(novo_ponto)
        lista_coordenadas_depois_dos_deslocamentos.append(coordenadas_pos_deslocamento)

        soma_distancias_deslocadas = soma_distancias(coordenadas_pos_deslocamento,referencia_convertida)
        vetor_soma_distancias_deslocadas.append(round(soma_distancias_deslocadas, 2))

    return vetor_soma_distancias_deslocadas,lista_coordenadas_depois_dos_deslocamentos


def imprimir_coordenadas_iniciais(lista_coordenadas):

    print("Pontos Originais: ")

    for i in range(0, len(lista_coordenadas)):
        print("      " + "(" + str(lista_coordenadas[i][0]) + "," + str(lista_coordenadas[i][1]) + "," + str(lista_coordenadas[i][2]) + ")")

def imprimir_coordenadas_deslocadas(lista_coordenadas, lista_coordenadas_deslocadas, qtd_ciclos, diferencial_deslocamento, referencia, vetor_soma_distancias_deslocadas):

        for i in range(1, qtd_ciclos + 1):
            print("Listagem de Pontos no Ciclo " + str(i) + ", Delta de deslocamento " + str(diferencial_deslocamento) + ": ")

            for j in range(0, len(lista_coordenadas)):

                    print("    " + "(" + str(lista_coordenadas_deslocadas[i-1][j][0]) + "," + str(lista_coordenadas_deslocadas[i-1][j][1]) + "," + str(lista_coordenadas_deslocadas[i-1][j][2]) + ")")

            print("Soma das distâncias para o ponto "+ str(referencia_convertida) + ": ", str(vetor_soma_distancias_deslocadas[i-1]))
            print()


#-----------------------------------CORPO DO PROGRAMA------------------------------------------------------------

i=1
vetor_coordenada=[]
lista_das_coordenadas = []
referencia_aux = []
referencia_convertida=[]
vetor_distancias_deslocadas = []
lista_coordenadas_depois_dos_deslocamentos = []



while i >= 1:

    coordenada = input("Digite a coordenada: ")

    if coordenada == "":

        ponto_de_referencia = input("Digite o ponto de referencia: ")
        referencia_aux = ponto_de_referencia.split()

        for i in range(0, 3):
            referencia_aux[i] = float(referencia_aux[i])
        referencia_convertida = referencia_aux
        break

    else:

        vetor_coordenada = coordenada.split()

        for i in range(0, 3):
            vetor_coordenada[i] = float(vetor_coordenada[i])
        lista_das_coordenadas.append(vetor_coordenada)

imprimir_coordenadas_iniciais(lista_das_coordenadas)
print("Soma das distâncias para o ponto "+ str(referencia_convertida) + ": ", soma_distancias(lista_das_coordenadas,referencia_convertida))

qtd_ciclos = int(input("Digite o número de ciclos: "))
diferencial_deslocamento = float(input("Digite o difirencial de deslocamento: "))

vetor_soma_distancias_deslocadas, lista_coordenadas_depois_dos_deslocamentos = deslocamento(lista_das_coordenadas, qtd_ciclos, diferencial_deslocamento, referencia_convertida)

imprimir_coordenadas_deslocadas(lista_das_coordenadas, lista_coordenadas_depois_dos_deslocamentos, qtd_ciclos, diferencial_deslocamento, referencia_convertida, vetor_soma_distancias_deslocadas)
