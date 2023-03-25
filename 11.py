
import openai
import spacy

# set the OpenAI API key
openai.api_key = "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"

# load a pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# define the categories and their keywords
categories = {
    "1": ["energy", "solar", "wind", "electricity", "power"],
    "2": ["water", "conservation", "irrigation", "rainwater"],
    "3": ["food", "organic", "local", "vegetarian", "vegan"],
    "4": ["transport", "bicycle", "public", "electric", "car"],
    "5": ["fashion", "sustainable", "ethical", "fair", "trade"]
}

# get user input
print("Hello!")
print("How can I assist you today?")
print("Please select a category:")
for key, value in categories.items():
    print(f"{key}. {value[0]}")
selected_category = input("> ")

# prompt user for input
print(f"Please enter your prompt related to {categories[selected_category][0]}:")
prompt = input("> ")

# check if the prompt contains keywords relevant to the selected category
relevant = False
for keyword in categories[selected_category]:
    if keyword in prompt.lower():
        relevant = True
        break

# check if the prompt is relevant to the selected category
if not relevant:
    print("Sorry, your prompt does not appear to be related to the selected category.")
else:
    # submit the prompt to GPT-3 and get a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # print the response from GPT-3
    print(response.choices[0].text.strip())
