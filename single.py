#1 /usr/bin/python3

import subprocess
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#url = "http://gachon.ac.kr/main.jsp" # user input

url = "https://htcap.org/scanme/domxss.php"

data = subprocess.check_output(['node', 'domdig.js', url]).decode()

#data = '\n[*] scan finished, tot vulnerabilities: 7\n[!] DOM XSS found: hash \xe2\x86\x92 ;alert(1); \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: #act \xe2\x86\x92 <img src="a" onerror="alert(1)"> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: hash \xe2\x86\x92 javascript:alert(1) \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: #act \xe2\x86\x92 \'><img src=a onerror=\'alert(1)\'> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: #act \xe2\x86\x92 "><img src=a onerror="alert(1)"> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: #act \xe2\x86\x92 \'><img src=a onerror=\'alert(1)\'> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: #act \xe2\x86\x92 ]]><img src="a" onerror="alert(1)"> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n'

for line in data.split('\n'):
    if "DOM XSS found: #" in line:
        _id = line.split("#")[1].split()[0]

        req = Request(url)
        res = urlopen(req)
        html = res.read().decode()

        bs = BeautifulSoup(html, 'html.parser')

        for i in bs.find_all('input'):
            if _id in str(i):
                print("PLEASE BETTER CHECK ON THIS")
                print(str(i)) # this is real data ok?

print(data) # this is real data ok?
