from django.shortcuts import render
from django.http import HttpResponseRedirect
from login_register.views import *  # this is imported to work with User database of Django
from .models import *
from django.contrib.auth.models import User
import datetime
# Create your views here.

def scores(request):
    if request.user.is_authenticated:
        
        context = {
            'score' : score,
            'username': request.user.username,
            'wrong' : wrong
        }
        if str(answer) == Docker_B.objects.get(id=value).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        return render(request,"result.html",context)
    else:
        return render(request,"index.html")


# displays the Questions from the Docker table
def docker_B(request):
    if request.user.is_authenticated:
        testname = request.POST.get('Testname')
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST.get('question_value')     # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Docker_B.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Docker_B.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Docker_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Docker_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


def aws_B(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(AWS_B.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == AWS_B.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': AWS_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == AWS_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def redhat_B(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Redhat_B.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Docker_B.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Redhat_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Redhat_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def python_B(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Python_B.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Python_B.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Python_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Docker_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def tensorflow_B(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Tensorflow_B.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Tensorflow_B.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Tensorflow_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Tensorflow_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def computervision_B(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(ComputerVision_B.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == ComputerVision_B.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': ComputerVision_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ComputerVision_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def kubernetes_B(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Kubernetes_B.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Kubernetes_B.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Kubernetes_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Docker_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def scikitlearn_B(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(ScikitLearn_B.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == ScikitLearn_B.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': ScikitLearn_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ScikitLearn_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def docker_I(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Docker_I.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Docker_I.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Docker_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Docker_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def aws_I(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(AWS_I.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == AWS_I.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': AWS_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Docker_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def redhat_I(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Redhat_I.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Redhat_I.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Redhat_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Docker_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def python_I(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Python_I.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Python_I.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Python_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Python_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def tensorflow_I(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Tensorflow_I.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Tensorflow_I.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Tensorflow_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Tensorflow_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def computervision_I(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(ComputerVision_I.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == ComputerVision_I.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': ComputerVision_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ComputerVision_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def kubernetes_I(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Kubernetes_I.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Kubernetes_I.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Kubernetes_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Kubernetes_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def scikitlearn_I(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(ScikitLearn_I.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == ScikitLearn_I.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': ScikitLearn_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ScikitLearn_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def docker_A(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Docker_A.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Docker_A.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Docker_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Docker_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def aws_A(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(AWS_A.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == AWS_A.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': AWS_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == AWS_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def redhat_A(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Redhat_A.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Redhat_A.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Redhat_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Redhat_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def python_A(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Python_A.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Python_A.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Python_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Python_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def tensorflow_A(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Tensorflow_A.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Tensorflow_A.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Tensorflow_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Tensorflow_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def computervision_A(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(ComputerVision_A.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == ComputerVision_A.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': ComputerVision_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ComputerVision_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def kubernetes_A(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(Kubernetes_A.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == Kubernetes_A.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': Kubernetes_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Kubernetes_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")


# displays the Questions from the table
def scikitlearn_A(request):
    if request.user.is_authenticated:
        testname = request.POST['Testname']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)

        maxi = len(ScikitLearn_A.objects.all())
        if maxi < value:
            context = {
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
             }
            if str(answer) == ScikitLearn_A.objects.get(id=value-1).Answer:
                context['score'] += 1  # if answer is right score ++
            else:
                context['wrong'] += 1  # if answer is wrong then wrong ++
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)

        context = {
            'test': ScikitLearn_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.first_name,
            'testname' : testname
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ScikitLearn_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        negative = round(0.3 * maxi)
        if context['wrong'] == negative:
            marks = Score(Email=request.user.username,TestName=context['testname'],Score=context['score'],Date=datetime.datetime.now())
            marks.save()
            return render(request,'result.html',context)
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")
