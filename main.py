import requests
from os import system
from bs4 import BeautifulSoup
import pandas as pd

url="https://sarkarinaukri.com/"
def safedata(path,url):
    r=requests.get(url)
    with open(path,"w",encoding="utf-8") as f:
        f.write(r.text)
def read_to_paser(path):
   try:
        with open(path,"r",encoding='utf-8') as f:
            data=f.read()
            soup=BeautifulSoup(data,'html.parser')
            news=soup.find_all(class_="td-module-meta-info")
            dict=[]
            for newe in news:
                if newe.h3 and newe.h3.a:
                    url=newe.h3.a.get('href')
                else:
                    url=None
                if newe.a:
                    job_type="".join(str(newe.a.string).split())
                else:
                    job_type="N/A"
                if newe.h3 and newe.h3.a:
                    job_title="".join(str(newe.h3.a.string).split())
                else:
                    job_title="N/A"
                da={"job_type" : job_type , "job_title" : job_title, "job_link" : url}
                dict.append(da)
            df_d=pd.DataFrame(dict)
            df=df_d.sort_values(by="job_title")
            df.to_csv("data.csv",index=False)
            print("data is present in data.csv")
            system("data.csv")
   except:
       print("Error Occurs")
       


safedata("data2.html",url)
read_to_paser("data2.html")