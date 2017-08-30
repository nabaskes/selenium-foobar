from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.google.com")

f = open("searches.txt","r+")
searches = f.read().split('\n')
if not searches:
    searches.append("lmao")
    searches.append("here comes dat boi")
    searches.append("The mighty King Cobra, King of the Jungle")

inputElement = driver.find_element_by_name("q")

for item in searches:
    print(item)
    inputElement.send_keys(item)
    WebDriverWait(driver, 10).until(EC.title_contains(item))
    WebDriverWait(driver, 10)

#driver.quit()
