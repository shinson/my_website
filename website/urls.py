from django.conf.urls import patterns, include, url
from blog.views import homeView, blogView, postView, categoryView
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	url(r'^$',homeView.as_view()),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^blog/', 'blog.views.blogView'),
	url(r'^contact', 'blog.views.contactView'),
	url(r'^thanks', 'blog.views.thanksView'),
	url(r'^blog/view/(?P<slug>[^\.]+)', 'blog.views.postView', name='view_blog_post'),
	url(r'^blog/category/(?P<slug>[^\.]+)', 'blog.views.categoryView', name='view_blog_category'),
 ]
