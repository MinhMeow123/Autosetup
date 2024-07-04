import os
import zipfile
import wget
import requests
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
#download
def download(url,local_filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        return True
    else:
        return False
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
    while True:
        os.system("wget https://www.mediafire.com/file/88smx13m9ot4nts/App.zip/file")
        os.system("wget https://download1503.mediafire.com/7zujfv499jlgEuH6lplmYaixdFhL_Y2f-AxO8bk6-vq1Cr6JvTRg-hLhBaqCE3BDtO2yOzQ9boPjPSdJPFIGMKju5oZJZX7I_Cda-qM58MBeCEAOAyHAbCEK7gQ55xh-59yq6zaHwKbOD4wrKjZEtyhMWimXRzyVNnlw6PxmA96z/88smx13m9ot4nts/App.zip")
        if testzip("/sdcard/Download/App.zip") == False:
            os.remove("/sdcard/Download/App.zip")
        else:
            break
else:
    pass
