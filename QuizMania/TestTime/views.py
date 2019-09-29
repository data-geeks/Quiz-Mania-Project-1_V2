from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from login_register.views import *
from .models import Questions
# Create your views here.

def initial(request):
    if request.user.is_authenticated:
        return render(request,'base.html')
    else:
        return HttpResponseRedirect("login_page")

def test(request):
    if request.user.is_authenticated:
        answer = request.POST.get('opsi')
        value = request.POST['question_value']
        value = int(value)+1
        score = request.POST['score']
        score = int(score)
        wrong = request.POST['wrong']
        wrong = int(wrong)
        context = {
            'test':Questions.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong
        }
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        if str(answer) == Questions.objects.get(id=value-1).Answer:
            context['score'] += 1
        else:
            context['wrong'] += 1
        if context['score'] == 2:
            return HttpResponseRedirect("login_reg")
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        return render(request,'testpage.html',context)
    else:
        return HttpResponseRedirect("login_page")