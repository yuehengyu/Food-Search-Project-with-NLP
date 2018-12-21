from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
# from django.template import RequestContext,loader
from templates.currentVoice import voiceinput
from templates.speechToText import speechtotest
from templates import keywordExaction
import requests
import json


##############################################################################
# Create your views here.
def input_voice(req):
    aa = voiceinput()
    text = speechtotest(aa)
    print(text.split("\n"))
    resultList = []
    for eachText in text.split("\n"):
        text_keyword = keywordExaction.NPExtractor(eachText)
        # result.append(text_keyword.extract())# 关键词的list
        result = text_keyword.extract()
        for eachWord in result:
            resultList.append(eachWord)# 关键词的list
    # result = text_keyword.extract()# 关键词的list
    print(resultList)
    with open('templates/popular_foods.txt', 'r') as f:
        data = f.readlines()  # popular_list的list
    # with open('G:/djiango/directlyStudy/templates/json.json', 'r') as f:
    #     json_text = json.load(f)
    json_result_list = []
    url = "http://129.100.20.40:3000/GlucoGuide/foods/search"

    for keyword in resultList:
        json_keyword_list = []

        for line in data:
            results = line[0:len(line) - 1].lower().find(keyword)
            result1 = keyword.find(line[0:len(line) - 1].lower())
            if results != -1 or result1 != -1:
                json_keyword_list.append(line[0:len(line) - 1])

        if len(json_keyword_list) == 0:
            payload = {"key": keyword, "maxResults": 50, "format": "json"}
            r = requests.post(url, data=payload)
            json_text = json.loads(r.text)
            food_text = json_text["food"]
            json_result_list.append(food_text[0])
        else:
            for popular_data in json_keyword_list:
                payload = {"key": popular_data, "maxResults": 50, "format": "json"}
                r = requests.post(url, data=payload)
                json_text = json.loads(r.text)
                food_text = json_text["food"]
                json_result_list.append(food_text[0])
    content = {'json_result_list': json_result_list, 'foodText': text}
    return render(req, 'json.html', content)


def init(req):
    return render(req, 'main.html')


def show_json(req):
    food = req.POST['food_text']
    text_keyword = keywordExaction.NPExtractor(food)
    result = text_keyword.extract()  # 关键词的list
    with open('templates/popular_foods.txt', 'r') as f:
        data = f.readlines()  # popular_list的list
    # with open('G:/djiango/directlyStudy/templates/json.json', 'r') as f:
    #     json_text = json.load(f)
    json_result_list = []
    url = "http://129.100.20.40:3000/GlucoGuide/foods/search"

    for keyword in result:
        json_keyword_list = []

        for line in data:
            results = line[0:len(line) - 1].lower().find(keyword)
            result1 = keyword.find(line[0:len(line) - 1].lower())
            if results != -1 or result1 != -1:
                json_keyword_list.append(line[0:len(line) - 1])

        if len(json_keyword_list) == 0:
            payload = {"key": keyword, "maxResults": 50, "format": "json"}
            r = requests.post(url, data=payload)
            json_text = json.loads(r.text)
            food_text = json_text["food"]
            json_result_list.append(food_text[0])
        else:
            for popular_data in json_keyword_list:
                payload = {"key": popular_data, "maxResults": 50, "format": "json"}
                r = requests.post(url, data=payload)
                json_text = json.loads(r.text)
                food_text = json_text["food"]
                json_result_list.append(food_text[0])
    content = {'json_result_list': json_result_list, 'foodText': food}
    return render(req, 'json.html', content)


def detail_information(req, itemid):
    url_imformation = "http://129.100.20.40:3000/GlucoGuide/foods/item"
    dataload = {"providerID": 4, "itemID": itemid, "format": "json"}  # 4换为当前循环的i
    information = requests.post(url_imformation, dataload)
    json_information = json.loads(information.text)
    number_information = json_information["servingSizeOptions"]["servingSizeOption"]
    lastone = len(number_information) - 1
    # content = {'cal': number_information[lastone]}
    return JsonResponse({'data': number_information[lastone]})

def show_detail(req, itemid):
    url_imformation = "http://129.100.20.40:3000/GlucoGuide/foods/item"
    dataload = {"providerID": 4, "itemID": itemid, "format": "json"}  # 4换为当前循环的i
    information = requests.post(url_imformation, dataload)
    json_information = json.loads(information.text)
    # number_information = json_information["servingSizeOptions"]["servingSizeOption"]
    # lastone = len(number_information) - 1
    # content = {'cal': information}
    return render(req, 'detail.html', {'information': json_information})
