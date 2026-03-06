from google import genai

from dotenv import load_dotenv

load_dotenv()


client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="what is the colour of the orange? Answer in one word",
)

print(response.text)

