import pandas as pd
import json
import os

# pega os nomes dos arquivos GTMPS ------------------
items = []
pasta = r"C:\Users\6113871\OneDrive - Thomson Reuters Incorporated\Documents\Thomson Reuters\ADO_roteiro\Impor_ADO"
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

    
lista_vazia = []    

pos = [ 0, 0];

for i in range(len(items)):    
    caminho = r"C:\Users\6113871\OneDrive - Thomson Reuters Incorporated\Documents\Thomson Reuters\ADO_roteiro\Impor_ADO\GTMPS-" + items[i]
    dados = ler(caminho)
    flag = False
    for i in range(len( dados['Revisions'] )) :
        if dados['Revisions'][i]['Fields'] != lista_vazia :            
            for el in range(len( dados['Revisions'][i]['Fields'] )) :
                if dados['Revisions'][i]['Fields'][el]['ReferenceName'] == 'Custom.Flagged' :
                    if dados['Revisions'][i]['Fields'][el]['Value'] == "True":
                        flag = True
                        
                if dados['Revisions'][i]['Fields'][el]['ReferenceName'] == 'System.AssignedTo' :
                    if dados['Revisions'][i]['Fields'][el]['Value'] == 'JIRAUSER33250' :
                        dados['Revisions'][i]['Fields'][el]['Value'] = 'vitor.vilela@thomsonreuters.com'
                        
                    elif dados['Revisions'][i]['Fields'][el]['Value'] == 'JIRAUSER33221' :
                        dados['Revisions'][i]['Fields'][el]['Value'] = 'antonio.barboza@thomsonreuters.com'
                        
                    elif dados['Revisions'][i]['Fields'][el]['Value'] == 'JIRAUSER35170' :
                        dados['Revisions'][i]['Fields'][el]['Value'] = 'carlos.cirqueira@thomsonreuters.com'
                        
                    elif dados['Revisions'][i]['Fields'][el]['Value'] == 'JIRAUSER35169' :
                        dados['Revisions'][i]['Fields'][el]['Value'] = 'leandro.antonazzi@thomsonreuters.com'
                        
                    elif dados['Revisions'][i]['Fields'][el]['Value'] == 'felipe.cassiani' :
                        dados['Revisions'][i]['Fields'][el]['Value'] = 'felipe.cassiani@thomsonreuters.com'
                        
                    elif dados['Revisions'][i]['Fields'][el]['Value'] == 'jose.paulon' :
                        dados['Revisions'][i]['Fields'][el]['Value'] = 'jose.paulon@thomsonreuters.com'
                        
                    elif dados['Revisions'][i]['Fields'][el]['Value'] == 'thainnara.santos' :
                        dados['Revisions'][i]['Fields'][el]['Value'] = 'thainnara.santos@thomsonreuters.com'
                        
                    elif dados['Revisions'][i]['Fields'][el]['Value'] == 'rodrigo.barbosa' :
                        dados['Revisions'][i]['Fields'][el]['Value'] = 'rodrigo.barbosa@thomsonreuters.com'
                        
                    elif dados['Revisions'][i]['Fields'][el]['Value'] == 'paulo.pardi' :
                        dados['Revisions'][i]['Fields'][el]['Value'] = 'paulo.pardi@thomsonreuters.com'
                        
                if (dados['Revisions'][i]['Fields'][el]['ReferenceName'] == 'System.State') :
                    pos[0] = i
                    pos[1] = el
                    
    if flag == True :               
        dados['Revisions'][pos[0]]['Fields'][pos[1]]['Value'] = "Impediment"



    with open(caminho, 'w') as jsonFile:
        json.dump(dados, jsonFile)
        jsonFile.close()
            



