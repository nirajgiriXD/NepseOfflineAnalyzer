from typing import final
from CommandDefinition import *
from DataManager import *
import MegaStorage
import Functions
import os

def commandLine():
    print("\t-------------------------------------------------------------------------------------------------------------------\n")
    numberOfCompanies = MegaStorage.numberOfCompanies
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
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Device is not connected to the Internet{MegaStorage.normal}", 60))
        commandLine()
        
    # Data Extract Option
    elif userCommandFiltered.find("extract")>=0:
        if userCommandFiltered.find("?")>=0:
            extractDef()
        else:
            message1 = ""
            message2 = ""
            print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
            print(f"\t\t[ Status ] :" + Functions.center(f"Checking few things...", 60), end='\r')
            if isConnected()==True:
                if dataIsUpdated()==False and MegaStorage.connectionError==False:
                    print("\n\tPhase 1\n")
                    marketDataExtractor()
                    if len(OutStandingShare)>=numberOfCompanies:
                        print("\n\n\tPhase 2\n")
                        reportDataExtractor()
                        if len(shareVolume)>=numberOfCompanies and len(shareReportDate)>=numberOfCompanies:
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
                    print(f"{MegaStorage.green}\t\t[ Message ] :" + Functions.center(f"Data is up to date (No need to extract data){MegaStorage.normal}", 60))
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
                for index in range(0, numberOfCompanies):
                    if userCommandFiltered==Symbol[index]:
                        Functions.companyDataDisplay(index)
                        break
                if (index+1)>=numberOfCompanies:
                    print("\n\t-------------------------------------------------------------------------------------------------------------------")
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
            for index in range(0, numberOfCompanies):
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
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Commany Name{MegaStorage.normal}", 60))
        commandLine()

    # Sort Company
    elif userCommandFiltered.find("sort")>=0:
        if userCommandFiltered.find("?")>=0:
            sortDef()
        else:
            size = len(SectorList1)
            userCommand = input("\t\tStock Analyzer> Sort> Sector: ")
            userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
            for index in range(0, size):
                if MegaStorage.SectorList1[index].find(userCommandFiltered)>=0:
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
                        print("\n\t-------------------------------------------------------------------------------------------------------------------")
                        print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Factor{MegaStorage.normal}", 60))
                    break
            if index>=size:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Sector Name{MegaStorage.normal}", 60))  
        commandLine()

    # Range selection of a sector
    elif userCommandFiltered.find("range")>=0:
        if userCommandFiltered.find("?")>=0:
            rangeDef()
        else:
            size = len(SectorList1)
            userCommand = input("\t\tStock Analyzer> Range> Sector: ")
            userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
            for index in range(0, size):
                if SectorList1[index].find(userCommandFiltered)>=0:
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
                            print("\n\t-------------------------------------------------------------------------------------------------------------------")
                            print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Range Factor{MegaStorage.normal}", 60))
                    except:
                        print("\n\t-------------------------------------------------------------------------------------------------------------------")
                        print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Range Limit{MegaStorage.normal}", 60))
                    finally:
                        break
            if index>=size:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Sector Name{MegaStorage.normal}", 60))
        commandLine()

    # Select Sector
    elif userCommandFiltered.find("sector")>=0:
        sectorError = True
        if userCommandFiltered.find("?")>=0:
            sectorDef()
        else:
            userCommand = input("\t\tStock Analyzer> Sector: ")
            userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
            for index in range(0, len(MegaStorage.SectorList1)):
                if userCommandFiltered.find(MegaStorage.SectorList1[index])>=0:
                    Functions.sectorDisplay(index)
                    sectorError = False
                    break
            if sectorError==True:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Commany Name{MegaStorage.normal}", 60))
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

    # Generate index report
    elif userCommandFiltered.find("index")>=0:
            if userCommandFiltered.find("?")>=0:
                indexDef()
            else:
                Functions.indexAnalysis()
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
                for index in range(0, numberOfCompanies):
                    if userCommandFiltered==Symbol[index]:
                        Functions.generateTechnicalReport(index)
                        companyError = False
                        break
                if companyError==True:
                    print("\n\t-------------------------------------------------------------------------------------------------------------------")
                    print(f"{MegaStorage.red}\t\t[ Error ] :" + Functions.center(f"Invalid Commany Name{MegaStorage.normal}", 60))
        commandLine()

    # Reset all existing files
    elif userCommandFiltered.find("reset")>=0:
        if userCommandFiltered.find("?")>=0:
            resetDef()
        else:
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print(f"{MegaStorage.yellow}")
            response = input("\t\tReset Files (Y/N) :\t")
            print(f"{MegaStorage.normal}")
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
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print(f"\t\t{MegaStorage.red}[ Error ] :" + Functions.center(f"Invalid Command{MegaStorage.normal}", 60))
        commandLine()

def menu():
    print("\n\t===================================================================================================================")
    print(Functions.center(f"{MegaStorage.bold}Main Menu{MegaStorage.normal}", 116))
    print("\t===================================================================================================================\n")
    print("\t\t1.\tUse 'extract' to get new data")
    print("\t\t2.\tUse 'news' to view latest news")
    print("\t\t3.\tUse 'summary' to get market overview")
    print("\t\t4.\tUse 'company' to view company's data")
    print("\t\t5.\tUse 'compare' to compare between companies")
    print("\t\t6.\tUse 'sort' to view sorted data for selected factor")
    print("\t\t7.\tUse 'sector' to view company data of selected sector")
    print("\t\t8.\tUse 'range' to view data of company within the given range")
    print("\t\t9.\tUse 'technical' to view technical perspective of report")
    print("\t\t10.\tUse 'report' to view an analyzed report of stocks")
    print("\t\t11.\tUse 'dividend' to view dividend giving stocks")
    print("\t\t12.\tUse 'reset' to reset all data and files")
    print("\t\t13.\tUse 'clear' to clear the screen")
    print("\t\t14.\tUse 'quit' to exit program")
    print("")
    commandLine()

def programLoader():
    #os.system('mode con: cols=132 lines=38')
    message1 = ""
    message2 = ""
    print("\n\t===================================================================================================================")
    print(Functions.center(f"{MegaStorage.bold}Stock Analyzer{MegaStorage.normal}", 121))
    print("\t===================================================================================================================\n")
    if Functions.isValidUser()==True:
        print(f"{MegaStorage.green}\t\t[ Greetings ] :" + Functions.center(f"Welcome {MegaStorage.username}{MegaStorage.normal}", 52))
        print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
        print("\t\t[ Status ] :" + Functions.center("Checking few things...", 55), end='\r')
        if isConnected()==True:
            if dataIsUpdated()==False and MegaStorage.connectionError==False:
                print(f"\t\t{MegaStorage.yellow}[ Status ] :" + Functions.center(f"Data is not up to date{MegaStorage.normal}", 60))
                print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
                response = input("\t\tUpdate Data (Y/N):\t")
                print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
                if response=="Y" or response=="y":
                    allFilesArePresent(False)
                    print("\n\tPhase 1\n")
                    marketDataExtractor()
                    if len(OutStandingShare)>=numberOfCompanies:
                        print("\n\n\tPhase 2\n")
                        reportDataExtractor()
                    if len(shareVolume)>=numberOfCompanies and len(shareReportDate)>=numberOfCompanies:
                        fundamentalDataUpdate()
                        print("\n\n\t-------------------------------------------------------------------------------------------------------------------")
                        print(f"\n\t\t{MegaStorage.green}[ Status ] :" + Functions.center(f"Data extraction was successful{MegaStorage.normal}", 60))
                        menu()
                    else:
                        print(f"\n\n\t-------------------------------------------------------------------------------------------------------------------")
                        print(f"\t\t{MegaStorage.red}[ Error ] :" + Functions.center(f"Failed to extract data{MegaStorage.normal}", 60))
                        Functions.programExit()
                else:
                    allFilesArePresent(True)
                    message1 = f"\t\t{MegaStorage.green}[ Status ] :" + Functions.center(f"Data loaded successfully from file{MegaStorage.normal}", 60)
                    message2 = f"\t\t{MegaStorage.red}[ Error ] :" + Functions.center(f"Failed to load data{MegaStorage.normal}", 60)
                    if dataLoader(message1, message2)==True:
                        menu()
            elif MegaStorage.connectionError==True:
                allFilesArePresent(True)
                message1 = f"\t\t{MegaStorage.yellow}[ Message ] :" + Functions.center(f"Sever connection failed (Data loaded successfully from file){MegaStorage.normal}", 60)
                message2 = f"\t\t{MegaStorage.red}[ Error ] :" + Functions.center(f"Failed to load data{MegaStorage.normal}", 60)
                if dataLoader(message1, message2)==True:
                    menu()
            else:
                allFilesArePresent(True)
                message1 = f"\t\t{MegaStorage.green}[ Status ] :" + Functions.center(f"Data is up to date and has been loaded successfully from file{MegaStorage.normal}", 60)
                message2 = f"\t\t{MegaStorage.red}[ Error ] :" + Functions.center(f"Data is up to date but unable to load from file{MegaStorage.normal}", 60)
                if dataLoader(message1, message2)==True:
                    menu()
        else:
            allFilesArePresent(True)
            message1 = f"\t\t{MegaStorage.green}[ Status ] :" + Functions.center(f"Data loaded successfully in offline mode{MegaStorage.normal}", 60)
            message2 = f"\t\t{MegaStorage.red}[ Error ] :" + Functions.center(f"Failed to load data in offline mode{MegaStorage.normal}", 60)
            if dataLoader(message1, message2)==True:
                menu()
    else:
        print(f"\t\t{MegaStorage.red}[ Alert ] :" + Functions.center(f"Invalid User Login Attempt{MegaStorage.normal}", 60))
        Functions.programExit()

# Program starts from here
programLoader()
