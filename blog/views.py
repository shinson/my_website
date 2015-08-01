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

class homeView(TemplateView):
	template_name = 'index.html'
	def get(self, request, **kwargs):
		context = self.get_context_data()
		return render(request, self.template_name, context)
	def get_context_data(self, **kwargs):
		context = {}
		return context	

def blogView(request):
	template = 'blog.html'
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
	return render(request, template, context)

	
def postView(request, slug):
	template_name = 'view_post.html'
	post = Post.objects.filter(slug = slug)
	return render(request, template_name, {'post':post})

	
def categoryView(request, slug):
	template_name = 'view_category.html'
	c = Category.objects.filter(slug = slug)
	return render(request, template_name,{'category': c,'posts': Post.objects.filter(category=c)})

def contactView(request):
	form = ContactForm(request.POST)
	if request.method == 'POST' and form.validate():
		subject = form.subject.data
		message = "{0}\n-{1}".format(form.message.data, form.name.data)
		sender = form.email.data
		recipients = ['sonia.hinson@gmail.com']
		send_mail(subject, message, sender, recipients)
		return HttpResponseRedirect(reverse('thanks'))
	return render_to_response('contact_me.html',{'form':form}, context_instance = RequestContext(request))

def thanksView(request):
		return render_to_response('thanks.html')
