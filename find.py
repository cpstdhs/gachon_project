#1 /usr/bin/python3

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import subprocess

C_END     = "\033[0m"
C_BOLD    = "\033[1m"
C_INVERSE = "\033[7m"
 
C_BLACK  = "\033[30m"
C_RED    = "\033[31m"
C_GREEN  = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE   = "\033[34m"
C_PURPLE = "\033[35m"
C_CYAN   = "\033[36m"
C_WHITE  = "\033[37m"
 
C_BGBLACK  = "\033[40m"
C_BGRED    = "\033[41m"
C_BGGREEN  = "\033[42m"
C_BGYELLOW = "\033[43m"
C_BGBLUE   = "\033[44m"
C_BGPURPLE = "\033[45m"
C_BGCYAN   = "\033[46m"
C_BGWHITE  = "\033[47m"

links = []

url = "http://gachon.ac.kr/main.jsp" # user input

url_base = "http://" + url.split("http://")[1].split('/')[0]

req = Request(url)
res = urlopen(req)
html = res.read().decode()

bs = BeautifulSoup(html, 'html.parser')

for link in bs.find_all('a'):
    data = link.get('href')
    try:
        if url.strip("http://").split('.')[0] in data:
            if "http" not in data:
                data = url_base + data
            links.append(data)
    except TypeError:
        continue

#print(links)

for link in links:
    #print(C_BOLD+C_RED+"[+] SCAN URL: "+C_END+C_GREEN+link)
    data = subprocess.check_output(['node', 'domdig.js', link])
    data = data.decode()
    print(data) # this is real data ok?
    #print(C_BOLD+C_RED+"[+] FINISH!")
