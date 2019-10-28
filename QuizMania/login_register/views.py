
from django.shortcuts import render,reverse
from django.http import Http404,HttpResponseRedirect,HttpResponse  
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User 
from TestTime.models import Score,Data
# Create your views here.

#this is to open the login and registeration page when user comes on website first time
def login_reg(request):
    if  not request.user.is_authenticated:
        return render(request,'index.html') # if user is not logged in open login form
    else:
        context = {
            "user":request.user
        }
        #return HttpResponseRedirect(reverse('login_page'))
        return render(request,'Catalog.html',context) # if user is logged in and again redirects to base url then show main catalog page

# this is to extract user data from registration form
def register(request):
    firstname  = request.POST['firstname']
    email = request.POST['email']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']
    if password == confirmpassword: 
        # adding the user details inside the database(default user database is being used)
        user = User.objects.create_user(username=email,first_name=firstname,email=email,password=password)
        user.save()
        data = Data(Name=firstname,Email=email,Password=password)
        data.save()
        # need to add a middle page or something which shows that Registration is Successful

        return render(request,"index.html") # after registration,send the user back to login page
    else:
        # need to work in this area that if user enters incorrect password then just prompt them for it
        raise Http404("Oops you entered incorrect password") # It gives a error page which tells if user has entered incorrect password

# this is to check the user has entered valid credentials while log in
def login_check(request):
    if request.user.is_authenticated:
        return render(request,'Catalog.html')
    # fetch the email and password to check login credentials
    email = request.POST['email']  
    password = request.POST['password']

    # set specially for admin of the page
    if email =='adhocnetworks@adhoc.co.in':
        user = authenticate(request,username=email,password=password)
        login(request,user)
        return HttpResponseRedirect('/admin_portal')

    # checks the credentials using default authenticate function
    user = authenticate(request,username=email,password=password)

    if user is not None: # user gets some value if user enters valid credentials
        login(request,user)  # creates a session for the user
        #return HttpResponseRedirect(reverse('login_page'))
        return HttpResponseRedirect(reverse('login_page')) # c is send to Catalog page which are set by JS in Catalog.html page
    else:
        return render(request,"index.html")  # open login page if user enters invalid credentials

# this is to delete cookies of user when log out
def logout_check(request):
    logout(request) # deletes the session of the user
    # as soon as user is logged out open the index page again
    if not request.user.is_authenticated:  # to check if session for user has been terminated successfully
        return HttpResponseRedirect(reverse('login_page'))
    else:
        return HttpResponseRedirect(reverse('logged_out'))
        
def stats(request):
    if not request.user.is_authenticated:  # to check if session for user has been terminated successfully
        return HttpResponseRedirect(reverse('login_page'))
    else:
        score = Score.objects.filter(Email=request.user.username)
        return render(request,"stats.html",{'scoreboard':score})
