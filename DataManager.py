from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MegaStorage import *
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
            print("\t\t[ Error ] :\tMarket data could not be loaded")
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
            print("\n\t\t[ Error ] :\tUnable to save data\n")
            Functions.programExit()

def marketDataExtractor():
    marketDataExtractionError = False
    try:
        Functions.clearMarketDataStorage()
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
            Functions.progressIndicator1(index+1, numberOfCompanies)
            Temporary.clear()
    except:
        marketDataExtractionError = True
    finally:
        driver.close()
        if len(OutStandingShare)>=numberOfCompanies and marketDataExtractionError==False:
            marketDataSaver()
        # else:
        #     print("\t\t[ Error ] :\tMarket data extraction was incomplete")

def newsExtractor():
    newsExtractorError = False
    numberOfNewsData = 63
    count = 0
    try:
        Functions.clearNewsDataStorage()
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get("http://www.nepalstock.com/news/")
        items = driver.find_elements_by_xpath("//table[@class='table table-condensed table-hover']//tbody//tr//td[@class='alnleft']")
        print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
        for item in items:
            if count>0:
                News.append(item.text)
            else:
                count = 1
        items = driver.find_elements_by_xpath("//table[@class='table table-condensed table-hover']//tbody//tr//td[@class='alnright']")
        count = 0
        for item in items:
            if count>=3:
                if count%3==0:
                    NewsSymbol.append(item.text)
                elif count%3==1:
                    NewsDate.append(item.text)
            count += 1
            Functions.progressIndicator1(count, numberOfNewsData)
        print("\n\n\t-------------------------------------------------------------------------------------------------------------------\n")
    except:
        newsExtractorError = True
    finally:
        driver.close()
        if newsExtractorError==True:
            print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
            print("\t\t[ Error ] : \tUnable to extract news")
        else:
            Functions.newsDisplay()
        
def reportDataLoader():
    Functions.clearReportDataStorage()
    reportDataLoaderError = False
    isEmpty = False
    try:
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
                try:
                    shareMovingAnalysis1.append(Temporary[8])
                except:
                    shareMovingAnalysis1.append("0")
                try:
                    shareMovingAnalysis2.append(Temporary[9])
                except:
                    shareMovingAnalysis2.append("0")
                try:
                    shareMovingAnalysis3.append(Temporary[10])
                except:
                    shareMovingAnalysis3.append("0")
                try:
                    sharePivotPoint.append(float(Temporary[11]))
                except:
                    sharePivotPoint.append(float(0))
                try:
                    shareSupportLevel1.append(float(Temporary[12]))
                except:
                    shareSupportLevel1.append(float(0))
                try:
                    shareSupportLevel2.append(float(Temporary[13]))
                except:
                    shareSupportLevel2.append(float(0))
                try:
                    shareSupportLevel3.append(float(Temporary[14]))
                except:
                    shareSupportLevel3.append(float(0))
                try:
                    shareResistanceLevel1.append(float(Temporary[15]))
                except:
                    shareResistanceLevel1.append(float(0))
                try:
                    shareResistanceLevel2.append(float(Temporary[16]))
                except:
                    shareResistanceLevel2.append(float(0))
                try:
                    shareResistanceLevel3.append(float(Temporary[17]))
                except:
                    shareResistanceLevel3.append(float(0))
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
            print("\t\t[ Error ] :\tReport data could not be loaded")
            Functions.programExit()

def reportDataSaver():
    reportDataSaverError = False
    for index in range(0, numberOfCompanies):
        try:
            dataFilePath = fileName2 + Symbol[index] + fileExtension
            dataString1 = f"{shareDataAsOf[index]} {shareVolume[index]} {sharePrice[index]} {shareOpenPrice[index]} {shareHighPrice[index]} {shareLowPrice[index]}"
            dataString2 =f"{share52WeeksHigh[index]} {share52WeeksLow[index]}"
            dataString3 = f"{shareMovingAnalysis1[index]} {shareMovingAnalysis2[index]} {shareMovingAnalysis3[index]} {sharePivotPoint[index]}"
            dataString4 = f"{shareSupportLevel1[index]} {shareSupportLevel2[index]} {shareSupportLevel3[index]}"
            dataString5 = f"{shareResistanceLevel1[index]} {shareResistanceLevel2[index]} {shareResistanceLevel3[index]}\n"
            dataString = dataString1 + " " + dataString2 + " " + dataString3 + " " + dataString4 + " " + dataString5
            
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
                print("\n\t\t[ Error ] :\tUnable to save data\n")
                Functions.programExit()

def reportDataExtractor():
    isFinancialReport = False
    reportExtractionError = False
    Functions.clearReportDataStorage()
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get("https://www.sharesansar.com/company/nepse")   
    try:
        for index in range(0, numberOfCompanies):
            script = Symbol[index]
            #Locating search bar
            search_bar = driver.find_element_by_id("companypagesearch")
            search_bar.send_keys(script)
            search_bar.send_keys(Keys.RETURN)

            #Extracting date, price, volume, low, high, open
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

            #Bullish/Bearish
            try:
                movingAnalysis1 = driver.find_element_by_xpath("((//table[@class='table table-bordered table-striped table-hover text-center company-table'])[5]//tbody//tr//td)[4]").text
                movingAnalysis1 = removeUnwantedCharacter(movingAnalysis1)
            except:
                movingAnalysis1 = "0"
            try:
                movingAnalysis2 = driver.find_element_by_xpath("((//table[@class='table table-bordered table-striped table-hover text-center company-table'])[5]//tbody//tr//td)[8]").text
                movingAnalysis2 = removeUnwantedCharacter(movingAnalysis2)
            except:
                movingAnalysis2 = "0"
            try:
                movingAnalysis3 = driver.find_element_by_xpath("((//table[@class='table table-bordered table-striped table-hover text-center company-table'])[5]//tbody//tr//td)[12]").text
                movingAnalysis3 = removeUnwantedCharacter(movingAnalysis3)
            except:
                movingAnalysis3 = "0"

            #Support/Resistance Level
            try:
                supportLevel3 = driver.find_element_by_xpath("((//table[@class='table table-bordered table-striped table-hover text-center company-table'])[4]//tr//td)[2]").text
                supportLevel3 = removeUnwantedCharacter(supportLevel3)
            except:
                supportLevel3 = "0"
            try:
                supportLevel2 = driver.find_element_by_xpath("((//table[@class='table table-bordered table-striped table-hover text-center company-table'])[4]//tr//td)[4]").text
                supportLevel2 = removeUnwantedCharacter(supportLevel2)
            except:
                supportLevel2 = "0"
            try:
                supportLevel1 = driver.find_element_by_xpath("((//table[@class='table table-bordered table-striped table-hover text-center company-table'])[4]//tr//td)[6]").text
                supportLevel1 = removeUnwantedCharacter(supportLevel1)
            except:
                supportLevel1 = "0"

            try:
                pivotPoint = driver.find_element_by_xpath("((//table[@class='table table-bordered table-striped table-hover text-center company-table'])[4]//tr//td)[8]").text
                pivotPoint = removeUnwantedCharacter(pivotPoint)
            except:
                pivotPoint = "0"
            try:
                resistantLevel1 = driver.find_element_by_xpath("((//table[@class='table table-bordered table-striped table-hover text-center company-table'])[4]//tr//td)[10]").text
                resistantLevel1 = removeUnwantedCharacter(resistantLevel1)
            except:
                resistantLevel1 = "0"
            try:
                resistantLevel2 = driver.find_element_by_xpath("((//table[@class='table table-bordered table-striped table-hover text-center company-table'])[4]//tr//td)[12]").text
                resistantLevel2 = removeUnwantedCharacter(resistantLevel2)
            except:
                resistantLevel2 = "0"
            try:
                resistantLevel3 = driver.find_element_by_xpath("((//table[@class='table table-bordered table-striped table-hover text-center company-table'])[4]//tr//td)[14]").text
                resistantLevel3 = removeUnwantedCharacter(resistantLevel3)
            except:
                resistantLevel3 = "0"

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
                    for index in range(0, lenData):
                        if Temporary[index].find("million")>=0:
                            isFinancialReport = True
                            if reportData.find("profit")>=0:
                                reportValue = str(float(Temporary[index-1]) * 1000000)
                            else:
                                reportValue = str(float(Temporary[index-1]) * (-1000000))
                            break
                        elif Temporary[index].find("billion")>=0:
                            isFinancialReport = True
                            if reportData.find("profit")>=0:
                                reportValue = str(float(Temporary[index-1]) * 1000000000)
                            else:
                                reportValue = str(float(Temporary[index-1]) * (-1000000000))
                            break
                    if isFinancialReport==True:
                        isFinancialReport = False
                        for index in range(0, lenData):
                            if Temporary[index].find("1st")>=0:
                                isFinancialReport = True
                                reportQuarter = "1"
                                break
                            elif Temporary[index].find("2nd")>=0:
                                isFinancialReport = True
                                reportQuarter = "2"
                                break
                            elif Temporary[index].find("3rd")>=0:
                                isFinancialReport = True
                                reportQuarter = "3"
                                break
                            elif Temporary[index].find("4th")>=0:
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

            shareMovingAnalysis1.append(movingAnalysis1)
            shareMovingAnalysis2.append(movingAnalysis2)
            shareMovingAnalysis3.append(movingAnalysis3)
            sharePivotPoint.append(float(pivotPoint))
            shareSupportLevel1.append(float(supportLevel1))
            shareSupportLevel2.append(float(supportLevel2))
            shareSupportLevel3.append(float(supportLevel3))
            shareResistanceLevel1.append(float(resistantLevel1))
            shareResistanceLevel2.append(float(resistantLevel2))
            shareResistanceLevel3.append(float(resistantLevel3))
            
            shareReportDate.append(reportDate)
            shareReportQuarter.append(float(reportQuarter))
            shareReportValue.append(float(reportValue))

            Functions.progressIndicator2(index+1, numberOfCompanies)
    except:
        reportExtractionError = True
    finally:
        driver.close()
        if len(shareResistanceLevel3)>=numberOfCompanies and len(shareReportDate)>=numberOfCompanies and reportExtractionError==False:
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
    if len(shareSupportLevel3)>=numberOfCompanies and len(shareReportDate)>=numberOfCompanies:
        print(message1)
        return True
    else:
        print(message2)
        Functions.programExit()

def allFilesArePresent():
    filesArePresentFlag = True
    filePath = fileName1 + "marketData" + fileExtension
    dataPath =  MegaStorage.fileName0 + "data" + fileExtension
    try:
        if os.path.exists(dataPath):
            if os.path.exists(filePath):
                for index in range(0, MegaStorage.numberOfCompanies):
                    filePath1 = fileName2 + Symbol[index] + fileExtension
                    filePath2 = fileName3 + Symbol[index] + fileExtension
                    if os.path.exists(filePath1) and os.path.exists(filePath2):
                        pass
                    else:
                        filesArePresentFlag = False
                        break
            else:
                filesArePresentFlag = False
        else:
            filesArePresentFlag = False
    except:
        filesArePresentFlag = False
    return filesArePresentFlag

def filesAreEmpty():
    filesAreEmpty = False
    filePath = fileName1 + "marketData" + fileExtension
    dataPath =  MegaStorage.fileName0 + "data" + fileExtension
    try:
        if os.path.getsize(dataPath)>0:
            if os.path.getsize(filePath)>0:
                for index in range(0, MegaStorage.numberOfCompanies):
                    filePath1 = MegaStorage.fileName2 + MegaStorage.Symbol[index] + MegaStorage.fileExtension
                    filePath2 = MegaStorage.fileName3 + MegaStorage.Symbol[index] + MegaStorage.fileExtension
                    if os.path.getsize(filePath1)>0 and os.path.getsize(filePath2)>0:
                        pass
                    else:
                        filesAreEmpty = False
                        break
            else:
                filesAreEmpty = False
        else:
            filesAreEmpty = True
    except:
        filesAreEmpty = False
    return filesAreEmpty

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
            print("\t\t[ Error ] :\tFile repair failure\n")
        else:
            print("\t\t[ Status ] :\tFiles have been reset\n")

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
            file = open(filePath, 'r')
            if os.path.getsize(filePath)>0:
                for last_line in file: pass
                if MegaStorage.dataAsOf in last_line:
                    isUpdated = True
                file.close()
            else:
                dataStatusError = True
        except:
            dataStatusError = True
        finally:
            if dataStatusError==True:
                print("\t\t[ Error ] :\tUnable to read data from file\n")
                Functions.programExit()
    return isUpdated
