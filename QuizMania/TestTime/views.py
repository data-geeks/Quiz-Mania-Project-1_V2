from django.shortcuts import render
from django.http import HttpResponseRedirect
from login_register.views import *  # this is imported to work with User database of Django
from .models import Questions
# Create your views here.

# opens the base.html page first initially which is rendered or dynamically changed using next test function
def initial(request):
    if request.user.is_authenticated:
        return render(request,'base.html')
    else:
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
# 1st Question in table should be same as Question written in base.html file
def test(request):
    if request.user.is_authenticated:
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test':Questions.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Questions.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return HttpResponseRedirect("login_reg")

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")