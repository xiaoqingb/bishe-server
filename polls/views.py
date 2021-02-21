from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import JsonResponse
from django.urls import reverse
from .models import Choice, Question, User
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

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    queryset = User.objects.all()
    return queryset
    question = get_object_or_404(User, user_id=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.user_name += 1
        selected_choice.save()

def vote(request, question_id):
    question = get_object_or_404(User, pk=question_id)
    return question

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.user_name += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))