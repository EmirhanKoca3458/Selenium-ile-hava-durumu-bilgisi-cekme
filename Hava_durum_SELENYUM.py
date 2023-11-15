"""

url
gün , durum , sıcaklık
il , ilçe

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Weather:
    def __init__(self,city):
        self.url = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=" 
        self.brower = webdriver.Chrome()
        self.city = city 
        self.brower.maximize_window()
        
        
        
    def CityWeather(self):  # il hava durumu
        self.brower.get(self.url + self.city)
        time.sleep(2)
        
        day = self.brower.find_element(By.XPATH,"//*[@id='_3_saatlik']/table/tbody/tr[2]/th/span[1]").text
        info = self.brower.find_element(By.XPATH,"//*[@id='pages']/div/section/div[5]/div[1]/div[2]/div[2]").text
        celcium = self.brower.find_element(By.XPATH,"//*[@id='pages']/div/section/div[5]/div[1]/div[1]").text
        print(f" İl: {self.city} Gün: {day}  Hava: {info} Sıcaklık: {celcium}")
        
        
              
            
    def TownWeather(self,district): # ilçe
        self.district = district
        
        self.brower.get(self.url + self.city+"&ilce=" + self.district )
            
        day = self.brower.find_element(By.XPATH,"//*[@id='_3_saatlik']/table/tbody/tr[2]/th/span[1]").text
        info = self.brower.find_element(By.XPATH,"//*[@id='pages']/div/section/div[5]/div[1]/div[2]/div[2]").text
        celcium = self.brower.find_element(By.XPATH,"//*[@id='pages']/div/section/div[5]/div[1]/div[1]").text
        print(f" İlçe: {self.district} Gün: {day}  Hava: {info} Sıcaklık: {celcium}")
        time.sleep(2)
        input("s")
            
            
    
    def close(self):
        print("Kapatılıyor ! ")
        self.brower.close()
    
    
    
hava = Weather("İstanbul")
#hava.CityWeather()
hava.TownWeather("Pendik")
hava.close()