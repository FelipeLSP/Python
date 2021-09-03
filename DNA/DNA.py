def hamming(vetor1, vetor2):

    count=0
    indice_diferenca=[]
    for i in range(0,len(vetor1)):
        if vetor1[i] != vetor2[i]:

            indice_diferenca.append(i + 1)
            count+= 1

    return count, indice_diferenca

def compara(k,vetorA,vetorB):

    posicao_inicial=[]
    i=0
    lista_diferenca = []
    while i <= (len(vetorB) - len(vetorA)):

        vetorTemp = vetorB[i:i + len(vetorA)]
        result, indice_diferenca = hamming(vetorA,vetorTemp)

        if  (result <= k):

            posicao_inicial.append(i + 1)
            lista_diferenca.append(indice_diferenca)
        i+=1


    return posicao_inicial, lista_diferenca

def imprimir(k, indice, diferenca):

    print("As substrings com distância no máximo", k, " do mofit e as  posições são:")

    for i in range(0,len(indice)):

        print(indice[i], end=" ")

        for j in range(0,len(diferenca[i])):

            print(diferenca[i][j], end=" ")
        print()



k = int(input("Digite o valor de k(valor máximo = 50): "))
motif = input("Digite o motif(máximo 50 caracteres): ")
dna = input("Digite o DNA(máximo 500 caracteres: ")

if k > 50 or len(motif) > 50 or len(dna) > 500:

    print("Valores não estão de acordo!")

else:

    indice, diferenca = compara(k,motif,dna)

    imprimir(k,indice, diferenca)