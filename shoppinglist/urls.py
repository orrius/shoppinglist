from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
        url(r'^lists/$', 'list.views.index', name='index'),
    url(r'^lists/(?P<list_name>\w+)/$', 'list.views.detail'),
    url(r'^lists/editamount', 'list.views.editamount'),
    url(r'^lists/newitem', 'list.views.newitem'),
    # url(r'^shoppinglist/', include('shoppinglist.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
    )
