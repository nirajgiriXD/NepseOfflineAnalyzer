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
    try:
        string = string.replace('', '')
    except: pass
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

def initialDataLoader():
    Functions.clearInitialDataStorage()
    initialDataLoaderError = False
    isEmpty = False
    sizeSymbol = 0
    sizeName = 0
    sizeSector = 0
    filePath1 = fileName0 + "companySymbol" + fileExtension
    filePath2 = fileName0 + "companyName" + fileExtension
    filePath3 = fileName0 + "companySector" + fileExtension
    try:
        if os.path.getsize(filePath1)>0 and os.path.getsize(filePath2)>0 and os.path.getsize(filePath3)>0:
            file = open(filePath1, 'r')
            for line1 in file:
                Symbol.append(line1.strip())
            sizeSymbol = len(Symbol)
            file.close()
            file = open(filePath2, 'r')
            for line2 in file:
                Name.append(line2.strip())
            sizeName = len(Name)
            file.close()
            file = open(filePath3, 'r')
            for line3 in file:
                Sector.append(line3.strip())
            sizeSector = len(Sector)
            file.close()
            if sizeSymbol==sizeName and sizeSymbol==sizeSector:
                MegaStorage.numberOfCompanies = sizeSymbol
            else:
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Symbol, Name and Sector Data Mismatched{MegaStorage.normal}", 60))
                Functions.programExit()
        else:
            isEmpty = True
    except:
        initialDataLoaderError = True
    finally:
        if initialDataLoaderError==True or isEmpty==True:
            print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Initial data could not be loaded{MegaStorage.normal}", 60) + "\n")
            Functions.programExit()

def marketDataLoader():
    numberOfCompanies = MegaStorage.numberOfCompanies
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
                    AvgVol30Day.append(Temporary[9])
                except:
                    AvgVol30Day.append(float(0))
                try:
                    MarketCapitalisation.append(Temporary[10])
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
            print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Market Data could not be Loaded{MegaStorage.normal}", 60))
            Functions.programExit()

def marketDataSaver():
    numberOfCompanies = MegaStorage.numberOfCompanies
    marketDataSaverError = False
    filePath = fileName1 + "marketData" + fileExtension
    try:
        open(filePath, 'w').close()
        file = open(filePath, 'a')
        for index in range(0, numberOfCompanies):
            string1 = f"{OutStandingShare[index]} {MarketPrice[index]} {PercentageChange[index]} {Avg120Day[index]} {OneYearYield[index]} {Eps[index]} "
            string2 = f"{PERatio[index]} {BookValue[index]} {Pbv[index]} {AvgVol30Day[index]} {MarketCapitalisation[index]}\n"
            string = string1 + string2
            file.write(string)
        file.close()
    except:
        marketDataSaverError = True
    finally:
        if marketDataSaverError==True:
            print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Unable to save Market Data{MegaStorage.normal}", 60))
            Functions.programExit()

def marketDataExtractor():
    numberOfCompanies = MegaStorage.numberOfCompanies
    marketDataExtractionError = False
    Functions.clearMarketDataStorage()
    try:
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        for index in range(0, numberOfCompanies):
            scriptLink = "https://merolagani.com/CompanyDetail.aspx?symbol=" + Symbol[index]
            driver.get(scriptLink)

            items = driver.find_elements_by_xpath("//tbody[@class='panel panel-default']//tr//td[@class='']")
            for item in items:
                try:
                    Temporary.append(removeUnwantedCharacter(item.text))
                except:
                    Temporary.append("0")
            try:
                OutStandingShare.append(float(Temporary[0]))
            except:
                OutStandingShare.append("0")
            try:
                MarketPrice.append(float(Temporary[1]))
            except:
                MarketPrice.append("0")
            try:
                PercentageChange.append(float(Temporary[2]))
            except:
                PercentageChange.append("0")
            try:
                Avg120Day.append(float(Temporary[6]))
            except:
                Avg120Day.append("0")
            try:
                OneYearYield.append(float(Temporary[7]))
            except:
                OneYearYield.append("0")
            try:
                Eps.append(float(removeFurther(Temporary[8])))
            except:
                Eps.append("0")
            try:
                PERatio.append(float(Temporary[9]))
            except:
                PERatio.append("0")
            try:
                BookValue.append(float(Temporary[10]))
            except:
                BookValue.append("0")
            try:
                Pbv.append(float(Temporary[11]))
            except:
                Pbv.append("0")
            
            # Dividend, Bonus and Right Share [12, 13, 14]
            try:
                AvgVol30Day.append(float(Temporary[15]))
            except:
                AvgVol30Day.append("0")
            try:
                MarketCapitalisation.append(Temporary[16])
            except:
                MarketCapitalisation.append("0")
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
        driver.close()
    except:
        newsExtractorError = True
    finally:
        if newsExtractorError==False and len(MegaStorage.NewsDate)>=20:
            print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
            Functions.newsDisplay()
        else:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Unable to Extract News{MegaStorage.normal}", 60))

def dividendDataSaver(index):
    try:
        filePath = fileName4 + Symbol[index] + fileExtension
        open(filePath, 'w').close()
        file = open(filePath, 'a')
        for count in range(0, len(arr3)):
            # Date, Bonus and Cash
            string = f"{arr1[count]} {arr3[count]} {arr2[count]}\n"
            file.write(string)
        file.close()
    except:
        print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Unable to save Dividend History Data{MegaStorage.normal}", 60))
        Functions.programExit()

def reportDataLoader():
    numberOfCompanies = MegaStorage.numberOfCompanies
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
                try:
                    divBonus.append(float(Temporary[2]))
                except:
                    divBonus.append(float(0.0))
                try:
                    divCash.append(float(Temporary[3]))
                except:
                    divCash.append(float(0.0))
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
            print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Unable to Load Report Data{MegaStorage.normal}", 60))
            Functions.programExit()

def reportDataSaver():
    numberOfCompanies = MegaStorage.numberOfCompanies
    reportDataSaverError = False
    try:
        filePath = fileName1 + "divData" + fileExtension
        open(filePath, 'w').close()
        file = open(filePath, 'a')
        for index in range(0, len(MegaStorage.divBCD)):
            cash = str("{:.2f}".format(MegaStorage.divCash[index]))
            bonus = str("{:.2f}".format(MegaStorage.divBonus[index]))
            string = f"{MegaStorage.divBCD[index]} {MegaStorage.divSymbol[index]} {bonus} {cash}\n"
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
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Unable to save Report Data{MegaStorage.normal}", 60))
                Functions.programExit()

def reportDataExtractor():
    numberOfCompanies = MegaStorage.numberOfCompanies
    isFinancialReport = False
    reportExtractionError = False
    Functions.clearReportDataStorage()
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get("https://www.sharesansar.com/proposed-dividend")   
    try:
        # Dividend Proposal
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
                        divCash.append(float(dividendList[index-3].text))
                        divBonus.append(float(dividendList[index-4].text))
                        divSymbol.append(dividendList[index-6].text)
            dividendList.clear()
        except:
            Functions.clearDivDataStorage()
            divCash.append(float(0.0))
            divBonus.append(float(0.0))
            divBCD.append("NULL")
            divSymbol.append("NULL")
            
        for index in range(0, numberOfCompanies):
            # Locating search bar
            search_bar = driver.find_element_by_id("companypagesearch")
            search_bar.send_keys(Symbol[index])
            search_bar.send_keys(Keys.RETURN)

            # Extracting date, price, volume, low, high, open, 52 weeks high-low
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

            # Extracting Name and Sector
            try:
                items = driver.find_elements_by_xpath("//table[@id='myTableCInfo']//tbody//tr//td")
                Name.append(removeFurther(items[3].text))
                Sector.append(items[5].text)
            except:
                Name.append("NULL")
                Sector.append("NULL")

            # Extracting Dividend History
            try:
                Functions.clearArray()
                driver.find_element_by_xpath("//a[@id='btn_cdividend']").click()
                sleep(3)
                items = driver.find_elements_by_xpath("//table[@id='myTableDiv']//tbody//tr//td")
                count = 0
                for item in items:
                    item = removeUnwantedCharacter(item.text)
                    sizeItem = len(item)
                    if (count-1)%8==0:
                        # Bonus
                        if sizeItem>0:
                            arr3.append(item)
                        else:
                            arr3.append(float(0.0))
                    elif (count-2)%8==0:
                        # Cash
                        if sizeItem>0:
                            arr2.append(item)
                        else:
                            arr2.append(float(0.0))
                    elif (count-7)%8==0:
                        # Fiscal Year
                        if sizeItem>0:
                            arr1.append(item)
                        else:
                            arr1.append(float(0.0))
                    count += 1
                if count>0:
                    dividendDataSaver(index)
            except: pass

            # Financial Report for net profit/loss
            try:
                financialReport = driver.find_element_by_id("btn_ccfinanrep")
                financialReport.click()
                reports = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//table[@id='myTableCFinanRep']//tbody//tr//td")))
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
    try:
        filePath1 = fileName0 + "data" + fileExtension
        filePath2 = fileName0 + "companySymbol" + fileExtension
        filePath3 = fileName0 + "companyName" + fileExtension
        filePath4 = fileName0 + "companySector" + fileExtension

        sizeSymbol = len(MegaStorage.Symbol)
        sizeName = len(MegaStorage.Name)
        sizeSector = len(MegaStorage.Sector)

        if sizeSymbol==sizeName and sizeSymbol==sizeSector:
            MegaStorage.numberOfCompanies = sizeSymbol
            open(filePath2, 'w').close()
            file = open(filePath2, 'a')
            for index in range(0, sizeSymbol):
                string = MegaStorage.Symbol[index] + "\n"
                file.write(string)
            file.close()

            open(filePath3, 'w').close()
            file = open(filePath3, 'a')
            for index in range(0, sizeName):
                string = MegaStorage.Name[index] + "\n"
                file.write(string)
            file.close()

            open(filePath4, 'w').close()
            file = open(filePath4, 'a')
            for index in range(0, sizeSector):
                string = MegaStorage.Sector[index] + "\n"
                file.write(string)
            file.close()

            file = open(filePath1, 'w')
            file.write(MegaStorage.dataAsOf)
            file.close()
        else:
            print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Symbol, Name and Sector Mismatched{MegaStorage.normal}", 60))
            Functions.programExit()
    except:
        print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Unable to update Fundamental Data{MegaStorage.normal}", 60))
        Functions.programExit()

def dataLoader(message1, message2):
    initialDataLoader()
    MegaStorage.UpdatedSymbol.clear()
    if not MegaStorage.numberOfCompanies==0:
        marketDataLoader()
    if len(OutStandingShare)>=numberOfCompanies:
        reportDataLoader()
    if len(shareVolume)>=numberOfCompanies and len(shareReportDate)>=numberOfCompanies:
        print(message1)
        return True
    else:
        print(message2)
        Functions.programExit()

def resetFiles():
    resetFilesError = False
    try:
        dataPath = fileName0 + "data" + fileExtension
        filePath = fileName1 + "marketData" + fileExtension
        filePath1 = fileName0 + "companySymbol" + fileExtension
        filePath2 = fileName0 + "companyName" + fileExtension
        filePath3 = fileName0 + "companySector" + fileExtension
        filePath4 = fileName1 + "divData" + fileExtension
        if not os.path.isdir(fileName0):
            os.makedirs(fileName0)
        open(dataPath, 'w').close()
        open(filePath1, 'w').close()
        open(filePath2, 'w').close()
        open(filePath3, 'w').close()
        if not os.path.isdir(fileName1):
            os.makedirs(fileName1)
        open(filePath, 'w').close()
        open(filePath4, 'w').close()
        if not os.path.isdir(fileName2):
            os.makedirs(fileName2)
        if not os.path.isdir(fileName3):
            os.makedirs(fileName3)
        if not os.path.isdir(fileName4):
            os.makedirs(fileName4)
        for index in range(0, numberOfCompanies):
            path1 = fileName2 + Symbol[index] + fileExtension
            path2 = fileName3 + Symbol[index] + fileExtension
            path3 = fileName4 + Symbol[index] + fileExtension
            open(path1, 'w').close()
            open(path2, 'w').close()
            open(path3, 'w').close()
    except:
        resetFilesError = True
    finally:
        if resetFilesError==True:
            print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"File Reset Failure{MegaStorage.normal}", 60))
        else:
            print(f"{MegaStorage.yellow}\t\t[ Status ] :" + Functions.center(f"Files have been Reset{MegaStorage.normal}", 60) + "\n")

def allFilesArePresent(updateFromFile):
    arr = []
    emptyFlag = False
    filePath01 = fileName0 + "companySymbol" + fileExtension
    filePath02 = fileName0 + "companyName" + fileExtension
    filePath03 = fileName0 + "companySector" + fileExtension
    filePath1 =  fileName0 + "data" + fileExtension
    filePath2 = fileName1 + "marketData" + fileExtension
    filePath04 = fileName1 + "divData" + fileExtension
    filePath3 = fileName0 + "user" + fileExtension
    try:
        if os.path.exists(filePath01):
            if os.path.getsize(filePath01)>0:
                MegaStorage.Symbol.clear()
                if updateFromFile==True:
                    Functions.clearInitialDataStorage()
                    file = open(filePath01, 'r')
                    for line in file:
                        MegaStorage.Symbol.append(line.strip())
                    file.close()
                else:
                    for index in range(0, len(MegaStorage.UpdatedSymbol)):
                        MegaStorage.Symbol.append(MegaStorage.UpdatedSymbol[index])
                MegaStorage.numberOfCompanies = len(MegaStorage.Symbol)
                MegaStorage.UpdatedSymbol.clear()
            else:
                MegaStorage.numberOfCompanies = 0
            if os.path.exists(filePath02):
                if os.path.exists(filePath03):
                    if os.path.exists(fileName3):
                        if os.path.exists(filePath1):
                            if os.path.exists(filePath2):
                                if os.path.exists(filePath04):
                                    for index in range(0, MegaStorage.numberOfCompanies):
                                        filePath3 = fileName2 + Symbol[index] + fileExtension
                                        filePath4 = fileName3 + Symbol[index] + fileExtension
                                        filePath5 = fileName4 + Symbol[index] + fileExtension
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
                                        if os.path.exists(filePath5): pass
                                        else:
                                            emptyFlag = True
                                            open(filePath5, 'w').close()
                                            arr.append("Dividend History Data (" + Symbol[index] + ")")
                                else:
                                    emptyFlag = True
                                    open(filePath04, 'w').close()
                                    arr.append("Dividend Proposal Data")
                            else:
                                emptyFlag = True
                                open(filePath2, 'w').close()
                                arr.append("Market Data")
                        else:
                            emptyFlag = True
                            open(filePath1, 'w').close()
                            arr.append("Date Data")
                    else:
                        emptyFlag = True
                        open(filePath3, 'w').close()
                        arr.append("User Data")
                else:
                    emptyFlag = True
                    open(filePath1, 'w').close()
                    open(filePath03, 'w').close()
                    arr.append("Company Sector")
            else:
                emptyFlag = True
                open(filePath1, 'w').close()
                open(filePath02, 'w').close()
                arr.append("Company Name")
        else:
            emptyFlag = True
            open(filePath1, 'w').close()
            open(filePath01, 'w').close()
            arr.append("Company Symbol")
            
        if emptyFlag==True:
            print(f"{MegaStorage.yellow}\t\t[ Status ] :" + Functions.center(f"New Files have been Created{MegaStorage.normal}", 60) + "\n")
            print("\t-------------------------------------------------------------------------------------------------------------------\n")
            for index in range(0, len(arr)):
                print(f"\t\t* {arr[index]}")
            print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    except:
        print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"File Management Error{MegaStorage.normal}", 60) + "\n")
        Functions.programExit()

def dataIsUpdated():
    isUpdated = False
    dataStatusError = False
    Functions.clearInitialDataStorage()
    try:
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get("https://www.sharesansar.com/today-share-price")
        MegaStorage.dataAsOf = driver.find_element_by_xpath("//h5//span[@class='text-org']").text
        MegaStorage.dataAsOf = removeUnwantedCharacter(MegaStorage.dataAsOf)
        count = 0
        items = driver.find_elements_by_xpath("//tbody//tr//td")
        for item in items:
            if (count-1)%21==0:
                item = removeUnwantedCharacter(item.text)
                if not item.find("/")>=0:
                    MegaStorage.UpdatedSymbol.append(item)
            count += 1
        driver.close()
    except:
        MegaStorage.connectionError = True
    if MegaStorage.connectionError==False:
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
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Unable to Read Data from File{MegaStorage.normal}", 60))
                Functions.programExit()
    return isUpdated
