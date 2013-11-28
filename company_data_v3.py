from BeautifulSoup import BeautifulSoup
import csv
import re
import urllib
import urllib2
from urllib2 import HTTPError
# import modules

symbolfile = open("symbols.txt")
symbolslist = symbolfile.read()
newsymbolslist = symbolslist.split("\n")

i = 0

f = csv.writer(open("stocks.csv","wb"))
# short cut to write

f.writerow(["Name","PE","Revenue % Quarterly","ROA% YOY","Operating Cashflow","Debt to Equity"])
#first write row statement

# define name_company as the following
while i<len(newsymbolslist):
    try:
        page = urllib2.urlopen("http://finance.yahoo.com/q/ks?s="+newsymbolslist[i] +"%20Key%20Statistics").read()
    except urllib2.HTTPError:
        continue
    soup = BeautifulSoup(page)
    name_company = soup.findAll("div", {"class" : "title"}) 
    for name in name_company: #add multiple iterations?        
        all_data = soup.findAll('td', "yfnc_tabledata1")
        stock_name = name.find('h2').string #find company's name in name_company with h2 tag
        try:    
            f.writerow([stock_name, all_data[2].getText(),all_data[17].getText(),all_data[13].getText(), all_data[29].getText(),all_data[26].getText()]) #write down PE data
        except (IndexError, HTTPError) as e:
            pass
    i+=1    