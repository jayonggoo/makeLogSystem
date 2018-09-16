from djcelery import celery
from subprocess import call

import subprocess

@celery.task(name='tasks.add')
def add(x, y):
    return x + y

@celery.task(name='tasks.sleeptask')
def sleeptask(i):
    from time import sleep
    sleep(i)
    return i

@celery.task(name='tasks.setCommnadOrder')
def setCommnadOrder():
    tmp = call('pwd')
    print(tmp)
	#makeFilebeat('filebeats.yml')
	#call('./filebeat run')
	#command = './filebeat run -d "publish"'
    command = './filebeat run -d "publish"'
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
