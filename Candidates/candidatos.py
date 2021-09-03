def contagem_de_votos(numero_candidatos,candidatos, vetor_votos):

    votos_brancos=0
    votos_nulos=0
    qtd_votos=[]
    for i in range(0, numero_candidatos):
        total_votos = vetor_votos.count(candidatos[i][1])
        qtd_votos.append(total_votos)
    votos_brancos = vetor_votos.count(0)
    votos_nulos = len(vetor_votos)-(votos_brancos+ sum(qtd_votos))

    return qtd_votos, votos_brancos,votos_nulos

def imprimir(numero_candidatos,candidatos,qtd_votos,votos_brancos):

    print("Resultado de Eleição: ")
    print()
    for i in range(0,numero_candidatos):
        print(str(candidatos[i][0])+ " - " +str(candidatos[i][1])+ " - com " + str(qtd_votos[i])+ " voto(s)")

    print("Brancos - com - "+str(votos_brancos)+ " voto(s)")
    print("Nulos - com - "+str(votos_nulos)+ " voto(s)")


#------------------------------CORPO DO PROGRAMA--------------------------------------------------------------------


numero_candidatos = int(input("Digite o número de candidatos: "))

candidatos = []
vetor_votos=[]
qtd_votos=[]
votos_brancos=0
votos_nulos=0

for i in range (1, numero_candidatos+1):

    nome = input("Digite o nome e número do candidato " +str(i)+ ": ")
    partes = nome.split("#")
    partes[1] = int(partes[1])
    candidatos.append(partes)

while i>=0:

    nome = input("Digite o número do seu candidato: ")
    i = int(nome)
    if i < 0:
        break
    else:
        partes = nome.split()
        partes = int(partes[0])
    vetor_votos.append(partes)

qtd_votos, votos_brancos, votos_nulos=contagem_de_votos(numero_candidatos,candidatos,vetor_votos)

imprimir(numero_candidatos,candidatos,qtd_votos,votos_brancos)