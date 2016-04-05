from django.shortcuts import render, render_to_response
from django.template import RequestContext
from ccompras.apps.ventas.models import producto
from ccompras.apps.home.forms import ContactForm
from django.core.mail import EmailMultiAlternatives
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

def contacto_view(request):
	info_enviado = False
	email = ""
	titulo = ""
	texto  = ""
	if request.method == 'POST':
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']
			#configurando el envio de mensaje a Gmail
			to_admin = 'callizayagutierrezalfredo@gmail.com'
			html_content = "Informacion recibida de [%s] <br><br><br>***Mensaje****<br><br>%s"%(email,texto)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') # Definimos el contenido como HTML
			msg.send() # Enviamos  en correo
	else:
		formulario = ContactForm()
	ctx ={'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render(request,'home/contacto.html',ctx)
