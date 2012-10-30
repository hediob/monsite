from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone

from football.models import Commentaire, Equipe, Joueur

def index(request):
    best_commentaires = Commentaire.objects.all().order_by('-note')[:5]
    worst_commentaires = Commentaire.objects.all().order_by('note')[:5]
    context = {'best_commentaires': best_commentaires, 'worst_commentaires': worst_commentaires}
    return render(request, 'index.html', context)
	
def liste_equipes(request, pays):
	equipes = Equipe.objects.filter(pays__iexact=pays)
	context = {'equipes': equipes, 'pays': pays}
	return render(request, 'liste_equipes.html', context)
	
def liste_joueurs(request, pays, equipe):
    equipe_selected = Equipe.objects.get(equipe__iexact=equipe)
    joueurs = Joueur.objects.filter(equipe_id=equipe_selected.id)
    context = {'joueurs': joueurs, 'equipe': equipe}
    return render(request, 'liste_joueurs.html', context)
	
def detail_joueur(request, pays, equipe, nom, prenom):
	joueur = Joueur.objects.filter(nom=nom).get(prenom=prenom)
	commentaires = Commentaire.objects.filter(joueur_id=joueur.id).order_by('-date')
	
	def moyenne(annee):
		i=1
		tableau_moyenne=[]
		while i<19:
			commentaires_match = Commentaire.objects.filter(n_match=i).filter(joueur_id=joueur.id).filter(saison=annee)
			moyenne = 0
			j = 0
			i+=1
			if commentaires_match:
				for commentaire in commentaires_match:
					moyenne+=commentaire.note
					j+=1
				moyenne/=float(j)
				tableau_moyenne.append(round(moyenne,2))
			else:
				tableau_moyenne.append('')
		return tableau_moyenne
	
	num_match=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
	tableau_moyenne_2012=moyenne(2012)
	tableau_moyenne_2013=moyenne(2013)
	tableau_moyenne_2014=moyenne(2014)
	
	context = {'joueur': joueur, 'commentaires': commentaires, 
		'num_match':num_match, 'tableau_moyenne_2012': tableau_moyenne_2012,
		'tableau_moyenne_2013': tableau_moyenne_2013,'tableau_moyenne_2014': tableau_moyenne_2014,
		'equipe': equipe, 'nom': nom, 'prenom': prenom,}
	return render(request, 'detail_joueur.html', context)
	
def add_commentaire(request, pays, equipe, nom, prenom):
	if (request.POST['note']=='no'):
		return HttpResponseRedirect(reverse('detail_joueur', args=(pays,equipe,prenom,nom)))
	else:
		joueur = Joueur.objects.filter(nom=nom).get(prenom=prenom)
		comm=Commentaire(commentaire=request.POST['commentaire'],note=request.POST['note'],n_match=request.POST['n_match'],saison=request.POST['saison'],date=timezone.now(),joueur_id=joueur.id)
		comm.save()
		return HttpResponseRedirect(reverse('validation', args=(pays,equipe,prenom,nom)))
	
def validation(request, pays, equipe, nom, prenom):
	context = {'pays': pays, 'equipe': equipe, 'nom': nom, 'prenom': prenom}
	return render(request, 'validation.html', context)