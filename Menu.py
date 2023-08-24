from CommandDefinition import *
from DataManager import *
import MegaStorage
import Functions
from time import sleep
import os

def commandLine():
    print("\t-------------------------------------------------------------------------------------------------------------------\n")
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
            newsExtractor()
        commandLine()
        
    # Data Ectract Option
    elif userCommandFiltered.find("extract")>=0:
        if userCommandFiltered.find("?")>=0:
            extractDef()
        else:
            marketDataExtractor()
        commandLine()

    # Company Symbol Search
    elif userCommandFiltered.find("company")>=0:
        index = -1
        if userCommandFiltered.find("?")>=0:
            companyDef()
        else:
            userCommand = input("\n\t\tCompany Name>\t")
            userCommandFiltered = removeUnwantedCharacter(userCommand.upper())
            for i in range(0, numberOfCompanies):
                if userCommandFiltered.find(Symbol[i])>=0:
                    index = i
                    break
            if index>=0:
                Functions.companyDataDisplay(index)
            else:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\t\t\t[ Error: Invalid Company Name ]")
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
                elif company2==Symbol[index]:
                    indexTwo = index
                    companyCount += 1
                if companyCount>=2:
                    break
            if companyCount>=2:
                Functions.compareCompanies(indexOne, indexTwo)
            else:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\t\t\t[ Error: Invalid Commany Name ]")
        commandLine()

    # Sort Company
    elif userCommandFiltered.find("sort")>=0:
        sortError = True
        if userCommandFiltered.find("?")>=0:
            sortDef()
        else:
            userCommand = input("\n\t\tFactor>\t")
            factor = removeUnwantedCharacter(userCommand.lower())
            if factor.find("pe")>=0 or factor.find("eps")>=0 or factor.find("price")>=0:
                userCommand = input("\t\tSector>\t")
                userCommandFiltered = removeUnwantedCharacter(userCommand.lower())
                for index in range(0, len(SectorList1)):
                    if MegaStorage.SectorList1[index].find(userCommandFiltered)>=0:
                        if factor.find("eps")>=0:
                            Functions.sortData(index, "eps", False, 0, 0)
                        elif factor.find("price")>=0:
                            Functions.sortData(index, "pe", False, 0, 0)
                        else:
                            Functions.sortData(index, "price", False, 0, 0)
                        sortError = False
                        break
                if sortError==True:
                    print("\n\t-------------------------------------------------------------------------------------------------------------------")
                    print("\t\t\t\t\t\t[ Error: Invalid Sector Name ]")
            else:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\t\t\t[ Error: Invalid Command ]")
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
                            else:
                                Functions.sortData(index, "pe", True, rangeLowerLimit, rangeUpperLimit)
                        else:
                            print("\n\t-------------------------------------------------------------------------------------------------------------------")
                            print("\t\t\t\t\t\t[ Error: Invalid Factor ]")
                    except:
                        print("\n\t-------------------------------------------------------------------------------------------------------------------")
                        print("\t\t\t\t\t\t[ Error: Invalid Range Limit ]")
            if sectorError==True:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\t\t\t[ Error: Invalid Sector Name ]")
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
                print("\t\t\t\t\t\t[ Error: Invalid Commany Name ]")
        commandLine()

    # Generate stock report
    elif userCommandFiltered.find("report")>=0:
        Functions.generateStockReport()
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
        print("\t\t\t\t\t\t[ Error: Invalid Command ]")
        commandLine()

def menu():
    print("\n\t===================================================================================================================")
    print("\t\t\t\t\t\t\t  MAIN MENU")
    print("\t===================================================================================================================\n")
    print("\t\t1. Use 'extract' to get new data")
    print("\t\t2. Use 'news' to view latest news")
    print("\t\t3. Use 'sort' to view sorted data")
    print("\t\t4. Use 'compare' to compare between companies")
    print("\t\t5. Use 'sector' to view data of particular company")
    print("\t\t6. Use 'company' to view  data of particular company")
    print("\t\t7. Use 'range' to view data of company within the given range")
    print("\t\t8. Use 'report' to view AI generated stock report")
    print("\t\t9. Use 'clear' to clear the screen")
    print("\t\t10. Use 'quit' to exit program")
    print("")
    commandLine()

# Program Starts Here:
marketDataLoader()
if len(OutStandingShare)>=numberOfCompanies:
    os.system("mode con cols=131 lines=720")
    menu()
else:
    print("\n\t-------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t[ Error: Data could not be fetched ]")
    print("\t-------------------------------------------------------------------------------------------------------------------")
    userCommand = input("\t\tGrab Data Online(Y/N)>\t")
    if userCommand=="Y" or userCommand=="y":
        marketDataExtractor()
    else:
        print("\n\n\t===================================================================================================================")
        print("\t\t\t\t\t[ EMPTY DATA SET: (Terminating Program) ]")
        print("\t===================================================================================================================\n\n")
        sleep(3)
        quit()
