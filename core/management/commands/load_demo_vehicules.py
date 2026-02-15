from django.core.management.base import BaseCommand
from core.models import Vehicule


# Images fournies par modèle (ordre du tableau : Roma, Huracán STO, 718 GT4 RS, 720S Spider, 812 Superfast, 911 Cabriolet)
DEMO_IMAGES = {
    "Ferrari Roma": "https://imgs.search.brave.com/wJWgFDbUMWi6NPFc8aTiwEqUUvKA5zyNbQ_x8NxJNlE/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/c3VwZXJjYXJzLm5l/dC9ibG9nL3dwLWNv/bnRlbnQvdXBsb2Fk/cy8yMDIwLzA3LzEw/NzE5MTcuanBn",
    "Lamborghini Huracán STO": "https://imgs.search.brave.com/ISDM9mMCiF52ElLF_BZQ8dPseDfTUSn16FwXb8CR-Hk/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/amFtZXNlZGl0aW9u/LmNvbS9saXN0aW5n/X2ltYWdlcy8yMDI2/LzAyLzA0LzExLzA5/LzI1L2IwNzE0ZDNl/LTQ2NTctNGRmOS1i/N2VjLTkxYzBkZGZm/OTc4ZS9qZS81MDd4/MzEyeGMuanBn",
    "Porsche 718 Cayman GT4 RS": "https://imgs.search.brave.com/tzfbLnIjstPCMznRR7I9zHw5c1VuZU6BY-XN1V_5Zos/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/YXV0b21vYmlsZS1z/cG9ydGl2ZS5jb20v/Z3VpZGUvcG9yc2No/ZS83MThjYXltYW5n/dDRycy9wb3JzY2hl/LTcxOC1jYXltYW4t/Z3Q0LXJzLmpwZw",
    "McLaren 720S Spider": "https://imgs.search.brave.com/K3SA8vT0a8FJG1nnticzjgHHZOThct0m95sEG5Mkqx0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/dG9wZ2Vhci1tYWdh/emluZS5mci93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxOC8xMi9t/Y2xhcmVuXzcyMHNf/c3BpZGVyXzA2Lmpw/Zw",
    "Ferrari 812 Superfast": "https://imgs.search.brave.com/jx8z1D5vWG4sKHwmUvtsQWCNH4IYNeEyJuSzbOhByNA/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/c3VwZXJjYXJzLm5l/dC9ibG9nL3dwLWNv/bnRlbnQvdXBsb2Fk/cy8yMDE3LzA3Lzgx/Mi1zdXBlcmZhc3Rf/MS0zNzB4MjQ3Lmpw/Zw",
    "Porsche 911 Turbo Cabriolet": "https://imgs.search.brave.com/8zCKM6LJqFaX8a1TXN6Xa_bNPGtn6-NS1Q-f_QlyX4U/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/bGFyZ3VzLmZyL2lt/YWdlcy9waG90b3Mv/cnNpL19HX0pQRy9W/b2l0dXJlcy9QT1JT/Q0hFLzkxMV9DYWJy/aW9sZXQvVklfOTky/L1BoMS9DYWJyaW9s/ZXRfMl9wb3J0ZXMv/VFJPSVNRVUFSVEFW/QU5UMS5qcGc",
}


class Command(BaseCommand):
    help = "Charge des véhicules de démo pour la vitrine (avec images Unsplash)."

    def handle(self, *args, **options):
        data = [
            {
                "titre": "Ferrari Roma",
                "marque": "ferrari",
                "modele": "Roma",
                "annee": 2022,
                "kilometrage": 19810,
                "prix": 219900,
                "puissance_ch": 620,
                "moteur": "V8 3.9 L twin-turbo",
                "description": "La Ferrari Roma incarne la dolce vita. Design épuré, moteur V8 turbo, conduite raffinée.",
                "en_vedette": True,
                "ordre_affichage": 10,
            },
            {
                "titre": "Lamborghini Huracán STO",
                "marque": "lamborghini",
                "modele": "Huracán STO",
                "annee": 2021,
                "kilometrage": 13505,
                "prix": 363490,
                "puissance_ch": 640,
                "moteur": "V10 5.2 L atmosphérique",
                "description": "Inspirée de la Huracán Super Trofeo. Légèreté, aéro et sensations pures.",
                "en_vedette": True,
                "ordre_affichage": 9,
            },
            {
                "titre": "Porsche 718 Cayman GT4 RS",
                "marque": "porsche",
                "modele": "718 Cayman GT4 RS",
                "annee": 2022,
                "kilometrage": 6861,
                "prix": 194900,
                "puissance_ch": 500,
                "moteur": "Flat-6 4.0 L atmosphérique",
                "description": "Le Cayman le plus radical. Moteur en position centrale, 500 ch, boîte PDK.",
                "en_vedette": True,
                "ordre_affichage": 8,
            },
            {
                "titre": "McLaren 720S Spider",
                "marque": "mclaren",
                "modele": "720S Spider",
                "annee": 2019,
                "kilometrage": 14946,
                "prix": 259900,
                "puissance_ch": 720,
                "moteur": "V8 4.0 L twin-turbo",
                "description": "720 ch, toit rétractable, lignes aérodynamiques. Une supercar au quotidien.",
                "en_vedette": True,
                "ordre_affichage": 7,
            },
            {
                "titre": "Ferrari 812 Superfast",
                "marque": "ferrari",
                "modele": "812 Superfast",
                "annee": 2019,
                "kilometrage": 4500,
                "prix": 339900,
                "puissance_ch": 800,
                "moteur": "V12 6.5 L atmosphérique",
                "description": "Le plus puissant V12 de série. 800 ch, propulsion, son inoubliable.",
                "en_vedette": True,
                "ordre_affichage": 6,
            },
            {
                "titre": "Porsche 911 Turbo Cabriolet",
                "marque": "porsche",
                "modele": "911 Type 991 Turbo Cabriolet",
                "annee": 2016,
                "kilometrage": 45898,
                "prix": 144900,
                "puissance_ch": 540,
                "moteur": "Flat-6 3.8 L twin-turbo",
                "description": "911 Turbo phase 2 en cabriolet. 540 ch, 4 roues motrices, toit ouvrant.",
                "en_vedette": False,
                "ordre_affichage": 0,
            },
        ]
        created = 0
        for d in data:
            titre = d["titre"]
            d["image_url"] = DEMO_IMAGES.get(titre, "")
            _, c = Vehicule.objects.update_or_create(
                titre=titre,
                defaults=d,
            )
            if c:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Véhicules de démo chargés. {created} créé(s), images externes mises à jour."))
