from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Functions
from DataManager import *
from MegaStorage import *

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

filePath01 = "data/companySymbol.txt"
file = open(filePath01, 'r')
MegaStorage.Symbol.clear()
for line in file:
    MegaStorage.Symbol.append(line.strip())
file.close()

def testFun():
    dateArr = []
    reportArr = []
    profitLossValue = []
    dateArrNew = []
    quarterArr = []
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get("https://www.sharesansar.com/proposed-dividend") 
    for companyIndex in range(0, len(MegaStorage.Symbol)):
        try:
            search_bar = driver.find_element_by_id("companypagesearch")
            search_bar.send_keys(MegaStorage.Symbol[companyIndex])
            search_bar.send_keys(Keys.RETURN)
            sleep(3)
            financialReport = driver.find_element_by_id("btn_ccfinanrep")
            financialReport.click()
            sleep(3)
            select = Select(driver.find_element_by_xpath("//select[@name='myTableCFinanRep_length']"))
            select.select_by_visible_text('50')
            sleep(3)
            reports = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//table[@id='myTableCFinanRep']//tbody//tr//td")))
            count = 0
            for item in reports:
                if (count%2)==0:
                    dateArr.append(item.text)
                else:
                    reportArr.append((item.text))
                count += 1
            
            for count1 in range(0, len(dateArr)):
                Temporary.clear()
                count = 0
                flag = False
                for word in reportArr[count1].split():
                    Temporary.append(word)
                    if word=="million":
                        if reportArr[count1].find("profit")>=0:
                            try:
                                profitLossValue.append(str(float(Temporary[count-1]) * 1000000))
                            except:
                                profitLossValue.append(float(0.0))
                        else:
                            try:
                                profitLossValue.append(str(float(Temporary[count-1]) * (-1000000)))
                            except:
                                profitLossValue.append(float(0.0))
                        flag = True
                        break
                    elif word=="billion":
                        if reportArr[count1].find("profit")>=0:
                            try:    
                                profitLossValue.append(str(float(Temporary[count-1]) * 1000000000))
                            except:
                                profitLossValue.append(float(0.0))
                        else:
                            try:
                                profitLossValue.append(str(float(Temporary[count-1]) * (-1000000000)))
                            except:
                                profitLossValue.append(float(0.0))
                        flag = True
                        break
                    count += 1
                if flag==True:
                    if reportArr[count1].find("1st")>=0:
                        quarterArr.append("1")
                    elif reportArr[count1].find("2nd")>=0:
                        quarterArr.append("2")
                    elif reportArr[count1].find("3rd")>=0:
                        quarterArr.append("3")
                    elif reportArr[count1].find("4th")>=0:
                        quarterArr.append("4")
                    else:
                        quarterArr.append("0")
                    dateArrNew.append(dateArr[count1])

            dateArrNew.reverse()
            quarterArr.reverse()
            profitLossValue.reverse()
            filePath = "testFile/" + MegaStorage.Symbol[companyIndex] + ".txt"
            open(filePath, 'w').close()
            file = open(filePath, 'a')
            for index in range(0, len(dateArrNew)): 
                string = f"{dateArrNew[index]} {profitLossValue[index]} {quarterArr[index]}\n"
                file.write(string)
            file.close()
            print(f"{MegaStorage.Symbol[companyIndex]}")
        except:
            print(f"\t{MegaStorage.Symbol[companyIndex]}")
        finally:
            dateArr.clear()
            reportArr.clear()
            profitLossValue.clear()
            dateArrNew.clear()
            quarterArr.clear()
            MegaStorage.Temporary.clear()
    driver.close()

testFun()