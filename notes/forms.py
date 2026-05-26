from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "description", "url"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "What do you want to study?"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Add your learning notes, ideas, or practice plan.",
                }
            ),
            "url": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://example.com"}),
        }
