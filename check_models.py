from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("=== Modèles disponibles sur votre compte Groq ===\n")

try:
    models = client.models.list()
    for model in models.data:
        print(f"✓ {model.id}")
except Exception as e:
    print(f"Erreur: {e}")