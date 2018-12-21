from templates.currentVoice import voiceinput
from templates.speechToText import speechtotest
from templates import keywordExaction
import requests
import json

aa = voiceinput()

text = speechtotest(aa)

print(text)

text_keyword = keywordExaction.NPExtractor(text)
result = text_keyword.extract()  #关键词的list
print(result)
# result = ['banana', 'apple']
with open('popular_foods.txt','r') as f:
    data = f.readlines()  #popular_list的list

url="https://test.glucoguide.com/GlucoGuide/foods/search"
for keyword in result:
    json_keyword_list = []
    for line in data:
        result = line[0:len(line)-1].lower().find(keyword)
        result1 = keyword.find(line[0:len(line)-1].lower())
        if result != -1 or result1 != -1:
            json_keyword_list.append(line[0:len(line)-1])

    if len(json_keyword_list) == 0:
        payload = {"key": keyword, "maxResults": 50, "format": "json"}
        r = requests.post(url, data=payload)
        json_text = json.loads(r.text)
        food_text = json_text["food"]
        print(food_text[0])  # apple列表中某个食品的粗略信息
    else:
        for popular_data in json_keyword_list:
            payload = {"key": popular_data, "maxResults": 50, "format": "json"}
            r = requests.post(url, data=payload)
            json_text = json.loads(r.text)
            food_text = json_text["food"]
            print(food_text[0])  # apple列表中某个食品的粗略信息



