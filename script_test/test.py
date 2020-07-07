# ---------------------------- Pass---------------------------------------------------|

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
# -----------------------------------------------------------------------------------|


# 1. ---------------------------------------------------------------------------------|
from selenium.webdriver.common.by import By 
from abc import ABC
from urllib.parse import urlparse


class PageElement(ABC):

    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url 

    def open_browser(self):
        self.webdriver.get(self.url) 
    
    def exit_browser(self):        
        self.webdriver.quit()


# 2. ---------------------------------------------------------------------------------|

class LoginPage(PageElement):

    button_togo_login = (By.CLASS_NAME, 'yx-njg')
    email = (By.ID, 'inputEmail')
    passw = (By.ID, 'inputPassword')
    check = (By.NAME, 'rememberme')
    # captcha = (By.CLASS_NAME, 'recaptcha-checkbox-unchecked')
    
    def login(self, email, passw):
       
        # click page init
        self.webdriver.find_element(*self.button_togo_login).click()      
        
        # Next tabs of page to login  
        self.webdriver.switch_to_window(webdriver.window_handles[1])
        sleep(2) 
       
        # Valide page
        url_browser = self.webdriver.current_url
        
        url ='https://phptravels.org/clientarea.php'
        
        if url == url_browser:
           
            # Imputs on fields 
            self.webdriver.find_element(*self.email).send_keys(email)    
           
            self.webdriver.find_element(*self.passw).send_keys(passw)
           
            self.webdriver.find_element(*self.check).click()    
           
            # self.webdriver.find_element(*self.captcha).click()
            
            return f'Ambas urls corretas: {url_browser}, {url}'
        
        else:
        
            return f'nops ): {url_browser}, {url}'    
        
    
class PageHome(PageElement):
    
        demo = (By.LINK_TEXT, 'Demo')
        pricing = (By.LINK_TEXT, 'Pricing')
        
        # Product       
        product = (By.CLASS_NAME, 'yx-njr')
        host_module = (By.LINK_TEXT, 'Hotels Module')
        flights_module = (By.LINK_TEXT, 'Flights Module')


        def click_links(self):
           
            url_demo = 'https://phptravels.com/demo' 
            url_pricing = 'https://phptravels.com/order'

            self.webdriver.find_element(*self.demo).click()
           
            sleep(2)
           
            url_browser_demo = self.webdriver.current_url 
        
            if url_browser_demo == url_demo:

                self.webdriver.find_element(*self.pricing).click()
                    
            url_browser_pricing = self.webdriver.current_url 
        
            if url_browser_pricing == url_pricing:
                
                print('clicks e urls ok')
           
            else:

                print('falhou!')
        
        def link_product(self):
          
            url_host_m = 'https://phptravels.com/hotels-module-features/'
           
            url_flights_module = 'https://phptravels.com/flights-module-features/'
            
            self.webdriver.find_element(*self.product).click()          
            
            sleep(2)
            
            self.webdriver.find_element(*self.host_module).click() 

            url_browser_host_m = self.webdriver.current_url   
            
            if url_browser_host_m == url_host_m:
            
                print(f'Urls estao ok corretas {url_browser_host_m} e {url_host_m}')
                
                self.webdriver.find_element(*self.product).click() 

                sleep(2)

                self.webdriver.find_element(*self.flights_module).click()        
                
                url__browser_flights_module = self.webdriver.current_url

                if url_flights_module == url__browser_flights_module:
               
                    print(f'Urls estao ok corretas {url__browser_flights_module} e {url_flights_module}')
                
                else:    

                    print (f'falha urls')

            else:

                print (f'falha urls')


class ValidedTexts(PageElement):

    title_support = (By.LINK_TEXT, 'SUPPORT') 
    text_support = (By.XPATH, '//*[@id="Main"]/section[2]/div/div[2]/div[1]/div/p')

    def suporttext(self):
        
        textpage = 'SUPPORT'
        
        alltext = 'We have a dedicated and expert support team for you, We communicate and help you with Livechat, Skype, Whatsapp and ticket system in real-time 24/7.'
        
        textpagebrowser = self.webdriver.find_element(*self.title_support).text

        assert textpage == textpagebrowser
    
        print(f'titulos corretos {textpage} e {textpagebrowser}')
    
        text_support_all = self.webdriver.find_element(*self.text_support).text

        if text_support_all == alltext:
        
            print(f'textos corretos {text_sup   port_all} e {alltext}')
        
        else:

            print(f'Erro {text_support_all}')


# 3. ---------------------------------------------------------------------------------|

#  Selenium call of functions 
from selenium.webdriver import Chrome  
from time import sleep 

webdriver = Chrome()
url = 'https://phptravels.com/'



page_home_valied_text = ValidedTexts(webdriver, url)
page_home_valied_text.open_browser()

page_home_valied_text.suporttext()

# --------------------------------------------------------|
# ***** PAGE HOME  ***********

# page_home = PageHome(webdriver, url)
# page_home.open_browser()


# page_home.click_links()
# page_home.link_product()
# sleep(4)
        
# page_home.exit_browser()


# --------------------------------------------------------|
# ***** PAGE LOGIN  ***********

# Pass instance and url  
# loga = LoginPage(webdriver, url)
# loga.open_browser()

# *Call function
# Insert value on field of login and printed on terminal true or false 

# print (loga.login(
#      email = 'mateus',
#      passw = 'abcd'
# ))

# loga.exit_browser()

