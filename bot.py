import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def LogIn(driver, username, pasword) :
    driver.find_element_by_id("user").send_keys(username)
    driver.find_element_by_id("parola").send_keys(pasword)
    driver.find_element_by_xpath("//*[@id=\"form-login\"]/div/div[2]/div[4]/button").click()
    time.sleep(3)

def isproblem(driver) :
    if driver.title == "www.pbinfo.ro":
        return 0
    else :
        return 1

def writeProblem(driver) :
    message = driver.find_element_by_xpath("//*[@id=\"form-incarcare-solutie\"]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div/pre")
    message.send_keys(Keys.SHIFT, Keys.INSERT)
    driver.find_element_by_xpath("//*[@id=\"btn-submit\"]").click()
    time.sleep(3)

def CopyProblem(driver) :
    copiedText = driver.find_element_by_xpath("//*[@id=\"post-354\"]/div[2]/pre").text
    print(copiedText)

    # Firefox - pbinfo 500_IQ
    # Chrome  - zecelainfo.com

driverFirefox = webdriver.Firefox(executable_path=r"C:\Users\jmogo\AppData\Local\Temp\Temp1_geckodriver-v0.28.0-win64.zip\geckodriver.exe")
driverFirefox.get("https://www.pbinfo.ro/")
LogIn(driverFirefox, "500_IQ", "exemplu1")

driverChrome = webdriver.Firefox(executable_path=r"C:\Users\jmogo\AppData\Local\Temp\Temp1_geckodriver-v0.28.0-win64.zip\geckodriver.exe")

for NrOfProblem in range (3627, 4001) :
    NewUrlPbinfo = "https://www.pbinfo.ro/probleme/" + str(NrOfProblem)
    UrlSolOFPbinfo = "https://www.pbinfo.ro/?pagina=solutie-oficiala&id=" + str(NrOfProblem)
    driverFirefox.get(NewUrlPbinfo)

    if isproblem(driverFirefox) == 1: #daca este pb pe pbinfo
        driverFirefox.get(UrlSolOFPbinfo)
        UrlZeceLaInfo = "https://www.zecelainfo.com/modulul2/"
        driverChrome.get(UrlZeceLaInfo)
        if "numai de utilizatorii" in driverFirefox.page_source: #daca nu o am pe 500IQ
            driverChrome.find_element_by_id("wp-block-search__input-1").send_keys(str(NrOfProblem)) #pun nr pb

            driverChrome.find_element_by_css_selector(".wp-block-search__button").click() #apas pe search

            time.sleep(1)
            driverChrome.find_element_by_css_selector("#post-9214 > footer:nth-child(4) > a:nth-child(1)").click() #apas pe readmore


            print(driverChrome.title)
            #if "Page not found" in driverChrome.page_source:
            #    driverChrome.title
            #else:
            #    CopyProblem(driverFirefox)
            #    writeProblem(driverFirefox)
