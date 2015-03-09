from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from mysite.models import Image,Text
import datetime

def hello(request):
    a=Image.objects.get(id=1)
    b=Text.objects.get(id=1)
    d = {'a':a,'b':b}
    return render_to_response("index.html",d)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)	