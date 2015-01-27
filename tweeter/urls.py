from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tweeter_app.views.index'),
    url(r'^login$', 'tweeter_app.views.login_view'),
    url(r'^logout$', 'tweeter_app.views.logout_view'),
    url(r'^signup$', 'tweeter_app.views.signup'),
    url(r'^ribbits$', 'tweeter_app.views.public'),
    url(r'^submit$', 'tweeter_app.views.submit'),
    url(r'^users/$', 'tweeter_app.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'tweeter_app.views.users'),
    url(r'^follow$', 'tweeter_app.views.follow'),
    # url(r'^ribbit/', include('tweeter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
