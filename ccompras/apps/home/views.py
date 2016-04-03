from django.shortcuts import render, render_to_response
from django.template import RequestContext
from ccompras.apps.ventas.models import producto
# Create your views here.
def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))


def about_view(request):
	mensaje = "esto es un mensaje desde mi vista"
	ctx = {
		'msg':mensaje
	}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def home(request):
	return render_to_response('home/home.html',context_instance=RequestContext(request))

def productos_view(request):
	prod = producto.objects.filter(status=True)
	ctx = {'productos':prod}
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))