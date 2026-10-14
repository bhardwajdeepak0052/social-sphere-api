##script to know what open models are accessible to me

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
print(os.environ.get("GROQ_API_KEY"))

try:
    print("Fetching available models from Groq...")
    models = client.models.list()

    print("\n--- Available Model IDs ---")
    for model in models.data:
        print(f"- {model.id}")

except Exception as e:
    print(f"Error fetching models: {e}")
