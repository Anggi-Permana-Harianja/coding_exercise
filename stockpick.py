import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def get_stocks_down_5_days():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=10)  # Fetch more days to ensure we have at least 5 trading days

    down_stocks = []
    stock_list = [
    "ATGL", "AMWL", "AIXI", "ANGO", "AEON", "ARBK", "APPS", "ALLO", "AAOI", "AZ",
    "ACCD", "AKTS", "ATNF", "AGL", "AP", "ATER", "ASRT", "AGEN", "AKYA", "ANGI",
    "AADI", "AUUD", "AEVA", "ADPT", "ALTG", "ANY", "ABSI", "ATRA", "ALHC",
    "AQST", "APVO", "AEMD", "AMLX", "ARVN", "AMTX", "ABCL", "AFMD", "AMN", "ABOS",
    "ALDX", "ARCT", "AVIR", "AKBA", "AMWD", "AREN", "AYI", "AIRI", "ALNT", "AUBN",
    "ARAY", "AMRC", "ARKG", "ALAR", "AX", "ANTX", "ASO", "ACVA", "ASTE", "AVD",
    "AZTA", "AISP", "ASTH", "ALLT", "ASLE", "AUR", "ANRO", "ACHR", "AWX", "AFYA",
    "ATRC", "ATLC", "ACRV", "ATRO", "AIOT", "ALEC", "AXGN", "ADTX", "ACNB", "AAGR",
    "ABTS", "AG", "ARBE", "AWRE", "ALTO", "ASGN", "AVNT", "ADTN", "ACA", "AVNS",
    "AFCG", "ANAB", "ATKR", "ARRY", "ALK", "AMRN", "AHCO", "AAL", "ATMU", "ALG",
    "ALKS", "AMAL", "AROW", "ASRV", "ACM", "ANL", "ACIU", "APEI", "AXTI", "ACHC",
    "ASB", "AILE", "AKA", "ARQQ", "AUMN", "ABCB", "ACDC", "AEO", "ALKT", "AUB",
    "ADD", "AOS", "AWI", "ASAN", "AVTE", "ADRT", "AIT", "ASIX", "ASM", "ATI",
    "ACU", "AAMC", "AVAH", "ARCB", "ASUR", "ALGM", "AUGX", "ADEA", "ARDX", "AN",
    "AMPX", "ADV", "ALLE", "ARHS", "AZZ", "ATLX", "AZEK", "AIN", "AFRM", "ALGT",
    "ARKO", "AFAR", "AGQ", "ALRM", "API", "ARL", "AMKR", "ACET", "ACLX", "ACIW",
    "ATNI", "ABG", "AEIS", "AXIL", "AMSC", "ATEC", "ALGS", "AVSC", "AHT", "AMCX",
    "AVO", "A", "AAON", "APOG", "AES", "ALSN", "ALVR", "ASTR", "ACIC", "ALRN",
    "AMPL", "ADNT", "ALCO", "AUNA", "ASH", "ANIK", "AVNW", "AFRI", "AVUV", "ARKK",
    "AIP", "AXON", "ABUS", "AFSM", "ATSG", "ACON", "AGM", "ARR", "ATXI", "AMBI",
    "AIV", "AVTR", "AIRT", "ACXP", "ALTM", "ARW", "AMTB", "ATLO", "ACAD", "AJX",
    "AIRR", "AMRK", "ADT", "ALTI", "AFMC", "AGFY", "ABM", "AAME", "ARIS", "ALX",
    "AGX", "AVA", "AWP", "ALGN", "ACES", "AREB", "AMBP", "AMRX", "ALRS", "AMID",
    "APD", "ACCO", "ACT", "AU", "AOSL", "ARMK", "AURA", "ADVM", "AIRG", "APLS",
    "ATGE", "APWC", "AORT", "AXL", "ARKB", "APPN", "AWR", "ANDE", "ARMP", "ABNB",
    "ASND", "AGRO", "ARKD", "ACTV", "ATEN", "AMC", "AAT", "ABR", "AXSM", "APAM",
    "AUMI", "AGCO", "ARKA", "AZPN", "ADMA", "AQWA", "ALT", "AEHR", "ATIP", "AMPS",
    "AVT", "AVMV", "AROC", "AWEG", "ABCS", "ACHL", "AKR", "ADI", "ARWR", "AGMI",
    "AVMC", "AHR", "AMCR", "ATS", "AEM", "ABL", "AGIO", "ALB", "AXP", "AUPH",
    "AL", "AIRL", "AME", "AMPH", "ATHM", "AHH", "ACN", "AEI", "AC", "AIR", "ABNY",
    "APLE", "ACRE", "AMBC", "ARGX", "ARKF", "ARKY", "AZTD", "AVDL", "AVY", "ADPV",
    "AMG", "ADUS", "ALV", "AWK", "ABIO", "ARKC", "AAAU", "AAP", "ANTE", "ASG",
    "ACB", "ACR", "AETH", "ARKZ", "ABEV", "ASR", "ATAI", "AUSF", "AWH", "AE",
    "ADM", "AXTA", "APRE", "AVDX", "ARKR", "AUST", "ARKX", "ALOT", "AVPT", "ASTS",
    "ARI", "ASC", "AESI", "AVGV", "ASTL", "AIVL", "AFG", "ANF", "AOUT", "ALXO",
    "AVLV", "AEE", "AVK", "AZUL", "ADAP", "ANIP", "ARKQ", "APTV", "AMBA", "ALLY",
    "AWAY", "APG", "ALEX", "AHOY", "AMBO", "ASNS", "ASPS", "ATNM", "APGE", "AXS",
    "ARES", "AVGE", "AVSU", "AGNC", "AUTL", "ADP", "AGI", "AMDS", "AVUS", "AMSF",
    "AKAM", "AMTD", "ATEX", "APPF", "ATO", "AIEQ", "APO", "AADR", "AOMR", "ARKW",
    "AVB", "AMH", "AMPY", "AGYS", "ARMN", "AVIE", "ALTL", "AGO", "AFLG", "ADX",
    "AOD", "AER", "ACP", "AEP", "APH", "ACSI", "AMX", "AVLC", "ARC", "ACI", "AQN",
    "AVBP", "AVRE", "AVMA", "ABEQ", "APUE", "AMPG", "ARLP", "AKRO", "AMGN", "AVDS",
    "ADIL", "ANSS", "ASHR", "ACVF", "AFGE", "AIG", "ABLV", "ARLO", "AVDV", "ACV",
    "ANEW", "ASBA", "AUDC", "ASA", "ACWV", "ATR", "AOTG", "ASET", "AVEE", "AGQI",
    "AL-A", "AEF", "APLD", "ARP", "AIO", "AOA", "APYX", "ALTR", "ABBV", "ARM",
    "AM", "AVSD", "AEZS", "APA", "ARVR", "ASST", "AMT", "ADME", "AFGC", "AGNG",
    "AIA", "ALE", "ARLU", "AVNM", "APRT", "AVES", "AVNV", "AZN", "AOR", "AUGZ",
    "ADFI", "ARGT", "AVDE", "AOK", "AAPR", "AESR", "ALL", "ACWI", "APLY", "ADVE",
    "AMAX", "ATFV", "ACWX", "AGD", "AMUB", "AVEM", "AAXJ", "ADSE", "AVXC", "AHLT",
    "AEMB", "AOM", "AVIV", "AMZZ", "ANGL", "AVSE", "ADC", "AGS", "AVIG", "AMZA",
    "ASX", "AHYB", "ARE", "AGG", "ACIO", "AGGS", "AXR", "AGGY", "APCB", "ACTG",
    "ALIM", "ARGD", "ASIA", "AFTY", "AMLP", "AMZU", "ALTY", "AMJB", "APIE", "ACST",
    "AGIH", "ALC", "ALVO", "ASHS", "AIBU", "AMOM", "ATMP", "AAPX", "AIQ", "ARCO",
    "AAPB", "AMNA", "AWF", "AEFC", "AOGO", "ADSK", "AJUL", "AMZP", "AIVI", "APRW",
    "AVMU", "AAN", "AGR", "APMU", "AFL", "AGGH", "AITR", "AMZY", "AAPL", "AAPY",
    "AOHY", "ARB", "AXNX", "AAPU", "AMZN", "ANNX", "ADBE", "AON", "AMAT", "AFIF",
    "ASMF", "AUGW", "AVSF", "AGOX", "AACT", "ALCY", "AY", "APRD", "APRH", "ATXS",
    "APRQ", "ATRI", "AB", "ABAT", "ABVC", "ADCT", "AFK", "AGBA", "AGRI", "AIF",
    "AIM", "AIRS", "ALLG", "ALLR", "ALUR", "ANIX", "ANSC", "APDN", "APLM", "APRJ",
    "ARQ", "ARTL", "ARYD", "ASAI", "ASTI", "ASXC", "ATHA", "ATOS", "ATPC", "AUGT",
    "AULT", "AVXL", "AGZ", "ACGL", "ARCC", "AAA", "AIFD", "AAPD", "AJAN", "AMK",
    "ADIV", "AIPI", "AMZD", "APOS", "AFGB", "APT", "AFB", "ATMC", "ATMV", "AIZN",
    "AFT", "AINC", "ATHS", "ABT", "AFBI", "AMED", "AIYY", "ACEL", "AIBD", "ASEA",
    "ACLS", "AMST", "AMR", "AGZD", "ALAI", "ANEB", "AI", "ASMB", "AVAL", "AEG",
    "ATOM", "AIZ", "ACAC", "ADN", "ALAB", "ARDC", "ANET", "ALUM", "ARCH", "AUID",
    "AQNB", "ASPN", "AYTU", "ADXN", "ACRS", "ABEO", "ARQT", "ASGI", "ACNT", "ANGH",
    "ANVS", "AJG", "ASTC", "AR", "AKTX", "AENT", "AYRO", "ATYR", "AMDY", "AVGO",
    "AVTX", "AMD", "AKAN", "ARTW", "ATCH", "AEYE", "AS", "AMS", "APP", "ATUS",
    "AA", "AQB", "AFGD", "AMPD", "AXDX", "AMLI", "ALMS", "AACI", "ALPP", "ATAT",
    "ACHV", "AIHS", "AIRJ", "ALBT", "ABVX", "ALLK", "ALNY", "AMDL", "AQMS", "AVAV",
    "APCX", "AVGR", "AIEV", "AREC", "AGAE", "ALIT", "AGMH", "AMP", "ARBB", "ASYS",
    "AIU", "APTO", "ADAG", "APLT", "ALCE", "AIRE", "ATXG", "AERT", "AZTR", "AHG",
    "AIMD", "ACMR", "ASPI", "ALSA", "ABVE", "AACG", "ACAB", "ASLN", "AEHL", "AMIX"
]


    for stock in stock_list:
        try:
            #print(f"Getting data for stock code: {stock}")
            # Download the stock data
            data = yf.download(stock, start=start_date, end=end_date)
            
            # Check if we have at least 5 days of data
            if len(data) < 5:
                print(f"Not enough data for {stock}")
                continue
            
            # Check the last 5 days
            last_5_days_close = data['Close'][-6:]
            if all(last_5_days_close[i] < last_5_days_close[i-1] for i in range(1, 5)):
                print(f"--------> {stock} is 5 days PRICE consecutively down")

            last_5_days = data.tail(5)
            down_days = sum(last_5_days['Close'] < last_5_days['Open'])
            if down_days == 5:
                print(f"--------> {stock} is 5 days sold CHEAPER consecutively")
    
        except Exception as e:
            print(f"Error processing {stock}: {str(e)}")

    return down_stocks

if __name__ == "__main__":
    get_stocks_down_5_days()