import requests
import webbrowser
import sys

url = "https://http.cat/"
url2 = "https://thecatapi.com/docs.html?ref=apilist.fun" #page not found

r = requests.get(url2)

if r.status_code == 200:
    None
else:
    webbrowser.open(url + str(r.status_code))

