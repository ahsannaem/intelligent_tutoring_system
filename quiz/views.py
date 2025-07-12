import pickle,os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from .forms import QuizForm
from .models import Question as Questions, Quiz_result, Adv
import random


def writereq(req):
    with open("./request.txt", "w") as file:
        file.write(str(req))
    print("File request is saved")


def logreq(request):
    writereq(request)
    return HttpResponse(str(request))


@login_required
def quiz(request):
    questions = Question.objects.order_by('?')[:1]  # Fetch 1 random question
    if request.method == 'POST':
        form = QuizForm(questions, request.POST)
        if form.is_valid():
            for q in questions:
                answer = form.cleaned_data.get(f'answer_{q.id}')  # Use question ID for consistency
                quiz_result = Quiz_result(
                    user=request.user,
                    question=q,
                    answer=answer,
                    is_correct=answer == q.correct_answer
                )
                quiz_result.save()
            return redirect('quiz_results')
    else:
        form = QuizForm(questions)
    
    return render(request, 'quiz.html', {'form': form, 'questions': questions})

@login_required
def take_quiz(request):
    # Fetch or create the user's profile
    user = request.user
    profile, _ = Profile.objects.get_or_create(user=user)  # Fetch or create the user's profile
    
    # Determine the user's level
    correct_count = profile.quiz_count  # You can base the level on quiz count or other criteria
    model = loadmodel()
    level = model.predict([[correct_count]])[0]  # Assuming the model returns the predicted level as a number

    # Fetch questions based on user level
    if level == 0:
        questions = list(Questions.objects.all())  # Fetch from Questions model if level is 0
    else:
        questions = list(Adv.objects.all())  # Fetch from Adv model otherwise
    
    random.shuffle(questions)  # Shuffle the list of questions
    questions = questions[:10]  # Get the first 10 questions after shuffling

    if request.method == 'POST':
        correct_count = 0
        new_answers = {int(key.split('_')[1]): value for key, value in request.POST.items() if key.startswith('question_')}
        
        for question_id, user_answer in new_answers.items():
            if level == 0:
                q = Questions.objects.get(id=question_id)
            else:
                q = Adv.objects.get(id=question_id)

            if user_answer == q.correct:
                correct_count += 1

        # Update the user's level based on the new correct count
        level = model.predict([[correct_count]])[0]

        recommendations = [
            "Please focus on Basic concepts such as programming fundamentals and control structures.",
            "Focus on OOP concepts such as Objects, Classes, Abstraction, Inheritance, Polymorphism, etc.",
            "Move onto more advanced concepts such as low-level API calls and building some real-world projects."
        ]
        
        recommendation = recommendations[int(level)]
        profile.quiz_count += 1
        profile.save()
        
        return render(request, 'quiz_result.html', {
            'correct_count': correct_count,
            'total_questions': len(questions),
            'reco': recommendation,
            'level': 1,
        })
    else:
        form = QuizForm(questions)
    
    return render(request, 'take_quiz.html', {'form': form})


def loadmodel():
    model_path = os.path.join(settings.BASE_DIR, 'static', 'scripts', 'linear_regression_model.pkl')
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"The model file does not exist at: {model_path}")
    
    with open(model_path, 'rb') as file:
        return pickle.load(file)
    



def new_view(request):
    materials = "basic"
    """View for beginners (level 0) learning materials."""
    return render(request, 'new.html', {
        'materials': materials,
        'level': 0
    })

def mid_view(request):
    materials = "medium"
    """View for intermediate (level 1) learning materials."""
    return render(request, 'mid.html', {
        'materials': materials,
        'level': 1
    })

def advance_view(request):
    materials = "Advance"
    """View for advanced (level 2) learning materials."""
    return render(request, 'advance.html', {
        'materials': materials,
        'level': 2
    })