from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title    = models.CharField(max_length=100)
	text  	 = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating   = models.BigIntegerField(default=0)
	author   = models.ForeignKey(User, related_name='+')
	likes    = models.ManyToManyField(User)

	def get_url(self):
		return "/full/path/to/question"

class Answer(models.Model):
	text     = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question)
	author   = models.ForeignKey(User)
