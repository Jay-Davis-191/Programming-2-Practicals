import wikipedia

search_input = input("What would you like to search? ")
while search_input.strip() != "":
    try:
        search_page = wikipedia.page(search_input, auto_suggest=False)
        print(search_page.title)
        print(search_page.url)
        print(search_page.content)
    except wikipedia.exceptions.DisambiguationError as related_searches:
        print(related_searches.options)
    search_input = input("\nWhat would you like to search? ")
print("Thanks for playing :)")

"""
try:
    summary_input = wikipedia.summary(search_input)
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)



print(wikipedia.search(search_input, results=5))
BL = wikipedia.page("Bruce Lee")
print(BL.title)
print(BL.url)
print(BL.content)
print(BL.images[0])
print(BL.links[0])
"""
