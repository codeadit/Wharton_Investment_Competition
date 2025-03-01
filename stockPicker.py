import yfinance as yf
# Normalize Function


def normalize(average, entered):
    constant = float(entered) / float(average)
    return (constant)

# Checks if the values are real or not, and determines value from that.


def check(value):
    if value is not None:
        value = value
    else:
        value = 0
    return value


def inversecheck(value):
    if value is not None:
        value = 1/value
    else:
        value = 0
    return value


def checktotalRevenue(value):
    if value is not None:
        value = value
    else:
        value = 1
    return value
# Normalization of Data for any stock. The data in the brackets of sector_dictionary is the data being fetched from seperate sector dictionaries


def ticker_score(sector_dictionary, eps, divy, profitMargin, ROE, ROA, CR, revenueGrowth, PS, Q, PEG, CFM, opmargin, DE):
    feps = normalize(sector_dictionary["EPS"], eps)  # Growth Metric
    fcr = normalize(sector_dictionary["current_ratio"], CR)  # Financial Health Metric
    fopmargin = normalize(sector_dictionary["opmargin"], opmargin)  # Profitability Metric
    fDE = normalize(sector_dictionary["debt_to_equity_ratio"], DE)  # Financial Health Metric
    fROE = normalize(sector_dictionary["ROE"], ROE)  # Profitability Metric
    fROA = normalize(sector_dictionary["ROA"], ROA)  # Profitability Metric
    frevenueGrowth = normalize(sector_dictionary["revenue_growth"], revenueGrowth)  # Growth Metric
    fPS = normalize(sector_dictionary["PSR"], PS)  # Valuation Metric
    fQ = normalize(sector_dictionary["quick_ratio"], Q)  # Profitability Metric
    fCFM = normalize(sector_dictionary["cash_flow_margin"], CFM)  # Profitability Metric
    fPEG = normalize(sector_dictionary["PEG"], PEG)  # Valuation Metric
    fdivy = normalize(sector_dictionary["dividend_yield"], divy)  # Profitability Metric
    fprofmargin = normalize(sector_dictionary["profit_margin"], profitMargin)
    # Weight is like this because there needs to be a good amount of growth in order for a stock to produce returns
    growthscore = 0.3 * (feps + frevenueGrowth)
    # Weight like this because there needs to be a good amount of profitiability in a stock, and show thru these metrics
    profitabilityscore = 0.25 * (fopmargin + fROE + fROA + fdivy + fprofmargin + fCFM)
    # We are following a Growth Value Investing combo strategy, and the company must have a good stock price in relation to its various ratios and metrics
    valulationscore = 0.25 * (fPS + fPEG)
    # Needs to be taken into consideration because tells us if a company is not on the verge of bankruptcy, but since most stocks are greater than 25B market cap, no heavy weightage on this needed
    financialhealthscore = 0.2 * (fcr + fDE + fQ)

    score = growthscore + profitabilityscore + financialhealthscore + valulationscore
    return score


# EPS, Opmargin, DE, Revenue Growth, PEG
# sector dictionaries
communications_dict = {
    'profit_margin': 0.1, 'current_ratio': 1.2, 'debt_to_equity_ratio': 1, 'EPS': 10.95, 'ROE': 0.1, 'ROA': 0.05,
    'revenue_growth': 0.08, 'PSR': 0.66666, 'quick_ratio': 1.5, 'cash_flow_margin': 0.15, 'PEG': 0.55555,
    'dividend_yield': 0.04, 'opmargin': 0.1}
healthcare_dict = {'profit_margin': 0.1, 'current_ratio': 1.5, 'debt_to_equity_ratio': 1, 'EPS': 14.38, 'ROE': 0.1,
                   'ROA': 0.07, 'revenue_growth': 0.03, 'PSR': 0.25, 'quick_ratio': 1.5, 'cash_flow_margin': 0.15,
                   'PEG': 0.55555, 'dividend_yield': 0.02, 'opmargin': 0.1}
technology_dict = {'profit_margin': 0.2, 'current_ratio': 1.5, 'debt_to_equity_ratio': 1, 'EPS': 25.42, 'ROE': 0.17,
                   'ROA': 0.15, 'revenue_growth': 0.15, 'PSR': 0.166666, 'quick_ratio': 1.5, 'cash_flow_margin': 0.2,
                   'PEG': 0.4, 'dividend_yield': 0.02, 'opmargin': 0.2}
financials_dict = {
    'profit_margin': 0.15, 'current_ratio': 1, 'debt_to_equity_ratio': 1, 'EPS': 12.91, 'ROE': 0.1, 'ROA': 0.05,
    'revenue_growth': 0.08, 'PSR': 0.66666, 'quick_ratio': 1.5, 'cash_flow_margin': 0.07, 'PEG': 0.588235,
    'dividend_yield': 0.02, 'opmargin': 0.15}
real_estate_dict = {'profit_margin': 0.1, 'current_ratio': 1.2, 'debt_to_equity_ratio': 1, 'EPS': 25.29, 'ROE': 0.1,
                    'ROA': 0.05, 'revenue_growth': 0.03, 'PSR': 0.33333, 'quick_ratio': 1.5, 'cash_flow_margin': 0.1,
                    'PEG': 0.625, 'dividend_yield': 0.04, 'opmargin': 0.1}
energy_dict = {'profit_margin': 0.1, 'current_ratio': 1.2, 'debt_to_equity_ratio': 1, 'EPS': 13.16, 'ROE': 0.05, 'ROA': 0.05,
               'revenue_growth': 0.06, 'PSR': 1, 'quick_ratio': 1.5, 'cash_flow_margin': 0.1, 'PEG': 0.769231, 'dividend_yield': 0.04,
               'opmargin': 0.05}
utilities_dict = {
    'profit_margin': 0.15, 'current_ratio': 1.2, 'debt_to_equity_ratio': 1, 'EPS': 11.44, 'ROE': 0.1, 'ROA': 0.05,
    'revenue_growth': 0.04, 'PSR': 0.66666, 'quick_ratio': 1.5, 'cash_flow_margin': 0.15, 'PEG': 0.66666,
    'dividend_yield': 0.02, 'opmargin': 0.1}
consumer_discretionary_dict = {
    'profit_margin': 0.1, 'current_ratio': 1.2, 'debt_to_equity_ratio': 1, 'EPS': 15.84, 'ROE': 0.1, 'ROA': 0.05,
    'revenue_growth': 0.07, 'PSR': 0.66666, 'quick_ratio': 1.5, 'cash_flow_margin': 0.05, 'PEG': 0.55555,
    'dividend_yield': 0.02, 'opmargin': 0.05}
consumer_staples_dict = {
    'profit_margin': 0.15, 'current_ratio': 1.2, 'debt_to_equity_ratio': 1, 'EPS': 9.48, 'ROE': 0.15, 'ROA': 0.1,
    'revenue_growth': 0.05, 'PSR': 0.66666, 'quick_ratio': 1.0, 'cash_flow_margin': 0.1, 'PEG': 0.666666,
    'dividend_yield': 0.01, 'opmargin': 0.1}
materials_dict = {
    'profit_margin': 0.05, 'current_ratio': 1.2, 'debt_to_equity_ratio': 1, 'EPS': 16.36, 'ROE': 0.1, 'ROA': 0.05,
    'revenue_growth': 0.05, 'PSR': 0.66666, 'quick_ratio': 1.5, 'cash_flow_margin': 0.05, 'PEG': 0.666666,
    'dividend_yield': 0.02, 'opmargin': 0.05}
industrials_dict = {
    'profit_margin': 0.05, 'current_ratio': 1.2, 'debt_to_equity_ratio': 1, 'EPS': 15.68, 'ROE': 0.1, 'ROA': 0.05,
    'revenue_growth': 0.05, 'PSR': 0.66666, 'quick_ratio': 1.5, 'cash_flow_margin': 0.1, 'PEG': 0.588235,
    'dividend_yield': 0.02, 'opmargin': 0.05}

# List of stocks from Penn Competition
communications_tickers = ["BIDU", "CMCSA", "GOGO", "GOOGL", "META", "MTCH", "NFLX", "NTES",
                          "SIRI", "SOHU", "VEON", "AMC", "DIS", "EDR", "IMAX", "RCI", "SPOT", "T", "TU", "VZ"]
healthcare_tickers = ["ACHC", "AMGN", "CPRX", "GILD", "GMAB", "HBIO", "ILMN", "LQDA", "MYGN", "REGN", "ABBV", "ABT", "AMN",
                      "BAX", "BMY", "CNC", "CVS", "GMED", "GSK", "IQV", "JNJ", "MCK", "MRK", "NVO", "NVS", "PBH", "PFE", "TEVA", "UNH", "VEEV"]
technology_tickers = ["AAPL", "ADBE", "AEHR", "AMD", "AVGO", "CSCO", "CTSH", "DBX", "DJCO", "FTNT", "INTC", "MANH", "MSFT", "NCTY",
                      "NVDA", "NXPI", "QCOM", "RTC", "SEDG", "TXN", "UTSI", "ANET", "ASGN", "BILL", "CRM", "DXC", "FICO", "ORCL", "SAP", "SNOW", "TSM", "XRX"]
financials_tickers = [
    "GBCI", "GEG", "ONB", "OZK", "PYPL", "SEIC", "TROW", "AFL", "ALL", "APAM", "AXP", "BAC", "BAM", "BCS", "BEN", "BLK", "BX", "C", "DB",
    "DFS", "GS", "ICE", "JPM", "KEY", "KKR", "L", "LAZ", "MA", "MCO", "MET", "MS", "MTB", "OPY", "PNC", "PRU", "RF", "SCHW", "UBS", "V",
    "WFC"]
real_estate_tickers = ['DLR', 'DOC', 'EXR', 'IRM', 'PSA']
energy_tickers = ["AMTX", "BP", "CCJ", "CVX", "ENB", "ET", "HES", "KMI", "NGS", "NOV", "OKE", "PSX", "SUN", "TRP", "WHD", "XOM"]
utilities_tickers = ["AEP", "MSEX", "YORW", "AWK", "D", "FE", "FTS", "NFG", "PCG", "SJW", "SO", "SRE", "UGI"]
consumer_discretionary_tickers = [
    "AMZN", "CAAS", "CAKE", "CZR", "ETSY", "GRPN", "HAS", "LE", "LULU", "MAR", "MAT", "ORLY", "PTON", "PZZA", "SBUX", "SFIX", "SWBI",
    "TSLA", "TXRH", "ULTA", "URBN", "VRA", "WEN", "AEO", "ANF", "APTV", "AZO", "BABA", "BBW", "BBY", "BNED", "BURL", "BWA", "CMG", "EDU",
    "F", "FL", "GM", "GRMN", "H", "HD", "HMC", "HOG", "HRB", "KMX", "LCII", "LOW", "LVS", "M", "MCD", "MOV", "NCLH", "NKE", "PLNT", "SONY",
    "TAL", "TCS", "TJX", "TM", "UA", "VFC", "WH", "WSM", "YUM"]
consumer_staples_tickers = ["CASY", "COST", "DLTR", "FIZZ", "JJSF", "KDP", "MNST", "PEP", "SFM", "WBA", "WDFC", "BUD", "CL",
                            "CPB", "DEO", "DG", "EL", "GIS", "HSY", "K", "KO", "MKC", "PG", "SYY", "TAP", "TGT", "THS", "TR", "TSN", "UL", "UNFI", "WMT"]
materials_tickers = ["CHNR", "IOSP", "KALU", "NTIC", "RGLD", "USLM", "APD", "ASH",
                     "CLW", "CRH", "CTVA", "DOW", "EMN", "FCX", "FMC", "KWR", "LAC", "NTR", "PKX", "X"]
industrials_tickers = [
    "AAL", "ARCB", "BECN", "CHPT", "HTLD", "JBLU", "LYFT", "MIDD", "PCAR", "ROCK", "SKYW", "VRSK", "BA", "CAT", "CNI", "CP", "CYD", "DAL",
    "DE", "FCN", "GD", "GE", "GEO", "LMT", "LUV", "NOC", "PLOW", "RBA", "RTX", "SAVE", "SNA", "TREX", "TWI", "TXT", "UBER", "UPS", "WNC",
    "ZTO"]

energy_tickers = []
materials_tickers = []
utliities_tickers = []
financials_tickers = []
consumer_discretionary_tickers = []
communications_tickers = []
healthcare_tickers = []
technology_tickers = []
industrials_tickers = []
consumer_staples_tickers = []

# List of stocks that beat the average.
final_communications_tickers = []
final_healthcare_tickers = []
final_technology_tickers = []
final_financials_tickers = []
final_real_estate_tickers = []
final_energy_tickers = []
final_utilities_tickers = []
final_consumer_discretionary_tickers = []
final_consumer_staples_tickers = []
final_materials_tickers = []
final_industrials_tickers = []

# Compiling all the data into tuples to make it an easy access in the for loop
sectors = [
    ("Communications", communications_dict, communications_tickers, final_communications_tickers),
    ("Healthcare", healthcare_dict, healthcare_tickers, final_healthcare_tickers),
    ("Technology", technology_dict, technology_tickers, final_technology_tickers),
    ("Financials", financials_dict, financials_tickers, final_financials_tickers),
    ("Real Estate", real_estate_dict, real_estate_tickers, final_real_estate_tickers),
    ("Energy", energy_dict, energy_tickers, final_energy_tickers),
    ("Utilities", utilities_dict, utilities_tickers, final_utilities_tickers),
    ("Consumer Discretionary", consumer_discretionary_dict, consumer_discretionary_tickers, final_consumer_discretionary_tickers),
    ("Consumer Staples", consumer_staples_dict, consumer_staples_tickers, final_consumer_staples_tickers),
    ("Materials", materials_dict, materials_tickers, final_materials_tickers),
    ("Industrials", industrials_dict, industrials_tickers, final_industrials_tickers)
]

# Main Code
for sector in sectors:
    sector_name = sector[0]
    sector_dictionary = sector[1]
    sector_tickers = sector[2]
    final_sector_list = sector[3]
    print(sector_name)
    # Getting Values for each stock in 1 sector. The metric in the parentheses is the metric being fetched from yfinance
    for ticker in sector_tickers:
        eps = check(yf.Ticker(ticker).info.get("forwardEps"))
        opmargin = check(yf.Ticker(ticker).info.get('operatingMargins'))
        divy = check(yf.Ticker(ticker).info.get("dividendYeild"))
        profitMargin = check(yf.Ticker(ticker).info.get("profitMargins"))
        ROE = check(yf.Ticker(ticker).info.get('returnOnEquity'))
        ROA = check(yf.Ticker(ticker).info.get("returnOnAssets"))
        CR = check(yf.Ticker(ticker).info.get("currentRatio"))
        DE = inversecheck(yf.Ticker(ticker).info.get('debtToEquity'))
        revenueGrowth = check(yf.Ticker(ticker).info.get('revenueGrowth'))
        PS = inversecheck(yf.Ticker(ticker).info.get("priceToSalesTrailing12Months"))
        Q = check(yf.Ticker(ticker).info.get("quickRatio"))
        PEG = inversecheck(yf.Ticker(ticker).info.get('pegRatio'))
        operatingCashFlow = check(yf.Ticker(ticker).info.get("operatingCashflow"))
        totalRevenue = checktotalRevenue(yf.Ticker(ticker).info.get("totalRevenue"))
        if totalRevenue == 1:
            CFM = 0
        else:
            CFM = check(operatingCashFlow/totalRevenue)
        marketCap = yf.Ticker(ticker).info.get('marketCap')

        score = ticker_score(sector_dictionary, eps, divy, profitMargin,
                             ROE, ROA, CR, revenueGrowth, PS, Q, PEG, CFM, opmargin, DE)
        # Checking if the score is greater than 14 because 1 is the average value for the stock's metric. And if it is greater, then the score must be greater.
        if score >= 3.25 and marketCap >= 20000000000:
            temp = [ticker, score]
            final_sector_list.append(temp)
            temp = []
            # Sorting list least to greatest
            final_sector_list = sorted(final_sector_list, key=lambda l: l[1], reverse=True)
        # Prints out the data for a stock if its score is greater than 50
        if score > 10 and score < 15:
            print(
                ticker,
                "EPS: ", normalize(sector_dictionary["EPS"], eps),
                "Dividend Yield: ", normalize(sector_dictionary["dividend_yield"], divy),
                "Profit Margin: ", normalize(sector_dictionary["profit_margin"], profitMargin),
                "ROE: ", normalize(sector_dictionary["ROE"], ROE),
                "ROA: ", normalize(sector_dictionary["ROA"], ROA),
                "Current Ratio: ", normalize(sector_dictionary["current_ratio"], CR),
                'Revenue Growth: ', normalize(sector_dictionary["revenue_growth"], revenueGrowth),
                "Price to Sales: ", normalize(sector_dictionary["PSR"], PS),
                "Quick Ratio: ", normalize(sector_dictionary["quick_ratio"], Q),
                "PEG Ratio: ", normalize(sector_dictionary["PEG"], PEG),
                "Cash Flow Margin: ", normalize(sector_dictionary["cash_flow_margin"], CFM),
                "Operating Margin: ", normalize(sector_dictionary["opmargin"], opmargin),
                "Debt to Equity Ratio: ", normalize(sector_dictionary["debt_to_equity_ratio"], DE)
            )

    # Printing final list for sector
    for stock in final_sector_list:
        print(stock[0], " - ", stock[1], "\n")
