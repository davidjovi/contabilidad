from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'contabilidad.views.home', name='home'),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^nosotros$', 'app.views.nosotrosView', name='nosotros'),
    url(r'^servicios$', 'app.views.serviciosView', name='servicios'),
    url(r'^servicios/contables$', 'app.views.serviciosView', name='servicios'),
    url(r'^servicios/tributarios$', 'app.views.tributarioView', name='tributario'),
    url(r'^servicios/financieros$', 'app.views.financieroView', name='financiero'),
    url(r'^servicios/laborales$', 'app.views.laboralView', name='laboral'),
    url(r'^contacto$', 'app.views.contactoView', name='contacto'),
    # url(r'^contabilidad/', include('contabilidad.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

urlpatterns += staticfiles_urlpatterns()