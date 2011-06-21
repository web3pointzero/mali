# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from mali.akdemir.models import Haber, Makale, Notdefteri

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

def index(request):
	return render_to_response("index.html")

def about(request):
	return render_to_response("about.html")

def hizmetler(request):
	return render_to_response("hizmetler.html")

def makaleler(request):
    obj_list = Makale.objects.all()
    paginator = Paginator(obj_list, 2)
    
    page = request.GET.get('page', 1)

    try:
        objs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        objs = paginator.page(paginator.num_pages)

    return render_to_response('makaleler.html',{ 'makale_list': objs})

def makale_detay(request, makale_id):
    m = get_object_or_404(Makale, pk=makale_id)
    return render_to_response('makale_detay.html', {'makale': m})

def sorucevap(request):
	return render_to_response("sorucevap.html")

def iletisim(request):
	return render_to_response("iletisim.html")

def linkler(request):
	return render_to_response("linkler.html")

def ekonomi(request):
	return render_to_response("ekonomi.html")

def sondakika(request):
	return render_to_response("sondakika.html")

def guncelmevzuat(request):
	return render_to_response("guncelmevzuat.html")

def notdefteri(request):
#    obj_list = Notdefteri.objects.all()
#    return render_to_response('notdefteri.html',{ 'notdefteri_list': obj_list})

    obj_list = Notdefteri.objects.all()
    paginator = Paginator(obj_list, 2)
    
    page = request.GET.get('page', 1)

    try:
        objs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        objs = paginator.page(paginator.num_pages)

    return render_to_response('notdefteri.html',{ 'notdefteri_list': objs})


def notdefteri_detay(request, notdefteri_id):
    n = get_object_or_404(Notdefteri, pk=notdefteri_id)
    return render_to_response('notdefteri_detay.html', {'notdefteri': n})

def basin(request):
	return render_to_response("basin.html")

def kanunlar(request):
	return render_to_response("kanunlar.html")
