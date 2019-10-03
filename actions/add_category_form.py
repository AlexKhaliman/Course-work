from django import forms

from categories.models import Tasks


class AddingForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            'name', 'comments', 'price', 'category', 'created_by'
        ]

    def save(self, commit=True):
        return super().save(commit)