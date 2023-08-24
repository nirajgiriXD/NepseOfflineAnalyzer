import MegaStorage
import os

def clearMarketDataStorage():
    MegaStorage.OutStandingShare.clear()
    MegaStorage.MarketPrice.clear()
    MegaStorage.PercentageChange.clear()
    MegaStorage.Avg120Day.clear()
    MegaStorage.OneYearYield.clear()
    MegaStorage.Eps.clear()
    MegaStorage.PERatio.clear()
    MegaStorage.BookValue.clear()
    MegaStorage.Pbv.clear()
    MegaStorage.Dividend.clear()
    MegaStorage.Bonus.clear()
    MegaStorage.RightShare.clear()
    MegaStorage.AvgVol130Day.clear()
    MegaStorage.MarketCapitalisation.clear()
    MegaStorage.Temporary.clear()

def progressIndicator(index):
    os.system('cls')
    progressIndicatorPercentage = "{:.2f}".format((index/MegaStorage.numberOfCompanies)*100)
    print("\n\t-------------------------------------------------------------------------------------------------------------------")
    print(f"\t\t\t\t\t[ Extracting Data (Progress: {progressIndicatorPercentage}%) ]")
    print("\t-------------------------------------------------------------------------------------------------------------------")

def newsDisplay():
    print("\n\n\t==================================================================================================================")
    print(f"\tSN\t\t\t\t\tSHARE NEWS\t\t\t\t\t\tSYMBOL\t   DATE")
    print("\t==================================================================================================================\n")
    for index in range(0, 20):
        print(f"\t{index+1}. {MegaStorage.News[index].ljust(89)}\t{MegaStorage.NewsSymbol[index].ljust(6)}\t{MegaStorage.NewsDate[index].ljust(10)}\n")

def companyDataDisplay(index):
    print("\n\t===================================================================================================================")
    print(f"\t\t\t\t\t{MegaStorage.Name[index]}")
    print("\t===================================================================================================================\n\n")
    print("\t\tSymbol = "+MegaStorage.Symbol[index])
    print("\t\tSector = "+MegaStorage.Sector[index])
    print("\t\tOutstanding Share = "+str(MegaStorage.OutStandingShare[index]))
    print("\t\tMarket Price = "+str(MegaStorage.MarketPrice[index]))
    print("\t\tPercentage Change = "+str(MegaStorage.PercentageChange[index]))
    print("\t\t120 Day Average = "+str(MegaStorage.Avg120Day[index]))
    print("\t\tOne year yield = "+str(MegaStorage.OneYearYield[index]))
    print("\t\tEPS = "+str(MegaStorage.Eps[index]))
    print("\t\tPE Ratio = "+str(MegaStorage.PERatio[index]))
    print("\t\tBook Value = "+str(MegaStorage.BookValue[index]))
    print("\t\tPBV = "+str(MegaStorage.Pbv[index]))
    print("\t\t130 Day Average Volume = "+str(MegaStorage.AvgVol130Day[index]))   
    print("\t\tMarket Capitalisation = "+MegaStorage.MarketCapitalisation[index])
    print("")

def compareCompanies(index1, index2):
    print("\n\t=======================================================================================================================================")
    print(f"\tFactors\t\t\t\t\t{MegaStorage.Symbol[index1]}\t\t\t\t|\t\t\t{MegaStorage.Symbol[index2]}")
    print("\t=======================================================================================================================================\n\n")
    print(f"\t{MegaStorage.DataSetPoint[0].ljust(26)}\t{MegaStorage.Name[index1].ljust(50)} {MegaStorage.Name[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[1].ljust(26)}\t{MegaStorage.Sector[index1].ljust(50)} {MegaStorage.Sector[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[2].ljust(26)}\t{str(MegaStorage.OutStandingShare[index1]).ljust(50)} {MegaStorage.OutStandingShare[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[3].ljust(26)}\t{str(MegaStorage.MarketPrice[index1]).ljust(50)} {MegaStorage.MarketPrice[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[4].ljust(26)}\t{str(MegaStorage.Avg120Day[index1]).ljust(50)} {MegaStorage.Avg120Day[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[5].ljust(26)}\t{str(MegaStorage.OneYearYield[index1]).ljust(50)} {MegaStorage.OneYearYield[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[6].ljust(26)}\t{str(MegaStorage.Eps[index1]).ljust(50)} {MegaStorage.Eps[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[7].ljust(26)}\t{str(MegaStorage.PERatio[index1]).ljust(50)} {MegaStorage.PERatio[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[8].ljust(26)}\t{str(MegaStorage.BookValue[index1]).ljust(50)} {MegaStorage.BookValue[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[9].ljust(26)}\t{str(MegaStorage.Pbv[index1]).ljust(50)} {MegaStorage.Pbv[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[10].ljust(26)}\t{str(MegaStorage.AvgVol130Day[index1]).ljust(50)} {MegaStorage.AvgVol130Day[index2]}")
    print(f"\t{MegaStorage.DataSetPoint[11].ljust(26)}\t{str(MegaStorage.MarketCapitalisation[index1]).ljust(50)} {MegaStorage.MarketCapitalisation[index2]}\n")

def sectorDisplay(index1):
    print("\n\n\t===================================================================================================================")
    print("\t\tSymbol\t\t\tPrice\t\t\tPE\t\t\tPBV\t\t\tEPS")
    print("\t===================================================================================================================\n\n")
    for index2 in range(0, MegaStorage.numberOfCompanies):
        if MegaStorage.SectorList2[index1].find(MegaStorage.Sector[index2])>=0:
            print(f"\t\t{MegaStorage.Symbol[index2]}\t\t\t{str(MegaStorage.MarketPrice[index2]).ljust(24)}{str(MegaStorage.PERatio[index2]).ljust(24)}{str(MegaStorage.Pbv[index2]).ljust(24)}{MegaStorage.MarketPrice[index2]}")
    print("")

def sortData(sectorIndex, factor, rangeFlag, rangeLowerLimit, rangeUpperLimit):
    sortFlag = False
    MegaStorage.arr1.clear()
    MegaStorage.arr2.clear()
    MegaStorage.arr3.clear()
    try:
        if factor=="eps":
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr1.append(MegaStorage.Eps[count])
        elif factor=="pe":
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr1.append(MegaStorage.PERatio[count])
        else:
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr1.append(MegaStorage.MarketPrice[count])

        if MegaStorage.SectorList1[sectorIndex]=="all":
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr2.append(MegaStorage.arr1[count])
                MegaStorage.arr3.append(count)
        else:
            for count in range(0, MegaStorage.numberOfCompanies):
                if MegaStorage.SectorList2[sectorIndex]==MegaStorage.Sector[count]:
                    MegaStorage.arr2.append(MegaStorage.arr1[count])
                    MegaStorage.arr3.append(count)
        
        MegaStorage.arr1.clear()
        lenArr = len(MegaStorage.arr3)
        for count1 in range(0, lenArr-1):
            for count2 in range(count1, lenArr-1):
                if MegaStorage.arr2[count1] > MegaStorage.arr2[count2 + 1]:
                    swap_var1 = MegaStorage.arr2[count2 + 1]
                    MegaStorage.arr2[count2 + 1] = MegaStorage.arr2[count1]
                    MegaStorage.arr2[count1] = swap_var1

                    swap_var2 = MegaStorage.arr3[count2 + 1]
                    MegaStorage.arr3[count2 + 1] = MegaStorage.arr3[count1]
                    MegaStorage.arr3[count1] = swap_var2
    except:
        sortFlag = True
    if sortFlag==False:
        print("\n\n\t===================================================================================================================")
        if factor=="eps":
            MegaStorage.arr3.reverse()
            print("\t\tSymbol\t\t\tEPS\t\t\tPE\t\t\tPBV\t\t\tPrice")
            print("\t===================================================================================================================\n\n")
            if rangeFlag==True:
                for count in range(0, lenArr):
                    index = MegaStorage.arr3[count]
                    if MegaStorage.Eps[index]>=rangeLowerLimit and MegaStorage.Eps[index]<=rangeUpperLimit:
                        print(f"\t\t{MegaStorage.Symbol[index]}\t\t\t{str(MegaStorage.Eps[index]).ljust(24)}{str(MegaStorage.PERatio[index]).ljust(24)}{str(MegaStorage.Pbv[index]).ljust(24)}{MegaStorage.MarketPrice[index]}")
            else:
                for count in range(0, lenArr):
                    index = MegaStorage.arr3[count]
                    print(f"\t\t{MegaStorage.Symbol[index]}\t\t\t{str(MegaStorage.Eps[index]).ljust(24)}{str(MegaStorage.PERatio[index]).ljust(24)}{str(MegaStorage.Pbv[index]).ljust(24)}{MegaStorage.MarketPrice[index]}")
            
        elif factor=="pe":
            print("\t\tSymbol\t\t\tPE\t\t\tPBV\t\t\tEPS\t\t\tPrice")
            print("\t===================================================================================================================\n\n")
            if rangeFlag==True:
                for count in range(0, lenArr):
                    index = MegaStorage.arr3[count]
                    if MegaStorage.PERatio[index]>=rangeLowerLimit and MegaStorage.PERatio[index]<=rangeUpperLimit:
                        print(f"\t\t{MegaStorage.Symbol[index]}\t\t\t{str(MegaStorage.PERatio[index]).ljust(24)}{str(MegaStorage.Pbv[index]).ljust(24)}{str(MegaStorage.Eps[index]).ljust(24)}{MegaStorage.MarketPrice[index]}")
            else:
                for count in range(0, lenArr):
                    index = MegaStorage.arr3[count]
                    print(f"\t\t{MegaStorage.Symbol[index]}\t\t\t{str(MegaStorage.PERatio[index]).ljust(24)}{str(MegaStorage.Pbv[index]).ljust(24)}{str(MegaStorage.Eps[index]).ljust(24)}{MegaStorage.MarketPrice[index]}")
            
        else:
            print("\t\tSymbol\t\t\tPrice\t\t\tPE\t\t\tPBV\t\t\tEPS")
            print("\t===================================================================================================================\n\n")
            if rangeFlag==True:
                for count in range(0, lenArr):
                    index = MegaStorage.arr3[count]
                    if MegaStorage.MarketPrice[index]>=rangeLowerLimit and MegaStorage.MarketPrice[index]<=rangeUpperLimit:
                        print(f"\t\t{MegaStorage.Symbol[index]}\t\t\t{str(MegaStorage.MarketPrice[index]).ljust(24)}{str(MegaStorage.PERatio[index]).ljust(24)}{str(MegaStorage.Pbv[index]).ljust(24)}{MegaStorage.Eps[index]}")
            else:
                for count in range(0, lenArr):
                    index = MegaStorage.arr3[count]
                    print(f"\t\t{MegaStorage.Symbol[index]}\t\t\t{str(MegaStorage.MarketPrice[index]).ljust(24)}{str(MegaStorage.PERatio[index]).ljust(24)}{str(MegaStorage.Pbv[index]).ljust(24)}{MegaStorage.Eps[index]}")
        
        print("")
    else:
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t[ Error: Unable To Sort Data ]")

def generateStockReport():
    pass

def programExit():
    print("\n\t===================================================================================================================")
    print("\t\t\t\t\t\t\tHAVE A GOOD DAY")
    print("\t===================================================================================================================\n\n")
    quit()
