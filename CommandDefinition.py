import MegaStorage
import Functions

def menuDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tMenu shows available commands and functions for manipulating and displaying different aspects of data.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: menu\n")

def newsDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tNews brings you the latest news by searching web.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: news\n")

def extractDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tExtract gets data from web and saves it which is then used by the program to display appropriate results.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: extract\n")

def companyDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tCompany shows details about a particular company.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: company")
    print("\t\tStock Analyzer> Company: upper\n")

def comparedef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tCompare allows user to compare between different aspects of any two companies of any sector.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: compare")
    print("\t\tStock Analyzer> Company Symbol [1]: upper")
    print("\t\tStock Analyzer> Company Symbol [2]: radhi\n")

def sortDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tSort displays data of selected sector with respect to the selected factor in a particular order.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: sort")
    print("\t\tStock Analyzer> Factor: price")
    print("\t\tStock Analyzer> Sector: hydropower\n")

def rangeDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tRange selects company within the given range of selected factor and sector.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: range")
    print("\t\tStock Analyzer> Sector: finance")
    print("\t\tStock Analyzer> Factor: eps")
    print("\t\tStock Analyzer> Factor> Enter lower limit [Factor]: 20")
    print("\t\tStock Analyzer> Factor> Enter upper limit [Factor]: 30\n")

def sectorDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tSector genertaes today's market sub indices performance.\n")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: sector")
    print("\t\tStock Analyzer> Sector: commercial bank\n")

def reportDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tReport generates share report based on candle stick pattern and predicts future outcome.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: report\n")

def technicalDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tTechnical generates technical report regarding various technical aspects of mentioned stock.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: technical")
    print("\t\tStock Analyzer> Company: upper\n")

def dividendDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tDividend shows stocks that have declared or proposed cash or/and share dividend.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: dividend\n")

def summaryDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tSummary gives an overview of the market considering volume and price of stocks.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: summary\n")

def resetDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tReset deletes all the existing files and then creates brand new files (not recommended).")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: reset\n")

def exitDef():
    Functions.lineMaker("-", "\n\t", 116, "\n")
    print(f"{MegaStorage.bold}\t\tDescription:{MegaStorage.normal}")
    print("\t\tExit terminates all ongoing program processes and then closes the program.")
    print(f"{MegaStorage.bold}\n\t\tFormat:{MegaStorage.normal}")
    print("\t\tStock Analyzer: exit\n")
