import requests
import json

url = "http://129.100.20.40:3000/GlucoGuide/foods/search"
data = "apple"
payload={"key": data, "maxResults":50, "pageNumber": 0, "format": "json"}
r = requests.post(url, data=payload)

# result_text=r.json()
json_text = json.loads(r.text)

print(json_text)          #所有包含apple的食物信息列表--json格式
food_text = json_text["food"]
print(len(food_text))     #所有包含apple的食物信息列表长度
print(food_text[0])       #apple列表中某个食品的粗略信息
print("##########################################")
###################################
url_imformation = "http://129.100.20.40:3000/GlucoGuide/foods/item"
dataload = {"providerID": 4, "itemID": food_text[1]["itemID"],"format":"json"}#4换为当前循环的i
information = requests.post(url_imformation, dataload)
json_information = json.loads(information.text)
print(json_information)     #详细信息的json格式
number_information = json_information["servingSizeOptions"]["servingSizeOption"]
print(len(number_information)-1)    #食品详细信息列表的长度
print(number_information[len(number_information)-1])      #某个食品的详细信息
###################################


