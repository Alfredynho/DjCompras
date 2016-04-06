from django.conf.urls  import patterns,url

urlpatterns = patterns('ccompras.apps.ventas.views',
	url(r'^add/producto/$','add_product_view',name='vista_agregar_producto'),
)
