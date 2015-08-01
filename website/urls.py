from django.conf.urls import include, url
from django.contrib import admin
from blog.views import homeView, blogView, postView, categoryView, contactView, thanksView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',homeView.as_view(), name="index"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^blog/', blogView, name="blog"),
	url(r'^contact/', contactView, name="contact"),
	url(r'^thanks/', thanksView, name="thanks"),
	url(r'^view/(?P<slug>[^\.]+)/', postView, name='view_post'),
	url(r'^category/(?P<slug>[^\.]+)/', categoryView, name='view_category'),
	url(r'^summernote/', include('django_summernote.urls')),
]
