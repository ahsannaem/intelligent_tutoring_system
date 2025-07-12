from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Question, Quiz_result, Result

class QuestionModelTest(TestCase):

    def setUp(self):
        self.question = Question.objects.create(
            id=1,
            text="What is the capital of France?",
            option_A="Berlin",
            option_B="Madrid",
            option_C="Paris",
            option_D="Rome",
            correct="Paris"
        )

    def test_question_creation(self):
        """Test that the Question is created correctly."""
        self.assertEqual(self.question.text, "What is the capital of France?")
        self.assertEqual(self.question.correct, "Paris")

    def test_get_options(self):
        """Test that get_options returns the correct options."""
        options = self.question.get_options()
        self.assertEqual(len(options), 4)
        self.assertIn(("Paris", "Paris"), options)
        self.assertIn(("Berlin", "Berlin"), options)

    def test_check_ans_correct(self):
        """Test that check_ans returns True for correct answer."""
        self.assertTrue(self.question.check_ans("Paris"))

    def test_check_ans_incorrect(self):
        """Test that check_ans returns False for incorrect answer."""
        self.assertFalse(self.question.check_ans("Berlin"))


class QuizResultModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.question = Question.objects.create(
            id=1,
            text="What is the capital of France?",
            option_A="Berlin",
            option_B="Madrid",
            option_C="Paris",
            option_D="Rome",
            correct="Paris"
        )
        self.quiz_result = Quiz_result.objects.create(
            user=self.user,
            question=self.question,
            answer="Paris",
            is_correct=True
        )

    def test_quiz_result_creation(self):
        """Test that the Quiz_result is created correctly."""
        self.assertEqual(self.quiz_result.user, self.user)
        self.assertEqual(self.quiz_result.answer, "Paris")
        self.assertTrue(self.quiz_result.is_correct)


class ResultModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.result = Result.objects.create(
            user=self.user,
            result=8  # Example score
        )

    def test_result_creation(self):
        """Test that the Result is created correctly."""
        self.assertEqual(self.result.user, self.user)
        self.assertEqual(self.result.result, 8)

