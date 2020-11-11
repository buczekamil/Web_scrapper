import datetime
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
             "2020", "by", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", '|', 'x', ]


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


# Scraple this sites


positive_words = 0
negative_words = 0

for site in sites:
    print(site)
    words = general_list_of_words(site)
    print(words)
    counter = words_counter(words)
    print(counter)
    pos = counter[0]
    neg = counter[1]
    positive_words += pos
    negative_words += neg
print('---------------------------------------------------------')
# Actual date
date_today = datetime.date.today()
# Actual day as a number (Monday is 1, Sunday is 7)
day_today = date_today.isoweekday()
print('Dzisiaj jest: ', date_today, "(", day_today, 'dzień tygodnia'")")
print('liczba słów pozytywnych: ', positive_words)
print('liczba słów negatywnych: ', negative_words)
print('---------------------------------------------------------')

url = "http://api.eia.gov/category/?api_key=      &category_id=714756"
request_json = requests.get(url)
zomato = request_json.json()
print(zomato)
