# Importar a tabela
# Abrir o navegador, entrar no google
#pegar xpath do campo de busca
#fazer a pesquisa com os dados da tabela

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()
navegador.get("https://google.com.br")

tabela = pd.read_excel('cotacao.xlsx')
display(tabela)


for linha in tabela.index:
    moeda = tabela.loc[linha, "MOEDA"]
    link = f"https://www.google.com.br/search?q=valor+do+{moeda}&source=hp&ei=yH0TZN_cO-Hz1sQPr4OIqAc&iflsig=AK50M_UAAAAAZBOL2XPV0yFZa5302sG0P9xYCUYwOBo1&ved=0ahUKEwjf4M_QpuH9AhXhuZUCHa8BAnUQ4dUDCAg&uact=5&oq=valor+do+EUR&gs_lcp=Cgdnd3Mtd2l6EANQAFgsYEJoAHAAeACAAQCIAQCSAQCYAQCgAQE&sclient=gws-wiz"
    navegador.get(link)
    valor = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
    #valor = valor.replace(".","").replace(",",".")
    tabela.loc[linha, "VALOR EM REAL"] = "R$ {:,.2f}".format(float(valor))
display(tabela)

# Exportar tabela

import datetime
data_atual = datetime.datetime.now().strftime("%d-%m_%H-%M")
tabela.to_excel(f"cotacao-atualiza_{data_atual}.xlsx", index=False)
