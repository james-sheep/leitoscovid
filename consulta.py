import requests
from datetime import datetime


def busca_api(cidade):
            
    url = "https://elastic-leitos.saude.gov.br/leito_ocupacao/_search"
    payload = {"size": 500, "query": {"match": {"municipio": cidade}}}

    r = requests.post(url, auth=('user-api-leitos', 'aQbLL3ZStaTr38tj'), json=payload)
    a = r.json()

    lista_de_dict = []

    for n in a['hits'].values():

        if type(n) == list:

            for i in n:
                resumo = i["_source"]
                if "nomeCnes" in resumo:
                    lista_de_dict.append(resumo)


    for n in lista_de_dict:
        tratamento1 = n["dataNotificacaoOcupacao"]
        tratamento2 = tratamento1[:10]
        data= datetime.strptime(tratamento2, '%Y-%m-%d').date()
        resultado = str(data.day)+"/"+str(data.month)+"/"+str(data.year)
        n["dataNotificacaoOcupacao"] = resultado
        
    return lista_de_dict