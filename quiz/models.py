from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    text= models.CharField(max_length=1000)
    option_A = models.CharField(max_length=500)
    option_B = models.CharField(max_length=500)
    option_C = models.CharField(max_length=500)
    option_D = models.CharField(max_length=500)
    correct = models.CharField(max_length=500)
    
    def get_options(self):
        return [
            (self.option_A, self.option_A),
            (self.option_B, self.option_B),
            (self.option_C, self.option_C),
            (self.option_D, self.option_D),
            
        ]
    def check_ans(self,choice):
        if choice == self.correct:
            return True
        else:
            return False
        
class Adv(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    text= models.CharField(max_length=1000)
    option_A = models.CharField(max_length=500)
    option_B = models.CharField(max_length=500)
    option_C = models.CharField(max_length=500)
    option_D = models.CharField(max_length=500)
    correct = models.CharField(max_length=500)
    
    def get_options(self):
        return [
            (self.option_A, self.option_A),
            (self.option_B, self.option_B),
            (self.option_C, self.option_C),
            (self.option_D, self.option_D),
            
        ]
    def check_ans(self,choice):
        if choice == self.correct:
            return True
        else:
            return False
        
class Quiz_result(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    
class Result(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    result = models.PositiveIntegerField("quiz_result")