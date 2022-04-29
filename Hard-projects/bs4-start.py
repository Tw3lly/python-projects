from bs4 import BeautifulSoup
# import lxml

# Beautiful Soup DEMO

# Site had emojis so we had to specify the encoding as UTF-8 to not get errors while opening the file
with open("website.html", encoding="utf-8") as website_file:
    contents = website_file.read()
    # print(contents)

# Can also use lxml by using the import lxml and then lmxl.parser (if a site doesn't work)
# Specify file, document type
soup = BeautifulSoup(contents, "html.parser")

# From the html file get the title tag
# print(soup.title)
# Diving deeper into the tag
# print(soup.title.name)
# # Get title and print as string
# print(soup.title.string)
#
# # Indents the file and makes it "pretty" and easier to read.
# print(soup.prettify())

# If we want to find all tags:
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # Strips out the text
    # print(tag.getText())
    # Strips out the link
    # print(tag.get("href"))
    pass

# Find specific heading using ID
# heading = soup.find(name="h1", id="name")
# print(heading)

# Find/select specific heading using Class
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# Looks for a anchor tag sitting in a p tag, using CSS selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)

# Example of finding by CSS selector ID
# name = soup.select_one(selector="#name")
# print(name)

# Selects headings and becomes a list.
headings = soup.select(".heading")
print(headings)
