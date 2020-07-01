#1 - Criar uma classe PageElement
    #a. Usando lib abstrata(abs)
    #b. Criar funcão com __init__  para receber webdriver e url 

# 2 - Criar Classes das featute passando como parametro o (PageElement)
    #a. Mapear os elementos da page
    #b. Criar funcão para realizar a ação
     
# 3 - Criar estrutura do selenium
    #a. Import lib 
    #b. declarar url 
    #c. Instanciar navegador
    #d. Passar para as funcoes __init__


from selenium.webdriver.common.by import By 
from abc import abc

#1
class PageElement(ABS):

    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url 





#---------------------------------------------------------------------------------|

#3 - Selenium e chamada das funções
from selenium.webdriver import Chrome 

browser = Chrome()
url = 'https://g1.globo.com/'
browser.get(url)
