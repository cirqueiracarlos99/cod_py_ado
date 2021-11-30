#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import json
import os

items = []
pasta = r"C:\Users\6113871\OneDrive - Thomson Reuters Incorporated\Documents\Thomson Reuters\ADO_roteiro\Impor_ADO"
time_o = 0
time_r = 0
time_c = 0

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
    print(caminho)
    dados = ler(caminho)
    cont = 0
    d = str(dados)
    
    # altera type para: DEV, FUNC, QA, UAT.
    '''
    if '] [UAT' in d :
        dados["Type"] = "UAT"
    if '] [DEV' in d :
        dados["Type"] = "DEV"
    if '] [FUNC' in d :
        dados["Type"] = "FUNC"
    if '] [QA' in d :
        dados["Type"] = "QA"
    '''
        
    # conerte os segundo para horas
    if dados['Revisions'][0]['Fields'][cont]['ReferenceName'] == "Microsoft.VSTS.Scheduling.OriginalEstimate":
        time_o = float( dados['Revisions'][0]['Fields'][cont]['Value'] ) 
        time_o = (time_o/60) / 60
        dados['Revisions'][0]['Fields'][cont]['Value'] = time_o
        cont += 1                
        
    if dados['Revisions'][0]['Fields'][cont]['ReferenceName'] == "Microsoft.VSTS.Scheduling.RemainingWork":
        time_r = float( dados['Revisions'][0]['Fields'][cont]['Value'] )
        time_r = (time_r/60) / 60
        dados['Revisions'][0]['Fields'][cont]['Value'] = time_r
        cont += 1
        
    if dados['Revisions'][0]['Fields'][cont]['ReferenceName'] == "Microsoft.VSTS.Scheduling.CompletedWork":
        time_c = float( dados['Revisions'][0]['Fields'][cont]['Value'] )
        time_c = (time_c/60) / 60
        dados['Revisions'][0]['Fields'][cont]['Value'] = time_c 
        
    # reescreve o aquivo .json  --------------------------------       
    with open(caminho, 'w') as jsonFile:
        json.dump(dados, jsonFile)
        jsonFile.close()


# In[29]:


import os

Item = []
pasta = r"C:\Users\6113871\OneDrive - Thomson Reuters Incorporated\Documents\Thomson Reuters\ADO_roteiro\Impor_ADO"

arquivos = os.listdir(pasta) 

for i in range(len(arquivos)):
    if 'GTMPS' in arquivos[i] :
        if '.json' in arquivos[i]  :
            Item.append( arquivos[i][6:] )


      


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




