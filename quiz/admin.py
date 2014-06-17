from django.contrib import admin
from quiz.models import Quiz, Result, Question, Answer, Value



#inlines
class ValueInline(admin.TabularInline):
    model = Value
    extra = 1
    
class QuestionsInline(admin.TabularInline):
    model = Question
    extra = 1
    
class ResultsInline(admin.TabularInline):
    model = Result
    extra = 1
    

#models   
class QuizAdmin(admin.ModelAdmin):
    inlines = (QuestionsInline,ResultsInline,)

class AnswerAdmin(admin.ModelAdmin):
    inlines = (ValueInline,)
    
# Register your models here.
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer, AnswerAdmin)

