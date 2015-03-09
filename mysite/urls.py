from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime ,hours_ahead
from django.contrib import admin 
import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   	url(r'^hello/$', hello),
   	url(r'^time/$',current_datetime),
   	url(r'^$', 'mysite.views.hello'),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
 	{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),

)
