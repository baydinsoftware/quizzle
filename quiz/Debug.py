from quiz.models import Quiz, Question, Answer, Result, Value

questions = Quiz.objects.filter(quiz__id = 1)
print questions

filtered_set = {}
for question in questions:
    for answers in question.answer_set.all():
        filtered_set[answers.title] = Value.objects.filter(answer__title = answers.title)

print filtered_set         
#for answers in question.answer_set.all():
        #values = request.POST[answers.title] ##Don't want POST data
#        values = request.POST.get(answers.title, None)
#        if values != None:
#            for value in values:
#                res = value.result
#                val = value.value
#                res.votes += val
                
