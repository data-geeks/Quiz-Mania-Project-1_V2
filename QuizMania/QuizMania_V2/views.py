from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"QuizMania_V2/index.html")

