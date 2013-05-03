from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

from ajaxuploader.views import AjaxFileUploader

import os
FRONTEND_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)))

from frontend.models import *

@csrf_exempt
def start(request):
    csrf_token = get_token(request)
    return render_to_response('import.html', {'csrf_token': csrf_token},
           context_instance = RequestContext(request))

import_uploader = AjaxFileUploader()

def display_problems(request):
    probs = Problem.objects.filter(is_visible=True)

    extra_context = {
        'problems' : probs,
    }

    return render_to_response("home.html",
                              extra_context,
                              context_instance=RequestContext(request))

def display_problem_prompt(request, prob):
    prob = Problem.objects.get(url=prob)
    inputs = Input.objects.filter(problem=prob)
    file_inputs = FileInput.objects.filter(problem=prob)

    algs = Algorithm.objects.filter(is_visible=True)

    extra_context = {
        'problem' : prob,
        'inputs'  : inputs,
        'file_inputs':file_inputs,
        'algorithms': algs,
    }

    return render_to_response("frontend/problem.html",
                              extra_context,
                              context_instance=RequestContext(request))


### AJAX ###
@csrf_exempt
def solve(request, prob, alg):
    data = request.POST

    prob = Problem.objects.get(url=prob)
    alg = Algorithm.objects.get(url=alg)

    inputs = Input.objects.filter(problem=prob)
    finputs = FileInput.objects.filter(problem=prob)
        

    print "Inputs: %s" % str(inputs)
    
    # specify problem and algorithm
    args = [prob.key,alg.key]

    # initialize inputs
    for input in inputs:
        print "checking input: %s" % input
        order = str(input.order)
        try:
            input.value = data[order]
        except:
            return HttpResponse("Error: Not enough variables provided!")
        args += [input.value]

    i = 0
    for finput in finputs:
        if i == 0:
            n = 'req1.csv'
        elif i == 1:
            n = 'pref1.csv'
        else:
            return HttpResponse("Too many files.")
        #file_with_quotes = os.path.join("media", finput.file.name)
        file = os.path.join("media", n)
        abs_url = os.path.join(FRONTEND_ROOT, "..", file)
        abs_url_quotes = "\"" + abs_url + "\""
        args += [abs_url_quotes]
        i += 1

    # get jar file
    path = os.path.join(FRONTEND_ROOT, '..', 'media', 'jarfile')
    print path
    jarfile = os.popen("ls -1tr %s | tail -n 1" % path).read().replace('\n','').replace('\r','')
    print jarfile

    command = "java -jar " + os.path.join(FRONTEND_ROOT, '..', 'media', 'jarfile', jarfile)
    for arg in args:
        command += " " + str(arg)

    # run Java backend
    print command
    response = os.popen(command)

    return HttpResponse(response)

@csrf_exempt
def update_file_input(request, file_input_id):
    file_input = FileInput.objects.get(id=file_input_id)

    print request.GET['fname']

    file_input.file = "uploads/" + request.GET['fname']
    file_input.save()

    return HttpResponse("success")
