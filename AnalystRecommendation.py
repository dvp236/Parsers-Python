import requests
import re



def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def analyse(ticker):
#     url = "https://markets.ft.com/data/equities/tearsheet/forecasts?s=NVDA:NSQ"
    url = "https://markets.ft.com/data/equities/tearsheet/forecasts?s="+ticker+":NSQ"
    res = requests.get(url)
#     print res.status_code
    x = res.text
#     x = cleanhtml(x)
#     print x
    buy = ""
    sell = ""
    outperform = ""
    underperform = ""
    hold = ""
    mediantarget = ""
    hightarget = ""
    lowtarget = ""
    try:
        x = x.split("Consensus recommendation")[1]
        cly= cleanhtml(x)
        fulltext = cly.split("recommendation details.")[1].split("The median")[0]

        buy = fulltext.split("Buy")[1].split("Outperform")[0]
        outperform = fulltext.split("Outperform")[1].split("Hold")[0]
        hold = fulltext.split("Hold")[1].split("Underperform")[0]
        underperform = fulltext.split("Underperform")[1].split("Sell")[0]
        sell = fulltext.split("Sell")[1].split("Share")[0]
        try:
            mediantarget = fulltext.split("median target of ")[1].split(",")[0]
            hightarget = fulltext.split("high estimate of ")[1].split("and")[0]
            lowtarget = fulltext.split("low estimate of ")[1]
        except:
            "Error in getting addtional data"
    except:
        try:
            url = "https://markets.ft.com/data/equities/tearsheet/forecasts?s="+ticker+":NYQ"
            res = requests.get(url)
               # print res.status_code
            x = res.text
            cly= cleanhtml(x)
            fulltext = cly.split("recommendation details.")[1].split("The median")[0]

            buy = fulltext.split("Buy")[1].split("Outperform")[0]
            outperform = fulltext.split("Outperform")[1].split("Hold")[0]
            hold = fulltext.split("Hold")[1].split("Underperform")[0]
            underperform = fulltext.split("Underperform")[1].split("Sell")[0]
            sell = fulltext.split("Sell")[1].split("Share")[0]
            try:
                mediantarget = fulltext.split("median target of ")[1].split(",")[0]
                hightarget = fulltext.split("high estimate of ")[1].split("and")[0]
                lowtarget = fulltext.split("low estimate of ")[1]
            except:
                "Error in getting addtional data"
        except:
            print "Error in getting data"

    #print fulltext



    result = {"Buy" : buy, "Outperform" : outperform, "Hold" : hold, "Underperform" : underperform, "Sell":sell}
    result.update({ "MedianTarget":mediantarget, "HighTarget":hightarget, "LowTarget":lowtarget})
    return result


analyse("AMZN")
