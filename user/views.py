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