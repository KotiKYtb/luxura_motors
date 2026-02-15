from django.shortcuts import render, get_object_or_404
from .models import Vehicule


def home(request):
    """Landing page avec véhicules en vedette."""
    vedettes = Vehicule.objects.filter(en_vedette=True)[:6]
    return render(request, "core/home.html", {"vedettes": vedettes})


def vehicule_list(request):
    """Liste de tous les véhicules."""
    vehicules = Vehicule.objects.all()
    return render(request, "core/vehicule_list.html", {"vehicules": vehicules})


def vehicule_detail(request, pk):
    """Détail d'un véhicule (pas de bouton achat, contact/RDV uniquement)."""
    vehicule = get_object_or_404(Vehicule, pk=pk)
    return render(request, "core/vehicule_detail.html", {"vehicule": vehicule})
