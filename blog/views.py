from django.shortcuts import render,render_to_response,  get_object_or_404
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Post, Category
from blog.forms import ContactForm
from django.template import Context, Template, loader, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import loader

def homeView(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def blogView(request):
	template = loader.get_template('blog.html')
	blog_list = Post.objects.all()
	paginator = Paginator(blog_list, 5)
	page = request.GET.get('page')
	try:
		all_posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		all_posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		all_posts = paginator.page(paginator.num_pages)
	context = {"categories": Category.objects.all(), "posts": Post.objects.all()[:5], "all_posts":all_posts }
	return HttpResponse(template.render(context, request))

	
def postView(request, slug):
	template = loader.get_template('view_post.html')
	post = Post.objects.filter(slug = slug)
	context = {'post':post};
	return HttpResponse(template.render(context, request))

	
def categoryView(request, slug):
	template = loader.get_template('view_category.html')
	c = Category.objects.filter(slug = slug)
	context = {'category': c,'posts': Post.objects.filter(category=c)}
	return HttpResponse(template.render(context, request))

def contactView(request):
	form = ContactForm(request.POST)
	if request.method == 'POST' and form.validate():
		subject = form.subject.data
		message = "{0}\n-{1}".format(form.message.data, form.name.data)
		sender = form.email.data
		recipients = ['contact@soniahinson.com']
		send_mail(subject, message, sender, recipients)
		return HttpResponseRedirect(reverse('thanks'))
	template = loader.get_template('contact_me.html')
	context = {'form':form}
	return HttpResponse(template.render(context, request))

def thanksView(request):
	template = loader.get_template('thanks.html')
	context = {}
	return HttpResponse(template.render(context, request))
