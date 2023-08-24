from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MegaStorage import *
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
    try:
        if os.path.getsize(fileName1)>0:
            file = open(fileName1, 'r')
            for index in range(0, numberOfCompanies):
                line = file.readline()
                for word in line.split():
                    if word=="NULL":
                        Temporary.append(0.0)
                    else:
                        Temporary.append(float(word))
                OutStandingShare.append(Temporary[0])
                MarketPrice.append(Temporary[1])
                PercentageChange.append(Temporary[2])
                Avg120Day.append(Temporary[3])
                OneYearYield.append(Temporary[4])
                Eps.append(Temporary[5])
                PERatio.append(Temporary[6])
                BookValue.append(Temporary[7])
                Pbv.append(Temporary[8])
                Dividend.append(Temporary[9])
                Bonus.append(Temporary[10])
                RightShare.append(Temporary[11])
                AvgVol130Day.append(Temporary[12])
                MarketCapitalisation.append(Temporary[13])
                Temporary.clear()
        else:
            isEmpty = True
    except:
        marketDataLoaderError = True
    finally:
        file.close()
        if marketDataLoaderError==True or isEmpty==True:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t[ Error ] : Market data could not be loaded")
            print("\t-------------------------------------------------------------------------------------------------------------------\n")
            Functions.programExit()

def marketDataSaver():
    try:
        open(fileName1, 'w').close()
        file = open(fileName1, 'a')
        for index in range(0, numberOfCompanies):
            string1 = f"{OutStandingShare[index]} {MarketPrice[index]} {PercentageChange[index]} {Avg120Day[index]} {OneYearYield[index]} {Eps[index]} "
            string2 = f"{PERatio[index]} {BookValue[index]} {Pbv[index]} {Dividend[index]} {Bonus[index]} {RightShare[index]} {AvgVol130Day[index]} "
            string3 = f"{MarketCapitalisation[index]}\n"
            string = string1 + string2 + string3
            file.write(string)
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print("\t\t[ Status ] : Market data updated successfully")
    except:
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print("\t\t[ Error ] : Unable to update market data")
    finally:
        file.close()

def marketDataExtractor():
    Functions.clearMarketDataStorage()
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get("https://merolagani.com/BrokerList.aspx")
    try:
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
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
            Functions.progressIndicator(index+1, numberOfCompanies)
            Temporary.clear()
    except: pass
    finally:
        if len(OutStandingShare)>=numberOfCompanies:
            marketDataSaver()
        else:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t[ Error ] : Unable to extract market data")
        driver.close()

def newsExtractor():
    News.clear()
    NewsDate.clear()
    NewsSymbol.clear()
    Temporary.clear()
    print("\n\t-------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t[ Extracting Data (Estimated Time: 10 sec) ]")
    print("\t-------------------------------------------------------------------------------------------------------------------")
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    newsExtractorError = False
    driver.get("http://www.nepalstock.com/news/")
    count = 0
    try:
        items = driver.find_elements_by_xpath("//table[@class='table table-condensed table-hover']//tbody//tr//td[@class='alnleft']")
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
    except:
        newsExtractorError = True
    finally:
        if newsExtractorError==True:
            print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
            print("\t\t\t\t\t\t[ Error: Unable To Extract News ]")
        else:
            Functions.newsDisplay()
        driver.close()

def reportDataLoader():
    Functions.clearReportDataStorage()
    reportDataLoaderError = False
    isEmpty = False
    try:
        for index in range(0, numberOfCompanies):
            filePath = "data2/" + Symbol[index] + fileExtension
            file = open(filePath, 'r')
            if os.path.getsize(filePath)>0:
                for last_line in file: pass
                for word in last_line.split():
                    if word=="NULL":
                        Temporary.append(0.0)
                    else:
                        Temporary.append(float(word))
                shareDataAsOf.append(Temporary[0])
                shareVolume.append(Temporary[1])
                sharePrice.append(Temporary[2])
                shareOpenPrice.append(Temporary[3])
                shareHighPrice.append(Temporary[4])
                shareLowPrice.append(Temporary[5])
                shareMovingAnalysis1.append(Temporary[6])
                shareMovingAnalysis2.append(Temporary[7])
                shareMovingAnalysis3.append(Temporary[8])
                sharePivotPoint.append(Temporary[9])
                shareResistanceLevel1.append(Temporary[10])
                shareResistanceLevel2.append(Temporary[11])
                shareResistanceLevel3.append(Temporary[12])
                shareSupportLevel1.append(Temporary[13])
                shareSupportLevel2.append(Temporary[14])
                shareSupportLevel3.append(Temporary[15])
                Temporary.clear()
            else:
                isEmpty = True
        if isEmpty==False:
            for index in range(0, numberOfCompanies):
                filePath = "report/" + Symbol[index] + fileExtension
                file = open(filePath, 'r')
                if os.path.getsize(filePath)>0:
                    for last_line in file: pass
                    for word in last_line.split():
                        Temporary.append(word)
                    shareReportDate.append(Temporary[0])
                    shareReportData.append(Temporary[1])
                else:
                    isEmpty = True
    except:
        reportDataLoaderError = True
    finally:
        file.close()
        if reportDataLoaderError==True or isEmpty==True:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t[ Error ] : Report data could not be loaded")
            print("\t-------------------------------------------------------------------------------------------------------------------\n")
            Functions.programExit()

def reportDataSaver():
    dataAppenderError = False
    for index in range(0, numberOfCompanies):
        try:
            dataFilePath = fileName2 + Symbol[index] + fileExtension
            dataString1 = shareDataAsOf[index] + " " + shareVolume[index] + " " + sharePrice[index] + " " + shareOpenPrice[index] + " " + shareHighPrice[index] + " " + shareLowPrice[index]
            dataString2 = shareMovingAnalysis1[index] + " " + shareMovingAnalysis2[index] + " " + shareMovingAnalysis3[index] + " " + sharePivotPoint[index]
            dataString3 = shareSupportLevel1[index] + " " + shareSupportLevel2[index] + " " + shareSupportLevel3[index]
            dataString4 = shareResistanceLevel1[index] + " " + shareResistanceLevel2[index] + " " + shareResistanceLevel3[index]
            dataString = dataString1 + " " + dataString2 + " " + dataString3 + " " + dataString4 + "\n"
            
            # append data in file
            dataFile = open(dataFilePath, 'a')
            dataFile.write(dataString)
            dataFile.close()
        except:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t[ Error ] : Unable to update report data file")
        try:
            reportFilePath = reportFileName + Symbol[index] + fileExtension
            reportString = shareReportDate[index] + " " + shareReportData[index] + "\n"
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
            dataAppenderError = True
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t[ Error ] : Unable to update financial report file")
            break
    if dataAppenderError==False:
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print("\t\t[ Status ] : Data saved successful")

def reportDataExtractor():
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
                if count==0:
                    reportDate = "NULL"
                    reportData = "NULL"
            except:
                reportDate = "NULL"
                reportData = "NULL"
            
            shareDataAsOf.append(dataAsOf)
            sharePrice.append(marketPrice)
            shareVolume.append(volume)
            shareOpenPrice.append(openPrice)
            shareHighPrice.append(highPrice)
            shareLowPrice.append(lowPrice)
            shareMovingAnalysis1.append(movingAnalysis1)
            shareMovingAnalysis2.append(movingAnalysis2)
            shareMovingAnalysis3.append(movingAnalysis3)
            shareReportDate.append(reportDate)
            shareReportData.append(reportData)
            sharePivotPoint.append(pivotPoint)
            shareSupportLevel1.append(supportLevel1)
            shareSupportLevel2.append(supportLevel2)
            shareSupportLevel3.append(supportLevel3)
            shareResistanceLevel1.append(resistantLevel1)
            shareResistanceLevel2.append(resistantLevel2)
            shareResistanceLevel3.append(resistantLevel3)
            Functions.progressIndicator(index+1, numberOfCompanies)

    except:
        reportExtractionError = True
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print("\t\t[ Error ] : Unable to get report data")
    finally:
        driver.close()
        if len(shareResistanceLevel3)>=numberOfCompanies and len(shareReportData)>=numberOfCompanies and reportExtractionError==False:
            reportDataSaver()
        else:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t[ Error ] : Data extraction was incomplete")

def fileStatus():
    readError = False
    try:
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get("https://www.sharesansar.com/company/ACLBSL")
        dataAsOf = driver.find_element_by_xpath("//div[@class='first-row margin-bottom-15']//span[@class='comp-ason']//span[@class='text-org']").text
        dataAsOf = removeUnwantedCharacter(dataAsOf)
        driver.close()
    except:
        dateExtraction = True
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print("\t\t[ Error ] : Unable to get data status")
    if dateExtraction==False:
        try:
            filePath = fileName2 + "ACLBSL.txt"
            file = open(filePath, 'r')
            if os.path.getsize(filePath)>0:
                for last_line in file: pass
                if dataAsOf in last_line:
                    isUpdated = True
            file.close()
        except:
            readError = True
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t[ Error ] : Unable to read data")
            print("\t-------------------------------------------------------------------------------------------------------------------\n")
            Functions.programExit()

        if readError==False and isUpdated==False:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t[ Warning ] : Data needs to be updated")
        elif isUpdated==True:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t[ Status ] : Data is up to date")

