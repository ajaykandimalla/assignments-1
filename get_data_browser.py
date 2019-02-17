import urllib.request
from bs4 import BeautifulSoup
weburl=urllib.request.urlopen("https://en.wikipedia.org/wiki/India")
print("result code:")
data=weburl.read()
#print(data)
soup = BeautifulSoup(data)
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

#print(text)
print(text.count("India"))
