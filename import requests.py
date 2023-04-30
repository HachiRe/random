import requests
import json
import base64

# Your OpenAI API key
API_KEY = "YOUR_API_KEY"

prompt = " aaa"

# Encode the prompt as base64
prompt_bytes = prompt.encode("ascii")
prompt_base64 = base64.b64encode(prompt_bytes).decode("ascii")

# Construct the API request payload
data = {
    "model": "image-alpha-001",
    "prompt": prompt_base64,
    "num_images": 1,
    "size": "512x512",
    "response_format": "url",
}

# Send the API request
response = requests.post(
    "https://api.openai.com/v1/images/generations", 
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"},
    data=json.dumps(data),
)

# Parse the response and get the image URL
response_data = response.json()["data"][0]
image_url = response_data["url"]

# Print the URL of the generated image
print(f"Generated image URL: {image_url}")

#remember to replace with 'YOUR_API_KEY' with your openai API key
