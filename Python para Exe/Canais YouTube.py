# %% [markdown]
# # Python para executável em programas mais complexos
# 
# ### Objetivo:
# 
# Muitas vezes nossos códigos puxam informações de outros arquivos ou, no caso de webscraping, usam outros arquivos como o chromedriver.exe para funcionar.
# 
# Nesses casos, precisamos não só tomar alguns cuidados, mas também adaptar o nosso código para funcionar.
# 
# ### O que usaremos:
# 
# - auto-py-to-exe para transformar o arquivo python em executável
# - pathlib ou os para adaptar todos os "caminhos dos arquivos"
# - Alternativamente, podemos usar o tkinter para permitir a gente escolher manualmente o arquivo, independente do computador que vamos rodar o programa
# 
# Vamos ver como isso funciona na prática
# 
# - Referências Úteis:
#     1. https://dev.to/eshleron/how-to-convert-py-to-exe-step-by-step-guide-3cfi
#     2. https://pypi.org/project/auto-py-to-exe/

# %% [markdown]
# ### Vamos rodar com um exemplo que temos na hashtag. Como pegar os links de vídeos do youtube
# 
# 

# %% [markdown]
# ### Importações

# %%
#importar bibliotecas
import time, urllib
from IPython.display import display
from selenium import webdriver 
import pandas as pd 
import numpy as np
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox

# %% [markdown]
# ### Pegando o arquivo em Excel do nosso computador 

# %%
#ler csv
import os
caminho = os.getcwd()

buscas_df = pd.read_csv(os.path.join(caminho, r'Canais Youtube.csv'), encoding = 'ISO-8859-1', sep=';')
display(buscas_df.head())

# %%
janela = Tk()
arquivo = tkinter.filedialog.askopenfilename(title = "Selecione o arquivo com os canais do YouTube a serem mapeados")
janela.destroy()

buscas_df = pd.read_csv(arquivo, encoding = 'ISO-8859-1', sep=';')
display(buscas_df.head())

# %% [markdown]
# ### Pegandos os links no youtube 

# %%
buscas_canais = buscas_df['ÿCanais'].unique()
# ler videos de todas as buscas
driver = webdriver.Chrome() 

hrefs = []
delay = 5
 
# pegando os itens dos canais
for canal in buscas_canais:
    if canal is np.nan:
        break
    hrefs.append(canal)
    driver.get(canal)
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div/div[1]')))
    time.sleep(2)
    tab = driver.find_elements(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div/div[1]')[0].click()
    time.sleep(2)
    altura = 0
    nova_altura = 1
    while nova_altura > altura:
            altura = driver.execute_script("return document.documentElement.scrollHeight")
            driver.execute_script("window.scrollTo(0, " + str(altura) + ");")
            time.sleep(3)
            nova_altura = driver.execute_script("return document.documentElement.scrollHeight")
    videos = driver.find_elements(By.ID, 'thumbnail')
    try:
        for video in videos:
            meu_link = video.get_attribute('href')
            if meu_link:
                if not 'googleadservices' in meu_link: 
                    hrefs.append(meu_link)
    except StaleElementReferenceException:
        time.sleep(2)
        videos = driver.find_elements(By.ID, 'thumbnail')
        for video in videos:
            meu_link = video.get_attribute('href')
            if meu_link:
                if not 'googleadservices' in meu_link: 
                    hrefs.append(meu_link)
    print('Pegamos {} vídeos do Canal {}'.format(len(videos), canal))


# %%

driver.quit()

# %% [markdown]
# ### Gerando arquivo final 

# %%
#salvando o resultado em um csv
hrefs_df = pd.DataFrame(hrefs)
hrefs_df.to_csv(r'Canais Prontos.csv', sep=',', encoding='utf-8')

janela = Tk()
messagebox.showinfo("Status do Progama", "Progama concluido com Sucesso. Pegue o arquivo no mesmo local onde está instalado este executável")
janela.destroy()


