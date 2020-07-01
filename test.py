#1 - create class abstract PageElement
    #a. Use lib abstract (abs)
    #b. Create function with  __init__  to get webdriver and url 

# 2 - Create class of features with parameters  the (Page Element)   
    #a. Get elements of pages
    #b. Create function to action on browser
     
# 3 - Create structs of selenium
    #a. Import lib 
    #b. Declare url 
    #c. Instantiate browser
    #d. Pass to functions __init__


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
url = 'https://phptravels.com/demo/'
browser.get(url)


