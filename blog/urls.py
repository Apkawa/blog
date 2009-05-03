from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('apkawa.blog.views',
    # Example:
    #(r'^post/', ),
    (r'^$','main'),
    (r'^category/([-\w]{,256})/$','category'),
    (r'^tag/(\d{1,4})/$','tag'),
    (r'^post/([-\w]{,256})/$','post'),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #(r'^admin/(.*)', admin.site.root),
)
