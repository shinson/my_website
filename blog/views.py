from django.shortcuts import render,render_to_response,  get_object_or_404
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Blog, Category
from blog.forms import ContactForm
from django.template import Context, Template, loader, RequestContext
from django.template.loader import get_template
from django.core.mail import send_mail

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
	


def contactView(request):
	form = ContactForm(request.POST)
	if request.method == 'POST' and form.validate():
		subject = form.subject.data
		message = "{0}\n-{1}".format(form.message.data, form.name.data)
		sender = form.email.data
		recipients = ['sonia.hinson@gmail.com']
		send_mail(subject, message, sender, recipients)
		return HttpResponseRedirect('/thanks/')
	return render_to_response('contact_me.html',{'form':form}, context_instance = RequestContext(request))

def thanksView(request):
		return render_to_response('thanks.html')