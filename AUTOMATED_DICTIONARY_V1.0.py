import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


os.mkdir("C:\\Users\\dogu2\\Desktop\\tureng\\")
os.chdir("C:\\Users\\dogu2\\Desktop\\tureng\\")

print("*********CURDEV DICTIONARY SCRAPER V1.0*********")
words = []
while len(words) < 5:
    word = input("Word: ")
    words.append(word)
print(words)
for wordd in words:
    url = requests.get("http://tureng.com/en/turkish-english"+"/"+wordd)
    content = url.content
    soup = BeautifulSoup(content, "html.parser")

    turkceleri = soup.find_all("td", class_="tr ts")
    ingilizceleri = soup.find_all("td", class_="en tm")

    tablo = {"English":[],
            "Turkish":[]}

    for ingilizce, turkcesi in zip(ingilizceleri, turkceleri):
        tablo["English"].append(ingilizce.getText())
        tablo["Turkish"].append(turkcesi.getText())

    data = pd.DataFrame(tablo)
    for word_count in words:
        pd.set_option("display.max_rows", 10)
        writer = pd.ExcelWriter(wordd+".xlsx")
        data.to_excel(writer, "sheet")
        writer.close()
    print("AN EXCEL HAS CREATED FOR "+wordd)
