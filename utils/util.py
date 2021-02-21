from django.http import JsonResponse

HttpCode = {
    'ok': 1,
    'error': 0,
    'unauth': 403,
}


def result(code=1, message="", data=None):
    print(data)
    json_dict = {"code": code, "message": message, "data": data}
    # if kwargs and isinstance(kwargs, dict) and kwargs.keys():
    #     json_dict.update(kwargs)
    return JsonResponse(json_dict, safe=False)


# 封装返回函数
def success_response(message='成功', data=None):
    """
    成功返回的公共函数
    :param message: 自定义信息
    :param data:  数据
    :return: 调用上方的result
    """
    # return JsonResponse(data)

    return result(HttpCode['ok'], message, data)


def error_response(message="", data=None):
    return result(HttpCode['error'], message, data)


def unauth():
    return result(HttpCode['unauth'], '用户未登陆')
