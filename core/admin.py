from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from .models import Vehicule, ImageVehicule


class ImageVehiculeInline(TabularInline):
    model = ImageVehicule
    extra = 1


@admin.register(Vehicule)
class VehiculeAdmin(ModelAdmin):
    list_display = ("titre", "marque", "annee", "kilometrage", "prix", "en_vedette", "ordre_affichage")
    list_filter = ("marque", "en_vedette")
    search_fields = ("titre", "modele", "marque")
    inlines = [ImageVehiculeInline]


@admin.register(ImageVehicule)
class ImageVehiculeAdmin(ModelAdmin):
    list_display = ("vehicule", "ordre", "legende")
