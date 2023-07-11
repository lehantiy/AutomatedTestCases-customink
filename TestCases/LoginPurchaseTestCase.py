import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from faker import Faker
from selenium.webdriver.support.select import Select

NewEmail = input("Enter your email adress: ")
faker = Faker("en_US")
driver = webdriver.Chrome()
action = ActionChains(driver)
driver.maximize_window()
driver.get('https://www.customink.com')
time.sleep(2)

class TestCase:
    def accountRegistering(self):
        page = driver.find_element(By.XPATH, "//a[@id='sb-menu-account']")
        if page.is_displayed():
            page.click()
        else:
            driver.find_element(By.XPATH, "//div[@class='sb-HeaderTop-hamburger']").click()
            driver.find_element(By.XPATH, "//nav[@class='sb-Menu slideout-menu slideout-menu-left']//a[@id='sb-menu-account']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineNone css-1yk1vai']").click()
        time.sleep(3)
        email = driver.find_element(By.XPATH, "//input[@id='user_email']")
        email.send_keys(NewEmail)
        time.sleep(1)
        password = driver.find_element(By.XPATH, "//input[@id='user_password']")
        password.send_keys("qwertyuiop")
        time.sleep(1)
        password_repeat = driver.find_element(By.XPATH, "//input[@id='user_password_confirmation']")
        password_repeat.send_keys("qwertyuiop")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='eu_consent']").click()
        time.sleep(1)
        continueButton = driver.find_element(By.XPATH, "//button[@id='signup_submit']")
        print(continueButton.is_displayed())
        continueButton.click()
        driver.find_element(By.XPATH, "//a[@class='sb-HeaderTop-inky']").click()

    def productChoosing(self):
        productsCatalog = driver.find_element(By.XPATH, "//a[@id='sb-menu-products']")
        action.move_to_element(productsCatalog).perform()
        time.sleep(2)
        hatsSection = driver.find_element(By.XPATH, "//div[@class='sb-MenuPanel is-Active']//a[@class='sb-MMP-nav-link'][normalize-space()='Hats']")
        action.move_to_element(hatsSection).perform()
        hatsSection.click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//body/div[@class='sb-PageWrapper']/main[@class='sb-Main']/div[@class='pc-Subcategories']/div[@class='pc-CatCards sb-Wrapper']/div[2]/div[2]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@title='Blue']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//body/div[@class='sb-PageWrapper']/main[@class='sb-Main']/div[@class='algolia-listing-pages no-pseudo']/div[@data-react-class='AlgoliaListingPages']/div[@class='pc-Styles']/div[@class='pc-Styles-body sb-Wrapper']/div[@class='pc-Styles-products is-filterSortShown is-filteredColor is-filteredColor--blue is-defaultQuoteShown']/div[@class='pc-Products']/div[1]/div[1]/a[1]/div[1]").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedBlue.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-disableElevation.MuiButton-fullWidth.MuiButton-root.MuiButton-contained.MuiButton-containedBlue.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-disableElevation.MuiButton-fullWidth.css-1bo7o26").click()
        time.sleep(4)

    def productCustomising(self):
        driver.get("https://www.customink.com/ndx/?EU=true&PK=245903&SK=245900&prefer_singles=false#/")

        try:
            GotItButton = driver.find_element(By.XPATH, "//button[normalize-space()='Got It!']")
        except Exception:
            print("Element GotItButton is not found")
            pass
        else:
            GotItButton.click()

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#_13-add-text").click()
        time.sleep(1)
        myText = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter text here']")
        myText.click()
        myText.send_keys("MY TEXT")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add To Design']").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".ndx-IconCardTool-container.ndx-IconCardTool--font.ndx-IconCardTool-container--clickable").click()
        time.sleep(1)
        fontSearch = driver.find_element(By.CLASS_NAME, "ndx-Search-input")
        fontSearch.click()
        time.sleep(1)
        fontSearch.send_keys("Montserrat")
        time.sleep(1)
        fontSearch.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "body div[id='root'] div[class='ndx-FontCategoryOverlay-listContainer'] div div div div:nth-child(1) div:nth-child(1) div:nth-child(1)").click()
        driver.find_element(By.XPATH, "//div[@class='ndx-MenuButton isActionable ndx-NavHeader-back']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[normalize-space()='Text Color']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@class='undefined css-1t45vmf']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='Done']").click()
        rotationSlider = driver.find_element(By.XPATH, "//div[@role='slider']")
        time.sleep(1)
        ActionChains(driver).drag_and_drop_by_offset(rotationSlider, 12, 0).perform()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".ndx-IconCardTool-container.ndx-IconCardTool--outline.ndx-IconCardTool-container--clickable").click()
        time.sleep(1)
        outlineSlider = driver.find_element(By.CSS_SELECTOR, "div[role='slider']")
        ActionChains(driver).drag_and_drop_by_offset(outlineSlider, 600, 0).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='undefined css-1p18xf8']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='Done']").click()
        time.sleep(2)
        resizeSelector = driver.find_element(By.XPATH, "//div[@class='ndx-Design-selection-handle isResize']")
        ActionChains(driver).drag_and_drop_by_offset(resizeSelector, -500, 50).perform()
        time.sleep(2)
        textOnHat = driver.find_element(By.XPATH, "//div[@class='ndx-Design-selection-dragzone']")
        ActionChains(driver).drag_and_drop_by_offset(textOnHat, -10, -100).perform()
        time.sleep(2)


    def purchasing(self):
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

        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='See Your All-Inclusive Price']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Buy Now']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your first name']").send_keys(faker.first_name())
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your last name']").send_keys(faker.last_name())
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='e.g. CalTech, General Electric']").send_keys(faker.company())
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter street name']']").send_keys(faker.street_address())
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Apt. / Suite']").send_keys(faker.building_number())
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys(faker.city())
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='ZIP']").send_keys(faker.postcode())
        time.sleep(1)
        country = driver.find_element(By.XPATH, "//select[@name='country']")
        selectCounry = Select(country)
        selectCounry.select_by_value("US")
        state = driver.find_element(By.XPATH, "//select[@name='country']")
        selectState = Select(state)
        selectState.select_by_value("California")
        driver.find_element(By.XPATH, "//input[@placeholder='Mobile number preferred']").send_keys(faker.phone_number())
        time.sleep(1)
        continueButton = driver.find_element(By.XPATH, "//button[normalize-space()='Continue to Payment']")
        print(continueButton.is_enabled())
        continueButton.click()






Script = TestCase()
# Script.accountRegistering()
# Script.productChoosing()
# Script.productCustomising()
Script.purchasing()