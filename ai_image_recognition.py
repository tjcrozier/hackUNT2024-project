import base64
import json
from openai import OpenAI

#API Key Handling
secrets = open("api_keys/keys.json")
key = json.load(secrets)["OPENAI_API_KEY"]


def GetImageDescription(image_in):
    client = OpenAI(api_key=key)

    # Function to encode the image
    def encode_image(image_in):
        with open(image_in, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
    image_path = "hotmoms.jpg"

    # Getting the base64 string
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        #Instructions for GPT within the triple quotes!
        {"role": "system", "content": "You are to describe the article of clothing in each image in ten words or less. Other items such as accessories should also be expected. If the item has any relevant text, include it regardless of the ten-word limit. If you cannot see any clothes or accessories, give it your best guess, still in 5 words or less"},
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "What is in this image?",
            },
            {
            "type": "image_url",
            "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}",
            "detail": "low",
            },
            },
        ],
        }
    ],
    )

    print(response.choices[0].message.content)
    
GetImageDescription("guh")