import csv
import datetime

import numpy
import pandas
from bs4 import BeautifulSoup
import requests
import negative_words as ng
import positive_words as ps

from sites_to_scraple import sites

# Words to be eliminated
to_remove = ['you', 'them', 'how', 'for', 'the', 'or', 'to', 'have', 'is', 'the', 'a', 'in', 'be', 'as', 'they', 'he',
             'she', 'it', 'and', 'her', 'at', 'his', 'may', 'in', 'why', 'with', 'also', 'if', 'are', 'has', 'of',
             'who', 'an',
             "do", "", "-", "my", "not", "\n", "ft", "ads", "on", "&", ".", "ft's", 'cs:', "us:", "so", "does",
             "2020", "by", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", '|', 'x', "%"]


def general_list_of_words(html):
    words = []
    # Create connection, get text
    html_content = requests.get(html).text
    soup = BeautifulSoup(html_content, "lxml")
    # Get words and split them into the list
    text = soup.get_text(",")
    text_splited = text.split(" ")
    for word in text_splited:
        word = word.lower()
        words += word.split(",")
    # Remove words that exist in list called "to_remove"
    words = [x for x in words if x not in to_remove]
    return words


def words_counter(words):
    negative_words_counter = 0
    positive_words_counter = 0
    for word in words:
        # Check if words are in the positive/negative words lists
        if word in ng.negative_words_list:
            negative_words_counter += 1
        elif word in ps.positive_words_list:
            positive_words_counter += 1
    return positive_words_counter, negative_words_counter


positive_words = 0
negative_words = 0
words_today = []
date_today = datetime.date.today()
day_today = date_today.isoweekday()

# OIL PRICES
# WTI CRUDE price
html = requests.get('https://oilprice.com/').text
soup = BeautifulSoup(html, 'lxml')
crude_wti = soup.find(attrs={"data-id": "45"})
crude_wti_value = soup.find(attrs={'class': "value"}).text
# BRENT CRUDE
html = requests.get('https://oilprice.com/').text
soup = BeautifulSoup(html, 'lxml')
brent_crude = soup.find(attrs={"data-id": "46"})
brent_crude_value = brent_crude.find(attrs={'class': "value"}).text
# NATURAL OIL
html = requests.get('https://oilprice.com/').text
soup = BeautifulSoup(html, 'lxml')
natural_oil = soup.find(attrs={"data-id": "51"})
natural_oil_value = natural_oil.find(attrs={'class': "value"}).text
# END - OIL PRICES


for site in sites:
    site_words_list = [site, date_today, day_today, ]
    print(site)
    words = general_list_of_words(site)
    print(words)
    site_words_list += [words]
    counter = words_counter(words)
    print(counter)
    pos = counter[0]
    neg = counter[1]
    positive_words += pos
    negative_words += neg
    words_today += site_words_list
differ = positive_words - negative_words

print('---------------------------------------------------------')
# Actual date
# date_today = datetime.date.today()
# Actual day as a number (Monday is 1, Sunday is 7)
# day_today = date_today.isoweekday()
print('Dzisiaj jest: ', date_today, "(", day_today, 'dzień tygodnia'")")
print('liczba słów pozytywnych: ', positive_words)
print('liczba słów negatywnych: ', negative_words)
print('CRUDE WTI: ', crude_wti_value)
print('BRENT CRUDE: ', brent_crude_value)
print('NATURAL OIL: ', natural_oil_value)
print('---------------------------------------------------------')

# Create csv file for a day
numpy.savetxt(f"{date_today}_words.csv", words_today, delimiter=",", fmt='%s')

# Create output file

# with open('main_output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
# #   writer.writerow(["Date", "Day", "Pos", "Neg"])

# Update file with main statistics

with open('main_output.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(
        [date_today, day_today, positive_words, negative_words, differ, crude_wti_value, brent_crude_value,
         natural_oil_value])


# Add labels
# df = pandas.read_csv("main_output.csv", header=None)
# df.to_csv("main_output.csv",
#           header=["Date", "Day", "Positive words", "Negative words", "Words differ", "CRUDE WTI", "BRENT CRUDE",
#                   "NATURAL OIL"], index=False)
