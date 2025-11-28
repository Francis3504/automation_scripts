import pandas as pd
url="https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes"
simpsons=pd.read_html(url,header=0,displayed_only=False,flavor="lxml",attrs={"class":"wikitable"})
print(len(simpsons))