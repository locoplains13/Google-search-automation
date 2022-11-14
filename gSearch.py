from googlesearch import search
import webbrowser
from winreg import *

#gets the default browser from the user
with OpenKey(HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice") as key:
    browser = QueryValueEx(key, 'Progid')[0]

print(browser)

# to search

query = str(input("Enter a search query you want to make: "))
num1 = int(input("How many searches do you want to make: "))

print("Searching...")

queryList = []

#getting the sites into the query list variable
for j in search(query, tld="co.in", num=num1, stop=num1, pause=2):
    queryList.append(j)

#check to see which browser the user has
if(browser == 'MSEdgeHTM'):
    webbrowser.register(browser, 
    None, 
    webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
elif(browser == 'FirefoxURL-308046B0AF4A39CB'):
    webbrowser.register(browser, 
    None, 
    webbrowser.BackgroundBrowser("C:\Program Files\Mozilla Firefox\\firefox.exe"))    
else:
    webbrowser.register(browser, 
    None, 
    webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

print("Opening...")

#open each url it got from the search function
for i in queryList:
    webbrowser.get(browser).open_new(i)
