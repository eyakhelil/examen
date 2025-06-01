from celery import shared_task
import requests
from api.ai_utils import suggest_field_mapping

# 🔁 Fonction 1 : si tu veux synchroniser vers une autre plateforme low-code
@shared_task
def sync_data_with_lowcode():
    url = "https://api.lowcodeplatform.com/data"  # Remplace par l'URL correcte
    headers = {"Authorization": "Bearer votre_cle_api"}
    data = {
        "name": "exemple",
        "value": 42,
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return "Données synchronisées avec succès"
    except requests.RequestException as e:
        return f"Erreur de synchronisation : {e}"

# 🟦 Fonction 2 : pour envoyer vers Bubble
@shared_task
def send_data_to_bubble():
    url = "https://eyakheili485-39154.bubbleapps.io/version-test/api/1.1/wf/receive_data"
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer TON_API_TOKEN"  # Décommente si besoin
    }
    data = {
        "name": "Hello from Django!",
        "value": 123
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        print("Status code:", response.status_code)
        print("Response:", response.text)
    except Exception as e:
        print("Error sending data to Bubble:", e)


@shared_task
def run_ai_mapping_task():
    source_fields = ["first_name", "last_name", "email"]
    target_fields = ["prenom", "nom", "adresse_email"]

    result = suggest_field_mapping(source_fields, target_fields)
    print("Résultat du mapping suggéré :")
    print(result)
    return result
