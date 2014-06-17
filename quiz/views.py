from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from quiz.models import Quiz,Answer,Question,Result,Value
from django.views import generic
from django.utils import timezone
from django.forms import ModelForm
from django import forms

# Create your views here.

def main(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz__id = quiz_id)
    filtered_set = {}
    for question in questions:
        for answers in question.answer_set.all():
            filtered_set[answers.title] = Value.objects.filter(answer__title = answers.title)
    return render(request, 'quiz/main.html', {'questions':questions,'filtered_set':filtered_set,'quiz':quiz})
    
    
    
def submit(request,quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz__id = quiz_id)
    results = Result.objects.filter(quiz__id = quiz_id)
    resultsDict = {}
    
    for question in questions:
        for answers in question.answer_set.all():
            #values = request.POST[answers.title]
            values = request.POST.get(answers.title, None)
            if values != None:
                for value in values:
                    res = value.result
                    val = value.value
                    res.votes += val
                
    return HttpResponseRedirect(reverse('quiz:result', args =(quiz.id,)))
    



def result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    quiz_results = Result.objects.filter(quiz__id = quiz_id)
    best_result = quiz_results[0]
    for result in quiz_results:
        if result.votes > best_result.votes:
            best_result = result
    
    return render(request, 'quiz/result.html', {'best_result':best_result})
    

