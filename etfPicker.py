import yfinance as yf


def check(value):
    if value is not None:
        value = value
    else:
        value = 0
    return value


stock_etf_tickers = [
    "ARKK", "LCTU", "XLC", "XLP", "XLE", "XLF", "PAVE", "XLV", "XLI", "RSP", "PHO", "PBW", "IBB", "DGRO", "IVV", "IJH", "IJR", "ESGU",
    "DSI", "USMV", "QUAL", "IWM", "ITA", "SPY", "XLU", "MOAT", "ESGV", "VHT", "VO", "VNQ", "VOO", "VTI", "MSOS", "XLY", "QQQ", "MTUM",
    "IWF", "IYW", "IPO", "XLK", "SMH", "VUG", "VGT", "AVUV", "IWD", "JEPI", "COWZ", "NOBL", "SCHD", "VIG", "VYM", "VTV"]
bond_etf_tickers = ["FTSL", "HYLS", "IGSB", "FALN", "HYG", "LQD", "JNK",
                    "VCIT", "VCSH", "EMB", "SHY", "TLT", "IEF", "SHV",
                    "GOVT", "BIL", "VGSH", "AGG", "BSV", "BND"]

stock_final_etf_tickers = []
bond_final_etf_tickers = []

sectors = [
    ("Stock ETF's", stock_etf_tickers, stock_final_etf_tickers),
    ("Bond ETF's", bond_etf_tickers, bond_final_etf_tickers)
]

for sector in sectors:
    etf_type = sector[0]
    etf_tickers = sector[1]
    final_etf_list = sector[2]
    print(etf_type)
    # Getting 5 year average return for each etf in 1 etf type.
    for etf in etf_tickers:
        five_return = check(yf.Ticker(etf).info.get("fiveYearAverageReturn"))
        final_etf_list.append([etf, five_return])

    final_etf_list = sorted(final_etf_list, key=lambda l: l[1], reverse=True)

    for etf in final_etf_list:
        print(etf[0], " - ", etf[1], "\n")
