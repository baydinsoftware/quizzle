from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from quiz.models import Quiz,Answer,Question,Result,Value
from django.views import generic
from django.utils import timezone
from django.forms import ModelForm
from django import forms
import itertools

# Create your views here.

def main(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz__id = quiz_id)
    number_ans = {}
    for question in questions:
        number_ans[question.title] = 0
        for answers in question.answer_set.all():
            number_ans[question.title] += 1
    
    print number_ans
    #iterator=itertools.count()
    return render(request, 'quiz/main.html', {'questions':questions,'number_ans':number_ans,'quiz':quiz})
    
    
def submit(request,quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz__id = quiz_id)
    results = Result.objects.filter(quiz__id = quiz_id)
    resultsDict = {}
    
    for result in results:
        result.votes = 0
        result.save()
        
        
    print request.POST
    for question in questions:
        #values = request.POST[answers.title]
        ans = Answer.objects.get(pk=request.POST[question.title])
        if ans != None:
            val = Value.objects.filter(answer__title = ans.title)
            for value in val:
                result = value.result
                result.votes = value.value
                result.save()
            
                
    return HttpResponseRedirect(reverse('quiz:result', args =(quiz.id,)))
    

def result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    quiz_results = Result.objects.filter(quiz__id = quiz_id)
    best_result = quiz_results[0]
    threshold = 9000
    
    for result in quiz_results:
        if result.votes > best_result.votes:
            best_result = result
           
    ### secondaries 
    #secondary_results = []
    #for result in quiz_results:
    #    if result.votes > threshold:
    #        secondary_results.append(result)
            
    return render(request, 'quiz/result.html', {'best_result':best_result,}) #'second_results': secondary_results})
    

