from django.db import models
from django.utils import timezone
import datetime

class Equipe(models.Model):
	equipe = models.CharField(max_length=200)
	pays = models.CharField(max_length=200)
	championnat = models.CharField(max_length=200)
	
	def __unicode__(self):
		return u"%s" % (self.equipe)
	
class Joueur(models.Model):
	nom = models.CharField(max_length=200)
	prenom = models.CharField(max_length=200)
	equipe = models.ForeignKey(Equipe)

	def __unicode__(self):
		return u"%s %s" % (self.prenom, self.nom)

class Commentaire(models.Model):
	commentaire = models.CharField(max_length=200)
	note = models.IntegerField()
	n_match = models.IntegerField()
	saison = models.IntegerField()
	date = models.DateTimeField()
	joueur = models.ForeignKey(Joueur)

	def was_published_recently(self):
		return self.date >= timezone.now() - datetime.timedelta(days=7)