from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from utils.util import success_response, error_response, unauth
import requests
import json
from .models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    data_json = json.loads(request.body)
    code = data_json.get('code')
    url = 'https://api.weixin.qq.com/sns/jscode2session'
          # '=0193d351264b4189f9c77c1a5eb56945&js_code=053eReGa1iPxyA0yDjJa17kRHV2eReGZ&grant_type=authorization_code '
    params = {
        'appid': 'wx3335aa84903f6375',
        'secret': '0193d351264b4189f9c77c1a5eb56945',
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    # 请求微信，拿到openid
    res = requests.get(url, params)
    res = json.loads(res.text)
    if not User.objects.filter(openid=res.get('openid')):
        user = User.objects.create()
        user.code = code
        user.openid = res.get('openid')
        user.user_name = data_json.get('nickName')
        user.avatar_url = data_json.get('avatarUrl')
        user.city = data_json.get('city')
        user.province = data_json.get('province')
        user.save()
    # response = requests.get(url=url, params=params)  # 用的是params
    # return JsonResponse(response, safe=False)
    return success_response('登陆成功', res)



def auth(request):
    data_json = json.loads(request.body)
    code = data_json.get('code')
    url = 'https://api.weixin.qq.com/sns/jscode2session'
          # '=0193d351264b4189f9c77c1a5eb56945&js_code=053eReGa1iPxyA0yDjJa17kRHV2eReGZ&grant_type=authorization_code '
    params = {
        'appid': 'wx3335aa84903f6375',
        'secret': '0193d351264b4189f9c77c1a5eb56945',
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    # 请求微信，拿到openid
    res = requests.get(url, params)
    res = json.loads(res.text)
    if not User.objects.filter(openid=res.get('openid')):
        user = User.objects.create()
        user.code = code
        user.openid = res.get('openid')
        user.user_name = data_json.get('nickName')
        user.avatar_url = data_json.get('avatarUrl')
        user.city = data_json.get('city')
        user.province = data_json.get('province')
        user.save()
    # response = requests.get(url=url, params=params)  # 用的是params
    # return JsonResponse(response, safe=False)
    return success_response('登陆成功', res)

def loginByCard(request):
    data_json = json.loads(request.body)
    userId = data_json.get('userId')
    res = json.loads(request.body)
    if User.objects.filter(
        openid=userId,
        card_id=res.get('cardId'),
        card_password=res.get('cardPassword')
    ):
        return success_response('登陆成功', res)
    elif User.objects.filter(
        card_id=res.get('cardId'),
        card_password=res.get('cardPassword')
    ):
        user = User.objects.filter(
            card_id=res.get('cardId'),
            card_password=res.get('cardPassword')
        )
        user = user[0]
        user.openid = userId
        user.save()
        return success_response('初次登陆成功', res)
    else:
        return error_response('账号密码错误，或账号不存在', res)

def adminLogin(request):
    data_json = json.loads(request.body)
    code = data_json.get('code')
    card_id = data_json.get('cardId')
    card_password = data_json.get('cardPassword')
    if User.objects.filter(card_id=card_id, card_password=card_password):
        return success_response('登陆成功')
    return error_response('登陆失败，请检查账号或者密码')


def userList(request):
    users = User.objects.all()
    arr = []
    for user in users:
        if user.openid == 'mock': continue
        arr.append({
            'id':user.id,
            'userId': user.openid,
            'cardId': user.card_password,
            'cardPassword': user.card_password,
            'userName': user.user_name,
            'userIdentity': user.user_identity,
            'userAvator': user.avatar_url,
        })
    return success_response('获取成功', arr)

def importUser(request):
    data_json = json.loads(request.body)
    users = data_json.get('arr')
    for user in users:
        if User.objects.filter(
            card_id=user['cardId']
        ): continue
        newUser = User.objects.create(
            # openid= user['userId'],
            card_id= user['cardId'],
            card_password= user['cardPassword'],
            user_identity= user['userIdentity'],
            # user_name= user['userName'],
            # avatar_url= user['userAvator'],
        )
        newUser.save()
    return success_response('导入成功')


def delete(request):
    data_json = json.loads(request.body)
    id = data_json.get('id')
    user = User.objects.filter(id=id)
    if user:
        user = user[0]
        user.delete()
    return success_response('删除成功')

def edit(request):

    data_json = json.loads(request.body)
    id = data_json.get('id')
    print(id)
    user = User.objects.filter(id=id)
    if user:
        user = user[0]
        user.card_id = data_json.get('cardId')
        user.openid = data_json.get('userId')
        user.card_password = data_json.get('cardPassword')
        user.user_identity = data_json.get('userIdentity')
        user.avatar_url = data_json.get('userAvator')
        user.user_name = data_json.get('userName')
        user.save()
        return success_response('修改成功')
    return error_response('用户不存在')

