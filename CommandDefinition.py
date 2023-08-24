import MegaStorage

def menuDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tMenu shows available commands and functions for manipulating and displaying different aspects of data.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> menu\n")

def newsDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tNews brings you the latest news by searching web.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> news\n")

def extractDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tExtract gets data from web and saves it which is then used by the program to display appropriate results.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> extract\n")

def companyDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tCompany shows details about a particular company.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> company")
    print("\t\tCompany>        upper\n")

def comparedef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tCompare allows user to compare between different aspects of any two companies of any sector.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> compare")
    print("\t\tFirst Company Symbol>  upper")
    print("\t\tSecond Company Symbol> radhi\n")

def sortDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tSort displays data of selected sector with respect to the selected factor in a particular order.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> sort")
    print("\t\tFactor>         price")
    print("\t\tSector>         hydropower\n")

def rangeDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tRange selects company within the given range of selected factor and sector.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> range")
    print("\t\tSector>         finance")
    print("\t\tFactor>         eps")
    print("\t\tEnter lower limit [Factor] : 20")
    print("\t\tEnter upper limit [Factor] : 30\n")

def sectorDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tSector filters out other sector and display company data of particular sector mentioned by user.\n")
    print(f"{MegaStorage.bold}\t\tSectors:{MegaStorage.normal}")
    print("\t\t1. Commercial Bank")
    print("\t\t2. Development Bank")
    print("\t\t3. Finance")
    print("\t\t4. Hydro Power")
    print("\t\t5. Life Insurance")
    print("\t\t6. Non-Life Insurance")
    print("\t\t7. Microfinance")
    print("\t\t8. Mutual Fund")
    print("\t\t9. Investment")
    print("\t\t10. Manufacturing And Processing")
    print("\t\t11. Hotels And Tourism")
    print("\t\t12. Reinsurance")
    print("\t\t13. Tradings")
    print("\t\t14. Others")
    print("\t\t15. All")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> sector")
    print("\t\tSector>         commercial bank\n")

def fundamentalDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tFundamental generates fundamental report based on company's performance over time.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> fundamental\n")

def reportDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tReport generates share report based on candle stick pattern and predicts future outcome.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> report\n")

def technicalDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tTechnical generates technical report regarding various technical aspects of mentioned stock.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> technical")
    print("\t\tCompany>        upper\n")

def dividendDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tDividend shows stocks that have declared or proposed cash or/and share dividend.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> dividend\n")

def summaryDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tSummary gives an overview of the market considering volume and price of stocks.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> summary\n")

def indexDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tSummary gives an overview of the market considering volume and price of stocks.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> summary\n")

def resetDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tReset deletes all the existing files and then creates brand new files (not recommended).")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> reset\n")

def exitDef():
    print("\n\t-------------------------------------------------------------------------------------------------------------------\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tExit terminates all ongoing program processes and then closes the program.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer> exit\n")
