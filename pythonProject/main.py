import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
url ="https://www.imdb.com/sundance/sundance-2021-movie-guide/ls082687564/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=fedb492a-7d54-4338-bfe2-4c5b0240db68&pf_rd_r=BGJ6Z8904F4P3FMKTWH3&pf_rd_s=center-2&pf_rd_t=60601&pf_rd_i=sundance&ref_=fea_sun_sun_guide2021_sm"

# Connect to the website and return the html to the variable ‘page’
try:
    page = urlopen(url)
except:
    print("Error opening the URL")

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
content = soup.find('div',class_="lister-list")
data = []

# Find the span and get data from it
for i in content.findAll('h3'):
    if(i.text != " "):
        span = i.text
        data.append(span)
        df = pd.DataFrame({"Titles".replace(",",""): data})
    # Dispaly number of cases
print(df)

# Exporing data into Excel
df.to_csv('Data.csv', index=False)

