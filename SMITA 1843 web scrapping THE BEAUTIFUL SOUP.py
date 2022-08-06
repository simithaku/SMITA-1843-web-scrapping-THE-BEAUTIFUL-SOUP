#!/usr/bin/env python
# coding: utf-8

# # 1) Write a python program to display all the header tags from wikipedia.org.
# 

# In[27]:


#loading libraries
import pandas as pd
import re
import requests
import bs4
from bs4 import BeautifulSoup



# In[7]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[8]:


page


# In[9]:


content=BeautifulSoup(page.content)
content


# In[26]:


Movie = []
Year = []
Rating = []

def IMDB_top_100(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    movie_name = soup.select("td.titleColumn a")
    for i in movie_name:
        Movie.append(i.get_text())
    movie_year = soup.find_all('span',class_='secondaryInfo')
    for i in movie_year:
        Year.append(i.get_text().replace('\n','').replace('(','').replace(')',''))
    movie_rating = soup.find_all('td',class_="ratingColumn imdbRating")
    for i in movie_rating:
        Rating.append(i.get_text().replace('\n',''))


# # 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.

# In[11]:


IMDB_top_100('https://www.imdb.com/chart/top/?sort=ir,desc&mode=simple&page=1')


# In[12]:


IMDB_top_100_movies = pd.DataFrame({})
IMDB_top_100_movies['Movie'] = Movie[0:100]
IMDB_top_100_movies['Year'] = Year[0:100]
IMDB_top_100_movies['Rating'] = Rating[0:100]

IMDB_top_100_movies


# # 3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[13]:


Movie_Indian = []
Year_Indian = []
Rating_Indian = []

def IMDB_top_100_Indian(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    movie_name = soup.select("td.titleColumn a")
    for i in movie_name:
        Movie_Indian.append(i.get_text())
    movie_year = soup.find_all('span',class_='secondaryInfo')
    for i in movie_year:
        Year_Indian.append(i.get_text().replace('\n','').replace('(','').replace(')',''))
    movie_rating = soup.find_all('td',class_="ratingColumn imdbRating")
    for i in movie_rating:
        Rating_Indian.append(i.get_text().replace('\n',''))


# In[14]:


Movie_Indian = []
Year_Indian = []
Rating_Indian = []

def IMDB_top_100_Indian(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    movie_name = soup.select("td.titleColumn a")
    for i in movie_name:
        Movie_Indian.append(i.get_text())
    movie_year = soup.find_all('span',class_='secondaryInfo')
    for i in movie_year:
        Year_Indian.append(i.get_text().replace('\n','').replace('(','').replace(')',''))
    movie_rating = soup.find_all('td',class_="ratingColumn imdbRating")
    for i in movie_rating:
        Rating_Indian.append(i.get_text().replace('\n',''))
IMDB_top_100_Indian('https://www.imdb.com/india/top-rated-indian-movies/?sort=ir,desc&mode=simple&page=1')
IMDB_top_100_Indian_movies = pd.DataFrame({})
IMDB_top_100_Indian_movies['Movie'] = Movie_Indian[0:100]
IMDB_top_100_Indian_movies['Year'] = Year_Indian[0:100]
IMDB_top_100_Indian_movies['Rating'] = Rating_Indian[0:100]

IMDB_top_100_Indian_movies


# # 4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm
# 

# In[15]:


page2= requests.get('https://presidentofindia.nic.in/former-presidents.htm')
soup2= BeautifulSoup(page2.content)

President_name=[]
for i in soup2.find_all('div', class_="presidentListing"):
    cells = i.find_all('h3')
    President_name.append(cells[0].text.strip())

Term=[]
for i in soup2.find_all('div', class_="presidentListing"):
    cells = i.find_all('p')
    Term.append(cells[0].text.strip().replace('Term of Office:',''))

print('-'*68)
print('\t\t\t Former Presidents List')
print('-'*68)

df_president=pd.DataFrame({'Name of President (life span)':President_name,'Term of Office':Term})
df_president


# # 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating
# page3

# In[16]:


page3= requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
soup3= BeautifulSoup(page3.content)

Team=[]
Matches=[]
Points=[]
Rating=[]
Ranking=[]
for i in soup3.find_all('tr')[:11]:
    cells = i.find_all('td')
    if len(cells) == 5:
        Ranking.append(cells[0].text.strip())
        Team.append(cells[1].text.strip().replace('\n'," , "))
        Matches.append(cells[2].text.strip())
        Points.append(cells[3].text.strip())
        Rating.append(cells[4].text.strip())
        

print("\t Top 10 ODI Teams in Men's Cricket")
print('-'*50)

df_team = pd.DataFrame({'Ranking':Ranking,'Team':Team,'Matches':Matches,'Points':Points,'Rating':Rating})  
df_team
 


# # b) Top 10 ODI Batsmen along with the records of their team and rating.

# In[17]:


page4= requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
soup4= BeautifulSoup(page4.content)

Player=[]
Team=[]
Rating=[]

for i in soup4.find_all('tr')[:11]:
    cells = i.find_all('td')
    if len(cells) == 5:
        Player.append(cells[1].text.strip().replace('\n'," , "))
        Team.append(cells[2].text.strip())
        Rating.append(cells[3].text.strip())
        
print('~'*40)
print(" Top 10 ODI Batsmen in Men's Cricket")
print('~'*40)

df_batting= pd.DataFrame({'Player':Player,'Team':Team,'Rating':Rating})  
df_batting


# # c) Top 10 ODI bowlers along with the records of their team and rating.
# 

# In[18]:


page5= requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
soup5= BeautifulSoup(page5.content)

Player=[]
Team=[]
Rating=[]

for i in soup5.find_all ('tr')[:11]:
    cells = i.find_all('td')
    if len(cells) == 5:
        Player.append(cells[1].text.strip().replace('\n'," , "))
        Team.append(cells[2].text.strip())
        Rating.append(cells[3].text.strip())

print('→'*40)
print("  Top 10 ODI Bowlers in Men's Cricket")
print('←'*40)

df_bowling=pd.DataFrame({'Player':Player,'Team':Team,'Rating':Rating})
df_bowling


# # 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# 

# In[19]:


page6= requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
soup6= BeautifulSoup(page6.content)

Team=[]
Matches=[]
Points=[]
Rating=[]
Ranking=[]
for i in soup6.find_all('tr')[:11]:
    cells = i.find_all('td')
    if len(cells) == 5:
        Ranking.append(cells[0].text.strip())
        Team.append(cells[1].text.strip().replace('\n'," , "))
        Matches.append(cells[2].text.strip())
        Points.append(cells[3].text.strip())
        Rating.append(cells[4].text.strip())

print('='*45)
print("     Top 10 ODI Teams in Women's Cricket")
print('='*45)
df_team1 = pd.DataFrame({' Ranking':Ranking,'Team':Team,'Matches':Matches,'Points':Points,'Rating':Rating})  
df_team1


# # b) Top 10 women’s ODI Batting players along with the records of their team and rating
# 

# In[20]:


page6= requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
soup6= BeautifulSoup(page6.content)

Player=[]
Team=[]
Rating=[]

for i in soup6.find_all('tr')[:11]:
    cells = i.find_all('td')
    if len(cells) == 5:
        Player.append(cells[1].text.strip().replace('\n'," , "))
        Team.append(cells[2].text.strip())
        Rating.append(cells[3].text.strip())
        
print('^'*50)
print("  Top 10 ODI Batting Players in Women's Cricket")
print('*'*50)
df_batting1= pd.DataFrame({'Player':Player,'Team':Team,'Rating':Rating})  
df_batting1


# # c) Top 10 women’s ODI all-rounder along with the records of their team and rating
# 

# In[21]:


page7= requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
soup7= BeautifulSoup(page7.content)

Player=[]
Team=[]
Rating=[]

for i in soup7.find_all('tr')[:11]:
    cells = i.find_all('td')
    if len(cells) == 5:
        Player.append(cells[1].text.strip().replace('\n'," , "))
        Team.append(cells[2].text.strip())
        Rating.append(cells[3].text.strip())
        
print('#'*50)
print("Top 10 women’s ODI all-rounder in Women's Cricket")
print('#'*50)


df_all_Rounder= pd.DataFrame({'Player':Player,'Team':Team,'Rating':Rating})  
df_all_Rounder


# # 7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# 
# 

# In[22]:


page8= requests.get('https://www.cnbc.com/world/?region=world')
soup8= BeautifulSoup(page8.content)

headline=[]
for i in soup8.find_all('a', class_="LatestNews-headline"):
    headline.append(i.get('title'))

time=[]
for i in soup8.find_all('span', class_="LatestNews-wrapper"):
    time.append(i.text)

News_Link = []
for i in soup8.find_all('a',class_="LatestNews-headline"):
    News_Link.append(i.get('href'))

print('↭'*50)
print('\t\t\t\t\t News Details')
print('↭'*50)

News=pd.DataFrame({'Headline': headline, 'Time': time,'News Link': News_Link})
News


# # 8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# 

# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles

# In[5]:


page9= requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
soup9= BeautifulSoup(page9.content)

Paper_Title=[]
for i in soup9.find_all('h2', class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    Paper_Title.append(i.text)

Authors=[]
for i in soup9.find_all('span', class_="sc-1w3fpd7-0 pgLAT"):
    Authors.append(i.text)  

Published_Date=[]
for i in soup9.find_all('span', class_="sc-1thf9ly-2 bKddwo"):
    Published_Date.append(i.text)  

Paper_URL=[]
for i in soup9.find_all('a', class_="sc-5smygv-0 nrDZj"):
    Paper_URL.append(i.get('href'))

print('~'*127)
print('\t\t\t\t\t\t Most Downloaded Articles')
print('~'*127)

Articles=pd.DataFrame({'Paper Title': Paper_Title,'Authors': Authors,'Published Date': Published_Date, 'Paper URL':Paper_URL})
Articles


# In[ ]:





# In[ ]:




