from django import forms
from qa.models import Question
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class AskForm(forms.Form):
	title = forms.CharField()
	text  = forms.CharField(widget=forms.Textarea)

	def save_and_get_url(self, cur_user):
		new_qs = Question(
				text=self.cleaned_data['text'], 
				title=self.cleaned_data['title'],
				#author=User.objects.all()[0]
				author=cur_user
		)
		new_qs.save()

		return "/question/" + str(new_qs.pk) + "/"


class AnswerForm(forms.Form):
	text = forms.CharField()
	question = forms.IntegerField()


class SignUpForm(forms.Form):
	username = forms.CharField()
	email    = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	def create_user(self):
		user = User.objects.create_user(
				self.cleaned_data['username'],
				self.cleaned_data['email'],
				self.cleaned_data['password'],
			)
	def log_user_in(self, request):
		user = authenticate(
			username=self.cleaned_data['username'],
			password=self.cleaned_data['password'],		
 		       )
		if user:
			login(request, user)

class LogInForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def log_user_in(self, request):
		user = authenticate(
			username=self.cleaned_data['username'],
			password=self.cleaned_data['password'],		
 		       )
		if user:
			login(request, user)
			return True
		else:
			return False

