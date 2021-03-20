import time

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from utils.util import success_response, error_response, unauth
import json
from user.models import User, lostAndFound


def submitLost(request):
    data_json = json.loads(request.body)
    item_type = {
        'lost': 0,
        'found': 1
    }
    if data_json.get('id'):
        print(data_json)
        lostItem = lostAndFound.objects.get(id=data_json.get('id'))
        lostItem.time = data_json.get('time')
        lostItem.place = data_json.get('place')
        lostItem.name = data_json.get('title')
        lostItem.lost_type = data_json.get('lostType')
        lostItem.wechat = data_json.get('wechat')
        lostItem.tell = data_json.get('tell')
        lostItem.remark_info = data_json.get('content')
        lostItem.image_url = data_json.get('imageUrl')
        lostItem.user_id = data_json.get('userId')
        lostItem.save()
    else:
        type = item_type[data_json.get('type')]
        lostItem = lostAndFound.objects.create()
        lostItem.time = data_json.get('time')
        lostItem.place = data_json.get('place')
        lostItem.name = data_json.get('name')
        lostItem.lost_type = data_json.get('lostType')
        lostItem.wechat = data_json.get('wechat')
        lostItem.remark_info = data_json.get('content')
        lostItem.image_url = data_json.get('imageUrl')
        lostItem.user_id = data_json.get('userId')
        lostItem.type = type
        lostItem.save()

    return success_response('发布成功');


def list(request):
    # data_json = json.loads(request.body)
    # print(data_json)
    res = []
    item_type = {
        'lost': 0,
        'found': 1
    }
    item_type_reverse = {
        '0': 'lost',
        '1': 'found'
    }
    type = item_type[request.GET.get('type', default='lost')]
    for item in lostAndFound.objects.all().filter(type=type):
        user = User.objects.get(openid=item.user_id)
        format_time = time.strftime("%Y-%m-%d", time.localtime(int(item.time) / 1000))
        res.append({
            'id': item.id,
            'time': format_time,
            'place': item.place,
            'title': item.name,
            'imgPath': item.image_url,
            'wechat': item.wechat,
            'content': item.remark_info,
            'tell': item.tell,
            'publishDate': item.publish_date,
            'avator': user.avatar_url,
            'publisher': user.user_name,
            'type': item_type_reverse[item.type]
        })
        print(item.type)

    return success_response('成功', res);
    # return success_response('成功', list(lostAndFound.objects.all().values()));
def userList(request):
    # data_json = json.loads(request.body)
    # print(data_json)
    res = []
    item_type = {
        'lost': 0,
        'found': 1
    }
    item_type_reverse = {
        '0': 'lost',
        '1': 'found'
    }
    for item in lostAndFound.objects.all().filter(user_id=request.GET.get('userId')):
        user = User.objects.get(openid=item.user_id)
        format_time = time.strftime("%Y-%m-%d", time.localtime(int(item.time) / 1000))
        res.append({
            'id': item.id,
            'time': format_time,
            'place': item.place,
            'title': item.name,
            'imgPath': item.image_url,
            'wechat': item.wechat,
            'content': item.remark_info,
            'publishDate': item.publish_date,
            'tell': item.tell,
            'avator': user.avatar_url,
            'publisher': user.user_name,
            'type': item_type_reverse[item.type]
        })

    return success_response('成功', res);
    # return success_response('成功', list(lostAndFound.objects.all().values()));

def detail(request):
    res = []
    item_type = {
        'lost': 0,
        'found': 1
    }
    item_type_reverse = {
        '0': 'lost',
        '1': 'found'
    }
    id = request.GET.get('id')
    for item in lostAndFound.objects.all().filter(id=int(id)):
        user = User.objects.get(openid=item.user_id)
        format_time = time.strftime("%Y-%m-%d", time.localtime(int(item.time) / 1000))
        res.append({
            'id': item.id,
            'time': format_time,
            'place': item.place,
            'title': item.name,
            'imgPath': item.image_url,
            'wechat': item.wechat,
            'content': item.remark_info,
            'publishDate': item.publish_date,
            'lostType': item.lost_type,
            'avator': user.avatar_url,
            'publisher': user.user_name,
            'publisherId': item.user_id,
            'tell': item.tell,
            'type': item_type_reverse[item.type],
        })

    return success_response('成功', res);
    # return success_response('成功', list(lostAndFound.objects.all().values()));