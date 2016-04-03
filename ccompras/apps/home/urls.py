from django.conf.urls  import patterns,url

urlpatterns = patterns('ccompras.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^perfil/$','home', name='perfil'),
	url(r'^productos/$','productos_view',name='vista_productos'),
)