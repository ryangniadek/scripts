# Script to search DuckDuckGo. Searches the list of arguments as one String
# It is reccomened that the following line be added to your bashrc file so this can be called a command

import sys, webbrowser

if len(sys.argv) == 1:
    sys.exit("No search term given")

url = "https://duckduckgo.com/?q="
terms = sys.argv[1:]

for term in terms:
    url = "%s%s+" % (url, term)

print("Loading.......")

print("DuckDuckGo search opened in new tab of default browser") if webbrowser.open_new_tab(url) else print("Operation failed")