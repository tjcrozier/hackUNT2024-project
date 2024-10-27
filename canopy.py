import requests
import json
from google import get_asins_from_google

# Define the URL of the GraphQL endpoint
url = 'https://graphql.canopyapi.co/'

asin_from_google = get_asins_from_google("yellow puffer jacket")[0]

# Define the GraphQL query
query = """
query amazonProduct($asin: String!) {
  amazonProduct(input: {asin: $asin}) {
    title
    mainImageUrl
    rating
    price {
      display
    }
  }
}
"""

secrets = open("api_keys/secrets.json")
key = json.load(secrets)["AMAZON_API_KEY"]

headers = {
    'Content-Type': 'application/json',
    'API-KEY': key,
}

variables = {
  'asin': asin_from_google,
}

# Define the request payload
payload = {
    'query': query,
    'variables': variables
}

# Send the POST request to the GraphQL endpoint
response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Query failed to run with a {response.status_code} status code.")
    print(f"Response: {response.text}")