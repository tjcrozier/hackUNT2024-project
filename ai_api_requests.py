from pydantic import BaseModel
from openai import OpenAI
import json

#Class to be returned by GPT

class CostumeIdea(BaseModel):
    name: str
    clothes_used: list[str]
    reason: str
    suggested_items: list[str]
    suggestion_reasoning: str
    
class CostumeWrapper(BaseModel):
    options: list[CostumeIdea]
    
def convert_to_json(wrapper: CostumeWrapper) -> str:
    # Convert to dictionary first, then to JSON string
    return json.dumps(wrapper.dict(), indent=4)
    
#Class for user input
class user_data():
    wardrobe = []
    user_notes = ""
    
#API Key Handling
secrets = open("api_keys/keys.json")
key = json.load(secrets)["OPENAI_API_KEY"]

def getSuggestions(wardrobe, num_of_ideas = 1, notes = ""):
    my_user = user_data()
    user_data.wardrobe = wardrobe
    user_data.user_notes = notes

    #Start OpenAI Client
    client = OpenAI(api_key=key)

    #TODO: Implement external list organization (database maybe?)

    #Get article names
    #for i in range(1, 5):
        #my_user.wardrobe.append(input("Enter item #" + str(i) + ": "))

    #OpenAI API Call
    #Model should be 4o-mini
    
    #print(str(my_user.wardrobe))

    sys_prompt = """
    Come up with three unique creative halloween costume/cosplay idea using the available articles of clothing.
    Try to use existing characters.
    Make your ideas as scary as possible.
    When choosing which clothes to use, you must use only clothes listed in the wardrobe, or,
    if you choose to add items not listed in the wardrobe, they must also be listed in the suggested items
    Try to make complete outfits, with a top, bottom, shoes, and accessories when applicable.
    Do not be afraid to include your suggestions in the clothes used! The clothes used field should mostly include
    items from the user's wardrobe, but should also include up to two items of your choosing.
    When coming up with multiple choices, do not include repeat ideas!
    When coming up with ideas, you may also include suggested items to add to complete the costume.
    """

    #User prompt should be thought of as a ChatGPT prompt.
    user_prompt = ""

    #Add user notes if they exist
    if(my_user.user_notes != ""):
        sys_prompt += ("Here are some user-defined notes: \n" + my_user.user_notes + "\n")
    
    user_prompt += ("Here is the user's wardrobe: \n")
    user_prompt += (str(my_user.wardrobe))

    #Debug
    print(sys_prompt, "\n", user_prompt, "\n")


    

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        # presence_penalty=2,
        messages=[
            #Instructions for GPT within the triple quotes!
            {"role": "system", "content": sys_prompt},
            #User message input after content":
            {"role": "user", "content": str(my_user.wardrobe)},
        ],
        response_format=CostumeWrapper
    )

    return(convert_to_json(completion.choices[0].message.parsed))
    #Print only the names of outputs
    #NOTE:
    #Elements of each response can be accessed like so
    #print(completion.choices[0].message.parsed.COSTUME_IDEA_MEMBER)
    #Where COSTUMEIDEA_MEMBER is a member of the costume_idea class
    """
    print(completion.choices[0].message.parsed.name)
    print(completion.choices[1].message.parsed.name)
    print(completion.choices[2].message.parsed.name)
    """

    #Print the full output of each
    # print("Option 1\n")
    # print(completion.choices[0].message.parsed)
    # print("Option 2\n")
    # print(completion.choices[1].message.parsed)
    # print("Option 3\n")
    # print(completion.choices[2].message.parsed)
    print(completion.choices[0].message.parsed)


clothes = ["red hat", "blue overalls", "brown boots"]
print(getSuggestions(clothes,4))
#print(json_output)
#print(type(json_output))
