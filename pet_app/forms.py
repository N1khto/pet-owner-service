from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from pet_app.models import Pet, PetFood, Species, Brand, PetOwner


class SpeciesSearchForm(forms.Form):
    species = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by species..."})
    )


class PetSearchForm(forms.Form):
    nickname = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by nickname..."})
    )


class BrandSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by brand name..."})
    )


class PetOwnerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )


class PetOwnerCreationForm(UserCreationForm):
    class Meta:
        model = PetOwner
        fields = UserCreationForm.Meta.fields + ("pet_owner_experience", )


class PetOwnerUpdateForm(forms.ModelForm):
    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name", "email", "pet_owner_experience"]
