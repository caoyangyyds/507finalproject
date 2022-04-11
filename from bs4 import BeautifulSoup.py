from bs4 import BeautifulSoup
url = "Top Artists – Billboard"
f = open("Top Artists – Billboard.html", 'rb')
html_text = f.read()
soup = BeautifulSoup(html_text, 'html.parser')
name = soup.find_all("h3", id="title-of-a-story")
namelist = []
for i in name[0:100]:
    namelist.append(i.string.strip())
print(namelist)



