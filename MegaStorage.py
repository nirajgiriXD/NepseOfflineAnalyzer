OutStandingShare = []
MarketPrice = []
PercentageChange = []
Avg120Day = []
OneYearYield = []
Eps = []
PERatio = [] 
BookValue = [] 
Pbv = [] 
Dividend = []
Bonus = []
RightShare = []
AvgVol130Day = [] 
MarketCapitalisation = []

News = []
NewsDate = []
NewsSymbol = []

arr1 = []
arr2 = []
arr3 = []

shareDataAsOf = []
shareVolume = []
sharePrice = []
shareLowPrice = []
shareHighPrice = []
shareOpenPrice = []
share52WeeksHigh = []
share52WeeksLow = []
sharePivotPoint = []
shareMovingAnalysis1 = []
shareMovingAnalysis2 = []
shareMovingAnalysis3 = []
shareResistanceLevel1 = []
shareResistanceLevel2 = []
shareResistanceLevel3 = []
shareSupportLevel1 = []
shareSupportLevel2 = []
shareSupportLevel3 = []

shareReportDate = []
shareReportValue = []
shareReportQuarter = []

Temporary = []
dataAsOf = ""
connectionError = False
numberOfCompanies = 205
barProgressCount1 = 1
barProgressCount2 = 1
bar = "____________________________________________________________________________________________________"

fileExtension = '.txt'
fileName0 = 'data/'
fileName1 = 'data1/'
fileName2 = 'data2/'
fileName3 = 'data3/'

Symbol = [
    "ACLBSL", "ADBL", "AIL", "AKJCL", "API", "AKPL", "AHPC", "ALBSL", "ALICL", "BOKL",
    "BARUN", "BFC", "BBC", "BNT", "BPCL", "CFCL", "CCBL", "CGH", "CBBL", "CHL",
    "CHCL", "CZBIL", "CIT", "CMF1", "CMF2", "CBL", "CLBSL", "CORBL", "DDBL", "DHPL",
    "EBL", "EIC", "EDBL", "FMDBL", "FOWAD", "GMFBS", "GBBL", "GIC", "GHL", "GBIME",
    "GILB", "GIMES1", "GFCL", "GBLBS", "GRDBL", "GLH", "GMFIL", "GLBSL", "GLICL", "GUFL",
    "HDHPC", "HURJA", "HBL", "HDL", "HGI", "HPPL", "HIDCL", "ICFC", "IGI", "ILBS",
    "JFL", "JSLBB", "JOSHI", "JBBL", "JLI", "KMCDB", "KPCL", "KSBBL", "KRBL", "KKHC",
    "KLBSL", "KBL", "KEF", "LBL", "LEMF", "LLBS", "LUK", "LEC", "LICN", "LBBL",
    "LGIL", "MBL", "MLBL", "MLBSL", "MSLB", "MFIL", "MEGA", "MERO", "MMFDB", "MDB",
    "MLBBL", "MEN", "MHNL", "MNBBL", "MPFL", "NBF2", "NABIL", "NEF", "NABBC", "NHPC",
    "NLICL", "NMFBS", "NIL", "NBB", "NBL", "NCCB", "NTC", "NFS", "NHDL", "NIFRA",
    "NICL", "NIB", "NLIC", "NRIC", "SBI", "NLBBL", "NGPL", "NIBLPF", "NIBSF1", "NICBF",
    "NICA", "NICGF", "NICLBSL", "NUBL", "NLG", "NMB50", "NMB", "NMBHF1", "NMBMF", "NRN",
    "OHL", "PMHPL", "PPCL", "PFL", "PRVU", "PRIN", "PLI", "PIC", "PCBL", "PLIC",
    "PROFL", "PICL", "RADHI", "RRHP", "RBCL", "RHPL", "RLFL", "RLI", "RHPC", "RMDC",
    "RSDC", "RURU", "SABSL", "SDLBSL", "SIC", "STC", "SMATA", "SFCL", "SLBSL", "SKBBL",
    "SANIMA", "SAEF", "SGI", "SLCF", "SHPC", "SJCL", "SAPDBL", "SNLB", "SADBL", "SICL",
    "SHINE", "SSHL", "SHIVM", "SIFC", "SBL", "SEF", "SIL", "SIGS2", "SINDU", "SHEL",
    "SHL", "SCB", "SMFDB", "SRBL", "SFMF", "SMB", "SLICL", "SLBS", "SWBBL", "SMFBS",
    "SLBBL", "SPDL", "TRH", "UNL", "UNHPL", "UFL", "UMRH", "UIC", "UMHL", "UPCL",
    "USLB", "UPPER", "VLBS", "WOMI", "YHL"
]
Name = [
    "Aarambha Chautari Laghubitta Bittiya Sanstha Ltd",
    "Agriculture Development Bank Ltd",
    "AJOD Insurance Ltd",
    "Ankhu Khola Jalvidhyut Company Ltd",
    "Api Power Company Ltd",
    "Arun Kabeli Power Ltd",
    "Arun Valley Hydropower Development Co. Ltd",
    "Asha Laghubitta Bittiya Sanstha Ltd",
    "Asian Life Insurance Co. Ltd",
    "Bank of Kathmandu Ltd",
    "Barun Hydropower Co. Ltd",
    "Best Finance Company Ltd",
    "Bishal Bazar Company Ltd",
    "Bottlers Nepal (Terai) Ltd",
    "Butwal Power Company Ltd",
    "Central Finance Co. Ltd",
    "Century Commercial Bank Ltd",
    "Chandragiri Hills Ltd",
    "Chhimek Laghubitta Bittiya Sanstha Ltd",
    "Chhyangdi Hydropower Ltd",
    "Chilime Hydropower Company Ltd",
    "Citizen Bank International Ltd",
    "Citizen Investment Trust",
    "Citizens Mutual Fund -1",
    "Citizens Mutual Fund -2",
    "Civil Bank Ltd",
    "Civil Laghubitta Bittiya Sanstha Ltd",
    "Corporate Development Bank Ltd",
    "Deprosc Laghubitta Bittiya Sanstha Ltd",
    "Dibyashwori Hydropower Ltd",
    "Everest Bank Ltd",
    "Everest Insurance Co. Ltd",
    "Excel Development Bank Ltd",
    "First Micro Finance Laghubitta Bittiya Sanstha Ltd",
    "Forward Community Microfinance Bittiya Sanstha Ltd",
    "Ganapati Microfinance Bittiya Sanstha Ltd",
    "Garima Bikas Bank Ltd",
    "General Insurance Company Ltd",
    "Ghalemdi Hydro Ltd",
    "Global IME Bank Ltd",
    "Global IME Laghubitta Bittiya Sanstha Ltd",
    "Global IME Samunnat Scheme-1",
    "Goodwill Finance Co. Ltd",
    "Grameen Bikas Laghubitta Bittiya Sanstha Ltd",
    "Green Development Bank Ltd",
    "Greenlife Hydropower Ltd",
    "Guheshowori Merchant Bank & Finance Co. Ltd",
    "Gurans Laghubitta Bittiya Sanstha Ltd",
    "Gurans Life Insurance Company Ltd",
    "Gurkhas Finance Ltd",
    "Himal Dolakha Hydropower Company Ltd",
    "Himalaya Urja Bikas Company Ltd",
    "Himalayan Bank Ltd",
    "Himalayan Distillery Ltd",
    "Himalayan General Insurance Co. Ltd",
    "Himalayan Power Partner Ltd",
    "Hydorelectricity Investment and Development Company Ltd",
    "ICFC Finance Ltd",
    "IME General Insurance Ltd",
    "Infinity Laghubitta Bittiya Sanstha Ltd",
    "Janaki Finance Ltd",
    "Janautthan Samudayic Laghubitta Bikas Bank Ltd",
    "Joshi Hydropower Development Company Ltd",
    "Jyoti Bikas Bank Ltd",
    "Jyoti Life Insurance Company Ltd",
    "Kalika Laghubitta Bittiya Sanstha Ltd",
    "Kalika power Company Ltd",
    "Kamana Sewa Bikas Bank Ltd",
    "Karnali Development Bank Ltd",
    "Khanikhola Hydropower Co. Ltd",
    "Kisan Lagubitta Bittiya Sanstha Ltd",
    "Kumari Bank Ltd",
    "Kumari Equity Fund",
    "Laxmi Bank Ltd",
    "Laxmi Equity Fund",
    "Laxmi Laghubitta Bittiya Sanstha Ltd",
    "Laxmi unnati Kosh",
    "Liberty Energy Company Ltd",
    "Life Insurance Co. Nepal",
    "Lumbini Bikas Bank Ltd",
    "Lumbini General Insurance Co. Ltd",
    "Machhapuchchhre Bank Ltd",
    "Mahalaxmi Bikas Bank Ltd",
    "Mahila Laghubitta Bittiya Sanstha Ltd",
    "Mahuli Samudayik Laghubitta Bittiya Sanstha Ltd",
    "Manjushree Finance Ltd",
    "Mega Bank Nepal Ltd",
    "Meromicrofinance Laghubitta Bittiya Sanstha Ltd",
    "Mirmire Microfinance Development Bank Ltd",
    "Miteri Development Bank Ltd",
    "Mithila Laghubitta Bittiya Sanstha Ltd",
    "Mountain Energy Nepal Ltd",
    "Mountain Hydro Nepal Ltd",
    "Muktinath Bikas Bank Ltd",
    "Multipurpose Finance Company Ltd",
    "NABIL BALANCED FUND-2",
    "Nabil Bank Ltd",
    "Nabil Equity Fund",
    "Narayani Development Bank Ltd",
    "National Hydro Power Company Ltd",
    "National Life Insurance Co. Ltd",
    "National Microfinance Bittiya Sanstha Ltd",
    "Neco Insurance Co. Ltd",
    "Nepal Bangladesh Bank Ltd",
    "Nepal Bank Ltd",
    "Nepal Credit And Commercial Bank Ltd",
    "Nepal Doorsanchar Comapany Ltd",
    "Nepal Finance Ltd",
    "Nepal Hydro Developers Ltd",
    "Nepal Infrastructure Bank Ltd",
    "Nepal Insurance Co. Ltd",
    "Nepal Investment Bank Ltd",
    "Nepal Life Insurance Co. Ltd",
    "Nepal Re-Insurance Company Ltd",
    "Nepal SBI Bank Ltd",
    "Nerude Laghubita Bikas Bank Ltd",
    "Ngadi Group Power Ltd",
    "NIBL Pragati Fund",
    "NIBL Samriddhi Fund-1",
    "NIC Asia Balanced Fund",
    "NIC Asia Bank Ltd",
    "NIC Asia Growth Fund",
    "NIC Asia Laghubitta Biitiya Sanstha Ltd",
    "Nirdhan Utthan Laghubitta Bittiya Sanstha Ltd",
    "NLG Insurance Company Ltd",
    "NMB 50",
    "NMB Bank Ltd",
    "NMB Hybrid Fund L-1",
    "NMB Laghubitta Bittiya Sanstha Ltd",
    "NRN Infrastructure and Development Ltd",
    "Oriental Hotels Ltd",
    "Panchakanya Mai Hydropower Ltd",
    "Panchthar Power Company Ltd",
    "Pokhara Finance Ltd",
    "Prabhu Bank Ltd",
    "Prabhu Insurance Ltd",
    "Prabhu Life Insurance Ltd",
    "Premier Insurance Co. Ltd",
    "Prime Commercial Bank Ltd",
    "Prime Life Insurance Company Ltd",
    "ProgressiveFinance Ltd",
    "Prudential Insurance Co. Ltd",
    "Radhi Bidyut Company Ltd",
    "Rairang Hydropower Development Company Ltd",
    "Rastriya Beema Company Ltd",
    "Rasuwagadhi Hydropower Company Ltd",
    "Reliance Finance Ltd",
    "Reliance Life Insurance Company Ltd",
    "Ridi Hydropower Development Company Ltd",
    "RMDC Laghubitta Bittiya Sanstha Ltd",
    "RSDC Laghubitta Bittiya Sanstha Ltd",
    "Ru Ru Jalbidhyut Pariyojana Ltd",
    "Sabaiko Laghubitta Bittiya Sanstha Ltd",
    "Sadhana Laghubitta Bittiya Sanstha Ltd",
    "Sagarmatha Insurance Co. Ltd",
    "Salt Trading Corporation",
    "Samata Gharelu Laghubitta Bittiya Sanstha Ltd",
    "Samriddhi Finance Company Ltd",
    "Samudayik Laghubitta Bittiya Sanstha Ltd",
    "Sana Kisan Bikas Laghubitta Bittiya sanstha Ltd",
    "Sanima Bank Ltd",
    "Sanima Equity Fund",
    "Sanima General Insurance Company Ltd",
    "Sanima Large Cap Fund",
    "Sanima Mai Hydropower Ltd",
    "Sanjen Jalavidhyut Company Ltd",
    "Saptakoshi Development Bank Ltd",
    "Sarathi Nepal Laghubitta Bittiya Sanstha Ltd",
    "Shangrila Development Bank Ltd",
    "Shikhar Insurance Co. Ltd",
    "Shine Resunga Development Bank Ltd",
    "Shiva Shree Hydropower Ltd",
    "Shivam Cements Ltd",
    "Shree Investment Finance Co. Ltd",
    "Siddhartha Bank Ltd",
    "Siddhartha Equity Fund",
    "Siddhartha Insurance Ltd",
    "Siddhartha Investment Growth Scheme-2",
    "Sindhu Bikash Bank Ltd",
    "Singati Hydro Energy Ltd",
    "Soaltee Hotel Ltd",
    "Standard Chartered Bank Ltd",
    "Summit Laghubitta Bittiya Sanstha Ltd",
    "Sunrise Bank Ltd",
    "Sunrise First Mutual Fund",
    "Support Microfinance Bittiya Sanstha Ltd",
    "Surya Life Insurance Company Ltd}",
    "Suryodaya Laghubitta Bittiya Sanstha Ltd",
    "Swabalamban Laghubitta Bittiya Sanstha Ltd",
    "Swabhimaan Laghubitta Bittiya Sanstha Ltd",
    "Swarojgar Laghubitta Bittiya Sanstha Ltd",
    "Synergy Power Development Ltd",
    "Taragaon Regency Hotel Ltd",
    "Unilever Nepal Ltd",
    "Union Hydropower Ltd",
    "United Finance Ltd",
    "United IDI Mardi RB Hydropower Ltd",
    "United Insurance Co. (Nepal) Ltd",
    "United Modi Hydropower Ltd",
    "Universal Power Company Ltd",
    "Unnati Sahakarya Laghubitta Bittiya Sanstha Ltd",
    "Upper Tamakoshi Hydropower Ltd",
    "Vijaya laghubitta Bittiya Sanstha Ltd",
    "Womi Microfinance Bittiya Sanstha Ltd",
    "Yak And Yeti Hotel Ltd"
]
Sector = [
    "Microfinance", "Commercial Bank", "Non-Life Insurance", "Hydro Power", "Hydro Power", 
    "Hydro Power", "Hydro Power", "Microfinance", "Life Insurance", "Commercial Bank", 
    "Hydro Power", "Finance", "Tradings", "Manufacturing And Processing", "Hydro Power", 
    "Finance", "Commercial Bank", "Hotels And Tourism", "Microfinance", "Hydro Power",
    "Hydro Power", "Commercial Bank", "Investment", "Mutual Fund", "Mutual Fund",
    "Commercial Bank", "Microfinance", "Development Bank", "Microfinance", "Hydro Power", 
    "Commercial Bank", "Non-Life Insurance", "Development Bank", "Microfinance", "Microfinance", 
    "Microfinance", "Development Bank", "Non-Life Insurance", "Hydro Power", "Commercial Bank",
    "Microfinance", "Mutual Fund", "Finance", "Microfinance", "Development Bank", 
    "Hydro Power", "Finance", "Microfinance", "Life Insurance", "Finance",
    "Hydro Power", "Hydro Power", "Commercial Bank", "Manufacturing And Processing", "Non-Life Insurance", 
    "Hydro Power", "Investment", "Finance", "Non-Life Insurance", "Microfinance", 
    "Finance", "Microfinance", "Hydro Power", "Development Bank", "Life Insurance", 
    "Microfinance", "Hydro Power", "Development Bank", "Development Bank", "Hydro Power", 
    "Microfinance", "Commercial Bank", "Mutual Fund", "Commercial Bank", "Mutual Fund", 
    "Microfinance", "Mutual Fund", "Hydro Power", "Life Insurance", "Development Bank", 
    "Non-Life Insurance", "Commercial Bank", "Development Bank", "Microfinance", "Microfinance", 
    "Finance", "Commercial Bank", "Microfinance", "Microfinance", "Development Bank",
    "Microfinance", "Hydro Power", "Hydro Power", "Development Bank", "Finance",
    "Mutual Fund", "Commercial Bank", "Mutual Fund", "Development Bank", "Hydro Power",
    "Life Insurance", "Microfinance", "Non-Life Insurance", "Commercial Bank", "Commercial Bank",
    "Commercial Bank", "Others", "Finance", "Hydro Power", "Investment",
    "Non-Life Insurance", "Commercial Bank", "Life Insurance", "Reinsurance", "Commercial Bank",
    "Microfinance", "Hydro Power", "Mutual Fund", "Mutual Fund", "Mutual Fund",
    "Commercial Bank", "Mutual Fund", "Microfinance", "Microfinance", "Non-Life Insurance",
    "Mutual Fund", "Commercial Bank", "Mutual Fund", "Microfinance", "Investment",
    "Hotels And Tourism", "Hydro Power", "Hydro Power", "Finance", "Commercial Bank",
    "Non-Life Insurance", "Life Insurance", "Non-Life Insurance", "Commercial Bank", "Life Insurance",
    "Finance", "Non-Life Insurance", "Hydro Power", "Hydro Power", "Non-Life Insurance",
    "Hydro Power", "Finance", "Life Insurance", "Hydro Power", "Microfinance",
    "Microfinance", "Hydro Power", "Microfinance", "Microfinance", "Non-Life Insurance",
    "Tradings", "Microfinance", "Finance", "Microfinance", "Microfinance",
    "Commercial Bank", "Mutual Fund", "Non-Life Insurance", "Mutual Fund", "Hydro Power",
    "Hydro Power", "Development Bank", "Microfinance", "Development Bank", "Non-Life Insurance",
    "Development Bank", "Hydro Power", "Manufacturing And Processing", "Finance", "Commercial Bank",
    "Mutual Fund", "Non-Life Insurance", "Mutual Fund", "Development Bank", "Hydro Power",
    "Hotels And Tourism", "Commercial Bank", "Microfinance", "Commercial Bank", "Mutual Fund",
    "Microfinance", "Life Insurance", "Microfinance", "Microfinance", "Microfinance",
    "Microfinance", "Hydro Power", "Hotels And Tourism", "Manufacturing And Processing", "Hydro Power",
    "Finance", "Hydro Power", "Non-Life Insurance", "Hydro Power", "Hydro Power",
    "Microfinance", "Hydro Power", "Microfinance", "Microfinance", "Hotels And Tourism"
]
SectorList1 = [
    "commercialbank", "developmentbank", "finance", "hydropower", "lifeinsurance", "nonlifeinsurance", 
    "microfinance", "mutualfund", "investment", "manufacturingandprocessing", "hotelandtourism",
    "reinsurance", "trading", "other", "all"
]
SectorList2 = [
    "Commercial Bank", "Development Bank", "Finance", "Hydro Power", "Life Insurance", "Non-Life Insurance", 
    "Microfinance", "Mutual Fund", "Investment", "Manufacturing And Processing", "Hotels And Tourism",
    "Reinsurance", "Tradings", "Others", "All"
]