from django.shortcuts import render,reverse
from django.http import Http404,HttpResponseRedirect,HttpResponse  
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User 
from TestTime.models import Score
# Create your views here.
def index(request):
    return render(request,"QuizMania_V2/Catalog.html")

def admin(request):
    if not request.user.is_authenticated:  # to check if session for user has been terminated successfully
        return HttpResponseRedirect(reverse('login_page'))
    else:
        if request.user.email == 'adhocnetworks@adhoc.co.in':
            return render(request,'QuizMania_V2/admin.html')
        else:
            return HttpResponseRedirect('login_reg')
def student_data(request):
    email = request.POST['search']
    if not request.user.is_authenticated:  # to check if session for user has been terminated successfully
        return HttpResponseRedirect(reverse('login_page'))
    else:
        score = Score.objects.filter(Email=email)
        return render(request,"QuizMania_V2/stats.html",{'scoreboard':score})

def add_test(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login_page'))
    else:
        course_name = request.POST['cname']
        course_category = request.POST['category']
        course_duration = request.POST['duration']
        course_level = request.POST['level']
        return render(request,'QuizMania_V2/admin.html')

