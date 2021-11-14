from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.memoryexpress.com/Category/VideoCards?Search=geforce%20rtx%203060&Sort=Price&PageSize=120").text
soup = BeautifulSoup(html_text, 'lxml')
gpuList = soup.find_all('div', class_ = "c-shca-icon-item")
for gpu in gpuList:
    cardNameList = gpu.find('div', class_ = "c-shca-icon-item__body-name").text.replace("  ","")
    cardPriceList = gpu.find('div', class_ = "c-shca-icon-item__summary-list").text.replace("+","")
    print(f'{cardNameList.strip()} costs {cardPriceList.replace(" ","").strip()}')