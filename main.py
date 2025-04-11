
#8A5puVeD
import requests

url: str = "https://www.jblanked.com/news/api/mql5/calendar/today/"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key 8A5puVeD",
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
    print(data[0]["Name"])
else:
    print(f"Error: {response.status_code}")
    print(response.json())