# Script to search DuckDuckGo. Searches the list of arguments as one String
# It is reccomened that the following line be added to your bashrc file so this can be called a command
#   alias search="python3 ~/scripts/search.py"
# then you can type
#   search word1 word2 ...
# and it will preform a search for that query on DuckDuckGo

import sys, webbrowser

if len(sys.argv) == 1:
    sys.exit("No search term given")

url = "https://duckduckgo.com/?q="
terms = sys.argv[1:]

for term in terms:
    url = "%s%s+" % (url, term)

print("Loading.......")

print("DuckDuckGo search opened in new tab of default browser") if webbrowser.open_new_tab(url) else sys.exit("Operation failed")