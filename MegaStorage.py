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

# Name, Symbol, Sector
UpdatedSymbol = []
Symbol = []
Name = []
Sector = []
SectorList1 = [
    "commercialbank", "developmentbank", "finance", "hydropower", "lifeinsurance", "nonlifeinsurance", 
    "microfinance", "mutualfund", "investment", "manufacturingandproducts", "hotelandtourism",
    "trading", "other", "all"
]
SectorList2 = [
    "Commercial Bank", "Development Bank", "Finance", "Hydropower", "Life Insurance", "Non-Life Insurance", 
    "Microfinance", "Mutual Fund", "Investment", "Manufacturing and Products", "Hotel & Tourism",
    "Trading", "Others", "All"
]