from CommandDefinition import *
from DataManager import *
import MegaStorage
import Functions
import os

def commandLine():
    print("\t-------------------------------------------------------------------------------------------------------------------\n")
    numberOfCompanies = MegaStorage.numberOfCompanies
    userCommand = input("\t\tStock Analyzer>\t")
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
                print("\t\t[ Error ] :" + Functions.center("Device is not connected to the Internet", 60))
        commandLine()
        
    # Data Extract Option
    elif userCommandFiltered.find("extract")>=0:
        if userCommandFiltered.find("?")>=0:
            extractDef()
        else:
            message1 = ""
            message2 = ""
            print("\n\t-------------------------------------------------------------------------------------------------------------------")
            print("\n\t\t[ Status ] :\tChecking few things...", end='\r')
            if isConnected()==True:
                if dataIsUpdated()==False and MegaStorage.connectionError==False:
                    print("\n\tPhase 1\n")
                    marketDataExtractor()
                    if len(OutStandingShare)>=numberOfCompanies:
                        print("\n\n\tPhase 2\n")
                        reportDataExtractor()
                        if len(shareVolume)>=numberOfCompanies and len(shareReportDate)>=numberOfCompanies:
                            fundamentalDataUpdate()
                            print("\t\t[ Status ] :" + Functions.center("Data extraction successful", 60))
                    else:
                        message1 = "\t\t[ Message ] :" + Functions.center("Data extraction unsuccessful (Data loaded successfully from file)", 60)
                        message2 = "\t\t[ Error ] :" + Functions.center("Data extraction unsuccessful and failed to load data from file", 60)
                        dataLoader(message1, message2)
                elif MegaStorage.connectionError==True:
                    message1 = "\t\t[ Message ] :" + Functions.center("Sever connection failed (Data loaded successfully from file)", 60)
                    message2 = "\t\t[ Error ] :" + Functions.center("Sever connection failed and failed to load data from file", 60)
                    dataLoader(message1, message2)
                else:
                    print("\t\t[ Message ] :" + Functions.center("Data is up to date (No need to extract data)", 60))
            else:
                print("\t\t[ Error ] :" + Functions.center("Data extraction failed (Device is not online)", 60))
        commandLine()

    # Company Symbol Search
    elif userCommandFiltered.find("company")>=0:
        if userCommandFiltered.find("?")>=0:
            companyDef()
        else:
            userCommand = input("\n\t\tCompany Symbol>\t")
            userCommandFiltered = removeUnwantedCharacter(userCommand.upper())
            for index in range(0, numberOfCompanies):
                if userCommandFiltered==Symbol[index]:
                    Functions.companyDataDisplay(index)
                    break
            if (index+1)>=numberOfCompanies:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print("\t\t[ Error ] :" + Functions.center("Invalid Company Name", 60))
        commandLine()

    # Compare Two Company
    elif userCommandFiltered.find("compare")>=0:
        companyCount = 0
        if userCommandFiltered.find("?")>=0:
            comparedef()
        else:
            userCommand = input("\n\t\tFirst Company Symbol>\t")
            company1 = removeUnwantedCharacter(userCommand.upper())
            userCommand = input("\t\tSecond Company Symbol>\t")
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
                print("\t\t[ Error ] :" + Functions.center("Invalid Commany Name", 60))
        commandLine()

    # Sort Company
    elif userCommandFiltered.find("sort")>=0:
        sortError = True
        if userCommandFiltered.find("?")>=0:
            sortDef()
        else:
            userCommand = input("\n\t\tFactor>\t")
            factor = removeUnwantedCharacter(userCommand.lower())
            if factor.find("pe")>=0 or factor.find("eps")>=0 or factor.find("price")>=0 or factor.find("share")>=0:
                userCommand = input("\t\tSector>\t")
                userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
                for index in range(0, len(SectorList1)):
                    if MegaStorage.SectorList1[index].find(userCommandFiltered)>=0:
                        if factor.find("eps")>=0:
                            Functions.sortData(index, "eps", False, 0, 0)
                        elif factor.find("pe")>=0:
                            Functions.sortData(index, "pe", False, 0, 0)
                        elif factor.find("share")>=0:
                            Functions.sortData(index, "share", False, 0, 0)
                        else:
                            Functions.sortData(index, "price", False, 0, 0)
                        sortError = False
                        break
                if sortError==True:
                    print("\n\t-------------------------------------------------------------------------------------------------------------------")
                    print("\t\t[ Error ] :" + Functions.center("Invalid Sector Name", 60))
            else:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print("\t\t[ Error ] :" + Functions.center("Invalid Factor", 60))
        commandLine()

    # Range selection of a sector
    elif userCommandFiltered.find("range")>=0:
        sectorError = True
        if userCommandFiltered.find("?")>=0:
            rangeDef()
        else:
            userCommand = input("\n\t\tSector>\t")
            userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
            for index in range(0, len(SectorList1)):
                if SectorList1[index].find(userCommandFiltered)>=0:
                    sectorError = False
                    userCommand = input("\t\tFactor>\t")
                    userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
                    try:
                        if userCommandFiltered=="price" or userCommandFiltered=="eps" or userCommandFiltered=="pe":
                            rangeLowerLimit = float(removeUnwantedCharacter(input(f"\t\tLower Limit [{userCommandFiltered.upper()}]:\t")))
                            rangeUpperLimit = float(removeUnwantedCharacter(input(f"\t\tUpper Limit [{userCommandFiltered.upper()}]:\t")))
                            if userCommandFiltered.find("price")>=0:    
                                Functions.sortData(index, "price", True, rangeLowerLimit, rangeUpperLimit)
                            elif userCommandFiltered.find("eps")>=0:
                                Functions.sortData(index, "eps", True, rangeLowerLimit, rangeUpperLimit)
                            elif userCommandFiltered.find("share")>=0:
                                Functions.sortData(index, "share", True, rangeLowerLimit, rangeUpperLimit)
                            else:
                                Functions.sortData(index, "pe", True, rangeLowerLimit, rangeUpperLimit)
                        else:
                            print("\n\t-------------------------------------------------------------------------------------------------------------------")
                            print("\t\t[ Error ] :" + Functions.center("Invalid Factor", 60))
                    except:
                        print("\n\t-------------------------------------------------------------------------------------------------------------------")
                        print("\t\t[ Error ] :" + Functions.center("Invalid Range Limit", 60))
            if sectorError==True:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print("\t\t[ Error ] :" + Functions.center("Invalid Sector Name", 60))
        commandLine()

    # Select Sector
    elif userCommandFiltered.find("sector")>=0:
        sectorError = True
        if userCommandFiltered.find("?")>=0:
            sectorDef()
        else:
            userCommand = input("\n\t\tSector>\t")
            userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
            for index in range(0, len(MegaStorage.SectorList1)):
                if userCommandFiltered.find(MegaStorage.SectorList1[index])>=0:
                    Functions.sectorDisplay(index)
                    sectorError = False
                    break
            if sectorError==True:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print("\t\t[ Error ] :" + Functions.center("Invalid Commany Name", 60))
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
            Functions.generateAutomatedReport()
        commandLine()

    # Gererate technical report of stock
    elif userCommandFiltered.find("technical")>=0:
        if userCommandFiltered.find("?")>=0:
            technicalDef()
        else:
            companyError = True
            userCommand = input("\n\t\tCompany Symbol>\t")
            userCommandFiltered = removeUnwantedCharacter(userCommand.upper())
            for index in range(0, numberOfCompanies):
                if userCommandFiltered==Symbol[index]:
                    Functions.generateTechnicalReport(index)
                    companyError = False
                    break
            if companyError==True:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print("\t\t[ Error ] :" + Functions.center("Invalid Commany Name", 60))
        commandLine()

    # Reset all existing files
    elif userCommandFiltered.find("reset")>=0:
        if userCommandFiltered.find("?")>=0:
            resetDef()
        else:
            print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
            response = input("\t\tReset Files (Y/N):\t")
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
        print("\t\t[ Error ] :" + Functions.center("Invalid Command", 60))
        commandLine()

def menu():
    print("\n\t===================================================================================================================")
    print(Functions.center("MAIN MENU", 116))
    print("\t===================================================================================================================\n")
    print("\t\t1. Use 'extract' to get new data")
    print("\t\t2. Use 'news' to view latest news")
    print("\t\t3. Use 'summary' to get market overview")
    print("\t\t4. Use 'compare' to compare between companies")
    print("\t\t5. Use 'company' to view  data of particular company")
    print("\t\t6. Use 'sort' to view sorted data for selected factor")
    print("\t\t7. Use 'sector' to view company data of selected sector")
    print("\t\t8. Use 'range' to view data of company within the given range")
    print("\t\t9. Use 'technical' to view technical perspective of report")
    print("\t\t10. Use 'report' to view an analyzed report of stocks")
    print("\t\t11. Use 'dividend' to view dividend giving stocks")
    print("\t\t12. Use 'reset' to reset all data and files")
    print("\t\t13. Use 'clear' to clear the screen")
    print("\t\t14. Use 'quit' to exit program")
    print("")
    commandLine()

def programLoader():
    #os.system('mode con: cols=132 lines=38')
    message1 = ""
    message2 = ""
    print("\n\t===================================================================================================================")
    print(Functions.center("Stock Analyzer", 116))
    print("\t===================================================================================================================\n")
    print("\n\t\t[ Status ] :" + Functions.center("Checking few things...", 60), end='\r')
    if isConnected()==True:
        if dataIsUpdated()==False and MegaStorage.connectionError==False:
            print("\t\t[ Status ] :" + Functions.center("Data is not up to date", 60))
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
                    print("\n\t\t[ Status ] :" + Functions.center("Data extraction was successful", 60))
                    menu()
                else:
                    print("\n\n\t-------------------------------------------------------------------------------------------------------------------")
                    print("\t\t[ Error ] :" + Functions.center("Failed to extract data", 60))
                    Functions.programExit()
            else:
                allFilesArePresent(True)
                message1 = "\t\t[ Status ] :" + Functions.center("Data loaded successfully from file", 60)
                message2 = "\t\t[ Error ] :" + Functions.center("Failed to load data", 60)
                if dataLoader(message1, message2)==True:
                    menu()
        elif MegaStorage.connectionError==True:
            allFilesArePresent(True)
            message1 = "\t\t[ Message ] :" + Functions.center("Sever connection failed (Data loaded successfully from file)", 60)
            message2 = "\t\t[ Error ] :" + Functions.center("Failed to load data", 60)
            if dataLoader(message1, message2)==True:
                menu()
        else:
            allFilesArePresent(True)
            message1 = "\t\t[ Status ] :" + Functions.center("Data is up to date and has been loaded successfully from file", 60)
            message2 = "\t\t[ Error ] :" + Functions.center("Data is up to date but unable to load from file", 60)
            if dataLoader(message1, message2)==True:
                menu()
    else:
        allFilesArePresent(True)
        message1 = "\t\t[ Status ] :" + Functions.center("Data loaded successfully in offline mode", 60)
        message2 = "\t\t[ Error ] :" + Functions.center("Failed to load data in offline mode", 60)
        if dataLoader(message1, message2)==True:
            menu()

# Program starts from here
programLoader()
