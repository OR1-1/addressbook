from django.conf.urls import patterns, include, url
from django.contrib import admin
import contacts.views
from django.core.urlresolvers import reverse, reverse_lazy
from contacts.models import Contact

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', contacts.views.ListContactView.as_view(), name='contacts-list',),
    # url(r'^new$', contacts.views.CreateContactView.as_view(), name='contacts-new',),
    url(r'^new$', contacts.views.CreateContactView.as_view(model=Contact, success_url=reverse_lazy('contacts-list')), name='contacts-new',),
    url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(model=Contact, success_url=reverse_lazy('contacts-list')), name='contacts-edit'),
)
