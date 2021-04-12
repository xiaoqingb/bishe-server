import time
from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from utils.util import success_response, error_response, unauth
import json
from user.models import UserFavorite, Apply, User, SchoolForum, ThumbUp, Comment


def publish(request):
    data_json = json.loads(request.body)
    user = User.objects.filter(
        openid=data_json.get('userId')
    )
    if not user or not user[0].card_id:
        return error_response('您未登陆认证，无法使用此功能')
    if data_json.get('id'):
        tropic_item = SchoolForum.objects.get(topic_id=data_json.get('id'))
    else:
        tropic_item = SchoolForum.objects.create()
    tropic_item.user_id = data_json.get('userId')
    tropic_item.topic_title = data_json.get('topicTitle')
    tropic_item.topic_type = data_json.get('topicType')
    tropic_item.topic_content = data_json.get('topicContent')
    tropic_item.publish_date = data_json.get('publishDate')
    tropic_item.save()
    return success_response('成功')


def delete(request):
    data_json = json.loads(request.body)
    tropic_item = SchoolForum.objects.filter(
        topic_id=data_json.get('id')
    )
    if tropic_item: tropic_item[0].delete()
    return success_response('删除成功')


def edit(request):
    data_json = json.loads(request.body)
    tropic_item = SchoolForum.objects.get(
        topic_id=data_json.get('id')
    )
    tropic_item.user_id = data_json.get('userId')
    tropic_item.topic_title = data_json.get('topicTitle')
    tropic_item.topic_type = data_json.get('topicType')
    tropic_item.topic_content = data_json.get('topicContent')
    tropic_item.publish_date = data_json.get('publishDate')
    tropic_item.read_nums = data_json.get('readNums')
    tropic_item.save()
    return success_response('编辑成功')


def list(request):
    arr = []
    topic_list = SchoolForum.objects.all()
    for item in topic_list:
        thumb_nums = 0
        thumb_list = ThumbUp.objects.filter(
            content_id=item.topic_id,
            content_type=1
        )
        if thumb_list:
            thumb_nums = len(thumb_list)
        comment_arr = []
        comment_list = Comment.objects.filter(topic_id=item.topic_id)
        for comment_item in comment_list:
            user_item = User.objects.filter(openid=comment_item.user_id)
            if user_item:
                user_item = user_item[0]
                comment_arr.append({
                    "id": comment_item.id,
                    "userId": user_item.openid,
                    "userName": user_item.user_name,
                    "avatorUrl": user_item.avatar_url,
                    "content": comment_item.content,
                    "publishDate": comment_item.publish_date,
                })
        user = User.objects.get(openid=item.user_id)
        arr.append({
            'id': item.topic_id,
            'userId': user.openid,
            'userName': user.user_name,
            'avatorUrl': user.avatar_url,
            'topicTitle': item.topic_title,
            'topicType': item.topic_type,
            'topicContent': item.topic_content,
            'publishDate': item.publish_date,
            'readNums': item.read_nums,
            'thumbUpNums': thumb_nums,
            'commentList': comment_arr,
        })
    return success_response('获取活动列表成功', arr);


def detail(request):
    arr = []
    topic_items = SchoolForum.objects.filter(topic_id=request.GET.get('id'))
    isThumb = 0
    if ThumbUp.objects.filter(
        content_id=request.GET.get('id'),
        user_id=request.GET.get('userId'),
        content_type=1,
    ):
        isThumb = 1
    for item in topic_items:
        thumb_nums = 0
        thumb_list = ThumbUp.objects.filter(
            content_id=item.topic_id,
            content_type=1
        )
        if thumb_list:
            thumb_nums = len(thumb_list)
        comment_arr = []
        comment_list = Comment.objects.filter(topic_id=request.GET.get('id'))
        for comment_item in comment_list:
            user_item = User.objects.filter(openid=comment_item.user_id)
            if user_item:
                user_item = user_item[0]
                comment_arr.append({
                    "id": comment_item.id,
                    "userId": user_item.openid,
                    "userName": user_item.user_name,
                    "avatorUrl": user_item.avatar_url,
                    "content": comment_item.content,
                    "publishDate": comment_item.publish_date,
                })
        user = User.objects.get(openid=item.user_id)
        arr.append({
            'id': item.topic_id,
            'userName': user.user_name,
            "userId": user.openid,
            'avatorUrl': user.avatar_url,
            'topicTitle': item.topic_title,
            'topicContent': item.topic_content,
            'publishDate': item.publish_date,
            'readNums': item.read_nums,
            'thumbUpNums': thumb_nums,
            'isThumbUp': isThumb,
            'commentList': comment_arr,
        })
        item.read_nums = int(item.read_nums) + 1
        item.save()
    return success_response('获取详情成功', arr)

def thumbUp(request):
    data_json = json.loads(request.body)
    if data_json.get('isThumbUp') == 1 or data_json.get('isThumbUp') == '1':
        thumb_item = ThumbUp.objects.create(
            content_id=data_json.get('id'),
            user_id=data_json.get('userId'),
            content_type=1
        )
        thumb_item.save()
        return success_response('成功')
    else:
        thumb_item = ThumbUp.objects.filter(
            content_id=data_json.get('id'),
            user_id=data_json.get('userId'),
            content_type=1,
        )
        thumb_item.delete()
        return success_response('取消成功')


def comment(request):
    data_json = json.loads(request.body)
    if not data_json.get('id'):
        comment_item = Comment.objects.create(
            user_id=data_json.get('userId'),
            topic_id=data_json.get('topicId'),
            content=data_json.get('content'),
            publish_date=data_json.get('publishDate'),
        )
        comment_item.save()
        return success_response('成功')
    else:
        comment_item = Comment.objects.get(
            topic_id=data_json.get('id'),
            user_id=data_json.get('userId'),
        )
        comment_item.content = data_json.get('content')
        comment_item.publish_date = data_json.get('publishDate')
        return success_response('删除成功')


def deleteComment(request):
    data_json = json.loads(request.body)
    comment_item = Comment.objects.filter(
        id=data_json.get('id'),
    )
    comment_item.delete()
    return success_response('删除成功')

