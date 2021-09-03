import math

def centroide(vetor_coordenadas):

    x_centroide = 0
    y_centroide = 0
    vetor_centroide=[]
    for i in range(0, len(vetor_coordenadas)):
        x_centroide += vetor_coordenadas[i][0]
        y_centroide += vetor_coordenadas[i][1]
    x_centroide = round(x_centroide/len(vetor_coordenadas),1)
    y_centroide = round(y_centroide/len(vetor_coordenadas),1)
    vetor_centroide.append(x_centroide)
    vetor_centroide.append(y_centroide)

    return vetor_centroide

def distancia_coordenadas(vetor_coordenadas, centroide):

    vetor_menor=[]
    vetor_maior=[]
    vetor_distancia=[]
    for i in range(0,len(vetor_coordenadas)):

        distancia = math.sqrt(((vetor_coordenadas[i][0] - centroide[0]) ** 2) + ((vetor_coordenadas[i][1] - centroide[1]) ** 2))
        vetor_distancia.append(distancia)

    temp_a = vetor_distancia[0]
    for i in range(1, len(vetor_distancia)):
        if  vetor_distancia[i] < temp_a:
            temp_b = vetor_distancia[i]
            vetor_menor = vetor_coordenadas[i]

    temp_b = vetor_distancia[0]
    for i in range(1, len(vetor_distancia)):
        if vetor_distancia[i] > temp_b:
            temp_b = vetor_distancia[i]
            vetor_maior = vetor_coordenadas[i]

    return vetor_menor, vetor_maior


#--------------------------CORPO DO PROGRAMA--------------------------------------------------------------



vetor_coordenadas = []

nome = input("Digite uma coordenada: ")
partes_a = nome.split()

if nome == "":
    print("Nenhum ponto lido. Portanto, não há centróide!!!")
    exit()

for ind in range(0,2):
    partes_a[ind] = int(partes_a[ind])
vetor_coordenadas.append(partes_a)
i=1

while i>=1:

    nome = input("Digite uma coordenada: ")
    if nome == "":
        break
    else:
        partes_b = nome.split()
        for ind in range(0,2):
            partes_b[ind] = int(partes_b[ind])
        vetor_coordenadas.append(partes_b)


vetor_centroide = centroide(vetor_coordenadas)
vetor_menor, vetor_maior = distancia_coordenadas(vetor_coordenadas, vetor_centroide)

print("Centróide: ", vetor_centroide)
print ("Ponto mais próximo do Centróide: ", vetor_menor)
print ("Ponto mais distante do Centróide: ", vetor_maior)