from django.shortcuts import render_to_response
from django.template import RequestContext
from ccompras.apps.ventas.forms import addProductFrom
from ccompras.apps.ventas.models import producto
def add_product_view(request):
	if request.method == "POST":
			form = addProductFrom(request.POST)
			info = "inicializando"
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				p = producto()
				p.nombre = nombre
				p.descripcion = descripcion
				p.status = True
				p.save()
				info = "Se guardo satisfactoriamente"
			else:
				info = "Informacion con datos incorrectos"
			form = addProductFrom()
			ctx = {'form':form, 'informacion':info}
			return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
	else:
			form = addProductFrom()
			ctx = {'form':form}
	return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))

