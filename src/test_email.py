# test_email.py
import os
from django.core.mail import send_mail
from django.conf import settings

# Assurez-vous que les variables d'environnement sont chargées
os.environ['DJANGO_SETTINGS_MODULE'] = 'first_saas.settings'  # Remplace par le chemin vers ton fichier settings.py

# Fonction de test d'envoi d'email
def test_email():
    subject = "Test Email"
    message = "Ceci est un email de test depuis Django."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['ecomsbranding@gmail.com']  # Remplace par une adresse valide

    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email envoyé avec succès!")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    test_email()
