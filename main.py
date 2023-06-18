import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/"

# Step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

#Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

#Step 3: HTML Tree traversal

# Commonly used types of objects:
# 1. tag

# title = soup.title
# print(type(title))
# 2. NavigableString
# print(type(title.string))
# 3. BeautifulSoup
# print(type(soup))
# 4. Comment


markup = "<P><!--THIS IS A COMMENT --></P>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))
# exit()

# Get the titleof the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

# Get first element in the HTML Page
print(soup.find('p'))


# Get classes of any element in the HTML page
print(soup.find('p')['class'])


# find all the element with class lead4
print(soup.find_all('p', class_="lead"))


# Get the text from the tags/soup
print(soup.find('p').get_text())

# Full text Get
print(soup.get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText = ("https://www.codewithharry.com/" +link.get('href'))
        all_links.add(link)
        print(linkText)


navbarSupportedContent = soup.find(id='navbarSupportedContent')
print(navbarSupportedContent.contents)