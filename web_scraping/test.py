import pandas as pd
import requests
from bs4 import BeautifulSoup
url="https://www.amazon.com/s?k=my+smile+amazon&adgrpid=1339207694522088&hvadid=83700758637092&hvbmt=bb&hvdev=c&hvlocphy=143111&hvnetw=o&hvqmt=b&hvtargid=kwd-83701655950204%3Aloc-196&hydadcr=17360_13697265&mcid=cb2dec98ebe43dfea6c9aafa14bb2437&msclkid=4414a424658f1c5fe115cd0d0d02aa2d&tag=mh0b-20&ref=pd_sl_34x11x96w0_b"
head={"User-Agent": "Mozila/5 (Windows NT)"}
html=requests.get(url,headers=head).text
soup=BeautifulSoup(html,"lxml")
titles=soup.find_all("span",class_="headline")
for t in titles:
    print(t)
