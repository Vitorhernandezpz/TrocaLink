import tkinter as tk
import troca_link
from selenium import webdriver

def pegar_links():
    url_antiga = link_antigo.get()
    url_novo = link_novo.get()
    navegador = webdriver.Chrome()

    troca_link.exec_troca_url(url_antiga, url_novo,navegador)
    print(url_antiga)
    print(url_novo)

def cancelar():
    print("Troca Cancelada")

janela = tk.Tk() #Tk() é a janela em si
janela.title("Troca de links")

janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

texto_orientacao = tk.Label(janela, text="Faça a troca dos links", width=40, height=2)
texto_orientacao.grid(row=0, column=0, columnspan=1, sticky='NSEW')

texto1 = tk.Label(janela, text="Insira o link que deseja remover", width=40)
texto1.grid(row=1, column=0)

link_antigo = tk.Entry(width=35)
link_antigo.grid(row=2, column=0)

texto2 = tk.Label(janela, text="Insira o link que deseja adicionar", width=40)
texto2.grid(row=3, column=0)

link_novo = tk.Entry(width=35)
link_novo.grid(row=4, column=0)

botao_trocar = tk.Button(janela, text="Trocar", command=pegar_links, width=10)
botao_trocar.grid(row=5, column=0)

botao_cancelar = tk.Button(janela, text="Cancelar", command=cancelar, width=10)
botao_cancelar.grid(row=5, column=1)


janela.mainloop()

#time.sleep(2)
#navegador.get("https://gkoplus.atlassian.net/wiki/search?text=%22http%3A%2F%2Fgko.com.br%2Fintranet%2Fwp-content%2Fuploads%2Fgmud%2Fvd%22")
#time.sleep(4)
