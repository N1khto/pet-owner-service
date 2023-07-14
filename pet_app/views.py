from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from pet_app.forms import (
    SpeciesSearchForm,
    PetSearchForm,
    BrandSearchForm,
    PetOwnerSearchForm,
    PetOwnerCreationForm,
    PetOwnerUpdateForm,
    PetFoodSearchForm,
)
from pet_app.models import Pet, PetOwner, PetFood, Species, Brand


def index(request):
    num_pet_owners = PetOwner.objects.count()
    num_pets = Pet.objects.count()
    num_brands = Brand.objects.count()
    num_foods = PetFood.objects.count()
    num_species = Species.objects.count()

    context = {
        "num_pet_owners": num_pet_owners,
        "num_pets": num_pets,
        "num_brands": num_brands,
        "num_foods": num_foods,
        "num_species": num_species,
    }

    return render(request, "pet_app/index.html", context=context)


class SpeciesListView(LoginRequiredMixin, generic.ListView):
    model = Species
    context_object_name = "species_list"
    template_name = "pet_app/species_list.html"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SpeciesListView, self).get_context_data(**kwargs)
        species = self.request.GET.get("species", "")
        context["search_form"] = SpeciesSearchForm(
            initial={"species": species}
        )
        return context

    def get_queryset(self):
        queryset = Species.objects.all()
        form = SpeciesSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                species__icontains=form.cleaned_data["species"]
            )
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
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PetListView, self).get_context_data(**kwargs)
        nickname = self.request.GET.get("nickname", "")
        context["search_form"] = PetSearchForm(initial={"nickname": nickname})
        return context

    def get_queryset(self):
        queryset = Pet.objects.prefetch_related("owner", "species")
        form = PetSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                nickname__icontains=form.cleaned_data["nickname"]
            )
        return queryset


class PetDetailView(LoginRequiredMixin, generic.DetailView):
    queryset = Pet.objects.select_related("owner")
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


class BrandListView(LoginRequiredMixin, generic.ListView):
    model = Brand
    context_object_name = "brand_list"
    template_name = "pet_app/brand_list.html"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BrandListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = BrandSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Brand.objects.prefetch_related("pet_foods")
        form = BrandSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class BrandCreateView(LoginRequiredMixin, generic.CreateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy("pet_app:brand-list")


class BrandUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy("pet_app:brand-list")


class BrandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Brand
    success_url = reverse_lazy("pet_app:brand-list")


class PetOwnerListView(LoginRequiredMixin, generic.ListView):
    queryset = PetOwner.objects.prefetch_related("pet_set")
    model = PetOwner
    context_object_name = "pet_owner_list"
    template_name = "pet_app/pet_owner_list.html"
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PetOwnerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = PetOwnerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        form = PetOwnerSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return self.queryset


class PetOwnerDetailView(LoginRequiredMixin, generic.DetailView):
    model = PetOwner
    queryset = PetOwner.objects.prefetch_related("pet_set__species")
    context_object_name = "pet_owner"
    template_name = "pet_app/pet_owner_detail.html"


class PetOwnerCreateView(LoginRequiredMixin, generic.CreateView):
    model = PetOwner
    form_class = PetOwnerCreationForm
    template_name = "pet_app/pet_owner_form.html"
    success_url = reverse_lazy("pet_app:pet-owner-list")


class PetOwnerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = PetOwner
    form_class = PetOwnerUpdateForm
    template_name = "pet_app/pet_owner_form.html"
    success_url = reverse_lazy("pet_app:pet-owner-list")


class PetOwnerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = PetOwner
    template_name = "pet_app/pet_owner_confirm_delete.html"
    success_url = reverse_lazy("pet_app:pet-owner-list")


class PetFoodListView(LoginRequiredMixin, generic.ListView):
    model = PetFood
    context_object_name = "pet_food_list"
    template_name = "pet_app/pet_food_list.html"
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PetFoodListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = PetFoodSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        queryset = PetFood.objects.select_related("brand")
        form = PetFoodSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset


class PetFoodDetailView(LoginRequiredMixin, generic.DetailView):
    model = PetFood
    queryset = PetFood.objects.all()
    context_object_name = "pet_food"
    template_name = "pet_app/pet_food_detail.html"


class PetFoodCreateView(LoginRequiredMixin, generic.CreateView):
    model = PetFood
    fields = "__all__"
    template_name = "pet_app/pet_food_form.html"
    success_url = reverse_lazy("pet_app:pet-food-list")


class PetFoodUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = PetFood
    fields = "__all__"
    template_name = "pet_app/pet_food_form.html"
    success_url = reverse_lazy("pet_app:pet-food-list")


class PetFoodDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = PetFood
    template_name = "pet_app/pet_food_confirm_delete.html"
    success_url = reverse_lazy("pet_app:pet-food-list")
