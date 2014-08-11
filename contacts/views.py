from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse, reverse_lazy
from contacts.models import Contact

class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'

class CreateContactView(CreateView):
    model = Contact
    template_name = 'edit_contact.html'

    # def get_successful_url(self):
        # return reverse_lazy('contacts-list')