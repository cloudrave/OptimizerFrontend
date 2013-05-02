from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

def display_problem_prompt(request, prob):
    prob = Problem.objects.get(url=prob)

    algs = Algorithm.objects.filter(is_visible=True)

    extra_context = {
        'problem' : prob,
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


### INTERNAL ###
def solve(prob, alg):
    sol = Solution(prob=prob)

    sol.serialized_vars = "{}"

    sol.save()

    return sol
