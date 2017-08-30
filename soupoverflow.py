from bs4 import BeautifulSoup
import requests

url = "https://stackoverflow.com/questions?page=1&sort=votes&pagesize=50"

f = open("searches.txt","a")

for i in range(1,201):
    url = "https://stackoverflow.com/questions?page="+str(i)+"&sort=votes&pagesize=50"
    print(url)
    text = requests.get(url,headers={}).content
    soup = BeautifulSoup(text,'html.parser')
    items = soup.find_all("div",attrs={"class":"summary"})
    for item in items:
        title = item.contents[1].find_all("a")[0].contents[0]
        try:
            f.write(str(title)+'\n')
        except:
            continue
        tags = []
        for tag in item.contents[5].find_all("a"):
            tags.append(tag.contents[0])
            try:
                f.write(str(title)+' '+str(tag.contents[0])+'\n')
            except:
                continue
        print(tags)
