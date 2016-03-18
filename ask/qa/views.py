from django.shortcuts 		import render, get_object_or_404
from django.http 		import HttpResponse
from qa.models 			import Question
from django.core.paginator 	import Paginator


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
	#return HttpResponse("OK")
	return render(request, "qa/question.html", { "question" : question })
