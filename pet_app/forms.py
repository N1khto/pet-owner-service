from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from pet_app.models import Pet, PetFood, Species, Brand


class SpeciesSearchForm(forms.Form):
    species = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by species..."})
    )
