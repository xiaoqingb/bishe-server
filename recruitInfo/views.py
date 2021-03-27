import time
from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from utils.util import success_response, error_response, unauth
import json
from user.models import UserFavorite, RecruitInfo, ThumbUp


def publish(request):
    data_json = json.loads(request.body)
    if data_json.get('id'):
        favorite_item = RecruitInfo.objects.get(recruit_id=data_json.get('id'))
    else:
        favorite_item = RecruitInfo.objects.create()
    favorite_item.job_description = data_json.get('jobDescription')
    favorite_item.job_responsibility = data_json.get('jobResponsibility')
    favorite_item.job_requirement = data_json.get('jobRequirement')
    favorite_item.job_type = data_json.get('jobType')
    favorite_item.salary = data_json.get('salary')
    favorite_item.publish_date = data_json.get('publishDate')
    favorite_item.recurit_end_date = data_json.get('recuritEndDate')
    favorite_item.e_mail = data_json.get('eMail')
    favorite_item.skill_tag_list = data_json.get('skillTagList')
    favorite_item.education_requirement = data_json.get('educationRequirement')
    favorite_item.publisher = data_json.get('publisher')
    favorite_item.company = data_json.get('company')
    favorite_item.address = data_json.get('address')
    favorite_item.image_url = data_json.get('imageUrl')
    favorite_item.status = data_json.get('status')
    favorite_item.save()
    return success_response('成功')


def delete(request):
    data_json = json.loads(request.body)
    favorite_item = RecruitInfo.objects.filter(
        recruit_id=data_json.get('id')
    )
    if favorite_item: favorite_item[0].delete()
    return success_response('删除成功')


def edit(request):
    data_json = json.loads(request.body)
    favorite_item = RecruitInfo.objects.get(
        recruit_id=data_json.get('id')
    )
    favorite_item.job_description = data_json.get('jobDescription')
    favorite_item.job_responsibility = data_json.get('jobResponsibility')
    favorite_item.job_requirement = data_json.get('jobRequirement')
    favorite_item.job_type = data_json.get('jobType')
    favorite_item.salary = data_json.get('salary')
    favorite_item.publish_date = data_json.get('publishDate')
    favorite_item.recurit_end_date = data_json.get('recuritEndDate')
    favorite_item.e_mail = data_json.get('eMail')
    favorite_item.skill_tag_list = data_json.get('skillTagList')
    favorite_item.education_requirement = data_json.get('educationRequirement')
    # favorite_item.is_collect=data_json.get('isCollect')
    # favorite_item.thumb_up_nums=data_json.get('thumbUpNums')
    # favorite_item.read_nums=data_json.get('readNums')
    favorite_item.publisher = data_json.get('publisher')
    favorite_item.company = data_json.get('company')
    favorite_item.address = data_json.get('address')
    favorite_item.image_url = data_json.get('imageUrl')
    favorite_item.save()
    return success_response('编辑成功')


def list(request):
    arr = []
    recruitList = RecruitInfo.objects.all()
    for item in recruitList:
        thumbUpNums = 0
        thumbs_list = ThumbUp.objects.filter(
            content_id=item.recruit_id,
        )
        if (thumbs_list):
            thumbUpNums = len(thumbs_list)
        arr.append({
            'id': item.recruit_id,
            'jobDescription': item.job_description,
            'jobResponsibility': item.job_responsibility,
            'jobRequirement': item.job_requirement,
            'jobType': item.job_type,
            'salary': item.salary,
            'publishDate': item.publish_date,
            'recuritEndDate': item.recurit_end_date,
            'eMail': item.e_mail,
            'skillTagList': item.skill_tag_list,
            'educationRequirement': item.education_requirement,
            # 'isCollect': item.is_collect,
            'thumbUpNums': thumbUpNums,
            'publisher': item.publisher,
            'company': item.company,
            'address': item.address,
            'imageUrl': item.image_url,
            'readNums': item.read_nums,
            'status': item.status,
        })
    return success_response('获取招聘列表成功', arr);


def detail(request):
    arr = []
    recruitList = RecruitInfo.objects.all().filter(recruit_id=request.GET.get('id'))
    isCollect = 0
    if UserFavorite.objects.filter(
        user_id=request.GET.get('userId'),
        content_id=request.GET.get('id'),
        content_type=2
    ):
        isCollect = 1
    isThumbUp = 0
    if ThumbUp.objects.filter(
        user_id=request.GET.get('userId'),
        content_id=request.GET.get('id'),
    ):
        isThumbUp = 1
    thumbUpNums = 0
    thumbs_list = ThumbUp.objects.filter(
        content_id=request.GET.get('id'),
    )
    if (thumbs_list):
        thumbUpNums = len(thumbs_list)
    for item in recruitList:
        arr.append({
            'id': item.recruit_id,
            'jobDescription': item.job_description,
            'jobResponsibility': item.job_responsibility,
            'jobRequirement': item.job_requirement,
            'jobType': item.job_type,
            'salary': item.salary,
            'publishDate': item.publish_date,
            'recuritEndDate': item.recurit_end_date,
            'eMail': item.e_mail,
            'skillTagList': item.skill_tag_list,
            'educationRequirement': item.education_requirement,
            # 'isCollect': item.is_collect,
            'thumbUpNums': item.thumb_up_nums,
            'readNums': thumbUpNums,
            'publisher': item.publisher,
            'isThumbUp': isThumbUp,
            'company': item.company,
            'address': item.address,
            'imageUrl': item.image_url,
            'status': item.status,
            'isCollect': isCollect,
        })
        item.read_nums = int(item.read_nums) + 1
        item.save()
    return success_response('获取详情成功', arr)


def favoriteEdit(request):
    data_json = json.loads(request.body)
    arr = []
    if data_json.get('isCollect') == 1 or data_json.get('isCollect') == '1':
        favorite_item = UserFavorite.objects.create(
            content_type=2,
            content_id=data_json.get('id'),
            user_id=data_json.get('userId')
        )
        favorite_item.save();
        return success_response('收藏成功', arr);
    else:
        items = UserFavorite.objects.filter(
            content_id=data_json.get('id'),
            user_id=data_json.get('userId'),
            content_type=2
        )
        for item in items:
            item.delete()

        return success_response('取消收藏成功', arr);



# 用户个人收藏列表
def userFavoriteList(request):
    res = []
    arr = []
    favorite_list = UserFavorite.objects.filter(
        user_id=request.GET.get('userId'),
        content_type=2,
    )
    for favorite_item in favorite_list:
        item = RecruitInfo.objects.all().filter(
            recruit_id=favorite_item.content
        )
        if item:
            item=item[0]
            arr.append({
                'id': item.recruit_id,
                'jobDescription': item.job_description,
                'jobResponsibility': item.job_responsibility,
                'jobRequirement': item.job_requirement,
                'jobType': item.job_type,
                'salary': item.salary,
                'publishDate': item.publish_date,
                'recuritEndDate': item.recurit_end_date,
                'eMail': item.e_mail,
                'skillTagList': item.skill_tag_list,
                'educationRequirement': item.education_requirement,
                # 'isCollect': item.is_collect,
                'thumbUpNums': item.thumb_up_nums,
                'publisher': item.publisher,
                'company': item.company,
                'address': item.address,
                'imageUrl': item.image_url,
                'status': item.status,
            })
    return success_response('成功', res);

def thumbUp(request):
    data_json = json.loads(request.body)
    apply_item = ThumbUp.objects.filter(content_id=data_json.get('id'), user_id=data_json.get('userId'))
    if apply_item:
        apply_item.delete()
        return success_response('取消成功');
    else:
        apply_item = ThumbUp.objects.create(
            content_id=data_json.get('id'),
            user_id=data_json.get('userId'),
        )
        apply_item.save();

    return success_response('成功');
