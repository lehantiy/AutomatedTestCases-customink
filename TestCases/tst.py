from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

class TestCase:
    def purchasing(self):
        driver.get("https://www.customink.com/ndx/?EU=true&PK=159506&SK=159500&prefer_singles=false#/welcomeBack")

        try:
            GotItButton = driver.find_element(By.XPATH, "//button[normalize-space()='Got It!']")
        except:
            print("No such element")
        else:
            GotItButton.click()

        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Get Price']").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedBlue.MuiButton-sizeLarge.MuiButton-containedSizeLarge.MuiButton-disableElevation.MuiButton-root.MuiButton-contained.MuiButton-containedBlue.MuiButton-sizeLarge.MuiButton-containedSizeLarge.MuiButton-disableElevation.proceedButton.css-kp9d1c").click()
        time.sleep(2)
        try:
            one_quantity = driver.find_element(By.XPATH, "//input[@id='sizeInputOne Size']")

        except:
            print("No one_quantity element")
            adultQuantity = driver.find_element(By.XPATH, "//input[@id='sizeInputAdult']")
            adultQuantity.send_keys("12")
        else:
            one_quantity.send_keys("12")



script = TestCase()
script.purchasing()