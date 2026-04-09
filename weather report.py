import requests

city_name = input("Enter the name of the City: ")
url = f'https://wttr.in/{city_name}?format=%C+%t'
response = requests.get(url)
print(response.text)