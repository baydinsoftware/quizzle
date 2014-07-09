from django.contrib import admin
from quiz.models import Quiz, Result, Question, Answer, Value, SecondResult



#inlines
class ValueInline(admin.TabularInline):
    model = Value
    extra = 3
    
class QuestionsInline(admin.TabularInline):
    model = Question
    extra = 1
    
class AnswersInline(admin.TabularInline):
    model = Answer
    extra = 4
    
class ResultsInline(admin.TabularInline):
    model = Result
    extra = 1
    
class SecResultInline(admin.TabularInline):
    model = SecondResult
    extra = 1
    
#models   
class QuizAdmin(admin.ModelAdmin):
    inlines = (QuestionsInline,ResultsInline)

class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswersInline,)
    
class AnswerAdmin(admin.ModelAdmin):
    inlines = (ValueInline,)
    
class ResultAdmin(admin.ModelAdmin):
    inlines = (SecResultInline,)
    
# Register your models here.
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)

