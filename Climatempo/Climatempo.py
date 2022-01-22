from bs4 import BeautifulSoup
from tkinter import*
import requests
import sys

def get_city_tmin_and_tmax(index, offline = False , debug = False ):

    codigo_cidade_online = lista_cidades_online[index]
    codigo_cidade_offline = lista_cidades_offline[index]

    if not offline:
        html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/" + codigo_cidade_online).content
        soup = BeautifulSoup(html,'html.parser')
    else:
        html = open(codigo_cidade_offline + ".html",'r').read()
        soup = BeautifulSoup(html,'html.parser')
    if debug:
        print(soup.prettify())

    cd = soup.find_all("span", itemprop= "name")
    cidade = cd[3].string
    ti = soup.find("span", id = "min-temp-1")
    tmin = ti.string
    ta = soup.find("span", id = "max-temp-1")
    tmax = ta.string

    return cidade,tmin,tmax

def imprimir(index):

    cidade,tmin,tmax = get_city_tmin_and_tmax(index)


    result = cidade + ": Temperatura mínima: " + tmin + "  Temperatura Máxima: " + tmax
    txt_temperaturas["text"] = result


lista_cidades_online = ["321/riodejaneiro-rj", "558/saopaulo-sp", "271/curitiba-pr", "107/belohorizonte-mg",
                 "363/portoalegre-rs","570/ubatuba-sp","377/florianopolis-sc","523/praiagrande-sp",
                 "798/guaruja-sp","292/cabofrio-rj"]

lista_cidades_offline = ["riodejaneiro-rj", "saopaulo-sp", "curitiba-pr", "belohorizonte-mg", "portoalegre-rs", "ubatuba-sp", "florianopolis-sc", "praiagrande-sp", "guaruja-sp", "cabofrio-rj"]


janela = Tk()
janela.title("Temperatura")

txt_orientador = Label(janela, text= "Clique no botão da cidade desejada:")
txt_orientador.grid(column = 0, row = 0)

txt_rj = Label(janela, text= "0 - Temperatura em Rio de Janeiro - RJ")
txt_rj.grid(column = 0, row = 1)
botao_rj = Button(janela, text = "Mostrar", command = lambda: imprimir(0))
botao_rj.grid(column = 1, row = 1)

txt_sp = Label(janela, text= "1 - Temperatura em São Paulo - SP      ")
txt_sp.grid(column = 0, row = 2)
botao_sp = Button(janela, text = "Mostrar", command = lambda: imprimir(1))
botao_sp.grid(column = 1, row = 2)

txt_cr = Label(janela, text= "2 - Temperatura em Curitiba - PR        ")
txt_cr.grid(column = 0, row = 3)
botao_cr = Button(janela, text = "Mostrar", command = lambda: imprimir(2))
botao_cr.grid(column = 1, row = 3)

txt_bh = Label(janela, text= "3 - Temperatura em Belo Horizonte - MG")
txt_bh.grid(column = 0, row = 4)
botao_bh = Button(janela, text = "Mostrar", command = lambda: imprimir(3))
botao_bh.grid(column = 1, row = 4)

txt_pa = Label(janela, text= "4 - Temperatura em Porto Alegre - RS")
txt_pa.grid(column = 0, row = 5)
botao_pa = Button(janela, text = "Mostrar", command = lambda: imprimir(4))
botao_pa.grid(column = 1, row = 5)

txt_ub = Label(janela, text= "5 - Temperatura em Ubatuba - SP")
txt_ub.grid(column = 0, row = 6)
botao_ub = Button(janela, text = "Mostrar", command = lambda: imprimir(5))
botao_ub.grid(column = 1, row = 6)

txt_fl = Label(janela, text= "6 - Temperatura em Florianópolis - SC")
txt_fl.grid(column = 0, row = 7)
botao_fl = Button(janela, text = "Mostrar", command = lambda: imprimir(6))
botao_fl.grid(column = 1, row = 7)

txt_pg = Label(janela, text= "7 - Temperatura em Praia Grande - SP")
txt_pg.grid(column = 0, row = 8)
botao_pg = Button(janela, text = "Mostrar", command = lambda: imprimir(7))
botao_pg.grid(column = 1, row = 8)

txt_gj = Label(janela, text= "8 - Temperatura em Guarujá - SP")
txt_gj.grid(column = 0, row = 9)
botao_gj = Button(janela, text = "Mostrar", command = lambda: imprimir(8))
botao_gj.grid(column = 1, row = 9)

txt_cf = Label(janela, text= "9 - Temperatura em Cabo Frio - RJ")
txt_cf.grid(column = 0, row = 10)
botao_cf = Button(janela, text = "Mostrar", command = lambda: imprimir(9))
botao_cf.grid(column = 1, row = 10)

txt_clima = Label(janela, text= "Clima: ")
txt_clima.grid(column = 0, row = 11)

txt_temperaturas = Label(janela, text = "")
txt_temperaturas.grid(column = 1, row = 11)

janela.mainloop()
