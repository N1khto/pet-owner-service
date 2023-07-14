from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator

from pet_app.models import PetOwner


class SpeciesSearchForm(forms.Form):
    species = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by species..."}),
    )


class PetSearchForm(forms.Form):
    nickname = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by nickname..."}),
    )


class BrandSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by brand name..."}
        ),
    )


class PetOwnerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username..."}
        ),
    )


class PetOwnerCreationForm(UserCreationForm):
    pet_owner_experience = forms.IntegerField(
        required=True,
        validators=[
            MaxValueValidator(
                limit_value=100, message="humans doesn't live so long"
            )
        ],
    )

    class Meta:
        model = PetOwner
        fields = UserCreationForm.Meta.fields + ("pet_owner_experience",)


class PetOwnerUpdateForm(forms.ModelForm):
    pet_owner_experience = forms.IntegerField(
        required=True,
        validators=[
            MaxValueValidator(
                limit_value=100, message="humans doesn't live so long"
            )
        ],
    )

    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name", "email", "pet_owner_experience"]


class PetFoodSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by title..."}
        ),
    )
