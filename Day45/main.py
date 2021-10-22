from bs4 import BeautifulSoup


with open("website.html", "rb") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.a)
print(soup.prettify())
all_anchor_tags = soup.findAll(name="a")
for tags in all_anchor_tags:
    print(tags.getText())
    print(tags.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

name = soup.select_one(selector="#name")
print(name)
all_heading = soup.select(".heading")
print(all_heading)
