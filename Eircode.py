import mechanize
import cookielib
from bs4 import BeautifulSoup
import random

def get_address(eircode):
    browser = mechanize.Browser(factory=mechanize.RobustFactory())
    url = "http://correctaddress.anpost.ie/pages/Search.aspx"
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6')]
    browser.open(url)
    html = browser.response().read()
    browser.select_form(nr=0)
    browser.form.set_all_readonly(False)
    browser["ctl00$body$txtEircode"] = str(eircode)
    request = browser.form.click()
    response = browser.submit()
    html = response.read()
    tag = BeautifulSoup(html).find(id="ctl00_body_hfTextToCopy")
    try:
        value = tag['value']
        address = value.replace("\n","\t")
        return address.replace(eircode,"")
    except:
        return "No Address"
        
def generate_record(RoutingKey):
    try:
        with open(RoutingKey+".txt") as f:
            previous = f.readlines()
        previous = str(previous)
    except:
        previous=""
    for u1 in "0 1 2 3 4 5 6 7 8 9 A C D E F H K N P R T V W X Y".split(" "):
        for u2 in "0 1 2 3 4 5 6 7 8 9 A C D E F H K N P R T V W X Y".split(" "):
            for u3 in "0 1 2 3 4 5 6 7 8 9 A C D E F H K N P R T V W X Y".split(" "):
                for u4 in "0 1 2 3 4 5 6 7 8 9 A C D E F H K N P R T V W X Y".split(" "):
                    eircode = RoutingKey+" "+u1+u2+u3+u4
                    if eircode in previous:
                        continue
                    else:
                        result = eircode+'\t'+get_address(eircode)+'\n'
                        print result
                        with open(RoutingKey+'.txt','a') as f: f.write(result)
    print "Done"

#This will create a text file called D6W.txt and then begin to populate it with
#eircodes and address for the Routing Key D6W. Most importantly, if the code is
#terminated and then ran again, it will continue from where it left off.

generate_record("D6W")
