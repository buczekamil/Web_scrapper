# def tag_visible(element):
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]', 'footer',]:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True
#
#
# def text_from_html(body):
#     soup = BeautifulSoup(body, 'html.parser')
#     visible_texts = soup.findAll(text=True)
#     # visible_texts = filter(tag_visible, texts)
#     return u" ".join(t.strip() for t in visible_texts)
#
# html = urllib.request.urlopen('https://www.economist.com/').read().lower()
# print(text_from_html(html))
import datetime
from _ast import comprehension
from datetime import date
from bs4 import BeautifulSoup
import requests


class SentimentScrapper:
    # Words to be eliminated
    to_remove = ['how', 'for', 'the', 'or', 'to', 'have', 'is', 'the', 'a', 'in', 'be', 'as', 'they', 'he', 'she', 'it',
                 'and', 'her', 'at', 'his', 'may', 'in', 'why', 'with', 'also', 'if', 'are', 'has', 'of', 'who', 'an',
                 "do", "", "-", "my", "not", "\n", "ft", "ads", "on", "&", ".", "ft's", 'cs:', "us:", "so", "does",
                 "2020", "by", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    # Actual date
    date_today = datetime.date.today()
    print(date_today)
    # Actual day as a number (Monday is 1, Sunday is 7)
    day_today = date_today.isoweekday()
    print(day_today)
    words = []

    def general_list_of_words(html):
        # Words list
        # Create connection, get text
        html_content = requests.get(html).text
        soup = BeautifulSoup(html_content, "lxml")
        # Get words and split them into the list
        text = soup.div.get_text(",")
        text_splited = text.split(" ")
        for word in text_splited:
            word = word.lower()
            SentimentScrapper.words += word.split(",")
        # Remove words that exist in list called "to_remove"
        words = [x for x in SentimentScrapper.words if x not in SentimentScrapper.to_remove]
        return words,  print(words), print(len(words))


    print(words), print(len(words))

# html_economist = "https://www.economist.com/"
# SentimentScrapper.general_list_of_words(html_economist)
# html_financialtimes = "https://www.ft.com/"
# SentimentScrapper.general_list_of_words(html_financialtimes)
html_wsj = "https://www.wsj.com/"
SentimentScrapper.general_list_of_words(html_wsj)

