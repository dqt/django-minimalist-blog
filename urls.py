from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'blog.xss.views.index'),
    url(
        r'^blog/view/(?P<slug>[^\.]+)',
        'blog.xss.views.view_post',
        name='view_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+)',
        'blog.xss.views.view_category',
        name='view_blog_category'),
)
