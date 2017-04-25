from django.conf.urls import include, url
from django.contrib import admin
# from blog.views import *
from website_info.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', homeView, name='index'),
	url(r'^admin/', include(admin.site.urls)),
	# url(r'^blog/', blogView, name='blog'),
	# url(r'^contact/', contactView, name='contact'),
	# url(r'^thanks/', thanksView, name='thanks'),
	# url(r'^view/(?P<slug>[^\.]+)/', postView, name='view_post'),
	# url(r'^category/(?P<slug>[^\.]+)/', categoryView, name='view_category'),
	# url(r'^summernote/', include('django_summernote.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
