from django import forms
from qa.models import Question
from django.contrib.auth.models import User

class AskForm(forms.Form):
	title = forms.CharField()
	text  = forms.CharField(widget=forms.Textarea)

	def save_and_get_url(self):
		new_qs = Question(
				text=self.cleaned_data['text'], 
				title=self.cleaned_data['title'],
				author=User.objects.all()[0]
		)
		new_qs.save()

		return "/question/" + str(new_qs.pk) + "/"


class AnswerForm(forms.Form):
	text = forms.CharField()
	question = forms.IntegerField()
