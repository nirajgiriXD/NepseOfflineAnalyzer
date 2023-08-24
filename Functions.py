from time import sleep
import MegaStorage

def clearArray():
    MegaStorage.arr1.clear()
    MegaStorage.arr2.clear()
    MegaStorage.arr3.clear()

def clearInitialDataStorage():
    MegaStorage.Symbol.clear()
    MegaStorage.Name.clear()
    MegaStorage.Sector.clear()
    MegaStorage.connectionError = False

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
    MegaStorage.AvgVol30Day.clear()
    MegaStorage.MarketCapitalisation.clear()
    MegaStorage.Temporary.clear()
    MegaStorage.barProgressCount = 1
    MegaStorage.bar = "____________________________________________________________________________________________________"

def clearDivDataStorage():
    MegaStorage.divBCD.clear()
    MegaStorage.divCash.clear()
    MegaStorage.divBonus.clear()
    MegaStorage.divSymbol.clear()

def clearReportDataStorage():
    clearDivDataStorage()
    MegaStorage.shareDataAsOf.clear()
    MegaStorage.shareVolume.clear()
    MegaStorage.sharePrice.clear()
    MegaStorage.shareLowPrice.clear()
    MegaStorage.shareHighPrice.clear()
    MegaStorage.shareOpenPrice.clear()
    MegaStorage.shareReportDate.clear()
    MegaStorage.share52WeeksHigh.clear()
    MegaStorage.share52WeeksLow.clear()
    MegaStorage.shareReportDate.clear()
    MegaStorage.shareReportValue.clear()
    MegaStorage.shareReportQuarter.clear()
    MegaStorage.Temporary.clear()
    MegaStorage.barProgressCount = 1
    MegaStorage.bar = "____________________________________________________________________________________________________"

def clearReportArrayStorage():
    MegaStorage.symbol.clear()
    MegaStorage.trend.clear()
    MegaStorage.remarks.clear()
    MegaStorage.bullPoint.clear()
    MegaStorage.bearPoint.clear()

def clearCompanyDataStorage():
    MegaStorage.companyVolume.clear()
    MegaStorage.companyPrice.clear()
    MegaStorage.companyLowPrice.clear()
    MegaStorage.companyHighPrice.clear()
    MegaStorage.companyOpenPrice.clear()
    MegaStorage.Temporary.clear()

def clearNewsDataStorage():
    MegaStorage.News.clear()
    MegaStorage.NewsDate.clear()
    MegaStorage.NewsSymbol.clear()
    MegaStorage.Temporary.clear()
    MegaStorage.barProgressCount = 1
    MegaStorage.bar = "____________________________________________________________________________________________________"

def companyDataReverse():
    MegaStorage.companyVolume.reverse()
    MegaStorage.companyPrice.reverse()
    MegaStorage.companyLowPrice.reverse()
    MegaStorage.companyHighPrice.reverse()
    MegaStorage.companyOpenPrice.reverse()

def center(str, length):
    blank = ""
    space = int((length - len(str))/2 + 8)
    if space<1:
        space = 1
    for index in range(0, space):
        blank = blank + " "
    return (blank + str)

def numberToWordConverter(num):
    num = float("{:.2f}".format(num))
    if abs(int(num/1000000000))>0:
        num = num/1000000000
        word = " Billion"
    elif abs(int(num/1000000))>0:
        num = num/1000000
        word = " Million"
    elif abs(int(num/1000))>0:
        num = num/1000
        word = " Thousand"
    else:
        word = " "
    return str(num) + word

def progressIndicator(index, total):
    progressIndicatorPercentage = float("{:.2f}".format((index/total)*100))
    while progressIndicatorPercentage>=MegaStorage.barProgressCount:
        MegaStorage.barProgressCount = MegaStorage.barProgressCount + 1
        MegaStorage.bar = MegaStorage.bar.replace('_', '█', 1)
    print(f"\t[ {progressIndicatorPercentage}% ] : {MegaStorage.bar}", end='\r')

def newsDisplay():
    print("\n\t==================================================================================================================")
    print(f"\tSN\t\t\t\t\tSHARE NEWS\t\t\t\t\t\tSYMBOL\t   DATE")
    print("\t==================================================================================================================\n")
    for index in range(0, 20):
        print(f"\t{index+1}. {MegaStorage.News[index].ljust(89)}\t{MegaStorage.NewsSymbol[index].ljust(6)}\t{MegaStorage.NewsDate[index].ljust(10)}\n")

def companyDataDisplay(index):
    print("\n\t===================================================================================================================")
    print(center(MegaStorage.Name[index], 116))
    print("\t===================================================================================================================\n")
    print(f"\t\tSector = {MegaStorage.Sector[index]}")
    print(f"\t\tMarket Price = {MegaStorage.sharePrice[index]}")
    print(f"\t\tPercentage Change = {MegaStorage.PercentageChange[index]} %")
    print(f"\t\tEPS = {MegaStorage.Eps[index]}")
    print(f"\t\tPBV = {MegaStorage.Pbv[index]}")
    print(f"\t\tPE Ratio = {MegaStorage.PERatio[index]}")
    print(f"\t\tBook Value = {MegaStorage.BookValue[index]}")
    print(f"\t\tOne year yield = {MegaStorage.OneYearYield[index]} %")
    print(f"\t\t120 Day Average = {MegaStorage.Avg120Day[index]}")
    print(f"\t\t30 Day Average Volume = {MegaStorage.AvgVol30Day[index]}")
    print(f"\t\t52 Weeks High-Low = {MegaStorage.share52WeeksHigh[index]}-{MegaStorage.share52WeeksLow[index]}")
    print(f"\t\tOutstanding Shares = {MegaStorage.OutStandingShare[index]}")   
    print(f"\t\tMarket Capitalisation = {MegaStorage.MarketCapitalisation[index]}")
    if MegaStorage.shareReportValue[index]>0:
        print(f"\t\tReport ({MegaStorage.shareReportDate[index]}) = {numberToWordConverter(MegaStorage.shareReportValue[index])} (Q{int(MegaStorage.shareReportQuarter[index])} Profit)")
    elif MegaStorage.shareReportValue[index]<0:
        print(f"\t\tReport ({MegaStorage.shareReportDate[index]}) = {numberToWordConverter(abs(MegaStorage.shareReportValue[index]))} (Q{int(MegaStorage.shareReportQuarter[index])} Loss)")
    else:
        print("\t\tReport = NULL")
    print("")

def compareCompanies(index1, index2):
    factor = ""
    print("\n\t=======================================================================================================================================")
    print("\tFactors" + center(MegaStorage.Symbol[index1], 88) + center(MegaStorage.Symbol[index2], 88))
    print("\t=======================================================================================================================================\n")
    factor = "Name:"
    print(f"\t{factor.ljust(26)}\t{MegaStorage.Name[index1].ljust(50)} {MegaStorage.Name[index2]}")
    factor = "Sector:"
    print(f"\t{factor.ljust(26)}\t{MegaStorage.Sector[index1].ljust(50)} {MegaStorage.Sector[index2]}")
    factor = "Price:"
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.sharePrice[index1]).ljust(50)} {MegaStorage.sharePrice[index2]}")
    factor = "EPS:"
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.Eps[index1]).ljust(50)} {MegaStorage.Eps[index2]}")
    factor = "PE:"
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.PERatio[index1]).ljust(50)} {MegaStorage.PERatio[index2]}")
    factor = "PBV:"
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.Pbv[index1]).ljust(50)} {MegaStorage.Pbv[index2]}")
    factor = "Book Value:"
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.BookValue[index1]).ljust(50)} {MegaStorage.BookValue[index2]}")
    factor = "1 Year Yield:"
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.OneYearYield[index1]).ljust(50)} {MegaStorage.OneYearYield[index2]}")
    factor = "120 Day Average:"
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.Avg120Day[index1]).ljust(50)} {MegaStorage.Avg120Day[index2]}")
    factor = "130 Day Average Volume:"
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.AvgVol30Day[index1]).ljust(50)} {MegaStorage.AvgVol30Day[index2]}")
    factor = "52 Weeks High-Low:"
    highLow52Weeks1 = str(MegaStorage.share52WeeksHigh[index1]) + "-" + str(MegaStorage.share52WeeksLow[index1])
    highLow52Weeks2 = str(MegaStorage.share52WeeksHigh[index2]) + "-" + str(MegaStorage.share52WeeksLow[index2])
    print(f"\t{factor.ljust(26)}\t{highLow52Weeks1.ljust(50)} {highLow52Weeks2}")
    factor = "Outstanding Share:"
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.OutStandingShare[index1]).ljust(50)} {str(MegaStorage.OutStandingShare[index2]).ljust(50)}")
    factor = "Market Capitalisation:"
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.MarketCapitalisation[index1]).ljust(50)} {MegaStorage.MarketCapitalisation[index2]}")
    if MegaStorage.shareReportValue[index1]>0:
        r1 = "Profit"
    elif MegaStorage.shareReportValue[index1]<0:
        r1 = "Loss"
    else:
        r1 = "NULL"
    if MegaStorage.shareReportValue[index2]>0:
        r2 = "Profit"
    elif MegaStorage.shareReportValue[index2]<0:
        r2 = "Loss"
    else:
        r2 = "NULL"
    if r1=="NULL" or r2=="NULL": pass
    else:
        try:
            factor = f"Q{int(MegaStorage.shareReportQuarter[index1])} {r1} - Q{int(MegaStorage.shareReportQuarter[index2])} {r2}:"
            print(f"\t{factor.ljust(26)}\t{numberToWordConverter(MegaStorage.shareReportValue[index1]).ljust(50)} {numberToWordConverter(MegaStorage.shareReportValue[index2]).ljust(50)}")
        except: pass
    print("")

def sectorDisplay(index1):
    print("\n\n\t===================================================================================================================")
    print("\t\tSymbol\t\t\tPrice\t\t\tPE\t\t\tPBV\t\t\tEPS")
    print("\t===================================================================================================================\n")
    for index2 in range(0, MegaStorage.numberOfCompanies):
        if MegaStorage.SectorList2[index1].find(MegaStorage.Sector[index2])>=0:
            print(f"\t\t{MegaStorage.Symbol[index2]}\t\t\t{str(MegaStorage.MarketPrice[index2]).ljust(24)}{str(MegaStorage.PERatio[index2]).ljust(24)}{str(MegaStorage.Pbv[index2]).ljust(24)}{MegaStorage.MarketPrice[index2]}")
    print("")

def sortData(sectorIndex, factor, rangeFlag, rangeLowerLimit, rangeUpperLimit):
    clearArray()
    sortFlag = False
    try:
        if factor=="eps":
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr1.append(MegaStorage.Eps[count])
        elif factor=="pe":
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr1.append(MegaStorage.PERatio[count])
        elif factor=="share":
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr1.append(MegaStorage.OutStandingShare[count])
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
            print("\t===================================================================================================================\n")
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
        elif factor=="share":
            print("\t\tSymbol\t\t     Outstanding Share\t\tEPS\t\t\tPE\t\t\tPrice")
            print("\t===================================================================================================================\n\n")
            if rangeFlag==True:
                for count in range(0, lenArr):
                    index = MegaStorage.arr3[count]
                    if MegaStorage.OutStandingShare[index]>=rangeLowerLimit and MegaStorage.OutStandingShare[index]<=rangeUpperLimit:
                        print(f"\t\t{MegaStorage.Symbol[index]}\t\t\t{str(MegaStorage.OutStandingShare[index]).ljust(24)}{str(MegaStorage.Eps[index]).ljust(24)}{str(MegaStorage.PERatio[index]).ljust(24)}{MegaStorage.MarketPrice[index]}")
            else:
                for count in range(0, lenArr):
                    index = MegaStorage.arr3[count]
                    print(f"\t\t{MegaStorage.Symbol[index]}\t\t\t{str(MegaStorage.OutStandingShare[index]).ljust(24)}{str(MegaStorage.Eps[index]).ljust(24)}{str(MegaStorage.PERatio[index]).ljust(24)}{MegaStorage.MarketPrice[index]}")
            
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

def dividendReport():
    print("\n\t===================================================================================================================")
    print("\t\tSymbol\t\t\tBonus\t\tCash\t\tTotal\t\tPrice\t\tBook Closure Date")
    print("\t===================================================================================================================\n")
    for index in range(0, len(MegaStorage.divSymbol)):
        price = "-"
        for count in range(0, MegaStorage.numberOfCompanies):
            if MegaStorage.divSymbol[index].find(MegaStorage.Symbol[count])>=0:
                price = str(MegaStorage.sharePrice[count])
                break
        cash = str("{:.2f}".format(MegaStorage.divCash[index])) + " %"
        bonus = str("{:.2f}".format(MegaStorage.divBonus[index])) + " %"
        total = str("{:.2f}".format(MegaStorage.divCash[index] + MegaStorage.divBonus[index])) + " %"
        print(f"\t\t{str(MegaStorage.divSymbol[index]).ljust(24)}{bonus.ljust(16)}{cash.ljust(16)}{total.ljust(16)}{price.ljust(16)}{str(MegaStorage.divBCD[index]).ljust(24)}")
    print("")

def sortArray(factor):
    clearArray()
    sortError = False
    try:
        if factor=="volume":
            for count in range(0, MegaStorage.numberOfCompanies):
                if not MegaStorage.Sector[count]=="Mutual Fund":
                    MegaStorage.arr2.append(float(MegaStorage.shareVolume[count]))
                    MegaStorage.arr3.append(count)
        elif factor=="gainer":
            for count in range(0, MegaStorage.numberOfCompanies):
                if MegaStorage.PercentageChange[count]>=0:
                    MegaStorage.arr2.append(float(MegaStorage.PercentageChange[count]))
                    MegaStorage.arr3.append(count)
        elif factor=="loser":
            for count in range(0, MegaStorage.numberOfCompanies):
                if MegaStorage.PercentageChange[count]<0:
                    MegaStorage.arr2.append(float(MegaStorage.PercentageChange[count]))
                    MegaStorage.arr3.append(count)

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
        sortError = True
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t[ Error ] :" + center("Unable To Sort Data", 60))
    return sortError

def companyDataLoader(index):
    lines = []
    companyDataLoaderError = False
    try:
        clearCompanyDataStorage()
        filePath = MegaStorage.fileName2 + MegaStorage.Symbol[index] + MegaStorage.fileExtension
        file = open(filePath, 'r')
        for line in file:
            lines.append(line)
        for count in range(0, len(lines)):
            for word in str(lines[count]).split():
                MegaStorage.Temporary.append(word)
            MegaStorage.companyVolume.append(float(MegaStorage.Temporary[1]))
            MegaStorage.companyPrice.append(float(MegaStorage.Temporary[2]))
            MegaStorage.companyOpenPrice.append(float(MegaStorage.Temporary[3]))
            MegaStorage.companyHighPrice.append(float(MegaStorage.Temporary[4]))
            MegaStorage.companyLowPrice.append(float(MegaStorage.Temporary[5]))
            MegaStorage.Temporary.clear()
        if len(MegaStorage.companyVolume)>0:
            companyDataReverse()
        file.close()
    except:
        companyDataLoaderError = True
    finally:
            if companyDataLoaderError==True:
                print("\n\t-------------------------------------------------------------------------------------------------------------------")
                print("\t\t[ Error ] :" + center(f"Company data could not be loaded ({MegaStorage.Symbol[index]})", 60))
                print("\t-------------------------------------------------------------------------------------------------------------------")
                programExit()

def summaryReport():
    volumeArr = []
    gainerArr = []
    loserArr = []
    errorFlag = False
    arr = ["Top Volume","Volume", "Top Gainer", "Change", "Top Losers"]
    if sortArray("volume")==False:
        for index in range(0, len(MegaStorage.arr3)):
            volumeArr.append(MegaStorage.arr3[index])
        if sortArray("gainer")==False:
            for index in range(0, len(MegaStorage.arr3)):
                gainerArr.append(MegaStorage.arr3[index])
            if sortArray("loser")==False:
                for index in range(0, len(MegaStorage.arr3)):
                    loserArr.append(MegaStorage.arr3[index])
            else:
                errorFlag = True
        else:
            errorFlag = True
    else:
        errorFlag = True
    
    if errorFlag==False:
        volumeArr.reverse()
        gainerArr.reverse()
        print("\n\t===================================================================================================================")
        print(f"\t\t{arr[2].ljust(19)}{arr[3]}\t|\t{arr[0].ljust(19)}{arr[1]}\t|\t{arr[4].ljust(19)}{arr[3]}")
        print("\t===================================================================================================================\n")
        for index in range(0, 10):
            volumeSymbol = str(MegaStorage.Symbol[volumeArr[index]])
            volume = str(MegaStorage.shareVolume[volumeArr[index]])
            gainerSymbol = str(MegaStorage.Symbol[gainerArr[index]])
            gainer = str(MegaStorage.PercentageChange[gainerArr[index]])
            loserSymbol = str(MegaStorage.Symbol[loserArr[index]])
            loser = str(MegaStorage.PercentageChange[loserArr[index]])
            print(f"\t\t{gainerSymbol.ljust(19)}{gainer} %\t|\t{volumeSymbol.ljust(19)}{volume}\t|\t{loserSymbol.ljust(18)}{loser} %")
        print("")

def volumeAnalysis():
    totalVolume = 0
    avgVol = 0
    sizeVolume = len(MegaStorage.companyVolume)
    if sizeVolume>1:
        for index in range(0, sizeVolume):
            try:
                totalVolume = totalVolume + MegaStorage.companyVolume[index+1]
            except:
                totalVolume = totalVolume + MegaStorage.companyVolume[index]
            if (index+1)==3:
                break
        avgVol = totalVolume/(index+1)
        if not avgVol==0:
            return (MegaStorage.companyVolume[0]/avgVol)*100
        else:
            return totalVolume
    else:
        return totalVolume

def buyPressure():
    candleLength = MegaStorage.companyHighPrice[0] - MegaStorage.companyLowPrice[0]
    if not candleLength==0:
        return ((MegaStorage.companyPrice[0] - MegaStorage.companyLowPrice[0])*100)/candleLength
    else:
        return 50

def sellPressure():
    candleLength = MegaStorage.companyHighPrice[0] - MegaStorage.companyLowPrice[0]
    if not candleLength==0:
        return ((MegaStorage.companyHighPrice[0] - MegaStorage.companyPrice[0])*100)/candleLength
    else:
        return 50

def gapOpen():
    gapPer = 0.0
    if len(MegaStorage.companyPrice)>1 and MegaStorage.companyPrice[0]>0 and MegaStorage.companyPrice[1]>0:
        if MegaStorage.companyPrice[0]>MegaStorage.companyPrice[1]:
            gapPer = float(((MegaStorage.companyLowPrice[0]-MegaStorage.companyHighPrice[1])/MegaStorage.companyPrice[1])*100)
            if gapPer<0 or gapPer<1:
                gapPer = 0.0
        elif MegaStorage.companyPrice[0]<MegaStorage.companyPrice[1]:
            gapPer = float(((MegaStorage.companyHighPrice[0]-MegaStorage.companyLowPrice[1])/MegaStorage.companyPrice[1])*100)
            if gapPer>0 or abs(gapPer)<1:
                gapPer = 0.0
        else:
            gapPer = 0.0
    return gapPer

def bodyToCandleRatio():
    candleLength = MegaStorage.companyHighPrice[0] - MegaStorage.companyLowPrice[0]
    bodyLength = abs(MegaStorage.companyOpenPrice[0] - MegaStorage.companyPrice[0])
    try:
        ratio = (bodyLength / candleLength) * 100
    except:
        ratio = 0
    return ratio

def shadowToCandleRatio():
    candleLength = MegaStorage.companyHighPrice[0] - MegaStorage.companyLowPrice[0]
    bodyLength = abs(MegaStorage.companyOpenPrice[0] - MegaStorage.companyPrice[0])
    try:
        ratio = ((candleLength - bodyLength) / candleLength) * 100
    except:
        ratio = 0
    return ratio

def hammer():
    hammerResult = "NULL"
    candleLength = MegaStorage.companyHighPrice[0] - MegaStorage.companyLowPrice[0]
    bodyLength = abs(MegaStorage.companyOpenPrice[0] - MegaStorage.companyPrice[0])
    bodyRatio = (bodyLength/candleLength)*100
    ratio1 = 0
    ratio2 = 0
    if bodyRatio<55:
        if MegaStorage.companyPrice[0]>MegaStorage.companyOpenPrice[0]:
            ratio1 = ((MegaStorage.companyHighPrice[0]-MegaStorage.companyPrice[0])/candleLength)*100
            ratio2 = ((MegaStorage.companyOpenPrice[0]-MegaStorage.companyLowPrice[0])/candleLength)*100
        elif MegaStorage.companyPrice[0]<MegaStorage.companyPrice[1]:
            ratio1 = ((MegaStorage.companyHighPrice[0]-MegaStorage.companyOpenPrice[0])/candleLength)*100
            ratio2 = ((MegaStorage.companyPrice[0]-MegaStorage.companyLowPrice[0])/candleLength)*100
        if not ratio1==ratio2:
            if ratio1<(ratio2/2.5):
                hammerResult = "Hammer"
            elif ratio2<(ratio1/2.5):
                hammerResult = "InvertedHammer"
    # print(f"\t\t{bodyRatio}\t{shadowRatio}\t{ratio1}\t{ratio2}")
    return hammerResult

def engulfingBullish():
    if len(MegaStorage.companyVolume)>1:
        pass

def engulfingBearish():
    if len(MegaStorage.companyVolume)>1:
        pass

def morningDojiStar():
    morningDojiStarResult = "NULL"
    if len(MegaStorage.companyVolume)>2:
        if (MegaStorage.companyPrice[2]-MegaStorage.companyPrice[1])>0 and (MegaStorage.companyPrice[1]-MegaStorage.companyPrice[0])<0:
            morningDojiStarResult = "Morning Doji Star"
    return morningDojiStarResult

def eveningDojiStar():
    eveningDojiStarResult = "NULL"
    if len(MegaStorage.companyVolume)>2:
        if (MegaStorage.companyPrice[1]-MegaStorage.companyPrice[2])>0 and (MegaStorage.companyPrice[0]-MegaStorage.companyPrice[1])>0:
            eveningDojiStarResult = "Evening Doji Star"
    return eveningDojiStarResult

def gravestone(dojiLength):
    isGravestone = "NULL"
    gravestonePer = abs(((MegaStorage.companyPrice[0]-MegaStorage.companyLowPrice[0])/MegaStorage.companyPrice[0])*100)
    if gravestonePer<=dojiLength:
        isGravestone = "GraveStone"
    return isGravestone

def dragonfly(dojiLength):
    isDragonfly = "NULL"
    dragonflyPer = abs(((MegaStorage.companyHighPrice[0]-MegaStorage.companyPrice[0])/MegaStorage.companyPrice[0])*100)
    if dragonflyPer<=dojiLength:
        isDragonfly = "DragonFly"
    return isDragonfly

def doji():
    dojiResult = "NULL"
    dojiLength = 0.5
    if abs(((MegaStorage.companyOpenPrice[0]-MegaStorage.companyPrice[0])/MegaStorage.companyPrice[0])*100)<=dojiLength:
        if dragonfly(dojiLength)==True:
            dojiResult = "DragonFly"
        elif gravestone(dojiLength)==True:
            dojiResult = "GraveStone"
        else:
            if morningDojiStar()=="Morning Doji Star":
                dojiResult = "Morning Doji Star"
            elif eveningDojiStar()=="Evening Doji Star":
                dojiResult = "Evening Doji Star"
            else:
                dojiResult = "Doji"
    return dojiResult

def appendReportData(index, bullCount, bearCount, arr):
    details = ""
    sizeRemarks = len(arr)
    if bullCount==bearCount:
        if sizeRemarks>0:
            for count in range(0, sizeRemarks):
                if (count+1)==sizeRemarks:
                    details = details + arr[count]
                else:
                    details = details + arr[count] + ", "
            MegaStorage.remarks.append(details)
            MegaStorage.bullPoint.append(bullCount)
            MegaStorage.bearPoint.append(bearCount)
            MegaStorage.trend.append("Indecisive")
            MegaStorage.symbol.append(MegaStorage.Symbol[index])
    else:
        for count in range(0, sizeRemarks):
            if (count+1)==sizeRemarks:
                details = details + arr[count]
            else:
                details = details + arr[count] + ", "
        MegaStorage.remarks.append(details)
        MegaStorage.bullPoint.append(bullCount)
        MegaStorage.bearPoint.append(bearCount)
        if bullCount>bearCount:
            MegaStorage.trend.append("Bullish")
        elif bearCount>bullCount:
            MegaStorage.trend.append("Bearish")
        MegaStorage.symbol.append(MegaStorage.Symbol[index])

def generateAutomatedReport(disFilter, volFilter):
    arr = []
    clearReportArrayStorage()
    for index in range(0, MegaStorage.numberOfCompanies):
        if MegaStorage.Sector[index].find("Corporate Debentures")>=0: pass
        elif MegaStorage.Sector[index].find("Promoter Share")>=0: pass
        elif MegaStorage.Sector[index].find("Mutual Fund")>=0: pass
        else:
            companyDataLoader(index)
            bullCount = 0
            bearCount = 0
            errorFlag = False
            dojiResult = doji()
            hammerResult = hammer()
            gap = float("{:.2f}".format(gapOpen()))
            buy = float("{:.2f}".format(buyPressure()))
            sell = float("{:.2f}".format(sellPressure()))
            volume = float("{:.2f}".format(volumeAnalysis()))
            try:
                if volume>=volFilter:
                    # Buy-Sell Pressure Analysis
                    if buy>sell:
                        bullCount += 1
                        arr.append("BuyPressure")
                    elif buy<sell:
                        bearCount += 1
                        arr.append("SellPressure")
                    # Gap Open Analysis
                    if not gap==0:
                        if gap>0:
                            bullCount += 1
                            arr.append("GapOpen")
                        elif gap<0:
                            bearCount += 1
                            arr.append("GapOpen")
                    # Doji Analysis
                    if not dojiResult=="NULL":
                        if dojiResult=="DragonFly":
                            bullCount += 1
                            arr.append("DragonFly")
                        elif dojiResult=="GraveStone":
                            bearCount += 1
                            arr.append("GraveStone")
                        elif dojiResult=="Morning Doji Star":
                            bullCount += 1
                            arr.append("MorningDojiStar")
                        elif dojiResult=="Evening Doji Star":
                            bearCount += 1
                            arr.append("EveningDojiStar")
                        elif dojiResult=="Doji":
                            arr.append("Doji")
                    # Hammer Analysis
                    if not hammerResult=="NULL":
                        if hammerResult=="Hammer":
                            arr.append("Hammer")
                        elif hammerResult=="InvertedHammer":
                            arr.append("InvertedHammer")
                else:
                    if not gap==0:
                        if gap<0:
                            bullCount += 1
                            arr.append("GapOpen")
                        elif gap>0:
                            bearCount += 1
                            arr.append("GapOpen")
                for count in range(0, len(MegaStorage.divSymbol)):
                    if str(MegaStorage.Symbol[index]).find(MegaStorage.divSymbol[count])>=0:
                        bullCount += 1
                        arr.append("Dividend")
            except:
                errorFlag = True
            finally:
                if errorFlag==False:
                    arr.reverse()
                    appendReportData(index, bullCount, bearCount, arr)
                arr.clear()
            
    sizeArr = len(MegaStorage.symbol)
    if sizeArr>0:
        title = ["Symbol", "Bull-Bear", "Trend", "Check Points"]
        print("\n\t===================================================================================================================")
        print(f"\t\t{title[0].ljust(17)}{title[1].ljust(21)}{title[2].ljust(19)}{title[3]}")
        print("\t===================================================================================================================\n")
        for index in range(0, sizeArr):
            if disFilter=="BULL":
                if str(MegaStorage.trend[index])=="Bullish":
                    print(f"\t\t{str(MegaStorage.symbol[index]).ljust(19)}{str(MegaStorage.bullPoint[index])} - {str(MegaStorage.bearPoint[index]).ljust(14)}{str(MegaStorage.trend[index]).ljust(19)}{str(MegaStorage.remarks[index])}")
            elif disFilter=="BEAR":
                if str(MegaStorage.trend[index])=="Bearish":
                    print(f"\t\t{str(MegaStorage.symbol[index]).ljust(19)}{str(MegaStorage.bullPoint[index])} - {str(MegaStorage.bearPoint[index]).ljust(14)}{str(MegaStorage.trend[index]).ljust(19)}{str(MegaStorage.remarks[index])}")
            else:
                print(f"\t\t{str(MegaStorage.symbol[index]).ljust(19)}{str(MegaStorage.bullPoint[index])} - {str(MegaStorage.bearPoint[index]).ljust(14)}{str(MegaStorage.trend[index]).ljust(19)}{str(MegaStorage.remarks[index])}")
        print("")
    else:
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print(f"\t\t[ Message ] :" + {center("Unable to generate report (Pattern Uncertainity)", 60)})
    
def generateTechnicalReport(index):
    companyDataLoader(index)
    dojiResult = doji()
    buy = ("{:.2f}".format(buyPressure()))
    sell = ("{:.2f}".format(sellPressure()))
    volume = ("{:.2f}".format(volumeAnalysis()))
    b2cRatio = ("{:.2f}".format(bodyToCandleRatio()))
    s2cRatio = ("{:.2f}".format(shadowToCandleRatio()))
    if not gapOpen()==0:
        isGap = True
    else:
        isGap = False
    if dojiResult=="NULL": 
        dojiResult = False
    titleArr = [
        "Gap Opening", "Doji Candle", "Buy Percentage", "Sell Percentage", "Volume Percentage",
        "Body to Candle Ratio", "Shadow to Candle Ratio"
    ]

    print("\n\t===================================================================================================================")
    print(center(f"{MegaStorage.Name[index]}", 116))
    print("\t===================================================================================================================\n")
    print(f"\t\t{titleArr[0].ljust(27)} : {isGap}")
    print(f"\t\t{titleArr[1].ljust(27)} : {dojiResult}")
    print(f"\t\t{titleArr[2].ljust(27)} : {buy} %")
    print(f"\t\t{titleArr[3].ljust(27)} : {sell} %")
    print(f"\t\t{titleArr[4].ljust(27)} : {volume} %")
    print(f"\t\t{titleArr[5].ljust(27)} : {b2cRatio} / 100")
    print(f"\t\t{titleArr[6].ljust(27)} : {s2cRatio} / 100")
    # print(f"\t\t")
    print("")

def programExit():
    print("\n\t===================================================================================================================")
    print(center("Program Termination", 116))
    print("\t===================================================================================================================\n\n")
    sleep(3)
    quit()
