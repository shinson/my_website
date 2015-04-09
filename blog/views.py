from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, Template, loader, RequestContext
from django.template.loader import get_template

class homeView(TemplateView):
	template_name = 'index.html'
	def get(self, request, **kwargs):
		context = self.get_context_data()
		return render(request, self.template_name, context)
	def get_context_data(self, **kwargs):
		context = {}
		return context	

def blogView(request):
	template = 'blog_404.html'
	context = {"categories": Category.objects.all(), "posts": Blog.objects.all()[:5]}
	return render(request, template, context)

	
def postView(request, slug):
	post = get_object_or_404(Blog, slug=Blog.objects.values('slug'))
	return render_to_response('view_post.html', {'post': post}, context_instance = RequestContext(request))
# 	
def categoryView(request, slug):
	category = get_object_or_404(Category, slug=Categoryx.objects.values('slug'))
	return render_to_response('view_category.html', {
		'category': category,
		'posts': Blog.objects.filter(category=category)
	},
	context_instance = RequestContext(request))
