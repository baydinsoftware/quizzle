from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    #submitted = models.BooleanField()
#    url = models.URLField(max_length = 200)
    def __unicode__(self):
        return self.title
     
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    title = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.title
        
class Answer(models.Model):
    question = models.ForeignKey(Question)
    
    image = models.ImageField(upload_to='answers_images')
    title = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.title
    
    
class Result(models.Model):
    quiz = models.ForeignKey(Quiz)
    image = models.ImageField(upload_to='results_images')
    
    name = models.CharField(max_length = 200) #use for url
    description = models.TextField()
    second_description = models.TextField(blank=True)
    votes = models.IntegerField(default = 0)
 
    def __unicode__(self):
        return self.name
        
class Value(models.Model):
    answer = models.ForeignKey(Answer)
    result = models.ForeignKey(Result)
    
    value = models.IntegerField()
    def __unicode__(self):
        return str(self.result) +''+ str(self.value)
        
class SecondResult(models.Model):
    result = models.ForeignKey(Result)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    
        
# from quiz.models import Quiz, Question, Answer, Result, Value
    
