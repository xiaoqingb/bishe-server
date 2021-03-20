from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import JsonResponse
import requests

def index(request):
    """

    :param request:
    :return:
    """
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
    return HttpResponse(res)
    response = requests.get(url=url, params=params)  # 用的是params
    return JsonResponse(response, safe=False)
    # return HttpResponse(template.render(context, request))
