from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os  
import pandas as pd
import openpyxl
import pprint
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/Users/hoang/Desktop/Diem thi/chromedriver.exe")
url = "https://tracuu.hanoi.edu.vn/"
driver.get(url)
sbd = 0
dau = 1
cuoi = 1
day1 = []
day2 = []
day3 = []
dem = 0
for i in range(4000):
	sbd = str(dau)
	if dau <10:
		sbd="0"+str(dau)
	if cuoi <10:
		sbd+="000"+str(cuoi)
	elif cuoi<100:
		sbd+="00"+str(cuoi)
	elif cuoi>=100:
		sbd +="0"+str(cuoi)
	print(sbd)
	username = driver.find_element(By.ID,"ASPxPageControl1_ASPxTextBox1_I");
	print(username)
	username.send_keys(sbd)
	chon = driver.find_element(By.ID,"ASPxPageControl1_ASPxButton1")
	chon.click()
	time.sleep(1)
	try:
		h1 =driver.find_element(By.XPATH,"/html/body/form/div[4]/div/div[1]/div/div/table/tbody/tr[2]/td[1]").text
		h2 =driver.find_element(By.XPATH,"/html/body/form/div[4]/div/div[1]/div/div/table/tbody/tr[2]/td[2]").text
		h3 =driver.find_element(By.XPATH,"/html/body/form/div[4]/div/div[1]/div/div/table/tbody/tr[2]/td[3]").text
		day1.append(h1)
		day2.append(h2)
		day3.append(h3)
		cuoi+=1
	except:
		dau+=1
		cuoi=1
		dem+=1
	if dem > 100:
		break
	
data_series = {"sbd" : day1, "mon" :day2,"diem": day3}
df_data = pd.DataFrame(data_series)
df_data.to_excel('C:/Users/hoang/Desktop/Diem thi/output.xlsx')  
