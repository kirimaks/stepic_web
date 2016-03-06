from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title    = models.CharField(max_length=100)
	text  	 = models.TextField()
	added_at = models.DateTimeField()
	rating   = models.BigIntegerField()
	author   = models.ForeignKey(User, related_name='+')
	likes    = models.ManyToManyField(User)

class Answer(models.Model):
	text     = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question)
	author   = models.ForeignKey(User)
