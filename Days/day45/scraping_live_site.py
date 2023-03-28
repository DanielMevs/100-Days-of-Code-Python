import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# soup.find(name="a", class="storylink")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
# print(articles)

def title_link_getter(text):
    split_text = text.split(' (')
    if len(split_text) > 2:
        return ''.join(split_text[:-1]), split_text[-1].strip(')')

    elif split_text[-1][-1] != ')':
        return ' ('.join(split_text), ''
        
    else:
        return split_text[0], split_text[1].strip(')')

        
for article_tag in articles:
    text = article_tag.getText()
    title, link = title_link_getter(text)
    # print(text)
    article_texts.append(title)
    # link = article_tag.get("href")
    # print(link)
    article_links.append(link)

article_upvotes = [ int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvotes)
# print(int(article_upvotes[0].split()[0]))

largest_number = max(article_upvotes)
# print(largest_number)

largest_index = article_upvotes.index(largest_number)
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])
