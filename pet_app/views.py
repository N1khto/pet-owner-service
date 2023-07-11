from django.shortcuts import render


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
