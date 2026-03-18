# Acessamos a URL e transformamos o JSON em um dicionário Python (desserializar). 
# Quando baixamos, ele estará em Json e temos que transformar em algo que o Python entenderá. 

from urllib import response

import requests

# uma boa prática é dar nomes maiusculos para as classes
# Snake case para as variáveis e funções: minúsulo e underline para separar as palavras.

class Extract():
#() espaço que utilizamos para dizer quais as variáveis que serão utilizadas
    def __init__(self):
        pass
    #__init - método construtor. Serve para setar configurações. Uma vez que a classe for executada, ele vai iniciar a classe com as funções
    #self - referenciar ela mesma (classe). é como vamos relacionar os elementos dentro da propria classe. 
    #tudo que estiver dentro da classe é chamado de método (o def não é chamado mais de função).

    def extract_country(self, country:str) -> list[dict]:
        
        url=f"http://universities.hipolabs.com/search?country={country}"
        response = requests.get(url)
        response.raise_for_status()  
        universities = response.json()
        
        return universities
    
# a classe extract tem um método de extrair informações de país (def extract_country) da url que vamos utilizar
# f - string - pega a variável "country", nesse caso, e vai substituir onde tiver chave. Maneira rápida de personalizar a string de acordo com a variável.

# a responsablidade do extract é acessar a url, pegar as informações e transformar em um dicionário Python (desserializar)

