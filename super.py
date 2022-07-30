import requests

list = []

url_Hulk = "https://www.superheroapi.com/api.php/2619421814940190/search/Hulk"
url_Cap = "https://www.superheroapi.com/api.php/2619421814940190/search/Captain%20America"
url_Thanos = "https://www.superheroapi.com/api.php/2619421814940190/search/Thanos"

list_1 = [url_Hulk, url_Cap, url_Thanos]
list_name = ["Hulk", "Thanos", "Captain America"]
dict_name = {}

for url in list_1:
  response = requests.get(url)
  list.append(response.json())

for i in list:
    for item in i['results']:
        if item.get("name") in list_name:
            dict_name[item.get("name")] = int(item.get('powerstats').get("intelligence"))

max_val = max(dict_name, key=dict_name.get)
print(f'Самый умный {max_val}')




