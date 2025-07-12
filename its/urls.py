"""
URL configuration for its project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path
from its import views
from accounts import views as accounts_views
from django.contrib.auth.views import LoginView,LogoutView
from quiz import views as quiz_views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('admin/', admin.site.urls),
    path('quiz_depreciated/',views.quizpage, name = 'quiz'),
    path('index/',views.index, name= 'index'),
    path('progress/',views.progress),
    path('login/', LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', views.logout_view,name = 'logout'),
    path("dashboard/", views.dashboard, name= "dashboard"),
    path('signup/',accounts_views.signup_view, name= 'signup'),
    path('quiz/',quiz_views.take_quiz, name='quiz'),
    path('logreq',quiz_views.logreq,name="logreq"), #for debugging purpose
    path('take/',quiz_views.take_quiz,name='takequiz'),
    path("study/",views.study,name="study"),
    path('profile/',accounts_views.profile_page,name="profile"),
    path('new/', quiz_views.new_view, name='new'),        
    path('mid/', quiz_views.mid_view, name='mid'),         
    path('advance/', quiz_views.advance_view, name='advance'),  
]