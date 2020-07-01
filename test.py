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


# 1. ---------------------------------------------------------------------------------|
from selenium.webdriver.common.by import By 
from abc import ABC

class PageElement(ABC):

    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url 

    def open_browser(self):
        self.webdriver.get(self.url)     


# 2. ---------------------------------------------------------------------------------|

class FirstPart(PageElement):

    button = (By.CLASS_NAME, 'yx-njg')


    def click_button(self):
        self.webdriver.find_element(*self.button).click()



# 3. ---------------------------------------------------------------------------------|

#  Selenium e chamada das funções
from selenium.webdriver import Chrome  

webdriver = Chrome()
url = 'https://phptravels.com/demo/'




# ------------------------> FisrtPart 
# Pass instance and url  
click = FirstPart(webdriver, url)
click.open_browser()
# Call function
click.click_button()


# -----------------------> SecoundPart 