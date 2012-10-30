from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

from football import views
from football.models import Commentaire, Equipe, Joueur

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	
    url(r'^index/$', views.index, name='index'),
	
	url(r'^(?P<pays>[-A-Za-z]+)/$', views.liste_equipes, name='liste_equipes'),
		
	url(r'^(?P<pays>[-A-Za-z]+)/(?P<equipe>[-A-Z a-z]+)/$', views.liste_joueurs, name='liste_joueurs'),
		
    url(r'^(?P<pays>[-A-Za-z]+)/(?P<equipe>[-A-Z a-z]+)/(?P<prenom>[-A-Za-z]+)_(?P<nom>[-A-Z a-z]+)/$',
		views.detail_joueur, name='detail_joueur'),
	
	url(r'^(?P<pays>[-A-Za-z]+)/(?P<equipe>[-A-Z a-z]+)/(?P<prenom>[-A-Za-z]+)_(?P<nom>[-A-Z a-z]+)/add_commentaire/$',
		views.add_commentaire, name='add_commentaire'),
		
	url(r'^(?P<pays>[-A-Za-z]+)/(?P<equipe>[-A-Z a-z]+)/(?P<prenom>[-A-Za-z]+)_(?P<nom>[-A-Z a-z]+)/validation/$',
		views.validation, name='validation'),
)
