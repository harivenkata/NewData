from django.conf.urls.defaults import *
from newdata.views import hello, my_homepage_view
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
    # Example:
    # (r'^newdata/', include('newdata.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
#)

urlpatterns = patterns('',
    (r'^$', my_homepage_view,{'homepage_template':'newdata_homepage.html'},'homepage'),    
    ('^hello/$', hello),
)