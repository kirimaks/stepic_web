from django.shortcuts 		import render, get_object_or_404
from django.http 		import HttpResponse, HttpResponseRedirect
from qa.models 			import Question
from django.core.paginator 	import Paginator
from qa.forms 			import AskForm, SignUpForm, LogInForm


def test(request, *args, **kwargs):
	return HttpResponse("OK")

def home(request):
	questions_list  = Question.objects.all().order_by("-added_at")
	page_num 	= request.GET.get("page", 1)
	paginator 	= Paginator(questions_list, 10)
	cur_page 	= paginator.page(page_num)
	
	context = dict(
		cur_page  	= cur_page,
		paginator 	= paginator,
	)
	
	return render(request, "qa/home.html", context)
	

def best(request):
	questions_list 	= Question.objects.all().order_by("-rating")
	page_num 	= request.GET.get("page", 1)
	paginator 	= Paginator(questions_list, 10)
	cur_page 	= paginator.page(page_num)
	
	context = dict(
		cur_page  = cur_page,
		paginator = paginator,
	)
	
	return render(request, "qa/best.html", context)
	
def question(request, qid):
	question = get_object_or_404(Question, pk=qid)
	return render(request, "qa/question.html", { "question" : question })

def ask(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			url = form.save_and_get_url(request.user)
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
		return render(request, "qa/ask.html", { "form" : form })


def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.create_user()
			form.log_user_in(request)
			return HttpResponseRedirect("/")
	else:
		form = SignUpForm()
		return render(request, "qa/signup.html", { "form" : form })


def login(request):
	if request.method == "POST":
		form = LogInForm(request.POST)
		if form.is_valid():
			if form.log_user_in(request):
				return HttpResponseRedirect("/")
			else:
				# Form with errors.
				return render(request, "qa/login.html", { "form" : form })
		
	else:
		form = LogInForm()
		return render(request, "qa/login.html", { "form" : form })

