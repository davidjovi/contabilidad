# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.template import Context
from django.utils import simplejson
from forms import contactForm

def home(request):
	page = "content/content.html"
	return render_to_response('index.html', locals())

def nosotrosView(request):
	page = 'content/nosotros.html'
	return render_to_response('index.html', locals())

def serviciosView(request):
	page = 'content/servicios.html'
	pageService = 'content/service/contable.html'
	return render_to_response('index.html', locals())

def tributarioView(request):
	page = 'content/servicios.html'
	pageService = 'content/service/tributario.html'
	return render_to_response('index.html', locals())

def financieroView(request):
	page = 'content/servicios.html'
	pageService = 'content/service/financiera.html'
	return render_to_response('index.html', locals())

def laboralView(request):
	page = 'content/servicios.html'
	pageService = 'content/service/laboral.html'
	return render_to_response('index.html', locals())

def contactoView(request):
	page = 'content/contacto.html'
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			telefono = form.cleaned_data['telefono']
			asunto = form.cleaned_data['asunto']
			email = form.cleaned_data['email']
			mensaje = form.cleaned_data['mensaje']

			if request.is_ajax():
				data = {'ok', 'ok'}
				json = simplejson.dumps(data)

				return HttpResponse(json)

			return render_to_response('index.html', locals())

		else:

			return render_to_response('index.html', locals())

	else:
		form = contactForm()
		return render_to_response('index.html', locals())