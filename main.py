'''Ensure to run below lines in cmd
pip install requests
pip install bs4
Set Workspace encoding as UTF-8'''

import requests
from bs4 import BeautifulSoup

#store the website to be accessed in result
website_url=input("Enter the complete website URL starting from [http://]: ")
result=requests.get(website_url)

#to ensure we obtain HTTP 200
print(result.status_code)

if result.status_code!=200:
    print("Enter a valid website URL. Try copying from browser")
    break
#print header
print(result.headers)
#extract and print source of the page
print("The source code of page is: ")
src=result.content
print(src)

#use the BeautifulSoup module to parse and process source
soup = BeautifulSoup(src, 'lxml')

#give me all the links on the page
print("The list of links on the page: ")
links=soup.find_all("a")
print(links)
#print(type(links))
print("\n")      
     
#look through all links with "About between <a> and </a>
'''print("The links with text About: ")
for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])'''
        