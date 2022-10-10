#!/usr/bin/env python
# coding: utf-8

# In[22]:


from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import re

seed_url = "https://www.federalreserve.gov/newsevents/pressreleases.htm"
abc = "https://www.federalreserve.gov/newsevents/pressreleases"

urls = [seed_url]   
seen = [seed_url] 
target = []
opened = []          

maxNumUrl = 10; 
print("Starting with url="+str(urls))
while len(urls) > 0 and len(opened) < maxNumUrl:
   
    try:
        curr_url=urls.pop(0)
        print("num. of URLs in stack: %d " % len(urls))
        print("Trying to access= "+curr_url)
        req = urllib.request.Request(curr_url,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        opened.append(curr_url)

    except Exception as ex:
        print("Unable to access= "+curr_url)
        print(ex)
        continue   
   
    soup = BeautifulSoup(webpage)  
    for tag in soup.find_all('a', href = True): 
        childUrl = tag['href'] 
        o_childurl = childUrl
        childUrl = urllib.parse.urljoin(seed_url, childUrl)
        print("seed_url=" + seed_url)
        print("original childurl=" + o_childurl)
        print("childurl=" + childUrl)
        print("seed_url in childUrl=" + str(abc in childUrl))
        print("Have we seen this childUrl=" + str(childUrl in seen))

        if abc in childUrl and childUrl not in seen:
            print("***urls.append and seen.append***")
            urls.append(childUrl)
            seen.append(childUrl)
            print(childUrl)
            req1 = Request(childUrl,headers={'User-Agent': 'Mozilla/5.0'})
            webpage1 = urlopen(req1)
            soup1 = BeautifulSoup(webpage1, "html.parser")
            txt = soup1.get_text()
            x = txt.lower().count("covid")
            print(x)
            
            if x > 0:
                target.append(childUrl)
                print("***target acquired***")
                
            else:
                print("wrong")
        else:
            print("NAN")
            
        

print("num. of URLs seen = %d, and scanned = %d, and target = %d" % (len(seen), len(opened),len(target)))


for target_url in target:
    print(target_url)


