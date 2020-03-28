from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

import task_manager.task_manager_db_helper as tm_db

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = tm_db.get_all_tasks()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'task_manager/index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'task_manager/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'task_manager/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'task_manager/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('task_manager:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'task_manager/results.html', {'question': question})

