from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Example:
    #(r'^post/', ),
    (r'^$','apkawa.blog.views.main'),
    (r'^(tag|category)/(\w{,256})/$','apkawa.blog.views.sorted'),
    (r'^post/(\w{,256})/$','apkawa.blog.views.post'),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #(r'^admin/(.*)', admin.site.root),
)
