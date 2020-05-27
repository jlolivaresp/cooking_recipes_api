import pprint
import urllib
from urllib import request
import re
from bs4 import BeautifulSoup
import json


url = ('https://lovingitvegan.com/vegan-chocolate-chip-banana-bread/')
# url = ('https://www.acouplecooks.com/crispy-cauliflower-tacos/')
# url = ('https://www.loveandlemons.com/vegan-pasta/')
# url = ('https://www.delish.com/cooking/recipe-ideas/recipes/a51337/classic-lasagna-recipe/')

with urllib.request.urlopen(url) as response:
    soup = BeautifulSoup(response.read(), "html.parser")

print(soup.get_text)
# # lista = soup.find_all(string=re.compile("Ingredient"))
# lista = soup.find_all("p")
# # print(lista)
# for i in lista:
#     print(i)
# # for i in soup.find_all("li", "ingredient"):
# #     print(i)
