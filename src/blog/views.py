from .forms import GetsViewForm
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class GetsView(TemplateView):
    form = GetsViewForm
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        form = GetsViewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(self.request, "Thanks you for contact us.")
            return redirect("/")
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
