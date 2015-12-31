from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
            Return the last five published questions.
        :return:
        """
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


#def index(request):
    # display the latest 5 poll questions in the system separated by commas, according to publication date
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {
#        'latest_question_list': latest_question_list
#    }
#    return render(request, 'polls/index.html', context)


#def detail (request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})


#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        # request.POST is a dictionary like object that lets you access submitted data by key name, in this case request.POST['choice]
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # it will raise KeyError if choice wasn't provided in Post data.
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form.
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': 'You didn\'t select a choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # after incrementing the choice count, the code returns an HttpResponseRedirect
        #the reverse() function helps avoid having to hardcode a URL in the view function.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

