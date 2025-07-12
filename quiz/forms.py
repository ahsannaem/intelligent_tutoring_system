from django import forms
from .models import Question
import random
from django import forms
from .models import Question
import random

class QuizForm(forms.Form):
    def __init__(self,questions, *args, **kwargs):
        # Fetch questions directly from the database
        super(QuizForm, self).__init__(*args, **kwargs)

        # Create fields for each selected question
        for q in questions:
            self.fields[f'question_{q.id}'] = forms.ChoiceField(
                label=q.text,
                widget=forms.RadioSelect,
                choices=q.get_options()
            )


