from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config

# only plebs use Chrome
driver = webdriver.Firefox()
driver.get("http://www.google.com")

f = open("searches.txt", "r+")
searches = f.read().split('\n')
if not searches:
    # search a few memes if nothing else
    searches.append("lmao")
    searches.append("here comes dat boi")
    searches.append("The mighty King Cobra, King of the Jungle")

# navigate to Google login page
driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
inputElement = driver.find_element_by_name("identifier")
inputElement.send_keys(Config.user)
inputElement = driver.find_element_by_id("identifierNext")
inputElement.click()
WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.ID, "password")))
inputElement = driver.find_element_by_name("password")
inputElement.send_keys(Config.pw)
WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.ID, "passwordNext")))
inputElement = driver.find_element_by_id("passwordNext")
inputElement.click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"q")))


# you should be redirected to google homepage
for item in searches:
    # if foo bar pops up, click it!
    print(item)
    inputElement = driver.find_element_by_name("q").clear()
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys(item)
    inputElement.submit()
    WebDriverWait(driver, 10).until(EC.title_contains(item))
    try:
        ie = driver.find_element_by_xpath("//*[contains(text(),'foobar')]")
        break
    except:
        pass
    # we do this relatively slowly as the program fails on captchas
    WebDriverWait(driver, 30)

# driver.quit()
