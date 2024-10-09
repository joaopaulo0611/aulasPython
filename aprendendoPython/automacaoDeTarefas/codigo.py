import pyautogui
import time
import pandas

#Abrir o Sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(0.8)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(0.5)

#Logar no Sistema
pyautogui.click(x=680, y=393)
pyautogui.write("joao@gmail.com")
pyautogui.press("tab")
pyautogui.write("joao1234")
pyautogui.press("tab")
pyautogui.press("enter")

#Base de Dados
tabela = pandas.read_csv("automacaoDeTarefas\produtos.csv")
print(tabela)

#Cadastro de Dados
for linha in tabela.index:
    #codigo
    pyautogui.click(x=660, y=269)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)