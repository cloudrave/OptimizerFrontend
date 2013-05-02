from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # enables admin
    url(r'^admin/', include(admin.site.urls)),

    # home page displays problems to solve
    url(r'^$', 'frontend.views.display_problems'),

    # displays problem prompts e.g. /p/fence/
    url(r'^p/(\w+)/$', 'frontend.views.display_problem_prompt'),

    # solves problem e.g. /s/fence/pso/
    url(r'^s/(\w+)/(\w+)/$', 'frontend.views.display_solution'),

    ### AJAX ###

    # Returns JSON solution for problem.  e.g. /jsolve/fence/pso/
    url(r'^jsolve/(\w+)/(\w+)/$', 'frontend.views.'),
)
