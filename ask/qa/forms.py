from django import forms

class AskForm(forms.Form):
	title = forms.CharField()
	text  = forms.CharField(widget=forms.Textarea)

	def save_and_get_url(self):
		new_qs = Question(
				text=self.cleaned_data['text'], 
				title=self.cleaned_data['title'])
		new_qs.save()

		return "/question/" + news_qs.pk + "/"


class AnswerForm(forms.Form):
	text = forms.CharField()
	question = forms.IntegerField()
