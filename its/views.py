from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from accounts.models import Profile

@login_required
def quizpage(request):
    if request.user.is_authenticated:
        return render(request,"quizpage.html")

def index(request):
    return render(request,"index.html")

    
@login_required
def progress(request):
    return render(request,"progress.html")

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)  # Retrieve the profile for the logged-in user
        quiz_count = profile.quiz_count  # Access the quiz_count attribute
        rank = profile.rank
        quiz_count = quiz_count *10
        context = {
                'quiz_count': quiz_count,  # Pass the quiz_count to the template
                'rank':rank
            }

        return render(request, "dashboard.html", context)
    else:
        return redirect('login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request,'registration.html')
    
@login_required
def study(request):
    return render(request,'study.html')


@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')



