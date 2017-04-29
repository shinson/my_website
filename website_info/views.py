from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import *

def homeView(request):
	template = loader.get_template('index.html')
	work = Work.objects.all()
	skills = Skill.objects.all().order_by('category')
	media = Media.objects.all().order_by('category')
	projects = Project.objects.all()
	context = {"work": work, "skills": skills, "media": media, "projects": projects}
	return HttpResponse(template.render(context, request))
