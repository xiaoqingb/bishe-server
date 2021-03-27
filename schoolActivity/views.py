import time
from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from utils.util import success_response, error_response, unauth
import json
from user.models import UserFavorite, RecruitInfo, SchoolActivity, Apply, User


def publish(request):
    data_json = json.loads(request.body)
    if data_json.get('id'):
        activity_item = SchoolActivity.objects.get(activity_id=data_json.get('id'))
    else:
        activity_item = SchoolActivity.objects.create()
    activity_item.activity_title = data_json.get('activityTitle')
    activity_item.activity_content = data_json.get('activityContent')
    activity_item.enter_start_date = data_json.get('enterStartDate')
    activity_item.enter_end_date = data_json.get('enterEndDate')
    activity_item.activity_start_date = data_json.get('activityStartDate')
    activity_item.activity_end_date = data_json.get('activityEndDate')
    activity_item.holder = data_json.get('holder')
    # activity_item.enter_nums = data_json.get('enterNums')
    # activity_item.read_nums = data_json.get('readNums')
    activity_item.is_collect = data_json.get('isCollect')
    activity_item.publisher = data_json.get('publisher')
    activity_item.activity_place = data_json.get('activityPlace')
    activity_item.image_url = data_json.get('imageUrl')
    activity_item.status = data_json.get('status')
    activity_item.save()
    return success_response('成功')


def delete(request):
    data_json = json.loads(request.body)
    activity_item = SchoolActivity.objects.filter(
        activity_id=data_json.get('id')
    )
    if activity_item: activity_item[0].delete()
    return success_response('删除成功')


def edit(request):
    data_json = json.loads(request.body)
    activity_item = SchoolActivity.objects.get(
        activity_id=data_json.get('id')
    )
    activity_item.activity_title = data_json.get('activityTitle')
    activity_item.activity_content = data_json.get('activityContent')
    activity_item.enter_start_date = data_json.get('enterStartDate')
    activity_item.enter_end_date = data_json.get('enterEndDate')
    activity_item.activity_start_date = data_json.get('activityStartDate')
    activity_item.activity_end_date = data_json.get('activityEndDate')
    activity_item.holder = data_json.get('holder')
    # activity_item.enter_nums = data_json.get('enterNums')
    # activity_item.read_nums = data_json.get('readNums')
    activity_item.is_collect = data_json.get('isCollect')
    activity_item.publisher = data_json.get('publisher')
    activity_item.activity_place = data_json.get('activityPlace')
    activity_item.status = data_json.get('status')
    activity_item.image_url = data_json.get('imageUrl')
    activity_item.save()
    return success_response('编辑成功')


def list(request):
    arr = []
    recruitList = SchoolActivity.objects.all()
    for item in recruitList:

        applyList = []
        apply_list = Apply.objects.filter(content_id=item.activity_id)
        for apply_item in apply_list:
            user_item = User.objects.get(openid=apply_item.user_id)
            applyList.append({
                "userId": user_item.openid,
                "cardId": user_item.card_id,
                "cardPassword": user_item.card_password,
                "nickName": user_item.user_name,
                "userAvator": user_item.avatar_url
            })

        arr.append({
            'id': item.activity_id,
            'activityTitle': item.activity_title,
            'activityContent': item.activity_content,
            'enterStartDate': item.enter_start_date,
            'enterEndDate': item.enter_end_date,
            'activityStartDate': item.activity_start_date,
            'activityEndDate': item.activity_end_date,
            'holder': item.holder,
            'enterNums': item.enter_nums,
            'readNums': item.read_nums,
            'isCollect': item.is_collect,
            'publisher': item.publisher,
            'activityPlace': item.activity_place,
            'status': item.status,
            'imageUrl': item.image_url,
            'list': applyList,
        })
    return success_response('获取活动列表成功', arr);


def detail(request):
    arr = []
    recruitList = SchoolActivity.objects.all().filter(activity_id=request.GET.get('id'))
    isCollect = 0
    if UserFavorite.objects.filter(
        user_id=request.GET.get('userId'),
        content_id=request.GET.get('id'),
        content_type=3
    ):
        isCollect = 1
    isApply = 0
    if Apply.objects.filter(
        user_id=request.GET.get('userId'),
        content_id=request.GET.get('id'),
    ):
        isApply = 1
    for item in recruitList:
        arr.append({
            'id': item.activity_id,
            'activityTitle': item.activity_title,
            'activityContent': item.activity_content,
            'enterStartDate': item.enter_start_date,
            'enterEndDate': item.enter_end_date,
            'activityStartDate': item.activity_start_date,
            'activityEndDate': item.activity_end_date,
            'holder': item.holder,
            'enterNums': item.enter_nums,
            'readNums': item.read_nums,
            'isCollect': item.is_collect,
            'publisher': item.publisher,
            'activityPlace': item.activity_place,
            'status': item.status,
            'imageUrl': item.image_url,
            'isApply': isApply,
        })
        item.read_nums = int(item.read_nums) + 1
        item.save()
    return success_response('获取详情成功', arr);


def favoriteEdit(request):
    data_json = json.loads(request.body)
    arr = []
    if data_json.get('isCollect') == 1 or data_json.get('isCollect') == '1':
        activity_item = UserFavorite.objects.create(
            content_type=3,
            content_id=data_json.get('id'),
            user_id=data_json.get('userId')
        )
        activity_item.save();
        return success_response('收藏成功', arr);
    else:
        items = UserFavorite.objects.filter(
            content_id=data_json.get('id'),
            user_id=data_json.get('userId'),
            content_type=3
        )
        for item in items:
            item.delete()

        return success_response('取消收藏成功', arr);



# 用户个人收藏列表
def userFavoriteList(request):
    res = []
    arr = []
    activity_list = UserFavorite.objects.filter(
        user_id=request.GET.get('userId'),
        content_type=3,
    )
    for activity_item in activity_list:
        item = SchoolActivity.objects.all().filter(
            activity_id=activity_item.content
        )
        if item:
            item=item[0]
            arr.append({
                'id': item.activity_id,
                'activityTitle': item.activity_title,
                'activityContent': item.activity_content,
                'enterStartDate': item.enter_start_date,
                'enterEndDate': item.enter_end_date,
                'activityStartDate': item.activity_start_date,
                'activityEndDate': item.activity_end_date,
                'holder': item.holder,
                'enterNums': item.enter_nums,
                'readNums': item.read_nums,
                'isCollect': item.is_collect,
                'publisher': item.publisher,
                'activityPlace': item.activity_place,
                'imageUrl': item.image_url,
                'status': item.status,
            })
    return success_response('成功', res);

def apply(request):
    data_json = json.loads(request.body)
    apply_item = Apply.objects.filter(activity_id=data_json.get('id'),user_id=data_json.get('userId'))
    if apply_item:
        apply_item.delete()
    else:
        apply_item = Apply.objects.create(
            content_id=data_json.get('id'),
            user_id=data_json.get('userId'),
        )
        apply_item.save();

    return success_response('成功');

def enterList(request):
    data_json = json.loads(request.body)
    res = []
    apply_list = Apply.objects.filter(content_id=data_json.get('id'))
    for apply_item in apply_list:
        user_item = User.objects.get(openid=apply_item.user_id)
        res.append({
            "userId": user_item.openid,
            "cardId": user_item.card_id,
            "cardPassword": user_item.card_password,
            "nickName": user_item.user_name,
            "userAvator": user_item.avatar_url
        })

    return success_response('成功', res);
