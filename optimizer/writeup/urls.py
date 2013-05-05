from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, RedirectView

urlpatterns = patterns('',

    ### WRITEUP ###

    url(r'^final/$', TemplateView.as_view(template_name="writeup/final.html")),
   

)
