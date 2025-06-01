import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Charge les variables d'environnement

openai.api_key = os.getenv("OPENAI_API_KEY")

def suggest_field_mapping(source_fields, target_fields):
    prompt = f"""
Je souhaite mapper des champs entre deux systèmes.

Voici les champs source : {source_fields}
Voici les champs cibles : {target_fields}

Propose un mapping sous forme de JSON où chaque champ source est associé à un champ cible le plus pertinent.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=300,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Erreur lors de l’appel à OpenAI : {e}"
