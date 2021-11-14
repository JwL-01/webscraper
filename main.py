from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.memoryexpress.com/Category/VideoCards?Search=geforce%20rtx%203060&Sort=Price&PageSize=120").text
soup = BeautifulSoup(html_text, 'lxml')
gpuList = soup.find_all('div', class_ = "c-shca-icon-item")
cardNameList = soup.find_all('div', class_ = "c-shca-icon-item__body-name")
cardPriceList = soup.find_all('div', class_ = "c-shca-icon-item__summary-list")
for gpu in cardNameList:
    cardName = gpu.text.replace("  ", "")
    cardName = cardName.replace("   ","")
    for price in cardPriceList:
        cardPrice = price.text.replace("+", "")
        cardPrice = cardPrice.replace(" ", "")
        print(f'{cardName} costs {cardPrice}')