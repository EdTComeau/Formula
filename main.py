from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time


def RavioliRavioliGiveMeTheHypoallergenicFormuoli():
    zipCode = '02035'

    driver = webdriver.Firefox()

    driver.get("https://www.walgreens.com/store/c/well-beginnings-hypoallergenic-infant-formula-powder-with-iron/ID=300413751-product")
    driver.implicitly_wait(1)
    LookNearby = driver.find_element(by=By.ID, value="check-other-stores-dialog")
    LookNearby.click()
    time.sleep(3)
    ZipCodeSearch = driver.find_element(by=By.CSS_SELECTOR, value=".margin__top--medium > h4:nth-child(1) > a:nth-child(1)")
    ZipCodeSearch.click()
    ZipCodeEnter = driver.find_element(by=By.ID, value="wag-find-zip")
    ZipCodeEnter.send_keys(zipCode)
    SearchButton = driver.find_element(by=By.ID, value="findButtonId")
    SearchButton.click()


    driver.switch_to.new_window('tab')
    driver.get("https://www.walgreens.com/store/c/gerber-extensive-ha-hypoallergenic-powder-infant-formula-with-iron/ID=prod6286124-product")
    driver.implicitly_wait(1)
    time.sleep(3)
    LookNearby = driver.find_element(by=By.ID, value="check-other-stores-dialog")
    LookNearby.click()
    time.sleep(3)
    ZipCodeSearch = driver.find_element(by=By.CSS_SELECTOR, value=".margin__top--medium > h4:nth-child(1) > a:nth-child(1)")
    ZipCodeSearch.click()
    ZipCodeEnter = driver.find_element(by=By.ID, value="wag-find-zip")
    ZipCodeEnter.send_keys(zipCode)
    SearchButton = driver.find_element(by=By.ID, value="findButtonId")
    SearchButton.click()
    

    driver.switch_to.new_window('tab')
    driver.get("https://www.cvs.com/shop/cvs-health-hypoallergenic-infant-formula-powder-with-iron-prodid-3610053")
    driver.implicitly_wait(1)
    LookNearby = driver.find_element(by=By.CSS_SELECTOR, value="div.r-tzz3ar:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    LookNearby.click()
    time.sleep(3)
    ZipCodeEnter = driver.find_element(by=By.CSS_SELECTOR, value=".r-6vlu5k")
    ZipCodeEnter.send_keys(zipCode)
    SearchButton = driver.find_element(by=By.CSS_SELECTOR, value=".r-1jkjb > div:nth-child(1) > img:nth-child(2)")
    SearchButton.click()
    

    driver.switch_to.new_window('tab')
    driver.get("https://www.target.com/p/non-gmo-hypoallergenic-powder-infant-formula-19-8oz-up-38-up-8482/-/A-79550107#lnk=sametab")
    driver.implicitly_wait(1)
    time.sleep(3)
    LookNearby = driver.find_element(by=By.ID, value="addToCartButtonOrTextIdFor79550107")
    LookNearby.click()
    time.sleep(3)
    ZipCodeFind = driver.find_element(by=By.CSS_SELECTOR, value=".styles__ContentWrapper-sc-190xyua-1 > button:nth-child(2)")
    ZipCodeFind.click()
    time.sleep(3)
    ZipCodeEnter = driver.find_element(by=By.ID, value="zip-or-city-state")
    ZipCodeEnter.clear()
    ZipCodeEnter.send_keys(zipCode)
    SearchButton = driver.find_element(by=By.CSS_SELECTOR, value=".h-padding-h-wide")
    SearchButton.click()

