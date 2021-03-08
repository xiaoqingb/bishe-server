from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from utils.util import success_response, error_response, unauth
import requests
import json
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    code = request.GET.get('code', '')
    url = 'https://api.weixin.qq.com/sns/jscode2session'
          # '=0193d351264b4189f9c77c1a5eb56945&js_code=053eReGa1iPxyA0yDjJa17kRHV2eReGZ&grant_type=authorization_code '
    params = {
        'appid': 'wx3335aa84903f6375',
        'secret': '0193d351264b4189f9c77c1a5eb56945',
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    print(code)
    res = requests.get('https://api.weixin.qq.com/sns/jscode2session', params)
    # return HttpResponse(res)
    # return JsonResponse(res)
    res = json.loads(res.text)
    if 'errcode' in res:
        return unauth()
    # response = requests.get(url=url, params=params)  # 用的是params
    # return JsonResponse(response, safe=False)
    return success_response('登陆成功', res)