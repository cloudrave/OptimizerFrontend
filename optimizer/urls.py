from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # home page displays problems to solve
    url(r'^$', 'frontend.views.display_problems'),

    # displays problem prompts
    url(r'^p/(\w+)/$', 'frontend.views.display_problem_prompt'),

    # solves problem e.g. /s/fence/
    url(r'^s/(\w+)/(\w+)/$', 'frontend.views.display_solution'),
)
