from pydantic import BaseModel
from openai import OpenAI
import json

secrets = open("api_keys/keys.json")
key = json.load(secrets)["OPENAI_API_KEY"]

client = OpenAI(api_key=key)

clothes = []

#Get article names
for i in range(1, 5):
    clothes.append(input("Enter item #" + str(i) + ": "))

#OpenAI API Call
#Model should be 4o-mini

class costumeIdea(BaseModel):
    name: str
    clothes_used: list[str]
    reason: str
    suggested_items: list[str]
    suggestion_reasoning: str
    
print(str(clothes))

    
completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    n=3,
    presence_penalty=2,
    messages=[
        {"role": "system", "content": "Come up with a creative halloween costume/cosplay idea using the available articles of clothing. Try to use existing characters. When coming up with multiple choices, try to diversify and don't repeat ideas! When coming up with ideas, you may also include suggested items to add to complete the costume."},
        {"role": "user", "content": str(clothes)},
    ],
    response_format=costumeIdea
)

print(completion.choices[0].message.parsed.name)
print(completion.choices[1].message.parsed.name)
print(completion.choices[2].message.parsed.name)



"""print("Option 1\n")
print(completion.choices[0].message.parsed)
print("Option 2\n")
print(completion.choices[1].message.parsed)
print("Option 3\n")
print(completion.choices[2].message.parsed)"""