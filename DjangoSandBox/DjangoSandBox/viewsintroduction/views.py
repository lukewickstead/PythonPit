from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import PhoneAddress, PhoneContact


# Address Views
class PhoneAddressDetailView(DetailView):
    model = PhoneAddress
    fields = ["city", "street_name", "number"]
    template_name = "viewsintroduction/phoneaddress.html"


class PhoneAddressCreateView(CreateView):
    model = PhoneAddress
    fields = ["city", "street_name", "number"]
    template_name = "viewsintroduction/phoneaddresscreate.html"

    def form_valid(self, form):
        messages.success(self.request, "Address created successfully")
        return super(PhoneAddressCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Address has not been created")
        return super(PhoneAddressCreateView, self).form_invalid(form)


class PhoneAddressUpdateView(UpdateView):
    model = PhoneAddress
    fields = ["city", "street_name", "number"]
    template_name = "viewsintroduction/phoneaddressupdate.html"

    def form_valid(self, form):
        messages.success(self.request, "Address updated successfully")
        return super(PhoneAddressUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Address has not been updated")
        return super(PhoneAddressUpdateView, self).form_invalid(form)


class PhoneAddressDeleteView(DeleteView):
    model = PhoneAddress
    template_name = "viewsintroduction/phoneaddressdelete.html"

    def get_success_url(self):
        return reverse("viewsintroduction:address_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Address deleted successfully")
        return super().delete(request, *args, **kwargs)


class PhoneAddressListView(ListView):
    model = PhoneAddress
    template_name = 'viewsintroduction/phoneaddresslist.html'
    paginate_by = 5

    def get_queryset(self):
        return PhoneAddress.objects.all().order_by("city", "street_name", "number")


# Contact Views
class PhoneContactDetailView(DetailView):
    model = PhoneContact
    fields = ["name", "surname", "height", "date_of_birth", "is_family", "sex", "address"]
    template_name = "viewsintroduction/phonecontact.html"


class PhoneContactCreateView(CreateView):
    model = PhoneContact
    fields = ["name", "surname", "height", "date_of_birth", "is_family", "sex", "address"]
    template_name = "viewsintroduction/phonecontactcreate.html"

    def form_valid(self, form):
        messages.success(self.request, "Contact created successfully")
        return super(PhoneContactCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Contact has not been created")
        return super(PhoneContactCreateView, self).form_invalid(form)


class PhoneContactUpdateView(UpdateView):
    model = PhoneContact
    fields = ["name", "surname", "height", "date_of_birth", "is_family", "sex", "address"]
    template_name = "viewsintroduction/phonecontactupdate.html"

    def form_valid(self, form):
        messages.success(self.request, "Contact updated successfully")
        return super(PhoneContactUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Contact has not been updated")
        return super(PhoneContactUpdateView, self).form_invalid(form)


class PhoneContactDeleteView(DeleteView):
    model = PhoneContact
    template_name = "viewsintroduction/phonecontactdelete.html"

    def get_success_url(self):
        return reverse("viewsintroduction:contact_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Address deleted successfully")
        return super().delete(request, *args, **kwargs)


class PhoneContactListView(ListView):
    model = PhoneContact
    template_name = 'viewsintroduction/phonecontactlist.html'
    paginate_by = 5

    def get_queryset(self):
        return PhoneContact.objects.all().order_by("surname", "name")
