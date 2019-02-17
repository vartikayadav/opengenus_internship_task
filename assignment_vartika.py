import sys
import io
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def get_robots_txt(url):
    if url.endswith('/'):
        path=url
    else:
        path=url+'/'
    try:
        req=urlopen(path+"robots.txt",data=None)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        data=io.TextIOWrapper(req,encoding='utf-8')
        check=data.read()
        if ('Disallow') in check:
            m=check.index('Disallow')+8
            x=check[m:m+2]
            if (x==';/'):
                #case when all access is blocked
                return False
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
                print("Number of links to the same web page is "+str(c))
                return True


url_used=input('enter the url ')
value=get_robots_txt(url_used)
if value==False:
    print("Not allowed to access the data for srcaping!! ")

