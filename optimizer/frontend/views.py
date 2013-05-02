from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt


import os
FRONTEND_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)))

from frontend.models import *

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

    algs = Algorithm.objects.filter(is_visible=True)

    extra_context = {
        'problem' : prob,
        'inputs'  : inputs,
        'algorithms': algs,
    }

    return render_to_response("frontend/problem.html",
                              extra_context,
                              context_instance=RequestContext(request))

# Returns page with solution
def display_solution(request, prob, alg):
    prob = Problem.objects.get(url=prob)
    alg = Algorithm.objects.get(url=alg)

    solution = solve(prob, alg)

    extra_context = {
        'problem'  : prob,
        'algorithm': alg,
        'solution' : solution,
    }

    return render_to_response("frontend/solution.html",
                              extra_context,
                              context_instance=RequestContext(request))



### AJAX ###
@csrf_exempt
def solve(request, prob, alg):
    data = request.POST

    prob = Problem.objects.get(url=prob)
    alg = Algorithm.objects.get(url=alg)

    inputs = Input.objects.filter(problem=prob)

    for input in inputs:
        print "checking input: %s" % input

    sol = Solution(prob=prob)

    #print "FRONTEND_ROOT: %s" % FRONTEND_ROOT

    # specify problem and algorithm
    args = [prob.key,alg.key]

    args += [1000]

    command = "java -jar %s/backend.jar" % FRONTEND_ROOT
    for arg in args:
        command += " " + str(arg)

    # run Java backend
    response = os.popen(command)

    return HttpResponse(response)
