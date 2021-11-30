#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import json
import os


# Faz leitura 
def ler(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

lista_vazia = []    
caminho = r"C:\Users\6113871\OneDrive - Thomson Reuters Incorporated\Documents\Thomson Reuters\ADO_roteiro\Impor_ADO\GTMPS-14619.json"
dados = ler(caminho)
d = str(dados)

for i in range(len( dados['Revisions'] )) :
    if dados['Revisions'][i]['Fields'] != lista_vazia :        
        if dados['Revisions'][i]['Fields'][0]['ReferenceName'] == 'System.AssignedTo' :
            if dados['Revisions'][i]['Fields'][0]['Value'] == 'JIRAUSER33250' :
                dados['Revisions'][i]['Fields'][0]['Value'] = 'vitor.vilela@thomsonreuters.com'
            elif dados['Revisions'][i]['Fields'][0]['Value'] == 'JIRAUSER33221' :
                dados['Revisions'][i]['Fields'][0]['Value'] = 'antonio.barboza@thomsonreuters.com'
            elif dados['Revisions'][i]['Fields'][0]['Value'] == 'JIRAUSER35170' :
                dados['Revisions'][i]['Fields'][0]['Value'] = 'carlos.cirqueira@thomsonreuters.com'
            elif dados['Revisions'][i]['Fields'][0]['Value'] == 'JIRAUSER35169' :
                dados['Revisions'][i]['Fields'][0]['Value'] = 'leandro.antonazzi@thomsonreuters.com'
    
            with open(caminho, 'w') as jsonFile:
                json.dump(dados, jsonFile)
                jsonFile.close()
            




# In[ ]:





# In[ ]:




