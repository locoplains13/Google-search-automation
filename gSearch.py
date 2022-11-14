from googlesearch import search
import webbrowser
from winreg import *
with OpenKey(HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice") as key:
    browser = QueryValueEx(key, 'Progid')[0]
print(browser)
# to search

query = input("Enter a search query you want to make: ")
search_num = input("How many searches do you want to make: ")
queryList = search(query, num=10, lang = "en")

url = queryList[0]

print(url[0])

webbrowser.register(browser, None, "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")