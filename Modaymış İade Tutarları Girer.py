#Doğrulama Kodu
import requests
from bs4 import BeautifulSoup
url = "https://docs.google.com/spreadsheets/d/1AP9EFAOthh5gsHjBCDHoUMhpef4MSxYg6wBN0ndTcnA/edit#gid=0"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
first_cell = soup.find("td", {"class": "s2"}).text.strip()
if first_cell != "Aktif":
    exit()
first_cell = soup.find("td", {"class": "s1"}).text.strip()
print(first_cell)


from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import tkinter as tk
from tkinter import simpledialog
import chromedriver_autoinstaller



print(" ")
print("Oturum Açma Başarılı Oldu")
print(" /﹋\ ")
print("(҂`_´)")
print("<,︻╦╤─ ҉ - -")
print("/﹋\\")
print("(Kod Bekçisi)")
print("Mustafa ARI")
print(" ")
print("https://docs.google.com/spreadsheets/d/1yfHhnQ2YpPMxhqxSJn4I6prsxH4Fy-bob_k0E_60wkc/edit#gid=0")













google_sheet_url = "https://docs.google.com/spreadsheets/d/1yfHhnQ2YpPMxhqxSJn4I6prsxH4Fy-bob_k0E_60wkc/gviz/tq?tqx=out:csv"

try:
    google_df = pd.read_csv(google_sheet_url)
    google_excel_file = "E-Tablodaki İadeler.xlsx"
    google_df.to_excel(google_excel_file, index=False)
except requests.exceptions.RequestException as e:
    pass





chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--log-level=1') 
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  
driver = webdriver.Chrome(options=chrome_options)

login_url = "https://www.modaymis.com/kullanici-giris/?ReturnUrl=%2Fadmin"
driver.get(login_url)

email_input = driver.find_element("id", "EmailOrPhone")
email_input.send_keys("mustafa@modaymis.com")

password_input = driver.find_element("id", "Password")
password_input.send_keys("123456")
password_input.send_keys(Keys.RETURN)

# WebDriverWait kullanarak butonun görünmesini bekliyoruz
try:
    # Butonu bulmak için maksimum 10 saniye bekliyoruz
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "faprikabutton-yes"))
    )
    # Buton görünür olduğunda tıklıyoruz
    button.click()
except Exception as e:
    pass


# Google Sheets verilerini içeren Excel dosyasını okuyun
google_df = pd.read_excel("E-Tablodaki İadeler.xlsx")


# Giriş yaptıktan sonra işlem yapmak için her bir satırdaki "Link" sütunundaki URL'leri ziyaret edin
for index, row in google_df.iterrows():
    link = row["Link"]
    driver.get(link)
    
    # ToplamFiyat değerini alın
    total_price = row["Toplam Fiyat"]
    
    # Düzenleme butonunu bulun
    edit_button = driver.find_element(By.ID, "btnEditBankAccountNumber")

    # Düzenleme butonuna tıklayın
    edit_button.click()

    # İlgili input alanını bulun
    bank_account_input = driver.find_element(By.ID, "BankAccountNumber")

    # ToplamFiyat değerini alın
    total_price = row["Toplam Fiyat"]

    # İlgili input alanına değeri yazın
    bank_account_input.clear()
    bank_account_input.send_keys(total_price)

    # Değişiklikleri kaydetmek için gerekli butona tıklayın
    save_button = driver.find_element(By.ID, "btnSaveBankAccountNumber")
    save_button.click()

    # Kaydetme onayı için gerekli butonu bulun
    confirmation_button = driver.find_element(By.ID, "btnSaveBankAccountNumber-action-confirmation-submit-button")

    # Kaydetme onayı butonuna tıklayın
    confirmation_button.click()
    
    
    
kurgu_excel_adi = "E-Tablodaki İadeler.xlsx"

# Dosyayı sil
if os.path.exists(kurgu_excel_adi):
    os.remove(kurgu_excel_adi)
else:
    print(f"{kurgu_excel_adi} dosyası zaten mevcut değil.")


# Tarayıcıyı kapatın
driver.quit()





