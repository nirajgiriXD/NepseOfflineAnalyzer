from CommandDefinition import *
from DataManager import *
import MegaStorage
import Functions
import os

def commandLine():
    Functions.lineMaker("-", "\t", 116, "\n")
    # numberOfCompanies = MegaStorage.numberOfCompanies
    userCommand = input("\t\tStock Analyzer: ")
    userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
    
    # Menu Option
    if userCommandFiltered.find("menu")>=0:
        if userCommandFiltered.find("?")>=0:
            menuDef()
            commandLine()
        else:
            menu()

    # Clear Screen
    elif userCommandFiltered=="cls" or userCommandFiltered=="clear":
        os.system('cls')
        menu()

    # News Option
    elif userCommandFiltered.find("news")>=0:
        if userCommandFiltered.find("?")>=0:
            newsDef()
        else:
            if isConnected()==True:
                newsExtractor()
            else:
                Functions.lineMaker("-", "\n\t", 116, "")
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Device is not connected to the Internet{MegaStorage.normal}", 60))
        commandLine()
        
    # Data Extract Option
    elif userCommandFiltered.find("extract")>=0:
        if userCommandFiltered.find("?")>=0:
            extractDef()
        else:
            message1 = ""
            message2 = ""
            Functions.lineMaker("-", "\n\t", 116, "\n")
            print(f"\t\t[ Status ] :" + Functions.center(f"Checking few things...", 60), end='\r')
            if isConnected()==True:
                if dataIsUpdated()==False and MegaStorage.connectionError==False:
                    print("\n\tPhase 1\n")
                    marketDataExtractor()
                    if len(OutStandingShare)>=MegaStorage.numberOfCompanies:
                        print("\n\n\tPhase 2\n")
                        reportDataExtractor()
                        if len(shareVolume)>=MegaStorage.numberOfCompanies and len(shareReportDate)>=MegaStorage.numberOfCompanies:
                            fundamentalDataUpdate()
                            print(f"{MegaStorage.green}\t\t[ Status ] :" + Functions.center(f"Data extraction successful{MegaStorage.normal}", 60))
                    else:
                        message1 = f"{MegaStorage.yellow}\t\t[ Message ] :" + Functions.center(f"Data extraction unsuccessful (Data loaded successfully from file){MegaStorage.normal}", 60)
                        message2 = f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Data extraction unsuccessful and failed to load data from file{MegaStorage.normal}", 60)
                        dataLoader(message1, message2)
                elif MegaStorage.connectionError==True:
                    message1 = f"{MegaStorage.yellow}\t\t[ Message ] :" + Functions.center(f"Sever connection failed (Data loaded successfully from file){MegaStorage.normal}", 60)
                    message2 = f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Sever connection failed and failed to load data from file{MegaStorage.normal}", 60)
                    dataLoader(message1, message2)
                else:
                    message1 = f"{MegaStorage.green}\t\t[ Message ] :" + Functions.center(f"Data is up to date (No need to extract data){MegaStorage.normal}", 60)
                    message2 = f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Unable to load offline data{MegaStorage.normal}", 60)
                    dataLoader(message1, message2)
            else:
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Data extraction failed (Device is not online){MegaStorage.normal}", 60))
        print("")
        commandLine()

    # Company Symbol Search
    elif userCommandFiltered.find("company")>=0:
        if userCommandFiltered.find("?")>=0:
            companyDef()
        else:
            userCommand = input("\t\tStock Analyzer> Company: ")
            userCommandFiltered = removeUnwantedCharacter(userCommand.upper())
            if userCommandFiltered=="ALL":
                Functions.sectorDisplay(13)
            else:
                for index in range(0, MegaStorage.numberOfCompanies):
                    if userCommandFiltered==Symbol[index]:
                        Functions.companyDataDisplay(index)
                        break
                if (index+1)>=MegaStorage.numberOfCompanies:
                    Functions.lineMaker("-", "\n\t", 116, "")
                    print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Company Name{MegaStorage.normal}", 60))
        commandLine()

    # Compare Two Company
    elif userCommandFiltered.find("compare")>=0:
        companyCount = 0
        if userCommandFiltered.find("?")>=0:
            comparedef()
        else:
            userCommand = input("\t\tStock Analyzer> Company [1]: ")
            company1 = removeUnwantedCharacter(userCommand.upper())
            userCommand = input("\t\tStock Analyzer> Company [2]: ")
            company2 = removeUnwantedCharacter(userCommand.upper())
            for index in range(0, MegaStorage.numberOfCompanies):
                if company1==Symbol[index]:
                    indexOne = index
                    companyCount += 1
                    if company2==Symbol[index]:
                        indexTwo = index
                        companyCount += 1
                        break
                elif company2==Symbol[index]:
                    indexTwo = index
                    companyCount += 1
                if companyCount>=2:
                    break
            if companyCount>=2:
                if indexOne==indexTwo:
                    Functions.companyDataDisplay(indexOne)
                else:
                    Functions.compareCompanies(indexOne, indexTwo)
            else:
                Functions.lineMaker("-", "\n\t", 116, "")
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Commany Name{MegaStorage.normal}", 60))
        commandLine()

    # Sort Company
    elif userCommandFiltered.find("sort")>=0:
        sortErrorFlag = True
        if userCommandFiltered.find("?")>=0:
            sortDef()
        else:
            size = len(SectorList1)
            userCommand = input("\t\tStock Analyzer> Sort> Sector: ")
            userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
            for index in range(0, size):
                if MegaStorage.SectorList1[index].find(userCommandFiltered)>=0:
                    sortErrorFlag = False
                    userCommand = input("\t\tStock Analyzer> Sort> Factor: ")
                    factor = removeUnwantedCharacter(userCommand.lower())
                    if factor.find("eps")>=0:
                        Functions.sortData(index, "eps", False, 0, 0)
                    elif factor.find("pe")>=0:
                        Functions.sortData(index, "pe", False, 0, 0)
                    elif factor.find("share")>=0:
                        Functions.sortData(index, "share", False, 0, 0)
                    elif factor.find("price")>=0:
                        Functions.sortData(index, "price", False, 0, 0)
                    elif factor.find("bonus")>=0:
                        Functions.sortData(index, "bonus", False, 0, 0)
                    elif factor.find("cash")>=0:
                        Functions.sortData(index, "cash", False, 0, 0)
                    elif factor.find("dividend")>=0:
                        Functions.sortData(index, "dividend", False, 0, 0)
                    elif factor.find("growth")>=0:
                        Functions.sortData(index, "growth", False, 0, 0)
                    else:
                        Functions.lineMaker("-", "\n\t", 116, "")
                        print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Factor{MegaStorage.normal}", 60))
                    break
            if sortErrorFlag==True:
                Functions.lineMaker("-", "\n\t", 116, "")
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Sector Name{MegaStorage.normal}", 60))  
        commandLine()

    # Range selection of a sector
    elif userCommandFiltered.find("range")>=0:
        rangeErrorFlag = True
        if userCommandFiltered.find("?")>=0:
            rangeDef()
        else:
            size = len(SectorList1)
            userCommand = input("\t\tStock Analyzer> Range> Sector: ")
            userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
            for index in range(0, size):
                if SectorList1[index].find(userCommandFiltered)>=0:
                    rangeErrorFlag = False
                    userCommand = input("\t\tStock Analyzer> Range> Factor: ")
                    userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
                    try:
                        rangeLowerLimit = float(removeUnwantedCharacter(input(f"\t\tStock Analyzer> Range> Factor> Lower Limit [{userCommandFiltered.upper()}]: ")))
                        rangeUpperLimit = float(removeUnwantedCharacter(input(f"\t\tStock Analyzer> Range> Factor> Upper Limit [{userCommandFiltered.upper()}]: ")))
                        if userCommandFiltered.find("price")>=0:    
                            Functions.sortData(index, "price", True, rangeLowerLimit, rangeUpperLimit)
                        elif userCommandFiltered.find("eps")>=0:
                            Functions.sortData(index, "eps", True, rangeLowerLimit, rangeUpperLimit)
                        elif userCommandFiltered.find("share")>=0:
                            Functions.sortData(index, "share", True, rangeLowerLimit, rangeUpperLimit)
                        elif userCommandFiltered.find("pe")>=0:
                            Functions.sortData(index, "pe", True, rangeLowerLimit, rangeUpperLimit)
                        elif userCommandFiltered.find("cash")>=0:
                            Functions.sortData(index, "cash", True, rangeLowerLimit, rangeUpperLimit)
                        elif userCommandFiltered.find("bonus")>=0:
                            Functions.sortData(index, "bonus", True, rangeLowerLimit, rangeUpperLimit)
                        elif userCommandFiltered.find("dividend")>=0:
                            Functions.sortData(index, "dividend", True, rangeLowerLimit, rangeUpperLimit)
                        elif userCommandFiltered.find("growth")>=0:
                            Functions.sortData(index, "growth", True, rangeLowerLimit, rangeUpperLimit)
                        else:
                            Functions.lineMaker("-", "\n\t", 116, "")
                            print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Range Factor{MegaStorage.normal}", 60))
                    except:
                        Functions.lineMaker("-", "\n\t", 116, "")
                        print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Range Limit{MegaStorage.normal}", 60))
                    finally:
                        break
            if rangeErrorFlag==True:
                Functions.lineMaker("-", "\n\t", 116, "")
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Sector Name{MegaStorage.normal}", 60))
        commandLine()
    
    # Stocks that have declared dividend
    elif userCommandFiltered.find("dividend")>=0:
        if userCommandFiltered.find("?")>=0:
            dividendDef()
        else:
            Functions.dividendReport()
        commandLine()
    
    # Generate Market Summary
    elif userCommandFiltered.find("summary")>=0:
        if userCommandFiltered.find("?")>=0:
            summaryDef()
        else:
            Functions.summaryReport()
        commandLine()

    # Generate stock report
    elif userCommandFiltered.find("report")>=0:
        if userCommandFiltered.find("?")>=0:
            reportDef()
        else:
            if userCommandFiltered.find("bullish")>=0:
                Functions.generateAutomatedReport("BULL")
            elif userCommandFiltered.find("bearish")>=0:
                Functions.generateAutomatedReport("BEAR")
            elif userCommandFiltered.find("detail")>=0:
                Functions.generateAutomatedReport("DETAIL")
            elif userCommandFiltered.find("sector")>=0:
                Functions.generateAutomatedReport("SECTOR")
            else:
                Functions.generateAutomatedReport("NULL")
        commandLine()

    # Gererate technical report of stock
    elif userCommandFiltered.find("technical")>=0:
        if userCommandFiltered.find("?")>=0:
            technicalDef()
        else:
            companyError = True
            userCommand = input("\t\tStock Analyzer> Technical> Company: ")
            userCommandFiltered = removeUnwantedCharacter(userCommand.upper())
            if userCommandFiltered=="ALL":
                Functions.generateAutomatedReport("NULL")
            else:
                for index in range(0, MegaStorage.numberOfCompanies):
                    if userCommandFiltered==Symbol[index]:
                        Functions.generateTechnicalReport(index)
                        companyError = False
                        break
                if companyError==True:
                    Functions.lineMaker("-", "\n\t", 116, "")
                    print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Commany Name{MegaStorage.normal}", 60))
        commandLine()

    # Reset all existing files
    elif userCommandFiltered.find("reset")>=0:
        if userCommandFiltered.find("?")>=0:
            resetDef()
        else:
            Functions.lineMaker("\n\t", 116, "")
            response = input("\t\tReset Files (Y/N) :\t")
            if response=='Y' or response=='y':
                resetFiles()
        commandLine()

    # Quit Program
    elif userCommandFiltered.find("exit")>=0 or userCommandFiltered.find("quit")>=0:
        if userCommandFiltered.find("?")>=0:
            exitDef()
            commandLine()
        else:
            Functions.programExit()

    # Default
    else:
        Functions.lineMaker("-", "\n\t", 116, "")
        print(f"\t\t{MegaStorage.red}[ Error ] :" + Functions.center(f"Invalid Command{MegaStorage.normal}", 60))
        commandLine()

def menu():
    Functions.lineMaker("=", "\n\t", 116, "")
    if isTesting==False:
        print(Functions.center(f"{MegaStorage.bold}Main Menu{MegaStorage.normal}", 116))
    else:
        print(Functions.center(f"{MegaStorage.yellow}Dev Mode{MegaStorage.normal}", 116))
    Functions.lineMaker("=", "\t", 116, "\n")
    print("\t\t1.\tUse 'extract' to get new data")
    print("\t\t2.\tUse 'news' to view latest news")
    print("\t\t3.\tUse 'summary' to get market overview")
    print("\t\t4.\tUse 'company' to view company's data")
    print("\t\t5.\tUse 'compare' to compare between companies")
    print("\t\t6.\tUse 'sort' to view sorted data for selected factor")
    print("\t\t7.\tUse 'range' to view data of company within the given range")
    print("\t\t8.\tUse 'technical' to view technical perspective of report")
    print("\t\t9.\tUse 'report' to view an analyzed report of stocks")
    print("\t\t10.\tUse 'dividend' to view dividend giving stocks")
    print("\t\t11.\tUse 'reset' to reset all data and files")
    print("\t\t12.\tUse 'clear' to clear the screen")
    print("\t\t13.\tUse 'quit' to exit program")
    print("")
    commandLine()

def programLoader():
    #os.system('mode con: cols=132 lines=38')
    message1 = ""
    message2 = ""
    Functions.lineMaker("=", "\n\n\t", 116, "")
    if Functions.isValidUser()==True:
        print(Functions.center(f"{MegaStorage.bold}Stock Analyzer - {MegaStorage.username}{MegaStorage.normal}", 121))
        Functions.lineMaker("=", "\t", 116, "\n")
        try:
            print("\t\t[ Status ] :" + Functions.center("Checking few things...", 55), end='\r')
            if isConnected()==True and isTesting==False:
                if dataIsUpdated()==False and MegaStorage.connectionError==False:
                    print(f"\t\t{MegaStorage.yellow}[ Status ] :" + Functions.center(f"Data is not up to date{MegaStorage.normal}", 60))
                    Functions.lineMaker("-", "\n\t", 116, "\n")
                    response = input("\t\tUpdate Data (Y/N):\t")
                    Functions.lineMaker("-", "\n\t", 116, "\n")
                    if response=="Y" or response=="y":
                        allFilesArePresent(False)
                        print("\n\tPhase 1\n")
                        marketDataExtractor()
                        if len(OutStandingShare)>=MegaStorage.numberOfCompanies:
                            print("\n\n\tPhase 2\n")
                            reportDataExtractor()
                        if len(shareVolume)>=MegaStorage.numberOfCompanies and len(shareReportDate)>=MegaStorage.numberOfCompanies:
                            fundamentalDataUpdate()
                            Functions.lineMaker("-", "\n\n\t", 116, "\n")
                            message1 = f"{MegaStorage.green}\t\t[ Status ] :" + Functions.center(f"Data extraction was successful{MegaStorage.normal}", 60)
                            message2 = f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Failed to assign extracted data{MegaStorage.normal}", 60)
                            if dataLoader(message1, message2)==True:
                                menu()
                        else:
                            Functions.lineMaker("-", "\n\n\t", 116, "")
                            print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Failed to extract data{MegaStorage.normal}", 60))
                            Functions.programExit()
                    else:
                        allFilesArePresent(True)
                        message1 = f"{MegaStorage.green}\t\t[ Status ] :" + Functions.center(f"Data loaded successfully from file{MegaStorage.normal}", 60)
                        message2 = f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Failed to load data{MegaStorage.normal}", 60)
                        if dataLoader(message1, message2)==True:
                            menu()
                elif MegaStorage.connectionError==True:
                    allFilesArePresent(True)
                    message1 = f"{MegaStorage.yellow}\t\t[ Message ] :" + Functions.center(f"Sever connection failed (Data loaded successfully from file){MegaStorage.normal}", 60)
                    message2 = f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Failed to load data{MegaStorage.normal}", 60)
                    if dataLoader(message1, message2)==True:
                        menu()
                else:
                    allFilesArePresent(True)
                    message1 = f"{MegaStorage.green}\t\t[ Status ] :" + Functions.center(f"Data is up to date and has been loaded successfully from file{MegaStorage.normal}", 60)
                    message2 = f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Data is up to date but unable to load from file{MegaStorage.normal}", 60)
                    if dataLoader(message1, message2)==True:
                        menu()
            else:
                allFilesArePresent(True)
                message1 = f"{MegaStorage.green}\t\t[ Status ] :" + Functions.center(f"Data loaded successfully in offline mode{MegaStorage.normal}", 60)
                message2 = f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Failed to load data in offline mode{MegaStorage.normal}", 60)
                if dataLoader(message1, message2)==True:
                    menu()
        except:
            allFilesArePresent(True)
            message1 = f"{MegaStorage.green}\t\t[ Status ] :" + Functions.center(f"Data loaded successfully in offline mode{MegaStorage.normal}", 60)
            message2 = f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Online data extraction failed{MegaStorage.normal}", 60)
            if dataLoader(message1, message2)==True:
                menu()
    else:
        print(Functions.center(f"{MegaStorage.bold}Stock Analyzer{MegaStorage.normal}", 121))
        Functions.lineMaker("=", "\t", 116, "\n")
        print(f"\t\t{MegaStorage.red}[ Alert ] :" + Functions.center(f"Invalid User Login Attempt{MegaStorage.normal}", 60))
        Functions.programExit()

# Program starts from here
programLoader()
