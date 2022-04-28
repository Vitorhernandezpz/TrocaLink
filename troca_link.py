import pyautogui
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def deleta(QtDel):
    for i in range(QtDel):
        pyautogui.press('delete')


def clica_edit(navegador):
    try:
        element = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="property-panel"]/div[2]/div/a[2]'))
        )
        return element
    except:
        return 1
    # finally:
    # pass


def botao_checked(navegador):
    checkbox = navegador.find_element_by_id('notifyWatchers').is_selected()
    if checkbox == True:
        navegador.find_element_by_id('notifyWatchers').click()
        print('feito')
        return checkbox
    else:
        pass


def primeiro_link_visivel(navegador):
    try:
        element = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="content-body"]/main/div/div/div/ul/li[1]/div/div[1]/div[2]/div[1]/div[1]/a/span/span'))
        )
        return element
    except:
        print("falhou")
        return -1
    finally:
        pass


def clica_primeiro_link(navegador):
    try:
        element = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="content-body"]/main/div/div/div/ul/li[1]/div/div[1]/div[2]/div[1]/div[1]/a/span/span'))
        )
        return element
    finally:
        pass


def troca_link(QtDel, url_novo, navegador):
    pyautogui.click(x=758, y=203)
    time.sleep(1)
    pyautogui.hotkey('Fn', 'Home')
    time.sleep(1)
    deleta(QtDel)
    pyperclip.copy(url_novo)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(x=807, y=268)  # link text
    time.sleep(1)
    pyautogui.hotkey('Fn', 'Home')
    time.sleep(1)
    deleta(QtDel)
    pyperclip.copy(url_novo)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(4)
    navegador.find_element_by_xpath('//*[@id="link-browser-insert"]').click()
    time.sleep(10)

def exec_troca_url(url_antiga, url_novo, navegador):

    QtDel = len(url_antiga)
    print(QtDel)

    time.sleep(2)
    navegador.get("https://gkoplus.atlassian.net/wiki/search?text=%22http%3A%2F%2Fgko.com.br%2Fintranet%2Fwp-content%2Fuploads%2Fgmud%2Fvd%22")
    time.sleep(4)
    navegador.maximize_window()
    time.sleep(1)
    pyautogui.click(x=1340, y=89)
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="microsoft-auth-button"]/span[2]/span').click()
    # navegador.find_element(By.XPATH,'//*[@id="microsoft-auth-button"]/span[2]/span').click()
    time.sleep(5)
    pyperclip.copy('vitor.perez@gko.com.br')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    # pyautogui.write('*Senior104')
    # time.sleep(2)
    # pyautogui.press('enter')
    # time.sleep(2)
    # navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(13)

    while primeiro_link_visivel(navegador) != 1:
        time.sleep(4)
        pyautogui.click(x=558, y=245)  # barra de pesquisa
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.press('delete')
        time.sleep(1)
        pyperclip.copy('"' + url_antiga + '"')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'shift', 'r')
        time.sleep(5)
        clica_primeiro_link(navegador).click()  # primeirolink
        time.sleep(6)
        titulo = navegador.title
        print(titulo)
        time.sleep(1)
        pyautogui.click(x=1037, y=169)  # lapis para editar página
        time.sleep(9)
        pyperclip.copy(url_antiga)
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(4)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(3)
        pyautogui.click(x=1263, y=81)
        time.sleep(4)
        pyautogui.press('right')
        time.sleep(5)
        if clica_edit(navegador) != 1:
            clica_edit(navegador).click()
            time.sleep(1)
            troca_link(QtDel, url_novo, navegador)
            time.sleep(8)
            botao_checked()
            navegador.find_element_by_xpath('//*[@id="rte-button-publish"]').click()
            time.sleep(5)
        else:
            navegador.find_element_by_xpath('//*[@id="rte-button-cancel"]').click()
            time.sleep(5)
            time.sleep(4)
        navegador.get("https://gkoplus.atlassian.net/wiki/search?text=%22http%3A%2F%2Fgko.com.br%2Fintranet%2Fwp-content%2Fuploads%2Fgmud%2Fvd%22")
        time.sleep(5)

#url_antiga = "http://gko.com.br/intranet/wp-content/uploads/gmud/prottela"
#url_novo = "https://seniorsistemassa.sharepoint.com/sites/FL-GKO/GKOFRETE/GMud/Arq_Gerados_Auto/prottela"

#navegador = webdriver.Chrome()
