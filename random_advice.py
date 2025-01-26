import requests
import sys

url = "https://api.adviceslip.com/advice"

r = requests.get(url)

if r.status_code == 200:
    None
else:
    print(f'Error code: {r.status_code}')
    sys.exit()

content = r.json()
c = content.get("slip")

#advice = content.split()
#id = content.split(":")

print(c.get("advice"))

