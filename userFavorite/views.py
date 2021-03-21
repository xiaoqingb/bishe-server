import time
from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from utils.util import success_response, error_response, unauth
import json
from user.models import UserFavorite


def add(request):
    data_json = json.loads(request.body)
    favorite_item = UserFavorite.objects.filter(
        user_id=data_json.get('userId'),
        content_type=data_json.get('contentType'),
        content_id=data_json.get('contentID'),
    )
    # 不存在才生成
    if not favorite_item:
        favorite_item = UserFavorite.objects.create(
            content_type=data_json.get('contentType'),
            content_id=data_json.get('contentId'),
            user_id=data_json.get('userId'),
        )
        favorite_item.save();
    return success_response('收藏成功');

def cancel(request):
    data_json = json.loads(request.body)
    favorite_item = UserFavorite.objects.filter(
        user_id=data_json.get('userId'),
        content_type=data_json.get('contentType'),
        content_id=data_json.get('contentId'),
    )
    # 存在直接delete
    if favorite_item:
        # print(favorite_item)
        favorite_item[0].delete();
    return success_response('取消收藏成功');