from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

#Back and forth conversation
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
client = OpenAI()

print("Welcome to the StoryBot! Type 'quit' to exit.\n")

while True:
    # Ask the user for a topic
    topic = input("Enter a topic for your bedtime story: ")
    
    if topic.lower() == "quit":
        print("Goodbye! Sweet dreams 🌙✨")
        break

    # Call the OpenAI API to generate a story
    response = client.responses.create(
        model="gpt-5-nano",
        input=f"Write a one-sentence bedtime story about {topic}."
    )

    # Print the story
    print(response.output_text, "\n")