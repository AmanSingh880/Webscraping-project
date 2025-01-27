import requests
url="https://sarkarinaukri.com/"
def tofile(path,url):
    r=requests.get(url)
    with open(path,"w",encoding="utf-8") as f:
        f.write(r.text)
tofile("data.html",url)
