import urllib.request

page = urllib.request.urlopen("http://www.bestbuy/prices.html")
text = page.read().decode("utf8")
price = text[234:238]


print (text)
