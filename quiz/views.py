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

#Checks If submited

def main(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz__id = quiz_id)
    requestTestQ = Question.objects.get(pk = 1)
    print request.GET.get(requestTestQ.title)
    print requestTestQ
    
    #change if statement if doesn't work
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
                    result.votes = value.value
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
        print best_result
        number_ans = {}
        for question in questions:
            number_ans[question.title] = 0
            for answers in question.answer_set.all():
                number_ans[question.title] += 1
        
    else:
        #otherwise we just display the form
        number_ans = {}
        for question in questions:
            number_ans[question.title] = 0
            for answers in question.answer_set.all():
                number_ans[question.title] += 1
        best_result = None
        submitted = False
        
    print submitted
    return render(request, 'quiz/main.html', {'questions':questions,'number_ans':number_ans,
    'quiz':quiz,'best_result':best_result,'submitted':submitted})
    
    
def submit(request,quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz__id = quiz_id)
    results = Result.objects.filter(quiz__id = quiz_id)
    resultsDict = {}
    
    for result in results:
        result.votes = 0
        result.save()
        
    
    for question in questions:
        #values = request.POST[answers.title]
        ans = Answer.objects.get(pk=request.POST[question.title])
        if ans != None:
            val = Value.objects.filter(answer__title = ans.title)
            for value in val:
                result = value.result
                result.votes = value.value
                result.save()
            
    t = loader.get_template('quiz/main.html')
    c = RequestContext(request, )
    
    #return HttpResponseRedirect(reverse('quiz:result', args =(quiz.id,)))
    return HttpResponseRedirect(reverse('quiz:main', args =(quiz.id,)),t.render(c))

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
