from django.http import HttpResponse
from django.shortcuts import render
from apps.admin.models import Question

# Create your views here.
def index(request):
    """
    질문 목록 출력
    """
    question_list = Question.objects.order_by('-created_at')
    context = {'question_list' : question_list}

    return render(request, 'pybo/question_list.html', context)