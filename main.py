from bs4 import BeautifulSoup
#import pip._vendor.requests
from csv import writer

# First approach doesn't work, can not get the soup
#url = "https://www.realestate.com.au/buy/in-kelvin+grove,+qld+4059/list-1"
#page = pip._vendor.requests.get(url)

#soup = BeautifulSoup(page.content, 'html.parser')

# Second approach works good, but have to download a page
with open('home.html', 'r', encoding='utf8') as html_file:
    content = html_file.read()
    
soup = BeautifulSoup(content, 'lxml')

lists = soup.find_all('article', class_ = "Card__Box-sc-g1378g-0")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Price', 'Details', 'Area', 'Location', 'Link']
    thewriter.writerow(header)
    for list in lists:
        price = list.find('span', class_ = "property-price").text.replace('\n', '')
        raw = list.find_all('div', class_ = "View__PropertyDetail-sc-11ysrk6-0 gIMwxl")
        details = []
        for i in raw:
            details.append(i['aria-label'])
        area = []
        if(list.find('div', class_ = "View__PropertySize-sc-1psmy31-0 fBWHWc property-size")): 
            area = list.find('div', class_ = "View__PropertySize-sc-1psmy31-0 fBWHWc property-size")['aria-label']
        location = list.find('h2', class_ = "residential-card__address-heading").text.replace('\n', '')
        link_to_accommodation = 'https://www.realestate.com.au' + list.find('a', class_ = "details-link residential-card__details-link").get('href').replace('\n', '')
        info = [price, details, area, location, link_to_accommodation]
        thewriter.writerow(info)
    #print(info)
   
