from django import forms

from categories.models import Offers


class RespondForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = [
            'suggested_by', 'task', 'comment'
        ]

    def save(self, commit=True):
        return super().save(commit)