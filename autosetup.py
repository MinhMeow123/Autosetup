import os
import os.path
import zipfile
import wget
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama
os.system('cls' if os.name == 'nt' else 'clear')
#executor
print("Auto setup ug")
print("""
[1]:Delta
[2]:Fluxus
""")
while True:
    try:
        mode=int(input("Mode:"))
        if 1<= mode <= 2:
            break
        else:
            print("Wrong value")
    except:
        print("Value not set")
#tab ui
print("""--------------------
How many tab: """)
while True:
    try:
        tab=int(input(">"))
        if 1<= tab <= 10:
            break
        else:
            print("Chose 1-10")
    except:
        print("Wrong value")
#media fire dumbass
internal_urls = set()
external_urls = set()
def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
def gawl(url):
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.find_all("a"):
        href = a_tag.attrs.get("href", "")
        href = urljoin(url, href)
        if is_valid(href):
            if domain_name in href:
                internal_urls.add(href)
            else:
                external_urls.add(href)      
    for i in external_urls:
        if i[0:16] == "https://download":
            return i
#unzip
def unzip(a,b,c):

    with zipfile.ZipFile(a, 'r') as zip_ref:
        zip_ref.extract(b,c)
#unzip all
def unzipall(a,b):
    with zipfile.ZipFile(a, "r") as zObject:
        zObject.extractall(path=b)
#Check file exist
def cfe(file_path):
    return os.path.exists(file_path)

#zip file test
def testzip(file):
    try:
        with zipfile.ZipFile(file) as zip_ref:
            zip_ref.testzip()
        return True
    except Exception as ex:
        return False
#func
if mode == 1 :
    os.system("su")
    
    print()
    print("ready to check file")
    
    link=gawl("https://www.mediafire.com/file/88smx13m9ot4nts/App.zip/file")
    if not(cfe("/sdcard/Download/App.zip")):
        print("Dowload material...")    
        wget.download(link,out="App.zip")  
    else:
        print("Found file,ready to unzip...")
        
    print("Unzip File....")
    unzipall("/sdcard/Download/App.zip","/sdcard/Download/")
    
    print("install apk....")
    for i in range(1,6):
        print("Install...")
        os.system(f"pm install /sdcard/Download/{i}.apk/")
    
    
#----roblox
    if tab <=5 and not(cfe("/sdcard/Download/deltauvipgvip.zip")):
        print("Download deltauvipgvip.zip")
        wget.download(gawl("https://www.mediafire.com/file/dquqq9fg4jndvh6/deltauvipgvip.zip/file"),out="deltauvipgvip.zip")
    elif tab > 5 and not(cfe("sdcard/Download/deltasvip.zip")):
        print("Download deltasvip.zip")
        wget.download(gawl("https://www.mediafire.com/file/lfxn5c2i8bupfnh/deltasvip.zip/file"),out="deltasvip")
    print("Unzip roblox file...")
    if cfe("/sdcard/Download/deltauvipgvip.zip"):
        for i in range(1,tab+1):
            unzip("/sdcard/Download/deltauvipgvip.zip",f"delta{i}.apk","/sdcard/Download/")
    elif cfe("/sdcard/Download/deltasvip.zip"):
        for i in range(1,tab+1):
            unzip("/sdcard/Download/deltasvip.zip",f"delta{1}.apk","/sdcard/Download/")
    
    for i in range(1,tab+1):
        print(f"install delta{i}.apk")
        os.system(f"pm install /sdcard/Download/delta{1}.apk")
else:
    pass
