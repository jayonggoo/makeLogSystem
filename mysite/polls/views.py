from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from subprocess import call
from .models import Choice, Question, RegisterModel
import subprocess
import json

from polls import tasks

def test_celery(request):
	result = tasks.setCommnadOrder.delay()

	response_data = {}
	response_data['result'] = 'success'
	response_data['message'] = 'start'
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def index(request):
	#	setCommnadOrder()
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

def register(request):
	latest_data =RegisterModel.objects.order_by('-created_date')[:5]
	context = {'latest_data' : latest_data}
	return render(request, 'polls/register.html', context)

def detailRegister(request, data_id):
    registerModel = get_object_or_404(RegisterModel, pk=data_id)
    return render(request, 'polls/registerDetail.html', {'registerModel': registerModel})

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def setCommnadOrder():
	tmp = call('pwd')
	print(tmp)
	#makeFilebeat('filebeats.yml')
	#call('./filebeat run')
	#command = './filebeat run -d "publish"'
	command = 'nohup ./filebeat -e -d "publish"'
	subprocess.check_call(command.split())

def makeFilebeat(beatName):
	_beatName = beatName;
	print(_beatName);
	fw = open(_beatName, 'w')
	fw.write('filebeat.inputs:\n')
	fw.write('enabled: true\n')
	fw.write('paths:\n')
	fw.write('	- type: log\n')
	fw.write('	- /var/log/*.log\n')
	fw.write('output.elasticsearch:\n')
	fw.write(' hosts: ["localhost:9200"]\n')
	fw.close();
