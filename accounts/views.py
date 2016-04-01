from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Newsletter

def index(request):
	context = {}
	if request.method == "POST":
		n = Newsletter()
		n.email_address = request.POST.get("email_address", "")
		n.save()
		context["email_address"] = request.POST.get("email_address", "")
		#print dir(Newsletter.objects)
		context["last_email_address"] = Newsletter.objects.order_by('-date_added')[0].email_address
	
	return render(request, 'hello/index.html', context)
    #
    #context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    #})
    #return HttpResponse(template.render(context))

