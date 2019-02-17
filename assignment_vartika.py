import sys
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
url_used=input('enter the url ')
print("Task to access the webpage size")
try:
    html=urlopen(url_used)
    k=html.read()
    soup=BeautifulSoup(k,'lxml')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
except AttributeError as e:
    print(e)    
else:
    print("size of web page is"+"="+str(sys.getsizeof(k))+"bytes")
    print("Task to access the webpage links to the same domain")
    c=0
    for link in soup.find_all('a',href=True):
        if ((link['href']== url_used) or (link['href']=='/')):
            c=c+1
    print("Number of likns to the same web page is "+str(c))

