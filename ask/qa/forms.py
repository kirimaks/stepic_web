from django import forms

class AskForm(forms.Form):
	title = forms.CharField()
	text  = forms.CharField(widget=forms.Textarea)


class AnswerForm(forms.Form):
	text = forms.CharField()
	question = forms.IntegerField()
