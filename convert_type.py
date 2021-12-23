#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import os

items = []
pasta = r"C:\Users\6113871\OneDrive - Thomson Reuters Incorporated\Documents\Thomson Reuters\ADO_roteiro\Impor_ADO"

# pega os nomes dos arquivos GTMPS ------------------
arquivos = os.listdir(pasta) 

for i in range(len(arquivos)):
    if 'GTMPS' in arquivos[i] :
        if '.json' in arquivos[i]  :
            items.append( arquivos[i][6:] ) 
            
# -------------------------------------------------

# Faz leitura 
def ler(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

for i in range(len(items)):    
    caminho = r"C:\Users\6113871\OneDrive - Thomson Reuters Incorporated\Documents\Thomson Reuters\ADO_roteiro\Impor_ADO\GTMPS-" + items[i]
    dados = ler(caminho)
    d = str(dados)

    # altera type para: DEV, FUNC, QA, UAT
    if '] [UAT' in d :
        dados["Type"] = "UAT"
    if '] [DEV' in d :
        dados["Type"] = "DEV"
    if '] [FUNC' in d :
        dados["Type"] = "FUNC"
    if '] [QA' in d :
        dados["Type"] = "QA"

    with open(caminho, 'w') as jsonFile:
        json.dump(dados, jsonFile)
        jsonFile.close()


# In[ ]:




