from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import NoteForm
from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = "notes/list.html"
    context_object_name = "notes"


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/form.html"
    success_url = reverse_lazy("notes_list")
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
