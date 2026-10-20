import os
import requests
from dotenv import load_dotenv

load_dotenv()

r = requests.get(
    "https://api.groq.com/openai/v1/models",
    headers={"Authorization": "Bearer " + os.environ["GROQ_API_KEY"]},
)
print("Status:", r.status_code)
for m in r.json().get("data", []):
    print(m["id"])