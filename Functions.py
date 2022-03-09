from datetime import date
from time import sleep
import MegaStorage
import uuid
import sys
import os

def clearArray():
    MegaStorage.arr1.clear()
    MegaStorage.arr2.clear()
    MegaStorage.arr3.clear()
    MegaStorage.arr4.clear()
    MegaStorage.arr5.clear()
    MegaStorage.arr6.clear()
    MegaStorage.arr7.clear()

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
    return str("{:.2f}".format(num)) + word

def progressIndicator(index, total):
    progressIndicatorPercentage = float("{:.2f}".format((index/total)*100))
    while progressIndicatorPercentage>=MegaStorage.barProgressCount:
        MegaStorage.barProgressCount = MegaStorage.barProgressCount + 1
        MegaStorage.bar = MegaStorage.bar.replace('_', '█', 1)
    print(f"\t[ {progressIndicatorPercentage}% ] : {MegaStorage.bar}", end='\r')

# lineMaker ("LineSymbol", "FirstElement", "LengthOfLine", "LastElement")
def lineMaker(dashType, str1, length, str2):
    dash = ""
    for index in range(0, length):
        dash = dash + dashType
    print(f"{str1}{dash}{str2}")

def isValidUser():
    count = 0
    flag = False
    filePath = MegaStorage.fileName0 + "user" + MegaStorage.fileExtension
    if os.path.exists(filePath):
        if os.path.getsize(filePath)>0:
            file = open(filePath, 'r')
            for line in file:
                for word in line.split():
                    if (count%2)==0:
                        MegaStorage.username = word
                    else:
                        MegaStorage.macAdd = str(hex(uuid.getnode()))
                        if MegaStorage.macAdd==word:
                            flag = True
                            break
                    count += 1
                if flag==True:
                    break
            file.close()
    return flag

def dividendDataLoader(index):
    clearDivDataStorage()
    filePath = MegaStorage.fileName4 + MegaStorage.Symbol[index] + MegaStorage.fileExtension
    if os.path.getsize(filePath)>0:
        file = open(filePath, 'r')
        for line in file:
            MegaStorage.Temporary.clear()
            for word in line.split():
                MegaStorage.Temporary.append(word)
            try:
                MegaStorage.divBCD.append(int(str(MegaStorage.Temporary[0])[0:4]))
            except:
                MegaStorage.divBCD.append(int(0))
            try:
                MegaStorage.divBonus.append(float(MegaStorage.Temporary[1]))
            except:
                MegaStorage.divBonus.append(float(0.0))
            try:
                MegaStorage.divCash.append(float(MegaStorage.Temporary[2]))
            except:
                MegaStorage.divCash.append(float(0.0))
        file.close()
    else:
        MegaStorage.divBCD.append(int(0))
        MegaStorage.divBonus.append(float(0.0))
        MegaStorage.divCash.append(float(0.0))

def avgDividendFluctuation():
    arr = []
    avgDivFlux = 0.0
    currentDate = date.today()
    currentYear = currentDate.year + 57
    sizeOfArr = len(MegaStorage.divBCD)
    for count in range(0, sizeOfArr):
        arr.append(MegaStorage.divCash[count] + MegaStorage.divBonus[count])

    if sizeOfArr>=3:
        if MegaStorage.divBCD[0]==currentYear or MegaStorage.divBCD[0]==currentYear-1:
            if (MegaStorage.divBCD[0]-1)==MegaStorage.divBCD[1] and (MegaStorage.divBCD[0]-2)==MegaStorage.divBCD[2]:
                avgDivFlux = (abs(arr[0]-arr[1])+abs(arr[1]-arr[2]))/2
            elif (MegaStorage.divBCD[0]-1)==MegaStorage.divBCD[1] or (MegaStorage.divBCD[0]-2)==MegaStorage.divBCD[1]:
                avgDivFlux = (abs(arr[0]-arr[1])+abs(arr[1]-0))/2
            else:
                avgDivFlux = (abs(arr[0]-0)+abs(0-0))/2
        elif MegaStorage.divBCD[0]==currentYear-1 or MegaStorage.divBCD[0]==currentYear-2:
            if (MegaStorage.divBCD[0]-1)==MegaStorage.divBCD[1]:
                avgDivFlux = (abs(arr[0]-arr[1])+abs(arr[1]-0))/2
            else:
                avgDivFlux = (abs(arr[0]-0)+abs(0-0))/3
        elif MegaStorage.divBCD[0]==currentYear-2 or MegaStorage.divBCD[0]==currentYear-3:
            avgDivFlux = (abs(arr[0]-0)+abs(0-0))/2
        else:
            avgDivFlux = 0.0

    elif sizeOfArr==2:
        if MegaStorage.divBCD[0]==currentYear or MegaStorage.divBCD[0]==currentYear-1:
            if (MegaStorage.divBCD[0]-1)==MegaStorage.divBCD[1]:
                avgDivFlux = abs(arr[0]-arr[1])
            else:
                avgDivFlux = arr[0]
        elif MegaStorage.divBCD[0]==currentYear-1 or MegaStorage.divBCD[0]==currentYear-2:
            if (MegaStorage.divBCD[0]-1)==MegaStorage.divBCD[1]:
                avgDivFlux = (abs(0-arr[0])+abs(arr[0]-arr[1]))/2
            else:
                avgDivFlux = (abs(0-0)+abs(0-arr[0]))/2
        elif MegaStorage.divBCD[0]==currentYear-2 or MegaStorage.divBCD[0]==currentYear-3:
            avgDivFlux = (abs(0-0)+abs(0-arr[0]))/2
        else:
            avgDivFlux = 0.0

    elif sizeOfArr==1:
        if MegaStorage.divBCD[0]==currentYear or MegaStorage.divBCD[0]==currentYear-1:
            avgDivFlux = arr[0]
        elif MegaStorage.divBCD[0]==currentYear-1 or MegaStorage.divBCD[0]==currentYear-2:
            avgDivFlux = abs(0-arr[0])
        elif MegaStorage.divBCD[0]==currentYear-2 or MegaStorage.divBCD[0]==currentYear-3:
            avgDivFlux = (abs(0-0)+abs(0-arr[0]))/2
        else:
            avgDivFlux = 0.0

    return avgDivFlux

def avgDividend(factor):
    arr = []
    avgDividendResult = 0.0
    currentDate = date.today()
    currentYear = currentDate.year + 57
    if factor=="cash":
        for count in range(0, len(MegaStorage.divCash)):
            arr.append(MegaStorage.divCash[count])
    elif factor=="bonus":
        for count in range(0, len(MegaStorage.divBonus)):
            arr.append(MegaStorage.divBonus[count])
            
    sizeArr = len(arr)
    if sizeArr>=3:
        if MegaStorage.divBCD[0]==currentYear or MegaStorage.divBCD[0]==currentYear-1:
            if (MegaStorage.divBCD[0]-1)==MegaStorage.divBCD[1] and (MegaStorage.divBCD[0]-2)==MegaStorage.divBCD[2]:
                avgDividendResult = (arr[0]+arr[1]+arr[2])/3
            elif (MegaStorage.divBCD[0]-1)==MegaStorage.divBCD[1] or (MegaStorage.divBCD[0]-2)==MegaStorage.divBCD[1]:
                avgDividendResult = (arr[0]+arr[1]+0)/3
            else:
                avgDividendResult = (arr[0]+0+0)/3
        elif MegaStorage.divBCD[0]==currentYear-1 or MegaStorage.divBCD[0]==currentYear-2:
            if (MegaStorage.divBCD[0]-1)==MegaStorage.divBCD[1]:
                avgDividendResult = (arr[0]+arr[1]+0)/3
            else:
                avgDividendResult = (arr[0]+0+0)/3
        elif MegaStorage.divBCD[0]==currentYear-2 or MegaStorage.divBCD[0]==currentYear-3:
            avgDividendResult = (arr[0]+0+0)/3
        else:
            avgDividendResult = 0.0

    elif sizeArr==2:
        if MegaStorage.divBCD[0]==currentYear or MegaStorage.divBCD[0]==currentYear-1:
            if (MegaStorage.divBCD[0]-1)==MegaStorage.divBCD[1]:
                avgDividendResult = (arr[0]+arr[1])/2
            else:
                avgDividendResult = (arr[0]+0)/3
        elif MegaStorage.divBCD[0]==currentYear-1 or MegaStorage.divBCD[0]==currentYear-2:
            if (MegaStorage.divBCD[0]-1)==MegaStorage.divBCD[1]:
                avgDividendResult = (arr[0]+arr[1])/3
            else:
                avgDividendResult = (arr[0]+0)/3
        elif MegaStorage.divBCD[0]==currentYear-2 or MegaStorage.divBCD[0]==currentYear-3:
            avgDividendResult = (arr[0]+0)/3
        else:
            avgDividendResult = 0.0

    elif sizeArr==1:
        if MegaStorage.divBCD[0]==currentYear or MegaStorage.divBCD[0]==currentYear-1:
            avgDividendResult = arr[0]
        elif MegaStorage.divBCD[0]==currentYear-1 or MegaStorage.divBCD[0]==currentYear-2:
            avgDividendResult = arr[0]/2
        elif MegaStorage.divBCD[0]==currentYear-2 or MegaStorage.divBCD[0]==currentYear-3:
            avgDividendResult = arr[0]/3
        else:
            avgDividendResult = 0.0

    return avgDividendResult

def growthPercentage(index):
    profitLossArr = []
    quaterArr = []
    arrQ1V = []
    arrQ2V = []
    arrQ3V = []
    arrQ4V = []
    avgQ1V = 0
    avgQ2V = 0
    avgQ3V = 0
    avgQ4V = 0
    filePath = MegaStorage.fileName3 + MegaStorage.Symbol[index] + MegaStorage.fileExtension
    file = open(filePath, 'r')
    for line in file:
        MegaStorage.Temporary.clear()
        for word in line.split():
            MegaStorage.Temporary.append(word)
        try:
            value1 = float(MegaStorage.Temporary[1])
            value2 = int(MegaStorage.Temporary[2])
            if value1==0 or value2==0:
                pass
            else:
                profitLossArr.append(value1)
                quaterArr.append(value2)
        except:
            pass
    file.close()
    for count in range(0, len(quaterArr)):
        if quaterArr[count]==1:
            arrQ1V.append(profitLossArr[count])
        elif quaterArr[count]==2:
            arrQ2V.append(profitLossArr[count])
        elif quaterArr[count]==3:
            arrQ3V.append(profitLossArr[count])
        elif quaterArr[count]==4:
            arrQ4V.append(profitLossArr[count])
    for count in range(0, len(arrQ1V)):
        if count>=1:
            avgQ1V = avgQ1V+(((arrQ1V[count]-arrQ1V[count-1])/arrQ1V[count-1])*100)
    try:
        avgQ1V = avgQ1V/count
    except:
        avgQ1V = 0
    for count in range(0, len(arrQ2V)):
        if count>=1:
            avgQ2V = avgQ2V+(((arrQ2V[count]-arrQ2V[count-1])/arrQ2V[count-1])*100)
    try:
        avgQ2V = avgQ2V/count
    except:
        avgQ2V = 0
    for count in range(0, len(arrQ3V)):
        if count>=1:
            avgQ3V = avgQ3V+(((arrQ3V[count]-arrQ3V[count-1])/arrQ3V[count-1])*100)
    try:
        avgQ3V = avgQ3V/count
    except:
        avgQ3V = 0
    for count in range(0, len(arrQ4V)):
        if count>=1:
            avgQ4V = avgQ4V+(((arrQ4V[count]-arrQ4V[count-1])/arrQ4V[count-1])*100)
    try:
        avgQ4V = avgQ4V/count
    except:
        avgQ4V = 0
    count = 4
    if avgQ1V==0:
        count -= 1
    if avgQ2V==0:
        count -= 1
    if avgQ3V==0:
        count -= 1
    if avgQ4V==0:
        count -= 1
    if not count==0:
        growthPercentageResult = (avgQ1V+avgQ2V+avgQ3V+avgQ4V)/count
    else:
        growthPercentageResult = 0
    # if index==225:
    #     print(f"\n{growthPercentageResult}\n")
    return growthPercentageResult

def newsDisplay():
    print("\n\t==================================================================================================================")
    print(f"{MegaStorage.bold}\tSN\t\t\t\t\tSHARE NEWS\t\t\t\t\t\tSYMBOL\t   DATE{MegaStorage.normal}")
    print("\t==================================================================================================================\n")
    for index in range(0, 20):
        print(f"\t{index+1}. {MegaStorage.News[index].ljust(89)}\t{MegaStorage.NewsSymbol[index].ljust(6)}\t{MegaStorage.NewsDate[index].ljust(10)}\n")

def companyDataDisplay(index):
    print("\n\t===================================================================================================================")
    print(f"{MegaStorage.bold}" + center(MegaStorage.Name[index], 116) + f"{MegaStorage.normal}")
    print("\t===================================================================================================================\n")
    arr = [
        "Sector", "Market Price", "Percentage Change", "Earning Per Share (EPS)", "Price to Book Value (PBV)", "PE Ratio", "Book Value", "One Year Yield", "120 Day Average Price",
        "30 Day Average Volume", "52 Weeks High-Low", "Outstanding Shares", "Market Capitalisation", "Report", "Growth Rate", "Average Dividend"
    ]
    print(f"\t\t{arr[0].ljust(29)}:\t{MegaStorage.Sector[index]}")
    print(f"\t\t{arr[1].ljust(29)}:\t{MegaStorage.sharePrice[index]}")
    if MegaStorage.PercentageChange[index]>0:
        print(f"\t\t{arr[2].ljust(29)}:\t{MegaStorage.PercentageChange[index]} %")
    elif MegaStorage.PercentageChange[index]<0:
        print(f"\t\t{arr[2].ljust(29)}:\t{MegaStorage.PercentageChange[index]} %")
    print(f"\t\t{arr[3].ljust(29)}:\t{MegaStorage.Eps[index]}")
    print(f"\t\t{arr[4].ljust(29)}:\t{MegaStorage.Pbv[index]}")
    print(f"\t\t{arr[5].ljust(29)}:\t{MegaStorage.PERatio[index]}")
    print(f"\t\t{arr[6].ljust(29)}:\t{MegaStorage.BookValue[index]}")
    growth = str("{:.2f}".format(growthPercentage(index)))
    print(f"\t\t{arr[14].ljust(29)}:\t{growth} %")
    dividendDataLoader(index)
    avgDiv = str("{:.2f}".format(float(avgDividend("cash") + avgDividend("bonus"))))
    print(f"\t\t{arr[15].ljust(29)}:\t{avgDiv} %")
    print(f"\t\t{arr[7].ljust(29)}:\t{MegaStorage.OneYearYield[index]} %")
    print(f"\t\t{arr[8].ljust(29)}:\t{MegaStorage.Avg120Day[index]}")
    print(f"\t\t{arr[9].ljust(29)}:\t{MegaStorage.AvgVol30Day[index]}")
    print(f"\t\t{arr[10].ljust(29)}:\t{MegaStorage.share52WeeksHigh[index]}-{MegaStorage.share52WeeksLow[index]}")
    print(f"\t\t{arr[11].ljust(29)}:\t{numberToWordConverter(MegaStorage.OutStandingShare[index])}")   
    print(f"\t\t{arr[12].ljust(29)}:\t{numberToWordConverter(MegaStorage.MarketCapitalisation[index])}")
    if MegaStorage.shareReportValue[index]>0:
        factor = f"Report ({MegaStorage.shareReportDate[index]})"
        print(f"\t\t{factor.ljust(29)}:\t{numberToWordConverter(MegaStorage.shareReportValue[index])} (Q{int(MegaStorage.shareReportQuarter[index])} Profit)")
    elif MegaStorage.shareReportValue[index]<0:
        factor = f"Report ({MegaStorage.shareReportDate[index]})"
        print(f"\t\t{factor.ljust(29)}:\t{numberToWordConverter(abs(MegaStorage.shareReportValue[index]))} (Q{int(MegaStorage.shareReportQuarter[index])} Loss)")
    else:
        print(f"\t\t{arr[13].ljust(29)}:\tNULL")
    print("")

def compareCompanies(index1, index2):
    factor = ""
    print("\n\t===============================================================================================================================================")
    print(f"{MegaStorage.bold}\t\tFactors" + center(MegaStorage.Symbol[index1], 75) + center(MegaStorage.Symbol[index2], 75) + f"{MegaStorage.normal}")
    print("\t===============================================================================================================================================\n")
    factor = "Name"
    print(f"\t\t{factor.ljust(29)}:\t{MegaStorage.Name[index1].ljust(55)} {MegaStorage.Name[index2]}")
    factor = "Sector"
    print(f"\t\t{factor.ljust(29)}:\t{MegaStorage.Sector[index1].ljust(55)} {MegaStorage.Sector[index2]}")
    factor = "Price"
    print(f"\t\t{factor.ljust(29)}:\t{str(MegaStorage.sharePrice[index1]).ljust(55)} {MegaStorage.sharePrice[index2]}")
    factor = "Earning Per Share (EPS)"
    print(f"\t\t{factor.ljust(29)}:\t{str(MegaStorage.Eps[index1]).ljust(55)} {MegaStorage.Eps[index2]}")
    factor = "Price to Book Value (PBV)"
    print(f"\t\t{factor.ljust(29)}:\t{str(MegaStorage.Pbv[index1]).ljust(55)} {MegaStorage.Pbv[index2]}")
    factor = "PE Ratio"
    print(f"\t\t{factor.ljust(29)}:\t{str(MegaStorage.PERatio[index1]).ljust(55)} {MegaStorage.PERatio[index2]}")
    factor = "Book Value"
    print(f"\t\t{factor.ljust(29)}:\t{str(MegaStorage.BookValue[index1]).ljust(55)} {MegaStorage.BookValue[index2]}")
    factor = "Growth Rate"
    growth1 = str("{:.2f}".format(growthPercentage(index1))) + " %"
    growth2 = str("{:.2f}".format(growthPercentage(index2))) + " %"
    print(f"\t\t{factor.ljust(29)}:\t{growth1.ljust(55)} {growth2}")
    factor = "Average Dividend"
    dividendDataLoader(index1)
    avgDiv1 = str("{:.2f}".format(float(avgDividend("cash") + avgDividend("bonus")))) + " %"
    dividendDataLoader(index2)
    avgDiv2 = str("{:.2f}".format(float(avgDividend("cash") + avgDividend("bonus")))) + " %"
    print(f"\t\t{factor.ljust(29)}:\t{avgDiv1.ljust(55)} {avgDiv2}")
    factor = "One Year Yield"
    print(f"\t\t{factor.ljust(29)}:\t{str(MegaStorage.OneYearYield[index1]).ljust(55)} {MegaStorage.OneYearYield[index2]}")
    factor = "120 Day Average"
    print(f"\t\t{factor.ljust(29)}:\t{str(MegaStorage.Avg120Day[index1]).ljust(55)} {MegaStorage.Avg120Day[index2]}")
    factor = "30 Day Average Volume"
    print(f"\t\t{factor.ljust(29)}:\t{str(MegaStorage.AvgVol30Day[index1]).ljust(55)} {MegaStorage.AvgVol30Day[index2]}")
    factor = "52 Weeks High-Low"
    highLow52Weeks1 = str(MegaStorage.share52WeeksHigh[index1]) + "-" + str(MegaStorage.share52WeeksLow[index1])
    highLow52Weeks2 = str(MegaStorage.share52WeeksHigh[index2]) + "-" + str(MegaStorage.share52WeeksLow[index2])
    print(f"\t\t{factor.ljust(29)}:\t{highLow52Weeks1.ljust(55)} {highLow52Weeks2}")
    factor = "Outstanding Share"
    print(f"\t\t{factor.ljust(29)}:\t{numberToWordConverter(MegaStorage.OutStandingShare[index1]).ljust(55)} {numberToWordConverter(MegaStorage.OutStandingShare[index2])}")
    factor = "Market Capitalisation"
    print(f"\t\t{factor.ljust(29)}:\t{numberToWordConverter(MegaStorage.MarketCapitalisation[index1]).ljust(55)} {numberToWordConverter(MegaStorage.MarketCapitalisation[index2])}")
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
            factor = f"Q{int(MegaStorage.shareReportQuarter[index1])} {r1} - Q{int(MegaStorage.shareReportQuarter[index2])} {r2}"
            print(f"\t\t{factor.ljust(29)}:\t{numberToWordConverter(MegaStorage.shareReportValue[index1]).ljust(55)} {numberToWordConverter(MegaStorage.shareReportValue[index2])}")
        except: pass
    print("")

def sortData(sectorIndex, factor, rangeFlag, rangeLowerLimit, rangeUpperLimit):
    clearArray()
    sortFlag = False
    try:
        # Appending factor array to be sorted
        if factor=="eps":
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr1.append(MegaStorage.Eps[count])
        elif factor=="pe":
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr1.append(MegaStorage.PERatio[count])
        elif factor=="share":
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr1.append(MegaStorage.OutStandingShare[count])
        elif factor=="price":
            for count in range(0, MegaStorage.numberOfCompanies):
                MegaStorage.arr1.append(MegaStorage.MarketPrice[count])
        elif factor=="bonus" or factor=="cash" or factor=="dividend" or factor=="growth":
            for count in range(0, MegaStorage.numberOfCompanies):
                growth = growthPercentage(count)
                dividendDataLoader(count)
                avg1 = avgDividend("cash")
                avg2 = avgDividend("bonus")
                avg3 = avg1 + avg2
                avgFlux = avgDividendFluctuation()
                if factor=="cash":
                    MegaStorage.arr1.append(avg1)
                    MegaStorage.arr4.append(avg1)
                    MegaStorage.arr5.append(avg2)
                    MegaStorage.arr6.append(growth)
                    MegaStorage.arr7.append(avgFlux)
                elif factor=="bonus":
                    MegaStorage.arr1.append(avg2)
                    MegaStorage.arr4.append(avg1)
                    MegaStorage.arr5.append(avg2)
                    MegaStorage.arr6.append(growth)
                    MegaStorage.arr7.append(avgFlux)
                elif factor=="dividend":
                    MegaStorage.arr1.append(avg3)
                    MegaStorage.arr4.append(avg1)
                    MegaStorage.arr5.append(avg2)
                    MegaStorage.arr6.append(growth)
                    MegaStorage.arr7.append(avgFlux)
                elif factor=="growth":
                    MegaStorage.arr1.append(growth)
                    MegaStorage.arr4.append(avg1)
                    MegaStorage.arr5.append(avg2)
                    MegaStorage.arr6.append(growth)
                    MegaStorage.arr7.append(avgFlux)

        # Appoint factor related to the sector
        if MegaStorage.SectorList1[sectorIndex]=="all":
            for count in range(0, MegaStorage.numberOfCompanies):
                if not MegaStorage.Sector[count]=="Promoter Share" and not MegaStorage.Sector[count]=="Mutual Fund" and not MegaStorage.Sector[count]=="Corporate Debentures":
                    MegaStorage.arr2.append(MegaStorage.arr1[count])
                    MegaStorage.arr3.append(count)
        else:
            for count in range(0, MegaStorage.numberOfCompanies):
                if MegaStorage.SectorList2[sectorIndex]==MegaStorage.Sector[count] and not MegaStorage.Sector[count]=="Promoter Share" and not MegaStorage.Sector[count]=="Mutual Fund" and not MegaStorage.Sector[count]=="Corporate Debentures":
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
        MegaStorage.arr2.clear()
    except:
        sortFlag = True
    if sortFlag==False:
        print("\n\t====================================================================================================================================")
        if factor=="eps" or factor=="pe" or factor=="share" or factor=="price":
            if factor=="eps":
                MegaStorage.arr3.reverse()
                print(f"{MegaStorage.bold}\t\tSymbol\t\tEPS\t\tPE\t\tPBV\t\tPrice\t\t52 Weeks High\t\t52 Weeks Low{MegaStorage.normal}")
                print("\t====================================================================================================================================\n")
                if rangeFlag==True:
                    for count in range(0, lenArr):
                        index = MegaStorage.arr3[count]
                        if MegaStorage.Eps[index]>=rangeLowerLimit and MegaStorage.Eps[index]<=rangeUpperLimit:
                            print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(16)}{str(MegaStorage.Eps[index]).ljust(16)}{str(MegaStorage.PERatio[index]).ljust(16)}{str(MegaStorage.Pbv[index]).ljust(16)}{str(MegaStorage.MarketPrice[index]).ljust(19)}{str(MegaStorage.share52WeeksHigh[index]).ljust(23)}{MegaStorage.share52WeeksLow[index]}")
                else:
                    for count in range(0, lenArr):
                        index = MegaStorage.arr3[count]
                        print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(16)}{str(MegaStorage.Eps[index]).ljust(16)}{str(MegaStorage.PERatio[index]).ljust(16)}{str(MegaStorage.Pbv[index]).ljust(16)}{str(MegaStorage.MarketPrice[index]).ljust(19)}{str(MegaStorage.share52WeeksHigh[index]).ljust(23)}{MegaStorage.share52WeeksLow[index]}")
            
            elif factor=="pe":
                print(f"{MegaStorage.bold}\t\tSymbol\t\tPE\t\tPBV\t\tEPS\t\tPrice\t\t52 Weeks High\t\t52 Weeks Low{MegaStorage.normal}")
                print("\t====================================================================================================================================\n")
                if rangeFlag==True:
                    for count in range(0, lenArr):
                        index = MegaStorage.arr3[count]
                        if MegaStorage.PERatio[index]>=rangeLowerLimit and MegaStorage.PERatio[index]<=rangeUpperLimit:
                            print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(16)}{str(MegaStorage.PERatio[index]).ljust(16)}{str(MegaStorage.Pbv[index]).ljust(16)}{str(MegaStorage.Eps[index]).ljust(16)}{str(MegaStorage.MarketPrice[index]).ljust(19)}{str(MegaStorage.share52WeeksHigh[index]).ljust(23)}{MegaStorage.share52WeeksLow[index]}")
                else:
                    for count in range(0, lenArr):
                        index = MegaStorage.arr3[count]
                        print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(16)}{str(MegaStorage.PERatio[index]).ljust(16)}{str(MegaStorage.Pbv[index]).ljust(16)}{str(MegaStorage.Eps[index]).ljust(16)}{str(MegaStorage.MarketPrice[index]).ljust(19)}{str(MegaStorage.share52WeeksHigh[index]).ljust(23)}{MegaStorage.share52WeeksLow[index]}")
            
            elif factor=="share":
                print(f"{MegaStorage.bold}\t\tSymbol\t\tOutstanding Share\tEPS\t\tPE\t\tPrice\t\t52 Weeks High\t\t52 Weeks Low{MegaStorage.normal}")
                print("\t====================================================================================================================================\n")
                if rangeFlag==True:
                    for count in range(0, lenArr):
                        index = MegaStorage.arr3[count]
                        if MegaStorage.OutStandingShare[index]>=rangeLowerLimit and MegaStorage.OutStandingShare[index]<=rangeUpperLimit:
                            print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(16)}{str(MegaStorage.OutStandingShare[index]).ljust(23)}{str(MegaStorage.Eps[index]).ljust(16)}{str(MegaStorage.PERatio[index]).ljust(16)}{str(MegaStorage.MarketPrice[index]).ljust(19)}{str(MegaStorage.share52WeeksHigh[index]).ljust(23)}{MegaStorage.share52WeeksLow[index]}")
                else:
                    for count in range(0, lenArr):
                        index = MegaStorage.arr3[count]
                        print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(16)}{str(MegaStorage.OutStandingShare[index]).ljust(23)}{str(MegaStorage.Eps[index]).ljust(16)}{str(MegaStorage.PERatio[index]).ljust(16)}{str(MegaStorage.MarketPrice[index]).ljust(19)}{str(MegaStorage.share52WeeksHigh[index]).ljust(23)}{MegaStorage.share52WeeksLow[index]}")

            elif factor=="price":
                print(f"{MegaStorage.bold}\t\tSymbol\t\tPrice\t\tPE\t\tPBV\t\tEPS\t\t52 Weeks High\t\t52 Weeks Low{MegaStorage.normal}")
                print("\t====================================================================================================================================\n")
                if rangeFlag==True:
                    for count in range(0, lenArr):
                        index = MegaStorage.arr3[count]
                        if MegaStorage.MarketPrice[index]>=rangeLowerLimit and MegaStorage.MarketPrice[index]<=rangeUpperLimit:
                            print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(16)}{str(MegaStorage.MarketPrice[index]).ljust(16)}{str(MegaStorage.PERatio[index]).ljust(16)}{str(MegaStorage.Pbv[index]).ljust(16)}{str(MegaStorage.Eps[index]).ljust(19)}{str(MegaStorage.share52WeeksHigh[index]).ljust(23)}{MegaStorage.share52WeeksLow[index]}")
                else:
                    for count in range(0, lenArr):
                        index = MegaStorage.arr3[count]
                        print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(16)}{str(MegaStorage.MarketPrice[index]).ljust(16)}{str(MegaStorage.PERatio[index]).ljust(16)}{str(MegaStorage.Pbv[index]).ljust(16)}{str(MegaStorage.Eps[index]).ljust(19)}{str(MegaStorage.share52WeeksHigh[index]).ljust(23)}{MegaStorage.share52WeeksLow[index]}")
            print("")
        elif factor=="cash" or factor=="bonus" or factor=="dividend" or factor=="growth":
            MegaStorage.arr3.reverse()
            size = len(MegaStorage.arr3)
            arr = ["Symbol", "Avg Dividend", "Avg Bonus", "Avg Cash", "Price", "Growth", "Div Flux"]
            if factor=="cash":
                print(f"{MegaStorage.bold}\t\t{str(arr[0].ljust(17))}{str(arr[3]).ljust(17)}{str(arr[2]).ljust(17)}{str(arr[1]).ljust(21)}{str(arr[6]).ljust(17)}{str(arr[5]).ljust(17)}{str(arr[4])}{MegaStorage.normal}")
            elif factor=="bonus":
                print(f"{MegaStorage.bold}\t\t{str(arr[0].ljust(17))}{str(arr[2]).ljust(17)}{str(arr[3]).ljust(17)}{str(arr[1]).ljust(21)}{str(arr[6]).ljust(17)}{str(arr[5]).ljust(17)}{str(arr[4])}{MegaStorage.normal}")
            elif factor=="dividend":
                print(f"{MegaStorage.bold}\t\t{str(arr[0].ljust(17))}{str(arr[1]).ljust(19)}{str(arr[6]).ljust(17)}{str(arr[2]).ljust(17)}{str(arr[3]).ljust(17)}{str(arr[5]).ljust(17)}{str(arr[4])}{MegaStorage.normal}")
            elif factor=="growth":
                print(f"{MegaStorage.bold}\t\t{str(arr[0].ljust(17))}{str(arr[5]).ljust(17)}{str(arr[1]).ljust(21)}{str(arr[6]).ljust(17)}{str(arr[2]).ljust(17)}{str(arr[3]).ljust(17)}{str(arr[4])}{MegaStorage.normal}")
            print("\t====================================================================================================================================\n")
            for count in range(0, size):
                dividendDataLoader(count)
                index = MegaStorage.arr3[count]
                avgCash = MegaStorage.arr4[index]
                avgBonus = MegaStorage.arr5[index]
                avgDiv = avgBonus + avgCash
                growth = MegaStorage.arr6[index]
                avgFlux = MegaStorage.arr7[index]
                avgCashStr = str("{:.2f}".format(avgCash)) + " %"
                avgBonusStr = str("{:.2f}".format(avgBonus)) + " %"
                avgDivStr = str("{:.2f}".format(avgDiv)) + " %"
                growthStr = str("{:.2f}".format(growth)) + " %"
                avgFluxStr = str("{:.2f}".format(avgFlux)) + " %"
                if factor=="cash":
                    if rangeFlag==True:
                        if avgCash>=rangeLowerLimit and avgCash<=rangeUpperLimit:
                            print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(18)}{avgCashStr.ljust(17)}{avgBonusStr.ljust(19)}{avgDivStr.ljust(18)}{avgFluxStr.ljust(17)}{growthStr.ljust(17)}{str(MegaStorage.MarketPrice[index])}")
                    else:
                        print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(18)}{avgCashStr.ljust(17)}{avgBonusStr.ljust(19)}{avgDivStr.ljust(18)}{avgFluxStr.ljust(17)}{growthStr.ljust(17)}{str(MegaStorage.MarketPrice[index])}")
                elif factor=="bonus":
                    if rangeFlag==True:
                        if avgBonus>=rangeLowerLimit and avgBonus<=rangeUpperLimit:
                            print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(18)}{avgBonusStr.ljust(17)}{avgCashStr.ljust(19)}{avgDivStr.ljust(18)}{avgFluxStr.ljust(17)}{growthStr.ljust(17)}{str(MegaStorage.MarketPrice[index])}")
                    else:
                        print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(18)}{avgBonusStr.ljust(17)}{avgCashStr.ljust(19)}{avgDivStr.ljust(18)}{avgFluxStr.ljust(17)}{growthStr.ljust(17)}{str(MegaStorage.MarketPrice[index])}")
                elif factor=="dividend":
                    if rangeFlag==True:
                        if avgDiv>=rangeLowerLimit and avgDiv<=rangeUpperLimit:
                            print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(20)}{avgDivStr.ljust(17)}{avgFluxStr.ljust(17)}{avgBonusStr.ljust(17)}{avgCashStr.ljust(16)}{growthStr.ljust(17)}{str(MegaStorage.MarketPrice[index])}")
                    else:
                        print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(20)}{avgDivStr.ljust(17)}{avgFluxStr.ljust(17)}{avgBonusStr.ljust(17)}{avgCashStr.ljust(16)}{growthStr.ljust(17)}{str(MegaStorage.MarketPrice[index])}")
                elif factor=="growth":
                    if rangeFlag==True:
                        if growth>=rangeLowerLimit and growth<=rangeUpperLimit:
                            print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(17)}{growthStr.ljust(19)}{avgDivStr.ljust(20)}{avgFluxStr.ljust(17)}{avgBonusStr.ljust(17)}{avgCashStr.ljust(16)}{str(MegaStorage.MarketPrice[index])}")
                    else:
                        print(f"\t\t{str(MegaStorage.Symbol[index]).ljust(17)}{growthStr.ljust(19)}{avgDivStr.ljust(20)}{avgFluxStr.ljust(17)}{avgBonusStr.ljust(17)}{avgCashStr.ljust(16)}{str(MegaStorage.MarketPrice[index])}")
            print("")
    else:
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print(f"{MegaStorage.red}\t\t[ Error ] :" + center(f"Unable To Sort Data{MegaStorage.normal}", 60))

def dividendReport():
    dividendSize = len(MegaStorage.divSymbol)
    if dividendSize>0:
        print("\n\t===================================================================================================================")
        print(f"{MegaStorage.bold}\t\tSymbol\t\t\tPrice\t\tBonus\t\tCash\t\tTotal\t\tBook Closure Date{MegaStorage.normal}")
        print("\t===================================================================================================================\n")
        for index in range(0, dividendSize):
            price = "-"
            for count in range(0, MegaStorage.numberOfCompanies):
                if MegaStorage.divSymbol[index].find(MegaStorage.Symbol[count])>=0:
                    price = str(MegaStorage.sharePrice[count])
                    break
            cash = str("{:.2f}".format(MegaStorage.divCash[index])) + " %"
            bonus = str("{:.2f}".format(MegaStorage.divBonus[index])) + " %"
            total = str("{:.2f}".format(MegaStorage.divCash[index] + MegaStorage.divBonus[index])) + " %"
            print(f"\t\t{str(MegaStorage.divSymbol[index]).ljust(24)}{price.ljust(16)}{bonus.ljust(16)}{cash.ljust(16)}{total.ljust(16)}{str(MegaStorage.divBCD[index]).ljust(24)}")
        print("")
    else:
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print(f"{MegaStorage.yellow}\t\t[ Message ] :" + center(f"Dividend Data Unavailable{MegaStorage.normal}", 60))

def sortArray(factor):
    clearArray()
    sortError = False
    try:
        if factor=="volume":
            for count in range(0, MegaStorage.numberOfCompanies):
                if not MegaStorage.Sector[count]=="Promoter Share" and not MegaStorage.Sector[count]=="Mutual Fund" and not MegaStorage.Sector[count]=="Corporate Debentures":
                    try:
                        MegaStorage.arr2.append(float(MegaStorage.shareVolume[count]))
                    except: pass
                    MegaStorage.arr3.append(count)
        elif factor=="gainer":
            for count in range(0, MegaStorage.numberOfCompanies):
                if MegaStorage.PercentageChange[count]>0 and not MegaStorage.Sector[count]=="Promoter Share" and not MegaStorage.Sector[count]=="Mutual Fund" and not MegaStorage.Sector[count]=="Corporate Debentures":
                    try:
                        MegaStorage.arr2.append(float(MegaStorage.PercentageChange[count]))
                    except: pass
                    MegaStorage.arr3.append(count)
        elif factor=="loser":
            for count in range(0, MegaStorage.numberOfCompanies):
                if MegaStorage.PercentageChange[count]<0 and not MegaStorage.Sector[count]=="Promoter Share" and not MegaStorage.Sector[count]=="Mutual Fund" and not MegaStorage.Sector[count]=="Corporate Debentures":
                    try:
                        MegaStorage.arr2.append(float(MegaStorage.PercentageChange[count]))
                    except: pass
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
        print(f"{MegaStorage.red}\t\t[ Error ] :" + center(f"Unable To Sort Data{MegaStorage.normal}", 60))
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
                print(f"{MegaStorage.red}\t\t[ Error ] :" + center(f"Company data could not be loaded ({MegaStorage.Symbol[index]}){MegaStorage.normal}", 60))
                print("\t-------------------------------------------------------------------------------------------------------------------")
                programExit()

def summaryReport():
    try:
        numOfComToDisplay = 20
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
            lengthOfLoser = len(loserArr)
            lengthOfGainer = len(gainerArr)
            lengthOfVolume = len(volumeArr)
            print("\n\t===================================================================================================================")
            print(f"{MegaStorage.bold}\t\t{arr[2].ljust(19)}{arr[3]}\t|\t{arr[0].ljust(19)}{arr[1]}\t|\t{arr[4].ljust(19)}{arr[3]}{MegaStorage.normal}")
            print("\t===================================================================================================================\n")
            for index in range(0, numOfComToDisplay):
                if index < lengthOfVolume:
                    volumeSymbol = str(MegaStorage.Symbol[volumeArr[index]])
                    volume = str(MegaStorage.shareVolume[volumeArr[index]])
                else:
                    volumeSymbol = ""
                    volume = ""
                if index < lengthOfGainer:
                    gainerSymbol = str(MegaStorage.Symbol[gainerArr[index]])
                    gainer = f"{MegaStorage.green}" + str(MegaStorage.PercentageChange[gainerArr[index]]).ljust(5) + f"{MegaStorage.normal}" + " %"
                else:
                    gainerSymbol = ""
                    gainer = "".ljust(5)
                if index < lengthOfLoser:
                    loserSymbol = str(MegaStorage.Symbol[loserArr[index]])
                    loser = f"{MegaStorage.red}" + str(MegaStorage.PercentageChange[loserArr[index]]).ljust(6) + f"{MegaStorage.normal}" + " %"
                else:
                    loserSymbol = ""
                    loser = "".ljust(5)
                print(f"\t\t{gainerSymbol.ljust(19)}{gainer}\t|\t{volumeSymbol.ljust(19)}{volume}\t|\t{loserSymbol.ljust(18)}{loser}")
            print("")
    except:
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print(f"{MegaStorage.red}\t\t[ Error ] :" + center(f"Unable To Generate Market Summary{MegaStorage.normal}", 60))

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
    bodyRatio =  bodyToCandleRatio()
    ratio1 = 0
    ratio2 = 0
    if bodyRatio<55:
        if len(MegaStorage.companyVolume)>=2 and not candleLength==0:
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
    return hammerResult

def bullishBearishHarami():
    bullishBearishHaramiResult = "NULL"
    if len(MegaStorage.companyVolume)>1:
        if (MegaStorage.companyOpenPrice[1]-MegaStorage.companyPrice[0])>0 and (MegaStorage.companyOpenPrice[0]-MegaStorage.companyPrice[1])>0:
            if MegaStorage.companyPrice[0]>=(((MegaStorage.companyOpenPrice[1]-MegaStorage.companyPrice[1])/2)+MegaStorage.companyPrice[1]):
                bullishBearishHaramiResult = "BullishHarami"
        elif (MegaStorage.companyPrice[1]-MegaStorage.companyOpenPrice[0])>0 and (MegaStorage.companyPrice[0]-MegaStorage.companyOpenPrice[1])>0:
            if (((MegaStorage.companyPrice[1]-MegaStorage.companyOpenPrice[1])/2)+MegaStorage.companyOpenPrice[1])>MegaStorage.companyPrice[0]:
                bullishBearishHaramiResult = "BearishHarami"
    return bullishBearishHaramiResult

def engulfingBullishBearish():
    engulfingResult = "NULL"
    if len(MegaStorage.companyVolume)>1:
        if MegaStorage.companyPrice[0]>MegaStorage.companyPrice[1] and MegaStorage.companyPrice[0]>MegaStorage.companyOpenPrice[1]:
            if MegaStorage.companyOpenPrice[0]<MegaStorage.companyOpenPrice[1] and MegaStorage.companyOpenPrice[0]<MegaStorage.companyPrice[1]:
                engulfingResult = "EngulfingBullish"
        elif MegaStorage.companyOpenPrice[0]>MegaStorage.companyPrice[1] and MegaStorage.companyOpenPrice[0]>MegaStorage.companyOpenPrice[1]:
            if MegaStorage.companyPrice[0]<MegaStorage.companyPrice[1] and MegaStorage.companyPrice[0]<MegaStorage.companyOpenPrice[1]:
                engulfingResult = "EngulfingBearish"
    return engulfingResult

def morningEveningDojiStar():
    dojiStarResult = "NULL"
    if len(MegaStorage.companyVolume)>2:
        if (MegaStorage.companyPrice[2]-MegaStorage.companyPrice[1])>0 and (MegaStorage.companyPrice[1]-MegaStorage.companyPrice[0])<0:
            dojiStarResult = "MorningDojiStar"
        elif (MegaStorage.companyPrice[1]-MegaStorage.companyPrice[2])>0 and (MegaStorage.companyPrice[0]-MegaStorage.companyPrice[1])>0:
            dojiStarResult = "EveningDojiStar"
    return dojiStarResult

def morningEveningStar():
    starResult = "NULL"
    if len(MegaStorage.companyVolume)>2:
        if (MegaStorage.companyPrice[2]-MegaStorage.companyPrice[1])>0 and (MegaStorage.companyPrice[1]-MegaStorage.companyPrice[0])<0:
            starResult = "MorningStar"
        elif (MegaStorage.companyPrice[1]-MegaStorage.companyPrice[2])>0 and (MegaStorage.companyPrice[0]-MegaStorage.companyPrice[1])>0:
            starResult = "EveningStar"
    return starResult

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
    dojiLength = 0.8
    if abs(((MegaStorage.companyOpenPrice[0]-MegaStorage.companyPrice[0])/MegaStorage.companyPrice[0])*100)<=dojiLength:
        if dragonfly(dojiLength)==True:
            dojiResult = "DragonFly"
        elif gravestone(dojiLength)==True:
            dojiResult = "GraveStone"
        else:
            if morningEveningDojiStar()=="MorningDojiStar":
                dojiResult = "MorningDojiStar"
            elif morningEveningDojiStar()=="EveningDojiStar":
                dojiResult = "EveningDojiStar"
            else:
                dojiResult = "Doji"
    return dojiResult

def threeBlackCrowsAndWhiteSoldiers():
    result = "NULL"
    minRatio = 55
    if len(MegaStorage.companyVolume)>=3:
        candleLength = MegaStorage.companyHighPrice[2] - MegaStorage.companyLowPrice[2]
        bodyLength = abs(MegaStorage.companyOpenPrice[2] - MegaStorage.companyPrice[2])
        try: bodyRatio = (bodyLength/candleLength)*100
        except: bodyRatio = 0
        if MegaStorage.companyOpenPrice[2]>MegaStorage.companyPrice[2] and bodyRatio>minRatio:
            candleLength = MegaStorage.companyHighPrice[1] - MegaStorage.companyLowPrice[1]
            bodyLength = abs(MegaStorage.companyOpenPrice[1] - MegaStorage.companyPrice[1])
            try: bodyRatio = (bodyLength/candleLength)*100
            except: bodyRatio = 0
            if MegaStorage.companyOpenPrice[1]>MegaStorage.companyPrice[1] and MegaStorage.companyPrice[2]>MegaStorage.companyPrice[1] and bodyRatio>minRatio:
                candleLength = MegaStorage.companyHighPrice[0] - MegaStorage.companyLowPrice[0]
                bodyLength = abs(MegaStorage.companyOpenPrice[0] - MegaStorage.companyPrice[0])
                try: bodyRatio = (bodyLength/candleLength)*100
                except: bodyRatio = 0
                if MegaStorage.companyOpenPrice[0]>MegaStorage.companyPrice[0] and MegaStorage.companyPrice[1]>MegaStorage.companyPrice[0] and bodyRatio>minRatio:
                    result = "ThreeBlackCrows"
        
        elif MegaStorage.companyOpenPrice[2]<MegaStorage.companyPrice[2] and bodyRatio>minRatio:
            candleLength = MegaStorage.companyHighPrice[1] - MegaStorage.companyLowPrice[1]
            bodyLength = abs(MegaStorage.companyOpenPrice[1] - MegaStorage.companyPrice[1])
            try: bodyRatio = (bodyLength/candleLength)*100
            except: bodyRatio = 0
            if MegaStorage.companyOpenPrice[1]<MegaStorage.companyPrice[1] and MegaStorage.companyPrice[2]<MegaStorage.companyPrice[1] and bodyRatio>minRatio:
                candleLength = MegaStorage.companyHighPrice[0] - MegaStorage.companyLowPrice[0]
                bodyLength = abs(MegaStorage.companyOpenPrice[0] - MegaStorage.companyPrice[0])
                try: bodyRatio = (bodyLength/candleLength)*100
                except: bodyRatio = 0
                if MegaStorage.companyOpenPrice[0]<MegaStorage.companyPrice[0] and MegaStorage.companyPrice[1]<MegaStorage.companyPrice[0] and bodyRatio>minRatio:
                    result = "ThreeWhiteSoldiers"
        
    return result

def projectileSummary(bullPer, bearPer, indecisivePer):
    if bullPer>bearPer and bullPer>indecisivePer:
        calPer = bullPer - bearPer - indecisivePer
        if calPer>34:
            str = "Strong Bullish Sentiment ( NEPSE >= 1 % (Green Marubozu))"
        elif calPer>21:
            str = "Bullish Sentiment ( NEPSE >= 0.5 % (Green Hammer))"
        elif calPer>13:
            str = "Slightly Bullish Sentiment ( ~ NEPSE ~ (Green Doji))"
        else:
            str = "Indecisive ( ~ NEPSE ~ (Sideways))"
    elif bearPer>bullPer and bearPer>indecisivePer:
        calPer = bearPer - bullPer - indecisivePer
        if calPer>34:
            str =  "Strong Bearish Sentiment ( NEPSE >= 1 % (Red Marubozu))"
        elif calPer>21:
            str = "Bearish Sentiment ( NEPSE >= 0.5 % (Red Hammer))"
        elif calPer>13:
            str = "Slightly Bearish Sentiment ( ~ NEPSE ~ (Red Doji))"
        else:
            str = "Indecisive ( ~ NEPSE ~ (Sideways))"
    else:
        str = "Indecisive ( ~ NEPSE ~ (Sideways))"
    return str

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
            MegaStorage.trend.append(f"{MegaStorage.yellow}Indecisive{MegaStorage.normal}")
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
            MegaStorage.trend.append(f"{MegaStorage.green}Bullish{MegaStorage.normal}")
        elif bearCount>bullCount:
            MegaStorage.trend.append(f"{MegaStorage.red}Bearish{MegaStorage.normal}")
        MegaStorage.symbol.append(MegaStorage.Symbol[index])

def generateAutomatedReport(disFilter):
    arr = []
    volumeArr = []
    clearReportArrayStorage()
    # Patterns: Hammer, Doji, MorningStar, EveningStar, DragonFly, GraveStone, EngulfingBullish, EngulfingBearish, ThreeBlackCrows, ThreeWhiteSoldier
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
            haramiResult = bullishBearishHarami()
            starResult = morningEveningStar()
            engulfingResult = engulfingBullishBearish()
            threeBlackCrowsWhiteSoldiersResult = threeBlackCrowsAndWhiteSoldiers()
            # gap = float("{:.2f}".format(gapOpen()))
            buy = float("{:.2f}".format(buyPressure()))
            sell = float("{:.2f}".format(sellPressure()))
            volume = float("{:.2f}".format(volumeAnalysis()))
            try:
                # Volume Analysis
                if volume>=100:
                    volumeArr.append(MegaStorage.yellow + (str(volume) + " %").ljust(17) + MegaStorage.normal)
                    # Trading Pressure Analysis as per Volume Confirmation
                    if (buy*0.8)>=sell:
                        bullCount += 1
                        arr.append("BuyPressure")
                    elif (sell*0.8)>=buy:
                        bearCount += 1
                        arr.append("SellPressure")

                else:
                    volumeArr.append((str(volume) + " %").ljust(17))
                    
                # Doji Analysis
                if not dojiResult=="NULL":
                    if dojiResult=="DragonFly":
                        bullCount += 1
                    elif dojiResult=="GraveStone":
                        bearCount += 1
                    elif dojiResult=="MorningDojiStar":
                        bullCount += 1
                    elif dojiResult=="EveningDojiStar":
                        bearCount += 1
                    elif dojiResult=="Doji":
                        if len(MegaStorage.companyVolume)>=2:
                            if MegaStorage.companyPrice[2]<MegaStorage.companyPrice[1]:
                                bearCount += 1
                            elif MegaStorage.companyPrice[2]>MegaStorage.companyPrice[1]:
                                bullCount += 1
                    elif dojiResult=="Doji": pass
                    arr.append(dojiResult)
                
                else:
                    # Morning Star and Evening Star
                    if not starResult=="NULL":
                        if starResult=="MorningStar":
                            bullCount += 1
                        elif starResult=="EveningStar":
                            bearCount += 1
                        arr.append(starResult)
                
                # Hammer Analysis
                if not hammerResult=="NULL":
                    if len(MegaStorage.companyVolume)>2:
                        if MegaStorage.companyPrice[2]<MegaStorage.companyPrice[1] and hammerResult=="InvertedHammer":
                            bearCount += 1
                        elif MegaStorage.companyPrice[2]>MegaStorage.companyPrice[1] and hammerResult=="Hammer":
                            bullCount += 1
                    arr.append(hammerResult)

                # Harami Analysis
                if not haramiResult=="NULL":
                    if haramiResult=="BullishHarami":
                        bullCount += 1
                        arr.append("BullishHarami")
                    elif haramiResult=="BearishHarami":
                        bearCount += 1
                        arr.append("BearishHarami")

                # Engulfing Bullish Bearish
                if not engulfingResult=="NULL":
                    if engulfingResult=="EngulfingBullish":
                        bullCount += 1
                    elif engulfingResult=="EngulfingBearish":
                        bearCount += 1
                    arr.append(engulfingResult)

                # Three Black Crows and Three White Soldiers
                if not threeBlackCrowsWhiteSoldiersResult=="NULL":
                    if threeBlackCrowsWhiteSoldiersResult=="ThreeWhiteSoldiers":
                        bullCount += 1
                    elif threeBlackCrowsWhiteSoldiersResult=="ThreeBlackCrows":
                        bearCount += 1
                    arr.append(threeBlackCrowsWhiteSoldiersResult)
                
                # Dividend Analysis
                for count in range(0, len(MegaStorage.divSymbol)):
                    if str(MegaStorage.Symbol[index]).find(MegaStorage.divSymbol[count])>=0:
                        arr.append(f"{MegaStorage.yellow}Dividend{MegaStorage.normal}")
                        # bullCount += 1
                        # arr.append("Dividend")
            except:
                errorFlag = True
            finally:
                if errorFlag==False:
                    arr.reverse()
                    appendReportData(index, bullCount, bearCount, arr)
                arr.clear()
    sizeArr = len(MegaStorage.symbol)
    if sizeArr>0:
        title0 = [f"{MegaStorage.green}Bullish{MegaStorage.normal}", f"{MegaStorage.red}Bearish{MegaStorage.normal}", f"{MegaStorage.yellow}Indecisive{MegaStorage.normal}"]
        title1 = ["Symbol", "Bull-Bear", "Trend", "Volume", "Check Points"]
        title2 = ["Data Date", "Bull Count", "Bear Count", "Indecisive Count", "Clueless Count", "Bull Percentage", "Bear Percentage", "Indecisive Percentage", "Clueless Percentage", "Projectile Status"]
        print("\n\t===================================================================================================================")
        if disFilter=="NULL":
            print(center(f"{MegaStorage.bold}SUMMARY OF REPORT{MegaStorage.normal}", 116))
        elif disFilter=="SECTOR":
            print(center(f"{MegaStorage.bold}SECTOR REPORT{MegaStorage.normal}", 116))
        else:
            print(f"{MegaStorage.bold}\t\t{title1[0].ljust(13)}{title1[1].ljust(17)}{title1[2].ljust(16)}{title1[3].ljust(17)}{title1[4]}{MegaStorage.normal}")
        print("\t===================================================================================================================\n")
        if disFilter=="NULL":
            space = " "
            bullTotal = 0
            bearTotal = 0
            indecisiveTotal = 0
            for i in range(0, sizeArr):
                if MegaStorage.bullPoint[i]>MegaStorage.bearPoint[i]:
                    bullTotal = bullTotal + 1
                elif MegaStorage.bullPoint[i]<MegaStorage.bearPoint[i]:
                    bearTotal = bearTotal + 1
                else:
                    indecisiveTotal = indecisiveTotal + 1
            cluelessTotal = MegaStorage.numberOfCompanies - bullTotal - bearTotal - indecisiveTotal
            if bullTotal==0 and bearTotal==0:
                print(f"{MegaStorage.yellow}\t\t[ Message ] :" + {center(f"Unable to generate report (Pattern Uncertainity){MegaStorage.normal}", 60)})
            else:
                bullPer = (bullTotal / MegaStorage.numberOfCompanies)*100
                bearPer = (bearTotal/MegaStorage.numberOfCompanies)*100
                indecisivePer = (indecisiveTotal/MegaStorage.numberOfCompanies)*100
                print(f"\t\t{title2[0].ljust(23)}:{space.ljust(3)}{MegaStorage.dataAsOf}")
                print(f"\t\t{title2[1].ljust(23)}:{space.ljust(3)}{MegaStorage.green}{bullTotal}{MegaStorage.normal}")
                print(f"\t\t{title2[2].ljust(23)}:{space.ljust(3)}{MegaStorage.red}{bearTotal}{MegaStorage.normal}")
                print(f"\t\t{title2[3].ljust(23)}:{space.ljust(3)}{MegaStorage.yellow}{indecisiveTotal}{MegaStorage.normal}")
                print(f"\t\t{title2[4].ljust(23)}:{space.ljust(3)}{MegaStorage.yellow}{cluelessTotal}{MegaStorage.normal}")
                print(f"\t\t{title2[5].ljust(23)}:{space.ljust(3)}{MegaStorage.green}" + str("{:.2f}".format(bullPer)) + f"{MegaStorage.normal} %")
                print(f"\t\t{title2[6].ljust(23)}:{space.ljust(3)}{MegaStorage.red}" + str("{:.2f}".format(bearPer)) + f"{MegaStorage.normal} %")
                print(f"\t\t{title2[7].ljust(23)}:{space.ljust(3)}{MegaStorage.yellow}" + str("{:.2f}".format(indecisivePer)) + f"{MegaStorage.normal} %")
                print(f"\t\t{title2[8].ljust(23)}:{space.ljust(3)}{MegaStorage.yellow}" + str("{:.2f}".format((cluelessTotal/MegaStorage.numberOfCompanies)*100)) + f"{MegaStorage.normal} %")
                print(f"\t\t{title2[9].ljust(23)}:{space.ljust(3)}{projectileSummary(bullPer, bearPer, indecisivePer)}")
            print("")
        elif disFilter=="SECTOR":
            space = " "
            sectorBullPoint = []
            sectorBearPoint = []
            sectorIndecisivePoint = []
            sectorTotalCompanyCount = []
            for i in range(0, len(MegaStorage.SectorList2)):
                sectorBullPoint.append(0)
                sectorBearPoint.append(0)
                sectorIndecisivePoint.append(0)
                sectorTotalCompanyCount.append(0)
            for i in range(0, sizeArr):
                for j in range(0, len(MegaStorage.SectorList2)-1):
                    if MegaStorage.Sector[i]==MegaStorage.SectorList2[j]:
                        sectorTotalCompanyCount[j] += 1
                        if MegaStorage.bullPoint[i]>MegaStorage.bearPoint[i]:
                            sectorBullPoint[j] += 1
                        elif MegaStorage.bullPoint[i]<MegaStorage.bearPoint[i]:
                            sectorBearPoint[j] += 1
                        else:
                            sectorIndecisivePoint[j] += 1
                        break
            for i in range(0, len(MegaStorage.SectorList2)-1):
                try:
                    sectorBearPer = (sectorBearPoint[i]/sectorTotalCompanyCount[i])*100
                except:
                    sectorBearPer = 0
                try:
                    sectorBullPer = (sectorBullPoint[i]/sectorTotalCompanyCount[i])*100
                except:
                    sectorBullPer = 0
                try:
                    sectorIndecisivePer = f"{MegaStorage.yellow}" + "{:.2f}".format(100.00-sectorBullPer-sectorBearPer) + f"{MegaStorage.normal}"
                except:
                    sectorIndecisivePer = f"{MegaStorage.yellow}" + "{:.2f}".format(0) + f"{MegaStorage.normal}"
                try:
                    sectorBearPer = f"{MegaStorage.red}" + "{:.2f}".format((sectorBearPoint[i]/sectorTotalCompanyCount[i])*100) + f"{MegaStorage.normal}"
                except:
                    sectorBearPer = f"{MegaStorage.red}" + "{:.2f}".format(0) + f"{MegaStorage.normal}"
                try:
                    sectorBullPer = f"{MegaStorage.green}" + "{:.2f}".format((sectorBullPoint[i]/sectorTotalCompanyCount[i])*100) + f"{MegaStorage.normal}"
                except:
                    sectorBullPer = f"{MegaStorage.green}" + "{:.2f}".format(0) + f"{MegaStorage.normal}"
                if sectorBullPoint[i]>sectorBearPoint[i]:
                    print(f"\t\t{MegaStorage.SectorList2[i].ljust(29)}: {title0[0].ljust(21)}{space.ljust(7)}[ {sectorBullPer.ljust(16)}% | {sectorBearPer.ljust(16)}% | {sectorIndecisivePer.ljust(16)}% ]{space.ljust(7)}[ {MegaStorage.green}{str(sectorBullPoint[i]).ljust(2)}{MegaStorage.normal} | {MegaStorage.red}{str(sectorBearPoint[i]).ljust(2)}{MegaStorage.normal} | {MegaStorage.yellow}{str(sectorIndecisivePoint[i]).ljust(2)}{MegaStorage.normal} ]")
                elif sectorBearPoint[i]>sectorBullPoint[i]:
                    print(f"\t\t{MegaStorage.SectorList2[i].ljust(29)}: {title0[1].ljust(21)}{space.ljust(7)}[ {sectorBearPer.ljust(16)}% | {sectorBullPer.ljust(16)}% | {sectorIndecisivePer.ljust(16)}% ]{space.ljust(7)}[ {MegaStorage.red}{str(sectorBearPoint[i]).ljust(2)}{MegaStorage.normal} | {MegaStorage.green}{str(sectorBullPoint[i]).ljust(2)}{MegaStorage.normal} | {MegaStorage.yellow}{str(sectorIndecisivePoint[i]).ljust(2)}{MegaStorage.normal} ]")
                else:
                    print(f"\t\t{MegaStorage.SectorList2[i].ljust(29)}: {title0[2].ljust(21)}{space.ljust(7)}[ {sectorIndecisivePer.ljust(16)}% | {sectorBullPer.ljust(16)}% | {sectorBearPer.ljust(16)}% ]{space.ljust(7)}[ {MegaStorage.yellow}{str(sectorIndecisivePoint[i]).ljust(2)}{MegaStorage.normal} | {MegaStorage.green}{str(sectorBullPoint[i]).ljust(2)}{MegaStorage.normal} | {MegaStorage.red}{str(sectorBearPoint[i]).ljust(2)}{MegaStorage.normal} ]")
            print("")
        else:
            for index in range(0, sizeArr):
                if MegaStorage.bullPoint[index]>0 or MegaStorage.bearPoint[index]>0:
                    if disFilter=="BULL":
                        if str(MegaStorage.trend[index]).find("Bullish")>=0:
                            print(f"\t\t{str(MegaStorage.symbol[index]).ljust(15)}{str(MegaStorage.bullPoint[index])} - {str(MegaStorage.bearPoint[index]).ljust(11)}{MegaStorage.green}{str(MegaStorage.trend[index]).ljust(25)}{MegaStorage.normal}{volumeArr[index]}{str(MegaStorage.remarks[index])}")
                    elif disFilter=="BEAR":
                        if str(MegaStorage.trend[index]).find("Bearish")>=0:
                            print(f"\t\t{str(MegaStorage.symbol[index]).ljust(15)}{str(MegaStorage.bullPoint[index])} - {str(MegaStorage.bearPoint[index]).ljust(11)}{MegaStorage.red}{str(MegaStorage.trend[index]).ljust(25)}{MegaStorage.normal}{volumeArr[index]}{str(MegaStorage.remarks[index])}")
                    elif disFilter=="DETAIL":
                        print(f"\t\t{str(MegaStorage.symbol[index]).ljust(15)}{str(MegaStorage.bullPoint[index])} - {str(MegaStorage.bearPoint[index]).ljust(11)}{str(MegaStorage.trend[index]).ljust(25)}{volumeArr[index]}{str(MegaStorage.remarks[index])}")
            print("")
    else:
        print("\n\t-------------------------------------------------------------------------------------------------------------------")
        print(f"{MegaStorage.yellow}\t\t[ Message ] :" + {center(f"Unable to generate report (Pattern Uncertainity){MegaStorage.normal}", 60)})

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
    print(center(f"{MegaStorage.bold}{MegaStorage.Name[index]}{MegaStorage.normal}", 116))
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
    print(center(f"{MegaStorage.red}{MegaStorage.bold}Program Termination{MegaStorage.normal}", 121))
    print("\t===================================================================================================================\n\n")
    sleep(1)
    sys.exit()
