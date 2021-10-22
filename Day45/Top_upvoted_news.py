import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_news = response.text

soup = BeautifulSoup(yc_news, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_text = []
article_link = []
article_upvotes = []

for article in articles:
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_link.append(link)
# print(article_text)
# print(article_link)
sub_texts = soup.find_all(name="td", class_="subtext")
for subtext in sub_texts:
    if not subtext.find(name="span", class_="score"):
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(subtext.find(name="span", class_="score").getText().split()[0]))

max_upvote = max(article_upvotes)
max_index = article_upvotes.index(max_upvote)

print(max_upvote)
print(article_text[max_index])
print(article_link[max_index])

