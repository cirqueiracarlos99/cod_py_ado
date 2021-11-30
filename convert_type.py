#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import json
import os

# Faz leitura 
def ler(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

caminho = r"C:\Users\6113871\OneDrive - Thomson Reuters Incorporated\Documents\Thomson Reuters\ADO_roteiro\Impor_ADO\GTMPS-14619.json"
dados = ler(caminho)
print(dados)

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




