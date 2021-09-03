import math

def comp_Roda(x):

    pi = round(math.pi,3)
    return 2 * pi * (x/2)

def km_Cm(k):

    return k*100000

def ordem_Grandeza(fdist,fdiam):

    num = fdist // fdiam
    convert = str(num)
    exp = len(convert) - 3
    return exp

dist = int(input("Digite a distância percorrida: "))
diam = int(input("Digite o diâmetro da roda: "))

n = ordem_Grandeza(km_Cm(dist),comp_Roda(diam))
m = (km_Cm(dist)//comp_Roda(diam))/ (10**(n))
m = round(m,2)

if m < 3.16:

    n = n
else:
    n = n + 1

print("Distância percorrida: ", dist," km")
print("Diâmetro da roda: ", diam, " cm")
print("Ordem de grandeza da quantidade de voltas efetuadas: 10 elevado a ",n)
