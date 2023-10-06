from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=/home/pritam/projects/autoBuy90/telegram')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.telegram.org/k/#@QuickDealsx_quick_deals")
time.sleep(5)
elements = driver.find_elements(By.XPATH, "//div[@class='message spoilers-container']//a")
links = []
for e in elements:
    print(e)
    links.append(e.get_attribute('herf'))
print("all elements printed...")
# with open("links.txt", 'a') as file :
#     for i in links:
#         file.write(i+"\n")


time.sleep(1000)