from django.shortcuts import render
from django.db import models
from home.models import AppUser, AppMessage
from django.db.models import Q
from django.http import JsonResponse,HttpResponse
from home.forms import AppUserForm
from home.forms import AppUserLoginForm
from django.conf import settings
from django.conf.urls.static import static
import time

# Create your views here.




def cad(request):
    form_class = AppUserForm
    
    return render(request, 'cad.html', {
        'form': form_class,
    })


def index(request, oid):
	u      = AppUser.objects.all().filter(id = oid)
	others = AppUser.objects.filter(~Q(id = oid))

	return render(request, 'index.html', {'user': [u], 'others':[others]})


def requestMessages(request, u1, u2):
	messages = (AppMessage.objects.filter(whoSent = u1).filter(whoRecv = u2) | AppMessage.objects.filter(whoSent = u2).filter(whoRecv = u1)).order_by('id')
	for m in messages:
		print(m.msg)
	data = {
		'messages' : list(messages.values())
	}
	print data
	return JsonResponse(data)
	#return  JsonResponse({"oi":"ola"})
def requestMessages1(request, u1, u2, lastIdLoaded):
	messages = (AppMessage.objects.filter(id > lastIdLoaded).filter(whoSent = u1).filter(whoRecv = u2) | AppMessage.objects.filter(whoSent = u2).filter(whoRecv = u1)).order_by('id')
	for m in messages:
		print(m.msg)
	data = {
		'messages' : list(messages.values())
	}
	
	#return ret
	return  JsonResponse({'count':messages})

def countUnreadMessages(request,userId, idSent):
	counts = []
	for ids in idSent:
		messages = AppMessage.objects.filter(whoSent = idSent).filter(whoRecv = userId).filter(read=False).order_by('id').count()
		counts.append(messages)
	return JsonResponse({'count': counts})

def insertNewMessage(request, u1, u2, msg):
	u1db = AppUser.objects.get(id=u1)
	u2db = AppUser.objects.get(id=u2)
	AppMessage.objects.create(whoSent=u1db, whoRecv=u2db,msg=msg)
	return HttpResponse(request, "<h1>ok</h1>")

def requestFriends(request, userId):
	others = AppUser.objects.filter(~Q(id = userId))
	data = {
		'friends' : list(others.values())
	}
	return  JsonResponse(data)


def addUser(request):
	form_class = AppUserForm

	if request.method == 'POST':
		form = AppUserForm(request.POST, request.FILES)

		if(form.is_valid()):
			first_name = request.POST.get(
				'first_name', '')

			newuser = AppUser(first_name=first_name)
			f = request.FILES['image']
			print(f.name)
			name = str(time.time())
			handle_uploaded_file(f,name)
			newuser.image_url = name
			newuser.save()

			return index(request, newuser.id)
		else:
			print('form invalido')
	return render( request, 'cad.html', { 'form': form_class, } )

def handle_uploaded_file(f, name):
    destination = open('home/static/' + name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    print('ok')

def login(request):
	form_class = AppUserLoginForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if(form.is_valid()):
			first_name = request.POST.get(
				'first_name', '')

			query = AppUser.objects.filter(first_name = first_name)

			if(len(query) == 0):
				print('nao encontrado')
			else:
				print('encontrado')
				user = list(query)[0]
				return index(request, user.id)

			return render( request, 'login.html', { 'form': form_class, } )

	return render( request, 'login.html', { 'form': form_class, } )

def helper(request):

	return render(request, 'helper.html')