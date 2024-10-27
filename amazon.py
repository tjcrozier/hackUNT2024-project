import requests
from api_keys.constants import AMAZON_API_KEY

# Define the URL of the GraphQL endpoint
url = 'https://graphql.canopyapi.co/'

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

headers = {
    'Content-Type': 'application/json',
    'API-KEY': AMAZON_API_KEY(),
}

variables = {
  'asin': 'B0B3JBVDYP',
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
