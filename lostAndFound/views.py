import time
from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from utils.util import success_response, error_response, unauth
import json
from user.models import User, lostAndFound, UserFavorite

# 提交失物招领
def submitLost(request):
    data_json = json.loads(request.body)
    item_type = {
        'lost': 0,
        'found': 1
    }
    # 有id 就是要修改这个item信息
    if data_json.get('id'):
        # print(data_json)
        lost_item = lostAndFound.objects.get(id=data_json.get('id'))
        lost_item.time = data_json.get('time')
        lost_item.place = data_json.get('place')
        lost_item.name = data_json.get('title')
        lost_item.lost_type = data_json.get('lostType')
        lost_item.wechat = data_json.get('wechat')
        lost_item.tell = data_json.get('tell')
        lost_item.remark_info = data_json.get('content')
        lost_item.image_url = data_json.get('imageUrl')
        lost_item.user_id = data_json.get('userId')
        lost_item.save()
    else:
        type_ = item_type[data_json.get('type')]
        lost_item = lostAndFound.objects.create(
            time=data_json.get('time'),
            place=data_json.get('place'),
            name=data_json.get('title'),
            lost_type=data_json.get('lostType'),
            wechat=data_json.get('wechat'),
            remark_info=data_json.get('content'),
            publish_date=time.strftime('%Y-%m-%d'),
            image_url=data_json.get('imageUrl'),
            user_id=data_json.get('userId'),
            type = type_
        )
        lost_item.save()

    return success_response('发布成功');

# 列表
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
    arr = []
    type = item_type[request.GET.get('type', default='lost')]
    arr = lostAndFound.objects.all().filter(type=type, publish_status = 1)
    for item in arr:
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
            'checkTimes': item.check_times,
            'publisher': user.user_name,
            'type': item_type_reverse[item.type]
        })

    return success_response('成功', res);

# 用户个人列表
def userList(request):
    item_type_reverse = {
        '0': 'lost',
        '1': 'found'
    }
    res = []
    arr = []
    type = request.GET.get('publishStatus', default='published')
    if type == 'published':
        arr = lostAndFound.objects.all().filter(
            publish_status = 1,
            user_id=request.GET.get('userId')
        )
    if type == 'unpublish':
        arr = lostAndFound.objects.all().filter(
            publish_status = 0,
            user_id=request.GET.get('userId')
        )
    # 拿到收藏的列表
    if type == 'favorite':
        favorite_list = UserFavorite.objects.filter(
            user_id=request.GET.get('userId'),
            content_type=0,
        )
        # print(favorite_list)
        for favorite_item in favorite_list:
            item = lostAndFound.objects.all().filter(
                id=favorite_item.content_id,
            )
            if item: arr.append(item[0])
    for item in arr:
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
            'checkTimes': item.check_times,
            'type': item_type_reverse[item.type]
        })

    return success_response('成功', res);

# 详情
def detail(request):
    res = []
    item_type_reverse = {
        '0': 'lost',
        '1': 'found'
    }
    id = request.GET.get('id')
    for item in lostAndFound.objects.all().filter(id=int(id)):
        user = User.objects.get(openid=item.user_id)
        format_time = time.strftime("%Y-%m-%d", time.localtime(int(item.time) / 1000))
        favoriteItem = UserFavorite.objects.all().filter(
            user_id=request.GET.get('userId'),
            content_type=0,
            content_id=request.GET.get('id'),
        )
        favorite_status = 0
        # 如果存在，就可以收藏
        if favoriteItem: favorite_status = 1
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
            'checkTimes': item.check_times,
            'type': item_type_reverse[item.type],
            'favorite': favorite_status,
        })
        item.check_times +=1
        item.save()
    return success_response('成功', res);
    # return success_response('成功', list(lostAndFound.objects.all().values()));