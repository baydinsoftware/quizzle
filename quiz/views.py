from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from quiz.models import Quiz,Answer,Question,Result,Value,SecondResult
from django.views import generic
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from django.conf.urls import patterns, url
import itertools
import pdb

# Create your views here.



def main(request, quiz_id=1):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz__id = quiz_id)
    requestTestQ = questions[0]
     
    if request.GET.get(requestTestQ.title):
        
        results = Result.objects.filter(quiz__id = quiz_id)
        resultsDict = {}
    
        ##sets all results votes to 0
        for result in results:
            result.votes = 0
            result.save()
        
        
        for question in questions:
            #values = request.POST[answers.title]
            ##gets selected answer of question
            ans = Answer.objects.get(pk=request.GET[question.title])
            if ans != None:
                #finds the values associated with that answer
                val = Value.objects.filter(answer__title = ans.title)      
                
                #contributes the values to each result
                for value in val:
                    result = value.result
                    result.votes += value.value
                    result.save()
        
        ###processing results to find best
        
        #gets the new results
        quiz_results = Result.objects.filter(quiz__id = quiz_id)
        best_result = quiz_results[0]
        threshold = 9000
    
        for result in quiz_results:
            if result.votes > best_result.votes:
                best_result = result
                
        submitted = True
        number_ans = {}
        for question in questions:
            number_ans[question.title] = 0
            for answers in question.answer_set.all():
                number_ans[question.title] += 1
                
        second_results = SecondResult.objects.filter(result = best_result)
        
    else:
        #otherwise we just display the form
        number_ans = {}
        for question in questions:
            number_ans[question.title] = 0
            for answers in question.answer_set.all():
                number_ans[question.title] += 1
        best_result = None
        submitted = False
        second_results = None
        
    
    return render(request, 'quiz/main.html', {'questions':questions,'number_ans':number_ans,
    'quiz':quiz,'best_result':best_result,
    'submitted':submitted,'second_results':second_results})
    
    
def submit(request,quiz_id):
    
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    quiz_results = Result.objects.filter(quiz__id = quiz_id)
    questions = Question.objects.filter(quiz__id = quiz_id)
    results = Result.objects.filter(quiz__id = quiz_id)
    best_result = quiz_results[0]
    resultsDict = {}
    
    for result in results:
        result.votes = 0
        result.save()
       
    for question in questions:
            #values = request.POST[answers.title]
            ##gets selected answer of question
            ans = Answer.objects.get(pk=request.POST[question.title])
            
            
            print ans
            if ans != None:
                #finds the values associated with that answer
                val = Value.objects.filter(answer__title = ans.title)      
                
                #contributes the values to each result
                for value in val:
                    result = value.result
                    result.votes += value.value
                    result.save()
        
    for result in quiz_results:
            if result.votes > best_result.votes:
                best_result = result
                
    resultId = best_result.id
              
    #t = loader.get_template('quiz/main.html')
    #c = RequestContext(request, )
    
    #return HttpResponseRedirect(reverse('quiz:result', args =(quiz.id,)))
    return HttpResponseRedirect('/spirit/result/'+ str(resultId))

def result(request,result_id):
    ###processing results to find best
        
        
        #gets the new results
        #quiz_results = Result.objects.filter(quiz__id = quiz_id)
        #questions = Question.objects.filter(quiz__id = quiz_id)
        #best_result = quiz_results[0]
        #threshold = 9000
    
        #for result in quiz_results:
        #    if result.votes > best_result.votes:
        #        best_result = result
                
        best_result = Result.objects.get(id = result_id)
        second_results = SecondResult.objects.filter(result = best_result)
    
            
        return render(request, 'quiz/result.html', {'best_result':best_result,'second_results':second_results})
    
def twitter(request):
    return render(request, 'quiz/testshare.html')
