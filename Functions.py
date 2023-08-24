from time import sleep
import MegaStorage

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
    MegaStorage.barProgressCount1 = 1
    MegaStorage.barProgressCount2 = 1
    MegaStorage.bar = "____________________________________________________________________________________________________"

def clearReportDataStorage():
    MegaStorage.shareDataAsOf.clear()
    MegaStorage.shareVolume.clear()
    MegaStorage.sharePrice.clear()
    MegaStorage.shareLowPrice.clear()
    MegaStorage.shareHighPrice.clear()
    MegaStorage.shareOpenPrice.clear()
    MegaStorage.shareReportDate.clear()
    MegaStorage.share52WeeksHigh.clear()
    MegaStorage.share52WeeksLow.clear()
    MegaStorage.sharePivotPoint.clear()
    MegaStorage.shareMovingAnalysis1.clear()
    MegaStorage.shareMovingAnalysis2.clear()
    MegaStorage.shareMovingAnalysis3.clear()
    MegaStorage.shareResistanceLevel1.clear()
    MegaStorage.shareResistanceLevel2.clear()
    MegaStorage.shareResistanceLevel3.clear()
    MegaStorage.shareSupportLevel1.clear()
    MegaStorage.shareSupportLevel2.clear()
    MegaStorage.shareSupportLevel3.clear()
    MegaStorage.shareReportDate.clear()
    MegaStorage.shareReportValue.clear()
    MegaStorage.shareReportQuarter.clear()
    MegaStorage.Temporary.clear()
    MegaStorage.barProgressCount1 = 1
    MegaStorage.barProgressCount2 = 1
    MegaStorage.bar = "____________________________________________________________________________________________________"

def clearNewsDataStorage():
    MegaStorage.News.clear()
    MegaStorage.NewsDate.clear()
    MegaStorage.NewsSymbol.clear()
    MegaStorage.Temporary.clear()
    MegaStorage.barProgressCount1 = 1
    MegaStorage.barProgressCount2 = 1
    MegaStorage.bar = "____________________________________________________________________________________________________"

def center(str, length):
    blank = ""
    space = int((length - len(str))/2)
    if space<1:
        space = 1
    for index in range(0, space):
        blank = blank + " "
    return (blank + str)

def numberToWordConverter(num):
    num = float("{:.2f}".format(num))
    if int(num/1000000000)>0:
        num = num/1000000000
        word = " Billion"
    elif int(num/1000000)>0:
        num = num/1000000
        word = " Million"
    elif int(num/1000)>0:
        num = num/1000
        word = " Thousand"
    else:
        word = " "
    return str(num) + word

def progressIndicator1(index, total):
    progressIndicatorPercentage = "{:.2f}".format((index/total)*100)
    if float(progressIndicatorPercentage)>=MegaStorage.barProgressCount1:
        MegaStorage.barProgressCount1 = MegaStorage.barProgressCount1 + 1
        if float(progressIndicatorPercentage)>=MegaStorage.barProgressCount1:
            MegaStorage.barProgressCount1 = MegaStorage.barProgressCount1 + 1
            MegaStorage.bar = MegaStorage.bar.replace('_', '█', 1)
        MegaStorage.bar = MegaStorage.bar.replace('_', '█', 1)
    print(f"\t[ {progressIndicatorPercentage}% ] : {MegaStorage.bar}", end='\r')

def progressIndicator2(index, total):
    progressIndicatorPercentage = "{:.2f}".format((index/total)*100)
    if float(progressIndicatorPercentage)>=MegaStorage.barProgressCount2:
        MegaStorage.barProgressCount2 = MegaStorage.barProgressCount2 + 1
        if float(progressIndicatorPercentage)>=MegaStorage.barProgressCount2:
            MegaStorage.barProgressCount2 = MegaStorage.barProgressCount2 + 1
            MegaStorage.bar = MegaStorage.bar.replace('_', '█', 1)
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
    print("\t===================================================================================================================\n\n")
    print(f"\t\tSector = {MegaStorage.Sector[index]}")
    print(f"\t\tMarket Price = {MegaStorage.sharePrice[index]}")
    print(f"\t\tEPS = {MegaStorage.Eps[index]}")
    print(f"\t\tPBV = {MegaStorage.Pbv[index]}")
    print(f"\t\tPE Ratio = {MegaStorage.PERatio[index]}")
    print(f"\t\tBook Value = {MegaStorage.BookValue[index]}")
    print(f"\t\tOne year yield = {MegaStorage.OneYearYield[index]}")
    print(f"\t\t120 Day Average = {MegaStorage.Avg120Day[index]}")
    print(f"\t\t130 Day Average Volume = {MegaStorage.AvgVol130Day[index]}")
    print(f"\t\t52 Weeks High-Low = {MegaStorage.share52WeeksHigh[index]}-{MegaStorage.share52WeeksLow[index]}")
    print(f"\t\tOutstanding Shares = {MegaStorage.OutStandingShare[index]}")   
    print(f"\t\tMarket Capitalisation = {MegaStorage.MarketCapitalisation[index]}")
    if MegaStorage.shareReportValue[index]>0:
        print(f"\t\tReport (Q{int(MegaStorage.shareReportQuarter[index])} Profit) = {numberToWordConverter(MegaStorage.shareReportValue[index])}")
    elif MegaStorage.shareReportValue[index]<0:
        print(f"\t\tReport (Q{int(MegaStorage.shareReportQuarter[index])} Loss) = {numberToWordConverter(abs(MegaStorage.shareReportValue[index]))}")
    else:
        print("\t\tReport = NULL")
    print("")

def compareCompanies(index1, index2):
    factor = ""
    print("\n\t=======================================================================================================================================")
    print("\tFactors" + center(MegaStorage.Symbol[index1], 88) + center(MegaStorage.Symbol[index2], 88))
    print("\t=======================================================================================================================================\n\n")
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
    print(f"\t{factor.ljust(26)}\t{str(MegaStorage.AvgVol130Day[index1]).ljust(50)} {MegaStorage.AvgVol130Day[index2]}")
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

def movingAnalysisAvg(index):
    bullPoint = 0
    bearPoint = 0
    finalResult = ""
    if MegaStorage.shareMovingAnalysis1[index]=="BULLISH":
        bullPoint = bullPoint + 1
    elif MegaStorage.shareMovingAnalysis1[index]=="BEARISH":
        bearPoint = bearPoint - 1
    if MegaStorage.shareMovingAnalysis2[index]=="BULLISH":
        bullPoint = bullPoint + 1
    elif MegaStorage.shareMovingAnalysis2[index]=="BEARISH":
        bearPoint = bearPoint - 1
    if MegaStorage.shareMovingAnalysis3[index]=="BULLISH":
        bullPoint = bullPoint + 1
    elif MegaStorage.shareMovingAnalysis3[index]=="BEARISH":
        bearPoint = bearPoint - 1
    if bullPoint>bearPoint:
        finalResult = "BULLISH"
    else:
        finalResult = "BEARISH"
    return finalResult

def supportAvg(index):
    return (MegaStorage.shareSupportLevel1[index] + MegaStorage.shareSupportLevel2[index] + MegaStorage.shareSupportLevel3[index])/3

def resistanceAvg(index):
    return (MegaStorage.shareResistanceLevel1[index] + MegaStorage.shareResistanceLevel2[index] + MegaStorage.shareResistanceLevel3[index])/3

def generateSimpleCompanyReport(index):
    avgValue1 = movingAnalysisAvg(index)
    avgValue2 = "{:.2f}".format(float(supportAvg(index)))
    avgValue3 = "{:.2f}".format(float(resistanceAvg(index)))
    print("\n\t===================================================================================================================")
    print("\t\t\tMoving Analysis\t\t\t\tSupport Level\t\t\tResistance Level")
    print("\t===================================================================================================================\n\n")
    print(f"\t\t\t{MegaStorage.shareMovingAnalysis1[index]} (MA5)\t\t\t\t{MegaStorage.shareSupportLevel3[index]} (S1)\t\t\t{MegaStorage.shareResistanceLevel1[index]} (R1)")
    print(f"\t\t\t{MegaStorage.shareMovingAnalysis2[index]} (MA20)\t\t\t\t{MegaStorage.shareSupportLevel2[index]} (S2)\t\t\t{MegaStorage.shareResistanceLevel2[index]} (R2)")
    print(f"\t\t\t{MegaStorage.shareMovingAnalysis3[index]} (MA180)\t\t\t\t{MegaStorage.shareSupportLevel1[index]} (S3)\t\t\t{MegaStorage.shareResistanceLevel3[index]} (R3)")
    print("\n\t-------------------------------------------------------------------------------------------------------------------")
    print(f"\n\t\t\t{avgValue1}\t\t\t\t\t{avgValue2}\t\t\t\t{avgValue3}\n")

def generateAdvanceCompanyReport(index):
    pass

def oneDayPatternSeeker():
    pass

def inspectPeak(index):
    pricePercentOfHigh = ((MegaStorage.share52WeeksHigh[index] - MegaStorage.sharePrice[index])/MegaStorage.share52WeeksHigh[index])*100
    pricePercentOfLow = ((MegaStorage.sharePrice[index] - MegaStorage.share52WeeksLow[index])/MegaStorage.share52WeeksLow[index])*100
    if pricePercentOfHigh<5:
        pass
    elif pricePercentOfHigh>=5 and pricePercentOfHigh<=10:
        pass
    elif pricePercentOfLow:
        pass

def weeklyPatternSeeker():
    pass

def programExit():
    print("\n\t===================================================================================================================")
    print(center("Program Termination", 116))
    print("\t===================================================================================================================\n\n")
    sleep(3)
    quit()
