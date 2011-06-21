from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/ahmet/code/mali/static'}),
    (r'^admin/(.*)', admin.site.root),
    (r'^home/', 'mali.akdemir.views.index'),
    (r'^about/', 'mali.akdemir.views.about'),
    (r'^hizmetler/', 'mali.akdemir.views.hizmetler'),
    (r'^makaleler/$', 'mali.akdemir.views.makaleler'),
    (r'^makaleler/(?P<makale_id>\d+)/$', 'mali.akdemir.views.makale_detay'),
    (r'^sorucevap/', 'mali.akdemir.views.sorucevap'),
    (r'^iletisim/', 'mali.akdemir.views.iletisim'),
    (r'^linkler/', 'mali.akdemir.views.linkler'),
    (r'^kanunlar/', 'mali.akdemir.views.kanunlar'),
    (r'^ekonomi/', 'mali.akdemir.views.ekonomi'),
    (r'^sondakika/', 'mali.akdemir.views.sondakika'),
    (r'^guncelmevzuat/', 'mali.akdemir.views.guncelmevzuat'),
    (r'^notdefteri/$', 'mali.akdemir.views.notdefteri'),
    (r'^notdefteri/(?P<notdefteri_id>\d+)/$', 'mali.akdemir.views.notdefteri_detay'),
    (r'^basin/', 'mali.akdemir.views.basin'),
    # Example:
    # (r'^mali/', include('mali.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
)
