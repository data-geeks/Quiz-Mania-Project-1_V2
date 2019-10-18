from django.shortcuts import render,reverse,redirect
from django.http import Http404,HttpResponseRedirect,HttpResponse  
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User 
from TestTime.models import Score
from .models import Working_Test
from django.core.files.storage import FileSystemStorage 

# Create your views here.

def redirect_stats(request):
    if request.user.email == 'adhocnetworks@adhoc.co.in':
        return redirect('admin_portal')
    else:
        return HttpResponseRedirect('login_reg')

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
        if request.method == 'POST':
            course_name = request.POST['cname']
            course_category = request.POST['category']
            course_duration = request.POST['duration']
            course_level = request.POST['level']
            test = Working_Test(TestName=course_name,TestCategory=course_category,Duration=course_duration,Level=course_level)
            test.save()

            uploaded_file = request.FILES['test_file']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file) 
               
            return HttpResponseRedirect('admin_portal')
        else:
            return HttpResponse(request,"Please Contact Pykid...error has arrived")

