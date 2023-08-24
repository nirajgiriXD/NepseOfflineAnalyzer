import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MegaStorage import *
from time import sleep
import MegaStorage
import Functions
import socket
import os

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def removeUnwantedCharacter(string):
    string = string.replace(' ', '')
    string = string.replace(',', '')
    string = string.replace('%', '')
    string = string.replace('\n', '')
    string = string.replace(':', '')
    string = string.replace('', '')
    return string

def removeFurther(string):
    tranlation = ""
    for letter in string:
        if letter=='(':
            break
        else:
            tranlation = tranlation + letter
    return tranlation

def isConnected():
    try:
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False

def marketDataLoader():
    Functions.clearMarketDataStorage()
    marketDataLoaderError = False
    isEmpty = False
    filePath = fileName1 + "marketData" + fileExtension
    try:
        if os.path.getsize(filePath)>0:
            file = open(filePath, 'r')
            for index in range(0, numberOfCompanies):
                line = file.readline()
                for word in line.split():
                    if word=="NULL":
                        Temporary.append(0.0)
                    else:
                        Temporary.append(float(word))
                try:
                    OutStandingShare.append(Temporary[0])
                except:
                    OutStandingShare.append(float(0))
                try:
                    MarketPrice.append(Temporary[1])
                except:
                    MarketPrice.append(float(0))
                try:
                    PercentageChange.append(Temporary[2])
                except:
                    PercentageChange.append(float(0))
                try:
                    Avg120Day.append(Temporary[3])
                except:
                    Avg120Day.append(float(0))
                try:
                    OneYearYield.append(Temporary[4])
                except:
                    OneYearYield.append(float(0))
                try:
                    Eps.append(Temporary[5])
                except:
                    Eps.append(float(0))
                try:
                    PERatio.append(Temporary[6])
                except:
                    PERatio.append(float(0))
                try:
                    BookValue.append(Temporary[7])
                except:
                    BookValue.append(float(0))
                try:
                    Pbv.append(Temporary[8])
                except:
                    Pbv.append(float(0))
                try:
                    Dividend.append(Temporary[9])
                except:
                    Dividend.append(float(0))
                try:
                    Bonus.append(Temporary[10])
                except:
                    Bonus.append(float(0))
                try:
                    RightShare.append(Temporary[11])
                except:
                    RightShare.append(float(0))
                try:
                    AvgVol130Day.append(Temporary[12])
                except:
                    AvgVol130Day.append(float(0))
                try:
                    MarketCapitalisation.append(Temporary[13])
                except:
                    MarketCapitalisation.append(float(0))
                Temporary.clear()
            file.close()
        else:
            isEmpty = True
    except:
        marketDataLoaderError = True
    finally:
        if marketDataLoaderError==True or isEmpty==True:
            print("\t\t[ Error ] :" + Functions.center("Market data could not be loaded", 60))
            Functions.programExit()

def marketDataSaver():
    marketDataSaverError = False
    filePath = fileName1 + "marketData" + fileExtension
    try:
        open(filePath, 'w').close()
        file = open(filePath, 'a')
        for index in range(0, numberOfCompanies):
            string1 = f"{OutStandingShare[index]} {MarketPrice[index]} {PercentageChange[index]} {Avg120Day[index]} {OneYearYield[index]} {Eps[index]} "
            string2 = f"{PERatio[index]} {BookValue[index]} {Pbv[index]} {Dividend[index]} {Bonus[index]} {RightShare[index]} {AvgVol130Day[index]} "
            string3 = f"{MarketCapitalisation[index]}\n"
            string = string1 + string2 + string3
            file.write(string)
        file.close()
    except:
        marketDataSaverError = True
    finally:
        if marketDataSaverError==True:
            print("\n\t\t[ Error ] :" + Functions.center("Unable to save data", 60) + "\n")
            Functions.programExit()

def marketDataExtractor():
    marketDataExtractionError = False
    Functions.clearMarketDataStorage()
    try:
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get("https://merolagani.com/BrokerList.aspx")
        for index in range(0, numberOfCompanies):
            script = Symbol[index]
            search_icon = driver.find_element_by_xpath("//li[@class='dropdown search-form']//a[@class='dropdown-toggle']//i[@class='icon-search']")
            search_icon.click()
            search = driver.find_element_by_id("ctl00_AutoSuggest1_txtAutoSuggest")
            search.send_keys(script)
            search.send_keys(Keys.RETURN)

            items = driver.find_elements_by_xpath("//tbody[@class='panel panel-default']//tr//td[@class='']")
            for item in items:
                try:
                    Temporary.append(removeUnwantedCharacter(item.text))
                except:
                    Temporary.append("NULL")
            try:
                OutStandingShare.append(float(Temporary[0]))
            except:
                OutStandingShare.append("NULL")
            try:
                MarketPrice.append(float(Temporary[1]))
            except:
                MarketPrice.append("NULL")
            try:
                PercentageChange.append(float(Temporary[2]))
            except:
                PercentageChange.append("NULL")
            try:
                Avg120Day.append(float(Temporary[6]))
            except:
                Avg120Day.append("NULL")
            try:
                OneYearYield.append(float(Temporary[7]))
            except:
                OneYearYield.append("NULL")
            try:
                Eps.append(float(removeFurther(Temporary[8])))
            except:
                Eps.append("NULL")
            try:
                PERatio.append(float(Temporary[9]))
            except:
                PERatio.append("NULL")
            try:
                BookValue.append(float(Temporary[10]))
            except:
                BookValue.append("NULL")
            try:
                Pbv.append(float(Temporary[11]))
            except:
                Pbv.append("NULL")
            try:
                Dividend.append(float(removeFurther(Temporary[12])))
            except:
                Dividend.append("NULL")
            try:
                Bonus.append(float(removeFurther(Temporary[13])))
            except:
                Bonus.append("NULL")
            try:
                RightShare.append(float(removeFurther(Temporary[14])))
            except:
                RightShare.append("NULL")
            try:
                AvgVol130Day.append(float(Temporary[15]))
            except:
                AvgVol130Day.append("NULL")
            try:
                MarketCapitalisation.append(Temporary[16])
            except:
                MarketCapitalisation.append("NULL")
            Functions.progressIndicator(index+1, MegaStorage.numberOfCompanies)
            Temporary.clear()
    except:
        marketDataExtractionError = True
    finally:
        driver.close()
        if len(OutStandingShare)>=numberOfCompanies and marketDataExtractionError==False:
            marketDataSaver()

def newsExtractor():
    newsExtractorError = False
    numberOfNewsData = 63
    count = 0
    try:
        Functions.clearNewsDataStorage()
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get("http://www.nepalstock.com/news/")
        items = driver.find_elements_by_xpath("//table[@class='table table-condensed table-hover']//tbody//tr//td[@class='alnleft']")
        for item in items:
            if count>0:
                News.append(item.text)
            else:
                count = 1
        items = driver.find_elements_by_xpath("//table[@class='table table-condensed table-hover']//tbody//tr//td[@class='alnright']")
        if count>0:
            print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
        count = 0
        for item in items:
            if count>=3:
                if count%3==0:
                    NewsSymbol.append(item.text)
                elif count%3==1:
                    NewsDate.append(item.text)
            count += 1
            Functions.progressIndicator(count, numberOfNewsData)
    except:
        newsExtractorError = True
    finally:
        driver.close()
        if newsExtractorError==False and len(MegaStorage.NewsDate)>=20:
            print("\n\n\t-------------------------------------------------------------------------------------------------------------------\n")
            Functions.newsDisplay()
        else:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t[ Error ] :" + Functions.center("Unable to extract news", 60))

def reportDataLoader():
    Functions.clearReportDataStorage()
    reportDataLoaderError = False
    isEmpty = False
    try:
        filePath = fileName1 + "divData" + fileExtension
        file = open(filePath, 'r')
        if os.path.getsize(filePath)>0:
            for line in file:
                for word in line.split():
                    Temporary.append(word)
                divBCD.append(Temporary[0])
                divSymbol.append(Temporary[1])
                divPer.append(Temporary[2])
                Temporary.clear()
        else:
            isEmpty = True

        for index in range(0, numberOfCompanies):
            filePath = fileName2 + Symbol[index] + fileExtension
            file = open(filePath, 'r')
            if os.path.getsize(filePath)>0:
                for last_line in file: pass
                for word in last_line.split():
                    if word=="NULL":
                        Temporary.append(0.0)
                    else:
                        Temporary.append(word)
                try:
                    shareDataAsOf.append(Temporary[0])
                except:
                    shareDataAsOf.append(float(0))
                try:
                    shareVolume.append(float(Temporary[1]))
                except:
                    shareVolume.append(float(0))
                try:
                    sharePrice.append(float(Temporary[2]))
                except:
                    sharePrice.append(float(0))
                try:
                    shareOpenPrice.append(float(Temporary[3]))
                except:
                    shareOpenPrice.append(float(0))
                try:
                    shareHighPrice.append(float(Temporary[4]))
                except:
                    shareHighPrice.append(float(0))
                try:
                    shareLowPrice.append(float(Temporary[5]))
                except:
                    shareLowPrice.append(float(0))
                try:
                    share52WeeksHigh.append(float(Temporary[6]))
                except:
                    share52WeeksHigh.append(float(0))
                try:
                    share52WeeksLow.append(float(Temporary[7]))
                except:
                    share52WeeksLow.append(float(0))
                
                Temporary.clear()
            else:
                isEmpty = True
        file.close()
        if isEmpty==False:
            for index in range(0, numberOfCompanies):
                filePath = fileName3 + Symbol[index] + fileExtension
                file = open(filePath, 'r')
                if os.path.getsize(filePath)>0:
                    for last_line in file: pass
                    for word in last_line.split():
                        Temporary.append(word)
                    try:
                        shareReportDate.append(Temporary[0])
                    except:
                        shareReportDate.append("0")
                    try:
                        shareReportValue.append(float(Temporary[1]))
                    except:
                        shareReportValue.append("0")
                    try:
                        shareReportQuarter.append(float(Temporary[2]))
                    except:
                        shareReportQuarter.append("0")
                    Temporary.clear()
                else:
                    isEmpty = True
                    break
                file.close()
    except:
        reportDataLoaderError = True
    finally:
        if reportDataLoaderError==True or isEmpty==True:
            print("\t\t[ Error ] :" + Functions.center("Report data could not be loaded", 60))
            Functions.programExit()

def reportDataSaver():
    reportDataSaverError = False
    try:
        filePath = fileName1 + "divData" + fileExtension
        if float(divPer[0])>0:
            open(filePath, 'w').close()
            file = open(filePath, 'a')
            for index in range(0, len(divSymbol)):
                string = f"{MegaStorage.divBCD[index]} {MegaStorage.divSymbol[index]} {MegaStorage.divPer[index]}\n"
                file.write(string)
            file.close()
    except:
        reportDataSaverError = True

    for index in range(0, numberOfCompanies):
        try:
            dataFilePath = fileName2 + Symbol[index] + fileExtension
            dataString1 = f"{shareDataAsOf[index]} {shareVolume[index]} {sharePrice[index]} {shareOpenPrice[index]} {shareHighPrice[index]} {shareLowPrice[index]}"
            dataString2 =f"{share52WeeksHigh[index]} {share52WeeksLow[index]}\n"
            dataString = dataString1 + " " + dataString2
            
            # append data in file
            dataFile = open(dataFilePath, 'a')
            dataFile.write(dataString)
            dataFile.close()

        except:
            reportDataSaverError = True
            break
        try:
            reportFilePath = fileName3 + Symbol[index] + fileExtension
            reportString = f"{shareReportDate[index]} {shareReportValue[index]} {shareReportQuarter[index]}\n"

            # check for overwrite for financial report
            if os.path.getsize(reportFilePath)>0:
                reportFile = open(reportFilePath, 'r')
                for last_line in reportFile: pass
                reportFile.close()
                if shareReportDate[index] in last_line:
                    pass
                else:
                    reportFile = open(reportFilePath, 'a')
                    reportFile.write(reportString)
            else:
                reportFile = open(reportFilePath, 'a')
                reportFile.write(reportString)
            reportFile.close()
        except:
            reportDataSaverError = True
            break
        finally:
            if reportDataSaverError==True:
                print("\n\t\t[ Error ] :" + Functions.center("Unable to save report data", 60) + "\n")
                Functions.programExit()

def reportDataExtractor():
    isFinancialReport = False
    reportExtractionError = False
    Functions.clearReportDataStorage()
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get("https://www.sharesansar.com/proposed-dividend")   
    try:
        try:
            select = Select(driver.find_element_by_xpath("//select[@name='myTable_length']"))
            select.select_by_visible_text('50')
            sleep(3)
            dividendList = driver.find_elements_by_xpath("//table[@id='myTable']//tbody//tr//td")
            for index in range(0, len(dividendList)):
                if ((index-7)%9)==0:
                    if not dividendList[index].text.find("[")>=0:
                        if len(dividendList[index].text)>0:
                            divBCD.append(dividendList[index].text)
                        else:
                            divBCD.append("-")
                        divPer.append(dividendList[index-2].text)
                        divSymbol.append(dividendList[index-6].text)
            dividendList.clear()
        except:
            Functions.clearDivDataStorage()
            divPer.append("0")
            divBCD.append("NULL")
            divSymbol.append("NULL")
            
        for index in range(0, numberOfCompanies):
            script = Symbol[index]
            #Locating search bar
            search_bar = driver.find_element_by_id("companypagesearch")
            search_bar.send_keys(script)
            search_bar.send_keys(Keys.RETURN)

            #Extracting date, price, volume, low, high, open, 52 weeks high-low
            try:
                dataAsOf = driver.find_element_by_xpath("//div[@class='first-row margin-bottom-15']//span[@class='comp-ason']//span[@class='text-org']").text
                dataAsOf = removeUnwantedCharacter(dataAsOf)
            except:
                dataAsOf = "0"
            try:
                volume = driver.find_element_by_xpath("//span[@class='padding-fourth pd-sm-fx']").text
                volume = removeUnwantedCharacter(volume)[6:]
            except:
                volume = "0"
            try:
                try:
                    try:
                        marketPrice = driver.find_element_by_xpath("//span[@class='text-comp-green comp-price padding-second']").text
                        marketPrice = removeUnwantedCharacter(marketPrice)
                    except:
                        marketPrice = driver.find_element_by_xpath("//span[@class='text-comp-red comp-price padding-second']").text
                        marketPrice = removeUnwantedCharacter(marketPrice)
                except:
                    marketPrice = driver.find_element_by_xpath("//span[@class='text-comp-blue comp-price padding-second']").text
                    marketPrice = removeUnwantedCharacter(marketPrice)
            except:
                marketPrice = "0"
            try:
                openPrice = driver.find_element_by_xpath("(//div[@class='second-row margin-bottom-15']//span)[1]").text
                openPrice = removeUnwantedCharacter(openPrice)[4:]
            except:
                openPrice = "0"
            try:
                highPrice = driver.find_element_by_xpath("(//div[@class='second-row margin-bottom-15']//span[@class='padding-second'])").text
                highPrice = removeUnwantedCharacter(highPrice)[4:]
            except:
                highPrice = "0"
            try:
                lowPrice = driver.find_element_by_xpath("(//div[@class='second-row margin-bottom-15']//span)[5]").text
                lowPrice = removeUnwantedCharacter(lowPrice)[3:]
            except:
                lowPrice = "0"
            try:
                Temporary.clear()
                highLow52Weeks = driver.find_element_by_xpath("(//div[@class='b-shadow padding-bottom-20 margin-bottom-20']//div[@class='col-md-12']//div[@class='second-row margin-bottom-15'])[2]//span").text
                for word in highLow52Weeks.split():
                    Temporary.append(word)
                high52Weeks = removeUnwantedCharacter(Temporary[4])
                low52Weeks = removeUnwantedCharacter(Temporary[6])
            except:
                high52Weeks = "0"
                low52Weeks = "0"

            #Financial Report for net profit/loss
            try:
                financialReport = driver.find_element_by_id("btn_ccfinanrep")
                financialReport.click()
                WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//table[@id='myTableCFinanRep']//tbody//tr//td")))
                reports = driver.find_elements_by_xpath("//table[@id='myTableCFinanRep']//tbody//tr//td")
                count = 0
                for item in reports:
                    if count%2==0:
                        reportDate = item.text
                    else:
                        reportData = item.text
                    count += 1
                    if count>=2:
                        break
                if count<2:
                    reportDate = "NULL"
                    reportValue = "0"
                    reportQuarter = "0"
                else:
                    Temporary.clear()
                    for word in reportData.split():
                        Temporary.append(word)
                    lenData = len(Temporary)
                    for count in range(0, lenData):
                        if Temporary[count].find("million")>=0:
                            isFinancialReport = True
                            if reportData.find("profit")>=0:
                                reportValue = str(float(Temporary[count-1]) * 1000000)
                            else:
                                reportValue = str(float(Temporary[count-1]) * (-1000000))
                            break
                        elif Temporary[count].find("billion")>=0:
                            isFinancialReport = True
                            if reportData.find("profit")>=0:
                                reportValue = str(float(Temporary[count-1]) * 1000000000)
                            else:
                                reportValue = str(float(Temporary[count-1]) * (-1000000000))
                            break
                    if isFinancialReport==True:
                        isFinancialReport = False
                        for count in range(0, lenData):
                            if Temporary[count].find("1st")>=0:
                                isFinancialReport = True
                                reportQuarter = "1"
                                break
                            elif Temporary[count].find("2nd")>=0:
                                isFinancialReport = True
                                reportQuarter = "2"
                                break
                            elif Temporary[count].find("3rd")>=0:
                                isFinancialReport = True
                                reportQuarter = "3"
                                break
                            elif Temporary[count].find("4th")>=0:
                                isFinancialReport = True
                                reportQuarter = "4"
                                break
                        if isFinancialReport==False:
                            reportQuarter = "0"
                    else:
                        reportValue = "0"
            except:
                reportDate = "0"
                reportValue = "0"
                reportQuarter = "0"
            
            shareDataAsOf.append(dataAsOf)
            sharePrice.append(float(marketPrice))
            shareVolume.append(float(volume))
            shareOpenPrice.append(float(openPrice))
            shareHighPrice.append(float(highPrice))
            shareLowPrice.append(float(lowPrice))
            share52WeeksHigh.append(float(high52Weeks))
            share52WeeksLow.append(float(low52Weeks))
            
            shareReportDate.append(reportDate)
            shareReportQuarter.append(float(reportQuarter))
            shareReportValue.append(float(reportValue))

            Functions.progressIndicator(index+1, MegaStorage.numberOfCompanies)
    except:
        reportExtractionError = True
    finally:
        driver.close()
        if len(shareReportDate)>=numberOfCompanies and reportExtractionError==False:
            reportDataSaver()

def fundamentalDataUpdate():
    filePath = fileName0 + "data" + fileExtension
    file = open(filePath, 'w')
    file.write(MegaStorage.dataAsOf)
    file.close()

def dataLoader(message1, message2):
    marketDataLoader()
    if len(OutStandingShare)>=numberOfCompanies:
        reportDataLoader()
    if len(shareVolume)>=numberOfCompanies and len(shareReportDate)>=numberOfCompanies:
        print(message1)
        return True
    else:
        print(message2)
        Functions.programExit()

def allFilesArePresent():
    emptyFlag = False
    arr = []
    filePath1 =  MegaStorage.fileName0 + "data" + fileExtension
    filePath2 = fileName1 + "marketData" + fileExtension
    try:
        if os.path.exists(filePath1):
            if os.path.exists(filePath2):
                for index in range(0, MegaStorage.numberOfCompanies):
                    filePath3 = fileName2 + Symbol[index] + fileExtension
                    filePath4 = fileName3 + Symbol[index] + fileExtension
                    if os.path.exists(filePath3): pass
                    else:
                        emptyFlag = True
                        open(filePath3, 'w').close()
                        arr.append("Report Data (" + Symbol[index] + ")")
                    if os.path.exists(filePath4): pass
                    else:
                        emptyFlag = True
                        open(filePath4, 'w').close()
                        arr.append("Financial Data (" + Symbol[index] + ")")
            else:
                emptyFlag = True
                open(filePath2, 'w').close()
                arr.append("Market Data")
        else:
            emptyFlag = True
            open(filePath1, 'w').close()
            arr.append("Fundamental Data")
        if emptyFlag==True:
            print("\t\tNew files have been created:\n")
            for index in range(0, len(arr)):
                print(f"\t\t* {arr[index]}")
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
    except:
        print("\t\t[ Error ] :" + Functions.center("File Management Error", 60) + "\n")
        Functions.programExit()

def resetFiles():
    resetFilesError = False
    try:
        dataPath = fileName0 + "data" + fileExtension
        filePath = fileName1 + "marketData" + fileExtension
        if not os.path.isdir(fileName0):
            os.makedirs(fileName0)
        open(dataPath, 'w').close()
        if not os.path.isdir(fileName1):
            os.makedirs(fileName1)
        open(filePath, 'w').close()
        if not os.path.isdir(fileName2):
            os.makedirs(fileName2)
        if not os.path.isdir(fileName3):
            os.makedirs(fileName3)
        for index in range(0, numberOfCompanies):
            path1 = fileName2 + Symbol[index] + fileExtension
            path2 = fileName3 + Symbol[index] + fileExtension
            open(path1, 'w').close()
            open(path2, 'w').close()
    except:
        resetFilesError = True
    finally:
        if resetFilesError==True:
            print("\t\t[ Error ] :" + Functions.center("File repair failure", 60) + "\n")
        else:
            print("\t\t[ Status ] :" + Functions.center("Files have been reset", 60) + "\n")

def dataIsUpdated():
    isUpdated = False
    dataExtractionError = False
    dataStatusError = False
    MegaStorage.connectionError = False
    try:
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get("https://www.sharesansar.com/company/ACLBSL")
        MegaStorage.dataAsOf = driver.find_element_by_xpath("//div[@class='first-row margin-bottom-15']//span[@class='comp-ason']//span[@class='text-org']").text
        MegaStorage.dataAsOf = removeUnwantedCharacter(MegaStorage.dataAsOf)
        driver.close()
    except:
        dataExtractionError = True
        MegaStorage.connectionError = True
    if dataExtractionError==False:
        try:
            filePath = fileName0 + "data" + fileExtension
            if os.path.getsize(filePath)>0:
                file = open(filePath, 'r')
                for last_line in file: pass
                if MegaStorage.dataAsOf in last_line:
                    isUpdated = True
                file.close()
        except:
            dataStatusError = True
        finally:
            if dataStatusError==True:
                print("\t\t[ Error ] :" + Functions.center("Unable to read data from file", 60) + "\n")
                Functions.programExit()
    return isUpdated
