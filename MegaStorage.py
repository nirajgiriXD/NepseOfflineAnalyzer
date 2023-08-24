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

# Variable for dividend proposal
divSymbol = []
divBCD = []
divCash = []
divBonus = []

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

# Predetermined Variable as well as Temporary Variables
Temporary = []
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
    "finance", "microfinance", "commercialbank", "developmentbank", "lifeinsurance", "nonlifeinsurance", "hydropower",
    "investment", "mutualfund", "hotelandtourism", "manufacturingandproducts",
    "trading", "other", "all"
]
SectorList2 = [
    "Finance", "Microfinance", "Commercial Bank", "Development Bank", "Life Insurance", "Non-Life Insurance", "Hydropower",
    "Investment", "Mutual Fund", "Hotel & Tourism", "Manufacturing and Products",
    "Trading", "Others", "All"
]