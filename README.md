## crawling DOM for finding xss vulnerability automately on web platform
Chromium web browser를 이용한 web crawler인 [htcrawl](https://htcrawl.org) API를 사용하였다.
이를 이용하여 multiple page applications, single page applicaiton의 xss 취약점을 발견한다.

## KEY FEATURES
- --- htcrawl ---
- Runs inside a real browser (Chromium)
- Recursive DOM crawling engine
- --- DOMDig ---
- Support cookies, proxy, custom headers, htp auth and more
- Scriptable login sequences
- --- project ---
- Support multiple page applications with find.py
- as web developer, quick see vulnerablitiy with no web security knowledge
- inform the security measures

## GETTING STARTED
### Installation
```
git clone https://github.com/cpstdhs/gachon_project.git
cd gachon_project && npm i && cd ..
node gachon_project/domdig.js
```

### Example

```
python3 domdig/find.py (for multiple page applications with security measures, default: http://gachon.ac.kr/main.jsp)
python3 domdig/single.py (for single page applications with security measures, default: https://htcap.org/scanme/domxss.php)
```

```
ubuntu@ubuntu:~/project/domdig$ python3 single.py
PLEASE BETTER CHECK ON THIS
<input id="act" name="inp"/>
PLEASE BETTER CHECK ON THIS
<input id="act" name="inp"/>
PLEASE BETTER CHECK ON THIS
<input id="act" name="inp"/>
PLEASE BETTER CHECK ON THIS
<input id="act" name="inp"/>

[*] scan finished, tot vulnerabilities: 6
[!] DOM XSS found: hash → ;alert(1); → https://htcap.org/scanme/domxss.php#WWWW
[!] DOM XSS found: #act → <img src="a" onerror="alert(1)"> → https://htcap.org/scanme/domxss.php#WWWW
[!] DOM XSS found: hash → javascript:alert(1) → https://htcap.org/scanme/domxss.php#WWWW
[!] DOM XSS found: #act → "><img src=a onerror="alert(1)"> → https://htcap.org/scanme/domxss.php#WWWW
[!] DOM XSS found: #act → '><img src=a onerror='alert(1)'> → https://htcap.org/scanme/domxss.php#WWWW
[!] DOM XSS found: #act → 1 --><img src="a" onerror="alert(1)"> → https://htcap.org/scanme/domxss.php#WWWW">'"
```
