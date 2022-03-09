# Variable for First Phase Data Extraction
OutStandingShare = []
MarketPrice = []
PercentageChange = []
Avg120Day = []
OneYearYield = []
Eps = []
PERatio = [] 
BookValue = [] 
Pbv = [] 
AvgVol30Day = [] 
MarketCapitalisation = []

# Variables for News
News = []
NewsDate = []
NewsSymbol = []

# Variable for Sort Function
arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
arr6 = []
arr7 = []

# Variable for dividend proposal
divBCD = []
divCash = []
divBonus = []
divSymbol = []

# Variable for Second Phase Data Extraction
shareDataAsOf = []
shareVolume = []
sharePrice = []
shareLowPrice = []
shareHighPrice = []
shareOpenPrice = []
share52WeeksHigh = []
share52WeeksLow = []

# Report Data
shareReportDate = []
shareReportValue = []
shareReportQuarter = []

# All Data of a Company
companyVolume = []
companyPrice = []
companyLowPrice = []
companyHighPrice = []
companyOpenPrice = []

# Report Array
symbol = []
trend = []
remarks = []
bullPoint = []
bearPoint = []

# Testing Variables
godMode = True
isTesting = False

# Predetermined Variable as well as Temporary Variables
Temporary = []
fileDate = "NULL"
dataAsOf = ""
username = ""
macAdd = ""
connectionError = False
numberOfCompanies = 0
barProgressCount = 1
bar = "____________________________________________________________________________________________________"

# Path Variable
fileExtension = '.txt'
fileName0 = 'data/'
fileName1 = 'data1/'
fileName2 = 'data2/'
fileName3 = 'data3/'
fileName4 = 'data4/'

# Print Style
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
normal = '\033[0m'
bold = '\033[97m'

# Name, Symbol, Sector
UpdatedSymbol = []
Symbol = []
Name = []
Sector = []
SectorList1 = [
    "other", "finance", "trading", "hydropower", "investment", "mutualfund", "microfinance", "lifeinsurance", "commercialbank", "hotelandtourism", 
    "developmentbank", "nonlifeinsurance", "manufacturingandproducts", "all"
]
SectorList2 = [
    "Others", "Finance", "Trading", "Hydropower", "Investment", "Mutual Fund", "Microfinance", "Life Insurance", "Commercial Bank", "Hotel & Tourism", 
    "Development Bank", "Non-Life Insurance", "Manufacturing and Products", "All"
]