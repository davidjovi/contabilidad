# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.template import Context
from django.utils import simplejson
from forms import contactForm
from django.http import HttpResponseRedirect
from django.core import serializers
import json

def home(request):
	current = 'inicio'
	page = "content/content.html"
	return render_to_response('index.html', locals())

def nosotrosView(request):
	current = 'nosotros'
	page = 'content/nosotros.html'
	return render_to_response('index.html', locals())

def serviciosView(request):
	current = 'servicios'
	page = 'content/servicios.html'
	pageService = 'content/service/contable.html'
	return render_to_response('index.html', locals())

def tributarioView(request):
	current = 'servicios'
	page = 'content/servicios.html'
	pageService = 'content/service/tributario.html'
	return render_to_response('index.html', locals())

def financieroView(request):
	current = 'servicios'
	page = 'content/servicios.html'
	pageService = 'content/service/financiera.html'
	return render_to_response('index.html', locals())

def laboralView(request):
	current = 'servicios'
	page = 'content/servicios.html'
	pageService = 'content/service/laboral.html'
	return render_to_response('index.html', locals())

def contactoView(request):
	current = 'contacto'
	page = 'content/contacto.html'
	form = contactForm()
	return render_to_response('index.html', locals())
	

def contactValid(request):
	current = 'contacto'
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
				data = {'ok':'ok'}
				json = simplejson.dumps(data)
				# json = serializers.serialize('json', data)

				return HttpResponse(json, mimetype="application/javascript")

			# return render_to_response('index.html', locals())

		else:
			
			q = dict((k, map(unicode, v)) for (k,v) in form.errors.iteritems())

			data = {'ok':'not', 'errors': q}
			json = simplejson.dumps(data)
			return HttpResponse(json, mimetype="application/javascript")
			

	else:
		form = contactForm()
		return render_to_response('index.html', locals())
