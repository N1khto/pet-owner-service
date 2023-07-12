from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from pet_app.forms import SpeciesSearchForm, PetSearchForm
from pet_app.models import Pet, PetOwner, PetFood, Species, Brand


def index(request):

    num_pet_owners = PetOwner.objects.count()
    num_pets = Pet.objects.count()
    num_brands = Brand.objects.count()

    context = {
        "num_pet_owners": num_pet_owners,
        "num_pets": num_pets,
        "num_brands": num_brands
    }

    return render(request, "pet_app/index.html", context=context)


class SpeciesListView(LoginRequiredMixin, generic.ListView):
    model = Species
    context_object_name = "species_list"
    template_name = "pet_app/species_list.html"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SpeciesListView, self).get_context_data(**kwargs)
        species = self.request.GET.get("species", "")
        context["search_form"] = SpeciesSearchForm(initial={"species": species})
        return context

    def get_queryset(self):
        queryset = Species.objects.all()
        form = SpeciesSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(species__icontains=form.cleaned_data["species"])
        return queryset


class SpeciesCreateView(LoginRequiredMixin, generic.CreateView):
    model = Species
    fields = "__all__"
    success_url = reverse_lazy("pet_app:species-list")


class SpeciesUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Species
    fields = "__all__"
    success_url = reverse_lazy("pet_app:species-list")


class SpeciesDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Species
    success_url = reverse_lazy("pet_app:species-list")


class PetListView(LoginRequiredMixin, generic.ListView):
    model = Pet
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PetListView, self).get_context_data(**kwargs)
        nickname = self.request.GET.get("nickname", "")
        context["search_form"] = PetSearchForm(initial={"nickname": nickname})
        return context

    def get_queryset(self):
        queryset = Pet.objects.all()
        form = PetSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(nickname__icontains=form.cleaned_data["nickname"])
        return queryset


class PetDetailView(LoginRequiredMixin, generic.DetailView):
    model = Pet


class PetCreateView(LoginRequiredMixin, generic.CreateView):
    model = Pet
    fields = "__all__"
    success_url = reverse_lazy("pet_app:pet-list")


class PetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Pet
    fields = "__all__"
    success_url = reverse_lazy("pet_app:pet-list")


class PetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Pet
    success_url = reverse_lazy("pet_app:pet-list")