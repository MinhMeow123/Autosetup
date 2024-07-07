import os
os.system('echo "y" | termux-setup-storage && pkg install python tsu libexpat openssl -y && pip install Flask requests colorama bs4 wget')
import os.path
import zipfile
import wget
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama
import time
os.system('cls' if os.name == 'nt' else 'clear')
#executor
print("Auto setup ug")
print("""
Thanks for ticket rep support form ngquocthanh
and 100gb g*y p*rn form khang-phe-da
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

#Rootcheck
def root():
    try:
        # Execute the 'su' command to check for root access
        result = os.system('su -c "echo"')
        return result == 0
    except Exception as e:
        print(f"Error checking root status: {e}")
        return False
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
print("Delete google play")
os.system('su -c "pm uninstall -k --user 0 com.android.vending"')
print("Ready to check file")
link=gawl("https://www.mediafire.com/file/88smx13m9ot4nts/App.zip/file")
if not(cfe("/sdcard/Download/App.zip")):
    print("Dowload material...")    
    wget.download(link,out="App.zip")  
else:
    print("Found App.zip file,ready to unzip...")      
print("Unzip File....")
unzipall("/sdcard/Download/App.zip","/sdcard/Download/")
print("Unzip App.zip done")
print("Wait 5s cooldown")
time.sleep(5)
print("Done")
if mode == 1:    
#----roblox delta
    if tab <=5 and not(cfe("/sdcard/Download/delta.zip")):
        print("Download delta.zip")
        #wget.download("https://www.mediafire.com/file/0sacrbnq0izj8ug/delta.zip/file",out="trash.html")
        delta=gawl("https://www.mediafire.com/file/0sacrbnq0izj8ug/delta.zip/file")
        time.sleep(1)
        delta=gawl("https://www.mediafire.com/file/0sacrbnq0izj8ug/delta.zip/file")
        wget.download(delta,out="delta.zip")
        os.remove("/sdcard/Download/delta.zip")
        wget.download(delta,out="delta.zip")
    elif tab > 5 and not(cfe("/sdcard/Download/deltasvip.zip")):
        print("Download delta(large).zip")
        #wget.download("https://www.mediafire.com/file/lfxn5c2i8bupfnh/deltasvip.zip/file",out="trash.html")
        delta2=gawl("https://www.mediafire.com/file/lfxn5c2i8bupfnh/deltasvip.zip/file")
        time.sleep(1)
        delta2=gawl("https://www.mediafire.com/file/lfxn5c2i8bupfnh/deltasvip.zip/file")
        wget.download(delta2,out="deltasvip.zip")
        os.remove("/sdcard/Download/deltasvip.zip")
        wget.download(delta2,out="deltasvip.zip")
    print("Unzip Delta file...")
#----unzip
    time.sleep(1)
    if cfe("/sdcard/Download/deltasvip.zip"):
        for i in range(1,tab+1):
            unzip("/sdcard/Download/deltasvip.zip",f"delta{i}.apk","/sdcard/Download/")
    elif cfe("/sdcard/Download/delta.zip"):
        for i in range(1,tab+1):
            unzip("/sdcard/Download/delta.zip",f"delta{i}.apk","/sdcard/Download/")
#roblox-fluxus
else:
    if tab <=5 and not(cfe("/sdcard/Download/fluxus.zip")):
        print("Download fluxus.zip")
        wget.download("https://github.com/MinhMeow123/Autosetup/releases/download/database/fluxus.zip",out="fluxus.zip")
    elif tab > 5 and not(cfe("/sdcard/Download/fluxus2.zip")):
        print("Download fluxus2.zip")
        wget.download("https://github.com/MinhMeow123/Autosetup/releases/download/database/fluxus2.zip",out="fluxus2.zip")
        
    print("Unzip roblox file...")
#----unzip
    if cfe("/sdcard/Download/fluxus2.zip"):
        for i in range(1,tab+1):
            unzip("/sdcard/Download/fluxus2.zip",f"fluxus{i}.apk","/sdcard/Download/")
    elif cfe("/sdcard/Download/fluxus.zip"):
        for i in range(1,tab+1):
            unzip("/sdcard/Download/fluxus.zip",f"fluxus{i}.apk","/sdcard/Download/")
#root test
if not(root()):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Enable Root pls")
    exit()
#apk install
if mode==1:
    print("install apk....")
    for i in range(1,7):
        print(f"Install {i}.apk")
        os.system(f'su -c "pm install /sdcard/Download/{i}.apk/"')     
    os.system('su -c "pm uninstall -k --user 0 com.android.vending"')  
    for i in range(1,tab+1):
        print(f"install delta{i}.apk")
        os.system(f'su -c "pm install /sdcard/Download/delta{i}.apk"')
    os.system('su -c "pm install /sdcard/Download/2.apk"')
else:
    print("install apk....")
    for i in range(1,7):
        print(f"Install {i}.apk")
        os.system(f'su -c "pm install /sdcard/Download/{i}.apk/"')     
    os.system('su -c "pm uninstall -k --user 0 com.android.vending"')  
    for i in range(1,tab+1):
        print(f"install fluxus{i}.apk")
        os.system(f'su -c "pm install /sdcard/Download/fluxus{i}.apk"')
    os.system('su -c "pm install /sdcard/Download/2.apk"')
#vinh tool
os.system('su -c "cd /sdcard/download && export PATH=\$PATH:/data/data/com.termux/files/usr/bin && export TERM=xterm-256color && python ./tool.py"')