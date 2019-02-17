# opengenus_internship_task
It has been a very good experience to complete the assignment that I have been given by OpenGenus Foundation for the internship screening task.
The task that I am assigned states :-<br>
To develop a script in any language which will take a URL as an input and output the following information:<br>
<b>1)Size of the webpage in bytes<br></b>
<b>2)Number of links in that page pointing to same domain (find \<a\> tags)<br></b>

The concept behind this process is to gain the information about a webpage with the help of a URL and this can be achieved in several ways , two most common ones are<br>
<b>1)Using API<br></b>
<b>2)Using Web Scraping<br></b>
Well the first method is not always suitable as we many times the API are not present or for that purpose we have to rely on third parties ;besides there are certain strict rules on the data that is sent or returned in JSON  .
Hence the preferred way is Web Scraping as it's very customizable, and not having such rules.<br>
<b>a)</b>Now it's very important to ensure that we should not scrape a site thats does not allow access , although for the tasks assigned such problem won't
appear.For that we use robots.txt file .<br>
<b>b)</b>We also need to make sure that while requesting for a web page , we don't get errors and if we get then display error messages efficiently(HTTPError,URLError,etc..)<br>
<b>c)</b>In order to find the size of webpage in bytes ,we use sys module in python and then by .getsizeof() we find the size of the webpage in text format.<br>
<b>d)</b>In order to find the links on the webpage to the same domain we have used BeautifulSoup ,a python library ,to find all \<a\> tags that have links to the same domain ,ie, href="/" or href="same webpage url " and count the result in c
(we could also have used str.count approach) <br><br>
Following are the screenshots:-<br>
1)install bs4 (BeautifulSoup)<br>
![](images/pic11.JPG)<br>
2)importing required packages<br>
![](images/pic22.JPG)<br>
3)taking url as input and calling function to check
![](images/pic33%20(2).JPG)<br>
4)main content<br>
![](images/pic44.JPG)<br>
Following is the video to show the working:<br>
https://drive.google.com/open?id=11CmS-L-e36Pt4d_MyRO3d6hMIdS5lEju<br>
https://drive.google.com/open?id=1fHRgTlNVeo-JrfmiGwHDgJ9y9YWxVy1g

