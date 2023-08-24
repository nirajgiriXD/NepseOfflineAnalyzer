from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from MegaStorage import *
import Functions

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

# Data loader from file
def marketDataLoader():
    Functions.clearMarketDataStorage()
    file = open(fileName, 'r')
    marketDataLoaderError = False
    try:
        for index in range(0, numberOfCompanies):
            line = file.readline()
            for word in line.split():
                if word=="NULL":
                    Temporary.append(float(0.0))
                else:
                    Temporary.append(float(word))
            OutStandingShare.append(Temporary[0])
            MarketPrice.append(float(Temporary[1]))
            PercentageChange.append(Temporary[2])
            Avg120Day.append(Temporary[3])
            OneYearYield.append(Temporary[4])
            Eps.append(float(Temporary[5]))
            PERatio.append(float(Temporary[6]))
            BookValue.append(Temporary[7])
            Pbv.append(float(Temporary[8]))
            Dividend.append(Temporary[9])
            Bonus.append(Temporary[10])
            RightShare.append(Temporary[11])
            AvgVol130Day.append(Temporary[12])
            MarketCapitalisation.append(Temporary[13])
            Temporary.clear()
    except:
        marketDataLoaderError = True
    finally:
        file.close()
        if marketDataLoaderError==False:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t[ Status: Data Loaded Successfully ]")
            print("\t-------------------------------------------------------------------------------------------------------------------\n")
        else:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t[ Error: Data could not be Loaded ]")
            print("\t-------------------------------------------------------------------------------------------------------------------\n")

# Data saver to file
def marketDataSaver():
    open(fileName, 'w').close()
    file = open(fileName, 'a')
    if len(OutStandingShare)>=205:
        for index in range(0, len(OutStandingShare)):
            string1 = f"{OutStandingShare[index]} {MarketPrice[index]} {PercentageChange[index]} {Avg120Day[index]} {OneYearYield[index]} {Eps[index]} "
            string2 = f"{PERatio[index]} {BookValue[index]} {Pbv[index]} {Dividend[index]} {Bonus[index]} {RightShare[index]} {AvgVol130Day[index]} "
            string3 = f"{MarketCapitalisation[index]}\n"
            string = string1 + string2 + string3
            file.write(string)
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t[ Status: Data Saved Successfully ]")
    else:
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t[ Error: Unable To Save Data ]")
    file.close()

# Data extraction and assignment
def marketDataExtractor():
    Functions.clearMarketDataStorage()
    print("\n\t-------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t[ Extracting Data (Estimated Time: 5-10 min) ]")
    print("\t-------------------------------------------------------------------------------------------------------------------")
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get("https://merolagani.com/BrokerList.aspx")
    try:
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
            Functions.progressIndicator(index)
            Temporary.clear()
    except:
        pass
    finally:
        if len(OutStandingShare)>=205:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t[ Status: Data Extracted Successfully ]")
            marketDataSaver()
        else:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t[ Error: Unable To Extract Data ]")
        driver.close()

# News extraction and assignent
def newsExtractor():
    print("\n\t-------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t[ Extracting Data (Estimated Time: 10 sec) ]")
    print("\t-------------------------------------------------------------------------------------------------------------------")
    Functions.clearNewsStorage()
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
        newsExtractorError = False
        driver.close()
