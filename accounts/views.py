from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import SignUp

from .models import Profile
# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUp

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            profile = Profile(user=user)
            profile.save()
            messages.success(request, "Signup successful! Welcome to the platform.")
            return redirect('dashboard')  # Redirect to the dashboard on success
        else:
            messages.error(request, "Signup failed. Please check the information provided and try again.")
            return render(request, 'signup.html', {'form': form})  # Display the form with errors
    else:
        form = SignUp()
    return render(request, 'signup.html', {'form': form})

    
@login_required
def profile_page(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile.html',{'profile':profile,'user':request.user})
