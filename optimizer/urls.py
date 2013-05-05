from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, RedirectView

from django.contrib import admin
admin.autodiscover()

from frontend.views import *

urlpatterns = patterns('',
    # enables admin
    url(r'^admin/', include(admin.site.urls)),

    # home page displays problems to solve
    url(r'^$', display_problems),

    # displays problem prompts e.g. /p/fence/
    url(r'^p/(\w+)/$', display_problem_prompt),



    ### AJAX ###

    # Returns JSON solution for problem.  e.g. /jsolve/fence/pso/
    url(r'^jsolve/(\w+)/(\w+)/$', solve),

    url(r'^start$', start, name='start'),
    url(r'^ajax-upload$', import_uploader, name='my_ajax_upload'),

    url(r'^updateFileInput/(\d+)/$', update_file_input),



    ### WRITEUP ###
    url(r'^about/', include('writeup.urls')),


)
