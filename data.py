from bs4 import BeautifulSoup as bs
import csv
import requests

stars_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(stars_url)
headers = ["Proper Name","Distance","Mass","Radius","Luminosity"]
soup = bs(page.text,'html.parser')
star_table = soup.find('table')
temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    for i in td:
      row = [i.text.rstrip()]
      temp_list.append(row)
# print(temp_list)
# name = headers[0]
# distance = headers[1]
# mass = headers[2]
# radius = headers[3]
# luminos = headers[4]
# print(name)

# header_list = [name,distance,mass,radius,luminos]
# header = []
# header.append(header_list)

# for i in range(1,len(temp_list)):
    # name.append(temp_list[i][1])
    # distance.append(temp_list[i][3])
    # mass.append(temp_list[i][5])
    # radius.append(temp_list[i][6])
    # luminos.append(temp_list[i][7])

with open("scraper.csv","a+",encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    print(temp_list)
    csvwriter.writerows(temp_list)