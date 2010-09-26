from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^test/$', 'core.views.test'),
)
